import xlrd
def get_case(filename,sheetnum):
	case_dir='D:\\python\\work\\HDapi\\testcase_excel' + '\\' + filename + '.xlsx'

	datas = xlrd.open_workbook(case_dir)
	table = datas.sheets()[sheetnum]
	nor = table.nrows
	nol = table.ncols

if __name__ == '__main__':
	get_case('house',0)


