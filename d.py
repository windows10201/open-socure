import requests,re
id=""
pas=""
ua="Mozilla/5.0 (SymbianOS; Series60; Nokia5610 XpressMusic/2.0 (08.23); Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/533.4 (KHTML, like Gecko) Mobile Safari/533.4"
session = requests.Session()
free_fb = session.get('https://m.facebook.com').text
log_data = {"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":id,"pass":pas,"login":"Log In"}
header_freefb = {
"authority": 'm.facebook.com',
"method": 'GET',         
"scheme": 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'dpr': '3',
'sec-ch-prefers-color-scheme': 'dark',
'sec-ch-ua': '"(Not(A:Brand";v="99"',
'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-model': '"SH-03K"',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua-platform-version': '""',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
"user-agent": ua}
lo = session.post('https://m.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
log_cookies=session.cookies.get_dict().keys()
coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])


print(coki)