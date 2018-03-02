import xlrd
datas = xlrd.open_workbook('D:\person\learn\py\lianxi\post_case.xlsx')
table = datas.sheets()[0]
nor = table.nrows  #获取表格行数
nol = table.ncols  #获取表格列数
for i in range(1,nor):
	houseNum = table.cell_value(i,0)
	orgUuid = table.cell_value(i,1)
	floor = table.cell_value(i,2)
	houseUseFor = table.cell_value(i,3)
	residentNum = table.cell_value(i,4)
	emergencyPhone = table.cell_value(i,5)
	code = table.cell_value(i,6)
	massage = table.cell_value(i,7)
	print(houseNum)
#	print(table.row_values(i))
#print(nor,nol)