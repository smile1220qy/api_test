import xlrd

def get_sheet(file,name):
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name(name)
    return sheet

def get_case(sheet,case_name):
    for i in range(1,sheet.nrows):
        if sheet.cell(i,0).value == case_name:
            return sheet.row_values(i)
    return None

if __name__ == '__main__':
    sh = get_sheet("../data/data.xlsx","注册")
    case_date = get_case(get_sheet("../data/data.xlsx","注册"),"test_user_reg_normal")
    print(case_date)