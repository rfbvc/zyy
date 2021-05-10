from selenium import webdriver
from time import sleep, ctime
import os
import pytest
import unittest
class test(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        chrome_driver_binary = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_binary,chrome_options=options)
        self.driver.get("http://www.baidu.com")
        sleep(3)
    def test(self):
        self.driver.find_element_by_id("kw").send_keys("Test search")
        self.driver.find_element_by_id("su").click()
        sleep(3)
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
