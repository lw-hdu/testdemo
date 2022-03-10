# 从excel样式的测试用例中读取请求url和请求报文，将执行结果写入excel
import xlrd
import requests
import json
import time
from xlutils.copy import copy
headers = {"Content-Type": "application/json"}
excelDir = r'E:\code\cloudpc\post_test.xls'
# formatting_info=True保留Excel的原格式，打开的文件格式不能是xlsx
workData = xlrd.open_workbook(excelDir, formatting_info=True)
# 根据表单名称获取操作表单
sheetData = workData.sheet_by_name('north')
# 复制个副本文件并打开第1个sheet
workCopy = copy(workData)
sheetCopy = workCopy.get_sheet(0)
# 统计行数
rows = sheetData.nrows
for row in range(1, rows):
    # 将单元格中数据定义
    idNum = sheetData.cell(row, 0).value
    postUrl = sheetData.cell(row, 2).value
    postData = sheetData.cell(row, 3).value
    exceptResult = json.loads(sheetData.cell(row, 4).value)['result']
    # 发送请求
    postRes = requests.post(postUrl, data=postData, headers=headers)
    # 记录结果
    actionResult = postRes.json()['result']

    # 在复制的文件中写入测试结果
    sheetCopy.write(row, 5, postRes.text)
    if actionResult == exceptResult:
        sheetCopy.write(row, 6, "pass")
    else:
        sheetCopy.write(row, 6, "fail")
workCopy.save(r'E:\code\cloudpc\post_test_copy.xlsx')
