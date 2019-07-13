import requests
import tesserocr    #这个包莫名其妙装好了，但是无法识别教务处的验证码
from PIL import Image   #实际为pillow库
from Exceptions import HttpRequestsError
class VerigyCodeClient:
    localImgUrl = r'F:\Python\image\VerifyCode.jpg'
    # localImgUrl = r'F:\Python\image\123.jpg'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    key = ''
    reqResult = None

    def __init__(self):
        pass    #pass不起到任何作用，只占个位置

    #下载验证码的方法，输入url格式为'http://218.196.240.97/validateCodeAction.do'
    def getVerifyCode(self,url):
        self.reqResult = requests.get(url,headers=self.headers)
        #如果status不是200的话则抛出异常。
        if(self.reqResult.status_code != 200):
            raise HttpRequestsError('Status Error')
        #创建文件并写入，这里的方式一定要是wb，否则无法写入字节数据
        codeImage = open(self.localImgUrl,'wb')
        codeImage.write(self.reqResult.content)

    def showImage(self):
        img = Image.open(self.localImgUrl)
        img.show()

    #对图片进行二值化处理的函数
    def binaryImg(self,img,threshold = 100):
        Lim = img.convert('L')
        Lim.show()
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        # convert to binary image by the table
        bim = Lim.point(table, '1')
        bim.show()
        f = open(self.localImgUrl,'wb')
        bim.save(f)
        return bim

    def resizeImg(self,img):
        (x ,y) =img.size
        x_s = x * 3
        y_s = y * 3
        img = img.resize((x_s,y_s),Image.ANTIALIAS)
        return img

    def getKey(self):
        img = Image.open(self.localImgUrl)
        img = self.resizeImg(img)
        # 参数为阈值，因为0是黑色，255是白色
        bim = self.binaryImg(img,150) #阈值为150比较合适
        self.key = tesserocr.image_to_text(bim)
        print('识别完成')
        return self.key

        # self.key = input('请输入验证码')
        # return self.key


if __name__ == '__main__':
    client = VerigyCodeClient()
    client.getVerifyCode('http://218.196.240.97/validateCodeAction.do')
    client.showImage()
    print(client.getKey())