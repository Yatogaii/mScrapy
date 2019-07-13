#--------------       selenium与浏览器的交互   ----------------------#
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://218.196.240.97")
input_str = browser.find_element_by_id('q')
input_str.send_keys("ipad")
time.sleep(1)
input_str.clear()
input_str.send_keys("MakBook pro")
button = browser.find_element_by_class_name('btn-search')
button.click()
#运行的结果可以看出程序会自动打开Chrome浏览器并打开淘宝输入ipad,然后删除，重新输入MakBook pro，并点击搜索
#------------------------------------------------------------------
"""
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from selenum import webdriver
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from selenum import webdriver
ModuleNotFoundError: No module named 'selenum'
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> browser.get("http://http://218.196.240.97")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    browser.get("http://http://218.196.240.97")
  File "D:\Anaconda\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 332, in get
    self.execute(Command.GET, {'url': url})
  File "D:\Anaconda\lib\site-packages\selenium\webdriver\remote\webdriver.py", line 320, in execute
    self.error_handler.check_response(response)
  File "D:\Anaconda\lib\site-packages\selenium\webdriver\remote\errorhandler.py", line 242, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.WebDriverException: Message: Reached error page: about:neterror?e=dnsNotFound&u=http%3A//http//218.196.240.97&c=UTF-8&f=regular&d=%E6%88%91%E4%BB%AC%E6%97%A0%E6%B3%95%E8%BF%9E%E6%8E%A5%E8%87%B3%20http%20%E7%9A%84%E6%9C%8D%E5%8A%A1%E5%99%A8%E3%80%82

>>> browser.get("http://218.196.240.97")
>>> input_account = browser.find_element_by_name('zjh')
>>> input_account.sned_keyS('311722001013')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    input_account.sned_keyS('311722001013')
AttributeError: 'FirefoxWebElement' object has no attribute 'sned_keyS'
>>> input_account.sned_keys('311722001013')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    input_account.sned_keys('311722001013')
AttributeError: 'FirefoxWebElement' object has no attribute 'sned_keys'
>>> input_account.send_keyS('311722001013')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    input_account.send_keyS('311722001013')
AttributeError: 'FirefoxWebElement' object has no attribute 'send_keyS'
>>> input_account.send_keys('311722001013')
>>> input_pass = browser.find_element_by_name('mm')
>>>  input_yzm = browser.find_element_by_name('v_yzm')
SyntaxError: unexpected indent
>>> input_yzm = browser.find_element_by_name('v_yzm')
>>> input_pass.send_keys('000206')
>>> input_yzm.send_keys('kqwb')
>>> input_login = browser.find_element_by_id('btnSure')
>>> input_login.click()
>>>
"""
