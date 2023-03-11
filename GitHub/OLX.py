import random
from time import sleep
from selenium import webdriver

driver=webdriver.Chrome('./chromedriver.exe')
driver.get('https://www.olx.com.ar/autos_c378')
autos=driver.find_elements_by_xpath("//li[@data-aut-id='itemBox']")
arr=[]
for auto in autos:
    precio=auto.find_element_by_xpath(".//span[@data-aut-id='itemPrice']")
    print(precio.text)
    descripcion=auto.find_element_by_xpath(".//span[@data-aut-id='itemTitle']")
    print(descripcion.text)

driver.quit()
