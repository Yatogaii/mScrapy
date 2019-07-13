# 导入requests库
import requests# 登录类
from PIL import Image
from bs4 import BeautifulSoup
class Login(object):    # init 函数
    def __init__(self):
        # 请求头
        self.headers = {
             # 为什么问题会出道这里啊！！！
             # User-agent必须这样写
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0',
            # 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36'
            # 'Host':'218.196.240.97',
            # 'Referer':'http://218.196.240.97/loginAction.do',
            # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        # 登录请求地址
        self.post_url = 'http://218.196.240.97/loginAction.do'
        # 验证码请求地址
        self.yzm_url = 'http://218.196.240.97/validateCodeAction.do'
        # 维持一个session
        self.session = requests.session()
        # print(self.session.cookies)
        # login函数
    def login(self, account, password):
        print(self.session.cookies)
        self.session.get('http://218.196.240.97/',headers=self.headers)
        print(self.session.cookies)
        # 请求验证码并保存
        f = open('yzm.jpg','wb')
        res = self.session.get(self.yzm_url, headers=self.headers)
        print(self.session.cookies)
        f.write(res.content)
        f.close()
        img = Image.open('yzm.jpg')
        img.show()
        # 暂时手动输入验证码
        yzm = input("请查看当前目录下的验证码图片，输入验证码\n")
        print(len(yzm))
        # 登录请求数据
        post_data = {
            'zjh1': '',
            'tips': '',
            'lx': '',
            'evalue': '',
            'eflag': '',
            'fs': '',
            'dzslh': '',
            'zjh': account,
            'mm': password,
            'v_yzm': yzm,
        }
        # 请求登录
        loginResponse = self.session.post(self.post_url, data=post_data, headers=self.headers)
        print(self.session.cookies)
        # 打印结果
        print("状态码：" + str(loginResponse.status_code))
        print(loginResponse.content)
        soup = BeautifulSoup(loginResponse.content,'lxml')
        r = soup.find('td',class_='errorTop')
        if r!=None :
            print(r)
        else :
            print(loginResponse.text)
        f = open(r'F:/tmp.html','wb')
        f.write(loginResponse.content)
        f.close()
        res = self.session.get('http://218.196.240.97/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2018-2019学年春(两学期)#qb_2018-2019学年春(两学期) ')
        print(res.text)
        resultSoup = BeautifulSoup(res.content,'lxml')
        udata = resultSoup.find_all('tr',class_='odd')
        print('-----------------------')
        print(udata)
        print('-------------------------------------')
        grades = resultSoup.find_all('td')
        print(grades[2])
        print(grades[6])
# 测试
if __name__ == "__main__":
    myLogin = Login()
    myLogin.login(account='311722001013', password='000206')