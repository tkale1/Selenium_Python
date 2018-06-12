'''
Created on Jun 3, 2018

@author: tanmaykale
'''

import unittest
import requests
from nose.tools import assert_equals
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.keys import Keys




class AppleHomepageTestHyperlinks(unittest.TestCase):
    '''
    classdocs
    '''
    
    @classmethod
    def setUpClass(inst):
        inst.chrome_path = "/Users/tkale/PycharmProjects/web_test/test_website/chromedriver"
        # create a new Chrome session
        inst.driver = webdriver.Chrome(inst.chrome_path)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://www.apple.com/")
        
    def get_url(self, url):
        # added header because appleid.apple.com/us and locate.apple.com where giving Client side errors.
        headers = {
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,la;q=0.8",
            # "Connection": "keep-alive",
            # "Cookie": "dssid2=0eec411f-7abf-4dd4-8023-99c86b1b5a12; dssf=1; as_dc_pod=rno_88-0; s_cc=true; s_fid=4AFB9FE621B9D173-059CCA88B592E354; s_vi=[CS]v1|2D8A5283852E6CB2-40002CD5E04A22C1[CE]; ccl=R1Q9HhwsZNmZp8sUWlyyQcA400Tk2aum9PPpXvv8Qeo=; geo=US; as_pcts=Vwb8Ics1:u2XjhiYm3EL-7II5b+9-eSHgwGoGcuwnO0EddXB1IoNb6lpw; a=QQAVAAAACwBDmt4IMTAwMGw0UUoKcmV0X3N1Yl9ocAAAAAE=; itscc=2%7C1528079892940%60ret_sub_hp%6010000; s_nr=1528087029677; s_vnum=1530679029679%26vn%3D1; s_aca_ct=%5B%5BB%5D%5D; s_ptc=0.152%5E%5E0.000%5E%5E0.000%5E%5E0.000%5E%5E600%5E%5E0.104%5E%5E0.761%5E%5E0.004%5E%5E0.654%5E%5E1.426%5E%5E0.002%5E%5E1.584; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE=; optimizelyEndUserId=oeu1528097994512r0.05971537807838745; optimizelySegments=%7B%22341793217%22%3A%22direct%22%2C%22341794206%22%3A%22false%22%2C%22341824156%22%3A%22gc%22%2C%22341932127%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; pxro=1; s_sq=%5B%5BB%5D%5D; idclient=web; dslang=US-EN; site=USA; aidsp=8DDCAC5E0D88561B395D7AA280B10160AD62C7C3116C08829E3CF3344754D3A2D39AB4F475EB22CA1F388F6A5D24B1C73FD1453280BE9CDE17818C813A6CBAE4BFBEB86C3B0928B6DA25CE09024D344ACA3B17D1F94DB1D63CC8B2FA9B82E4EBFF405EAC9A40A66F140977EEBB7BC467A333215D02B79647; s_pathLength=homepage%3D1%2Clocate%3D1%2C; s_invisit_n2_us=0; s_vnum_n2_us=0|2",
            # "DNT": "1",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            }
        
        r = requests.get(url, headers=headers)
        return r.status_code
    
    def log_status(self):
        logger = logging.getLogger("mylogger")
        streamHandler = logging.StreamHandler()
        streamHandler.setLevel(logging.NOTSET)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        streamHandler.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(streamHandler)
        return logger

    def open_apple_home_page(self):
        self.chrome_path = "/Users/tkale/PycharmProjects/web_test/test_website/chromedriver"
        # create a new Chrome session
        self.driver2 = webdriver.Chrome(self.chrome_path)
        self.driver2.implicitly_wait(30)
        self.driver2.maximize_window()
        # navigate to the application home page
        self.driver2.get("http://www.apple.com/")


    def verify_all_links_in_section(self, elements_in_section):
        logger = self.log_status()
        failing_links = []
        # count = 0
        output_dict = dict()

        for element, url in elements_in_section.items():
            if not element or '#' in url:
                del elements_in_section[element]
                continue

        for element, url in elements_in_section.items():
            self.open_apple_home_page()
            print(element.encode('utf-8'), url.encode('utf-8'))
            self.driver2.find_element_by_link_text(element).click()
            print(self.driver2.current_url.encode('utf-8'))

            if url.encode('utf-8') != self.driver2.current_url.encode('utf-8'):
                failing_links.append(element.encode('utf-8'))
            self.driver2.quit()


        if not failing_links:
            return "All links seems to be working properly"
        else:
            return failing_links
        

    # def test_global_nav_links(self):
    #     print("Verifying Global Nav Links")
    #     global_nav = self.driver.find_elements_by_xpath('//nav[@id="ac-globalnav"]//a')
    #
    #     elements = dict()
    #     for element in global_nav:
    #         elements[element.text] = element.get_attribute('href')
    #
    #     print (self.verify_all_links_in_section(elements))
            

    # def test_homepage_body_links(self):
    #     print("Verifying Homepage Body Links")
    #     homepage_body_links = self.driver.find_elements(By.XPATH, '//main//a')
    #
    #     elements = dict()
    #     for element in homepage_body_links:
    #         elements[element.text] = element.get_attribute('href')
    #
    #     print(self.verify_all_links_in_section(elements))
    #
    def test_homepage_footer_links(self):
        print("Verifying Footer Links")
        footer_links = self.driver.find_elements(By.XPATH, '//footer//a')

        elements = dict()
        for element in footer_links:
            elements[element.text] = element.get_attribute('href')

        print(self.verify_all_links_in_section(elements))


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()
        

if __name__ == '__main__':
    unittest.main()