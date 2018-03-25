#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @time   : 18-3-25 下午7:05
# @author : Feng_Hui
# @email  : capricorn1203@126.com
from selenium import webdriver
import time
from selenium.webdriver import ChromeOptions
from pyvirtualdisplay import Display


class TestSelenium(object):

    test_url1 = "https://www.oschina.net/news/industry"
    test_url2 = "https://www.taobao.com"
    test_url3 = "http://www.jikexueyuan.com"

    def test_selenium_js(self):
        """测试selenium框架执行js"""
        browser = webdriver.Chrome()
        browser.get(self.test_url1)
        time.sleep(10)
        # html = browser.page_source
        # print(html)
        # browser.quit()
        for i in range(3):
            # exec_result = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);"
            #                                      "var lenOfPage=document.body.scrollHeight;return lenOfPage")
            # print(exec_result)
            # browser.execute_script("return alert('from selenium');")
            print(browser.execute_script("return document.title"))

    def test_selenium_image(self):
        """测试selenium不加载图片"""
        chrome_opt = ChromeOptions()
        prefs = {'profile.managed_default_content_settings.image': 2}
        chrome_opt.add_experimental_option("prefs", prefs)
        browser = webdriver.Chrome()
        browser.get(self.test_url2)
        print(browser.current_url)
        print(browser.get_cookies())

    def test_selenium_quietly(self):
        """无界面运行chromedriver"""
        # display = Display(visible=0, size=(800, 600))
        display = Display(size=(800, 600))
        display.start()
        browser = webdriver.Chrome()
        browser.get(self.test_url3)
        print(browser.current_url)
        print(browser.title)


if __name__ == "__main__":
    test_sel = TestSelenium()
    test_sel.test_selenium_quietly()
