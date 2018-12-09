#1.导入xlrd
import xlrd

#2.打开excel(work_book)
excel = xlrd.open_workbook("../data/data.xlsx")

#3.指定工作表
# sheet = excel.sheet_by_name("登录")
# sheet = excel.sheet_by_index(0)

#4.读取信息
# print(sheet.nrows) #有效数据行数
# print(sheet.ncols) #有效数据列数
#
# print(sheet.row_values(0)) #打印第一行数据
# print(sheet.row_values(1)) #打印第二行数据
# print(sheet.cell(1,0).value) #打印指定单元格数据

#练习1  输入表明、用例名返回数据
# sheet2 = excel.sheet_by_name("注册")
# for h in range(1,sheet2.nrows):
#     print(sheet2.row_values(h))
#练习2
# def read_date(sheet,casename):
#     sheet3 = excel.sheet_by_name(sheet)
#     case_data = sheet3.row_values()
#     sheet3.get_rows("test_user_reg_normal")
#     print(sheet3.get_rows("test_user_reg_normal"))
#     # return case_data



