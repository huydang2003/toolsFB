import os
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def initOptions(filePath):
	options = Options()
	options.add_argument('--ignore-certificate-errors')
	# options.add_argument('--log-level=3')
	options.add_argument("user-data-dir="+filePath)
	options.add_argument("--window-size=1080,720")
	# options.add_argument('--app=https://www.facebook.com/')
	return options

def initDriver(filePath):
	options = initOptions(filePath)
	driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe', options=options)
	return driver

def getCookieFB(driver):
	cookies = driver.get_cookies()
	cookie = ''
	for child in cookies:
		gt = f"{child['name']}={child['value']}"
		cookie = cookie + gt + ';'
	return cookie

def saveCookie(cookie):
	f = open('data/cookie.txt', 'w')
	f.write(cookie)
	f.close()

def main():
	filePath = input("Keo tha profile vao day: ").replace('"', '')
	driver = initDriver(filePath)
	cookie = getCookieFB(driver)
	input("Enter -> thoat")
	driver.quit()
if __name__ == '__main__':
	main()