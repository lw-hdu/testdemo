import requests
res=requests.get('https://www.shanbay.com/api/v1/vocabtest/category/?_=1565790540865')
code_json=res.json()
choice=int(input('请选择出题范围：0：GMAT；1：考研；2：高考；3：四级；4：六级；5：英专；6：托福；7：GRE；8：雅思；9：任意\n'))
url_code=code_json['data'][choice][0]
#print(url_code)
##获取测试单词
danci=requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+url_code+'&_=1565792136215')
danci_json=danci.json()['data']
list_know=[]
list_nuknow=[]
for danci in danci_json:
    test_danci=print('这个单词认识吗'+danci['content'])
    answer=input('认识输入Y，不认识按enter\n')
    if answer=='Y':
        list_know.append(danci['content'])
    else:
        list_nuknow.append(danci['content'])
print(list_know)
print(list_nuknow)


