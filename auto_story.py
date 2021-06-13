import os
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def initOptions(filePath):
	options = Options()
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-running-insecure-content')
	options.add_argument("--disable-extensions")
	options.add_argument("--proxy-server='direct://'")
	options.add_argument("--proxy-bypass-list=*")
	options.add_argument('--disable-gpu')
	options.add_argument('--disable-dev-shm-usage')
	options.add_argument('--no-sandbox')
	options.add_argument("--mute-audio")
	options.add_argument("user-data-dir="+filePath)
	options.add_argument("--window-size=1000,600")
	options.add_argument('--app=https://www.facebook.com/stories')
	return options

def initDriver(filePath):
	options = initOptions(filePath)
	driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe', options=options)
	return driver

# chọn story
def click_story(driver, xpath):
	try:
		WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
		ele = driver.find_element_by_xpath(xpath)
		ele.click()
		return True
	except:
		return False

# Keo thanh truot
def drag_scroll(driver):
	driver.execute_script('document.querySelector("#viewer_dialog > div > div > div > div > div").scrollBy(0,0.5*window.innerHeight)')

# click nut react
def click_react(driver, xpath):
	try:
		ele = driver.find_element_by_xpath(xpath)
		ele.click()
	except:
		pass

# ấn nút spause
def click_pause(driver):
	xpath = '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div[1]'
	WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))
	ele = driver.find_element_by_xpath(xpath)
	ele.click()

# tu dong
def auto_react(driver, react):
	# danh sach xpath cam xuc
	list_react = {
		'like': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[1]',
		'love': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]',
		'thuong': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]',
		'haha': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[4]',
		'wow': '//*[@id="viewer_dialog"]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[5]'
	}
	xpath_react = list_react[react]
	stt = 0
	while True:
		stt += 1
		xpath_point = f'//*[@id="viewer_dialog"]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div[2]/div[{stt}]'
		while True:
			drag_scroll(driver)
			check = click_story(driver, xpath_point)
			if check == True:
				break
			else:
				return 0
		time.sleep(2)
		click_pause(driver)
		if random.randint(1,10) > 5:
			click_react(driver, xpath_react)
			time.sleep(1)

def main(filePath, react):
	options = initOptions(filePath)
	driver = initDriver(filePath)
	title = driver.title
	if len(title)>20:
		time.sleep(90)
	auto_react(driver, react)
	driver.quit()

if __name__ == '__main__':
	# filePath = r'E:\FB nuôi\Nick1\profiles'
	filePath = input("Keo tha profile vao day: ").replace('"', '')
	list_react = {
		0: 'like',
		1: 'love',
		2: 'thuong',
		3: 'haha',
		4: 'wow'
	}
	for vt in list_react:
		print(vt,'|',list_react[vt])
	vt = int(input("Chon react: "))
	react = list_react[vt]
	main(filePath, react)