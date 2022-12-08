from selenium import webdriver 
import time as t
import numpy as np
import pandas as pd
import pyautogui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import string

output = pd.DataFrame(columns = ['Picture','Name','Percent'])

def out():
    outputd.to_excel('C:\\Users\\WilliamWilson\\Desktop\\cashback\\doffers.xlsx')
    outputp.to_excel('C:\\Users\\WilliamWilson\\Desktop\\cashback\\poffers.xlsx')
def try_clickid(id):
    try:
        clk = d.find_element_by_id(id)
        clk.click()
    except NoSuchElementException:
        t.sleep(5)
        print("1")
        try:
            clk = d.find_element_by_id(id)
            clk.click()
        except NoSuchElementException:
            print(id)
            t.sleep(5)


def clickcss(css):
  clk = d.find_element_by_css_selector(css)
  clk.click()
def clickid(id):
  clk = d.find_element_by_id(id)
  clk.click()
def sendid(keys,id):
  snd = d.find_element_by_id(id)
  snd.send_keys(keys)
def to_value(val):
  val1 = val.text
  val2 = val1.replace(',', '')
  value = float(val2.strip('$'))
  return(value)

d = webdriver.Chrome()
outputd = pd.DataFrame()
outputp = pd.DataFrame()
def get_x(x):
    global outputd
    global outputp
    
    d.get("https://www.topcashback.com/search/merchants/?letter="+x)
    t.sleep(5)
    try_clickid("ctl00_GeckoTwoColPrimary_Paging_lbtnView100")
    select = Select(d.find_element_by_id('ctl00_GeckoTwoColPrimary_ddlOrderBy'))
    select.select_by_value('Highest $')
    t.sleep(5)
    df = pd.read_html(d.page_source)[0]
    outputd = outputd.append(df)
    select = Select(d.find_element_by_id('ctl00_GeckoTwoColPrimary_ddlOrderBy'))
    select.select_by_value('Highest %')
    t.sleep(5)
    df = pd.read_html(d.page_source)[0]
    outputp = outputp.append(df)
    
    out()
    print (t.time)
    print(outputp.tail())
    print(outputd.tail())




for i,c in enumerate(string.ascii_lowercase):
    
    get_x(c)
d.close()



t.sleep(3)

output = outputp.append(outputd)

output.to_excel('C:\\Users\\WilliamWilson\\OneDrive - HarrellPartners\\Desktop\\cashback\\offers.xlsx')
