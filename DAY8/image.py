# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:55:12 2019

@author: NITS
"""

from selenium import webdriver
from time import sleep                         


#url ="http://forsk.in/images/Forsk_logo_bw.png"
url = "https://collegedunia.com/college/15381-swami-keshvanand-institute-of-technology-management-and-gramothan-skit-jaipur#"

source = webdriver.Chrome("E:\Machine learning\DAY8\chromedriver_win32\chromedriver.exe")
source.get(url)

sleep(2)

#new1 = source.find_element_by_xpath("/html/body/img")
new2 = source.find_element_by_xpath("/html/body/div[6]/div[2]/div/a/img")
#new1.screenshot("forsktechnologies.png")
new2.screenshot("skitlogo.png")
sleep(5)
source.quit()

#src="https://images.static-collegedunia.com/public/college_data/images/logos/1414559341skit_logo1.jpg?tr=w-72,h-80,c-force"
 