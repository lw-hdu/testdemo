##北向接口
import  requests,json,time,pymysql,hashlib
from biling import start,heart,end
#获取秒级时间戳
timeStamp=time.time()
timeArray = time.localtime(timeStamp)
id = time.strftime("%Y%m%d%H", timeArray)
#生成token
it=int(time.time())
#print(it)
strno='xview'+str(it)+'desktops'
md5 = hashlib.md5()
b = strno.encode(encoding='utf-8')
md5.update(b)
str_md5 = md5.hexdigest()
token='xview:'+str(it)+':'+str_md5

headers={"Content-Type":"application/json"}
sheaders={
	"X-Auth-Token":token,
	"Content-Type":"application/json"
	}
#创建数据库连接
conn=pymysql.connect(user='root',password='mysql',host='10.221.122.117',database='cloudpc')
cursor=conn.cursor()
#用户查询
def d_user():
    cursor.execute('SELECT * FROM cpc_user WHERE user_code="'+id+'"')
    conn.commit()
    users=cursor.fetchall()
    for user in users:
        user_code=user[1]
        user_uuid=user[10]
        #print('user_code:{}'.format(user_code),'\n''user_uuid:{}'.format(user_uuid))
        return user_uuid
#桌面池信息查询
def d_pool():
    cursor.execute(
        '''SELECT 
        pool_size,
        pool_uuid 
        FROM
        cpc_pool_uuid 
        WHERE pool_uuid IN (
            '317bbc94abb511ea97dffab16efa4700',
            '3f1c5c68aa2611ea9eaffaf905f7ea00',
            'cbd6a7c2aaf711ea97dffab16efa4700',
            '96fd3b1aaaf711ea91d6faf905f7ea00'
        )'''
    )
    conn.commit()
    pools=cursor.fetchall()
    for pool in pools:
        pool_size=pool[0]
        pool_uuid=pool[1]
        print('pool_uuid:{}'.format(pool_uuid),'\n''pool_size:{}'.format(pool_size),'\n')
#订购信息           
def d_order():
    cursor.execute('SELECT o.PRODUCT_ID,u.USER_CODE FROM cpc_user u,cpc_order o WHERE u.ID=o.USER_ID AND u.USER_CODE="'+id+'"')
    conn.commit()
    orders=cursor.fetchall()
    for order in orders:
        product=order[0]
        print('用户订购的产品id：'+str(product),'\n')
#升档信息
def d_mount():
    cursor.execute('SELECT m.MOUNT_PRODUCT_ID FROM cpc_user u,cpc_product_mount m WHERE u.ID=m.USER_ID AND u.USER_CODE="'+id+'"')
    conn.commit()
    mounts=cursor.fetchall()
    for mount in mounts:
        mount_product=mount[0]
        print('用户升档产品id:'+str(mount),'\n')
#用户与设备绑定
def d_devsn():
    cursor.execute('SELECT d.DEVSN FROM cpc_user u,cpc_user_devsn d WHERE u.ID=d.USER_ID AND u.`USER_CODE`="'+id+'"')
    conn.commit()
    devsns=cursor.fetchall()
    for devsn in devsns:
        user_devsn=devsn[0]
        print('用户与设备绑定：'+str(user_devsn),'\n')
#发送请求
def res(d_name,d_url,d_data,d_header=headers):
    d_res=requests.post(d_url,data=json.dumps(d_data),headers=d_header)
    d_result=d_res.json()['result']
    print(d_name+'接口的结果：'+d_result,'\n',d_name+'接口耗时：{}'.format(d_res.elapsed.total_seconds()),'\n') 
#用户新增
add_name='用户注册'
adduser_url='http://10.221.122.115:10003/userSync'
adduser_data={
        "userName":"name"+id,
        "userCode":id,
        "password":"123456",
        "userType":"1",
        "phone":id
    }
res(add_name,adduser_url,adduser_data)
#密码修改
pass_name='密码修改'
pass_url='http://10.221.122.115:10003/passwdSync'
pass_data={
        "userName":"name"+id,
        "userCode":id,
        "password":"123"
    }
res(pass_name,pass_url,pass_data)

#产品订购
print('订购前桌面池查询')
d_pool()
order_name='产品订购'
order_url='http://10.221.122.115:10003/orderSync'
for i in range(2):
    if i==0:
        product='pmonth'
    else:
        product='pfee'
    order_data={
            "userCode":id,
            "productCode":product,
            "subTime":it,
            "effectTime":it,
            "expireTime":"1622772442"
        }
    res(order_name,order_url,order_data)
print('订购后桌面池查询')
d_pool()
print('订购产品查询')
d_order()
#升档
up_name='升档'
up_url='http://10.221.122.115:10003/orderChangeSync'
up_data={
  "userCode":id,
  "phone":id,
  "originalProductCode":"pmonth",
  "newProductCode":"pup",
  "action":"1",
  "subTime":it,
  "effectTime":it,
  "expireTime":it
}
res(up_name,up_url,up_data)
print('升档后查询')
d_mount()
#认证
auth_name='用户认证'
auth_url='http://10.221.122.115:10004/authentication/password'
auth_data={
        "subject":id,
        "subjectType":"0",
        "password":"TwOu+/9GExHXP0OtXyaJDw",
        "DEVSN":"devsn_"+id,
        "devType":"1000"	
    }
res(auth_name,auth_url,auth_data,sheaders)
print('登录后查询用户与设备的绑定')
d_devsn()
#登录登出
log_url='http://10.221.122.115:10004/loginout'
for k in range(2):
    if k==0:
        ltype=0
        log_action='登入：'
    else:
        ltype=1
        log_action='登出：'
    log_data={
            "uuid":d_user(),
            "time":it,
            "type":ltype	
        }
    res(log_action,log_url,log_data,sheaders)
#取消订购
orderdel_name='取消订购'
orderdel_url='http://10.221.122.115:10003/orderDelete'
orderdel_data={
        "userCode":id,
        "productCodeList":"pfee"
    }
res(orderdel_name,orderdel_url,orderdel_data)
print('取消订购后查询')
d_order()
#用户暂停/恢复/注销
userdel_url='http://10.221.122.115:10003/businessSuspend'
for j in range(3):
    if j==0:
        status=1
        userdel_action='暂停用户：'
    elif j==1:
        status=0
        userdel_action='恢复用户：'
    else :
        status=9
        userdel_action='销户：'
    userdel_data={
        "phone":id,
        "userCode":id,
        "status":status
    }
    res(userdel_action,userdel_url,userdel_data)
print('销户后桌面池查询')
d_pool()
print('销户后订购查询')
d_order()
print('销户后升档信息查询')
d_mount()
print('销户后用户与设备的绑定关系查询')
d_devsn()

#关闭游标
cursor.close()
#关闭连接
conn.close()

start()
time.sleep(10)
heart()
time.sleep(10)
end()