# -*- coding: utf-8 -*-
import requests
import json
global s
s = requests.session()

def talk(content, userid):
    
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key": "d0184d613806fa2b7d9240d502414b08", "info": content, "userid": userid}
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)
    code = j['code']
	
    if code == 100000:
        recontent = j['text']
    elif code == 200000:
        recontent = j['text']+j['url']
    elif code == 302000:
        recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
    elif code == 308000:
        recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
    else:
        recontent = '我已经挂掉了，快多回复几句给我充电'
		
    return recontent