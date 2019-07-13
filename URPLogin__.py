# 界面中的VerifyCode后的random只是为为了避免浏览器调用缓存
from tools.getVerifyCode import  VerigyCodeClient
import requests
url = 'http://218.196.240.97/'  # URP教务处登录界面\
zjh = '311722001013'
mm = '000206'
yzm = ''
params = {
    'dzslh':'',
    'eflag':'',
    'evalue':'',
    'fs':'',
    'lx':'',
    'mm':mm,
    'tips':'',
    'v_yzm':yzm,
    'zjh':zjh,
    'zjh1':''
}
vfClient = VerigyCodeClient()
vfClient.getVerifyCode(r'http://218.196.240.97/validateCodeAction.do')
yzm = vfClient.getKey()
url = r'http://218.196.240.97/loginAction.do'
res = requests.post(url,params=params)
print(res.status_code)
f = open(r'F:/tmp.html','wb')
print(res.content)
f.write(res.content)