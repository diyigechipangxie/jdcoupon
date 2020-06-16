#!/bin/bash/evn python
# encoding=utf-8
"""
@file:jdWebdriver.py
@time:6/16/20|10:11 AM
"""
from random import randint
from selenium import webdriver
from selenium.webdriver import ActionChains
import requests
import time
import datetime
import schedule


class Coupon(object):
	def __init__(self):
		self.driver = webdriver.Chrome()

	def fetch(self):
		self.driver.get("https://www.jd.com/")
		self.driver.find_element_by_id("ttbar-login").click()
		time.sleep(10)
		self.driver.find_element_by_link_text(u'京东家电').click()
		handlers = self.driver.window_handles
		self.driver.switch_to.window(handlers[-1])
		time.sleep(5)
		js = "document.documentElement.scrollTop={}".format(randint(900, 1000))
		self.driver.execute_script(js)
		self.driver.implicitly_wait(30)
		self.driver.find_element_by_xpath('//*[@id="29"]/div[1]/a/div/img').click()
		self.i_handler()
		self.driver.switch_to.window(self.i_handler()[-1])
		self.driver.execute_script(js)
		self.driver.implicitly_wait(20)
		action = ActionChains(self.driver)
		action.move_by_offset(1200, 528).perform()
		while True:
			if time.ctime().split()[3].split(':')[0] == '14':
				action.click().perform()
			else:
				time.sleep(1)
				print('now is {}'.format(time.ctime()))

	def i_handler(self):
		handlers = self.driver.window_handles
		return handlers

	def __del__(self):
		self.driver.quit()

	@classmethod
	def start(cls):
		c = Coupon()
		c.fetch()
		schedule.every(2).hours.do(c.fetch)
		while True:
			schedule.run_pending()
			time.sleep(1)


if __name__ == '__main__':
	c = Coupon()
	c.fetch()
