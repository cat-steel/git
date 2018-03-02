def get_url(api_name):
	fp = open('D:\\python\\work\\HDapi\\config\\api_house.txt')
	api_infos = fp.readlines()
	fp.close()
	api_urls = []
	for api in api_infos:
		api_f = api.strip(' \t\r\n')
		api_c = api_f.split('=')
		if api_name == api_c[0]:
			return api_c[1]
		else:
			print('错误的接口名')
