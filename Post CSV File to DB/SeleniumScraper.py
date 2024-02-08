
#pip install selenium

import logging
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
options = Options()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
options.log_level = logging.ERROR

import time
import getpass
import csv
filename = input("Name of the CSV File: ")
pagetoscrape = webdriver.Chrome(options=options)
pagetoscrape.get("https://www.scrapethissite.com/pages/forms/?page_num=1")
file = open(f"{filename}.CSV","w")
writer= csv.writer(file)
writer.writerow(["ID","name","wins","losses","goals_for","goals_against"])

pagenum=1
id_counter = 1
while True:
    name = pagetoscrape.find_elements(By.CLASS_NAME, "name")
    wins = pagetoscrape.find_elements(By.CLASS_NAME, "wins")
    losses = pagetoscrape.find_elements(By.CLASS_NAME, "losses")
    gf = pagetoscrape.find_elements(By.CLASS_NAME, "gf")
    ga = pagetoscrape.find_elements(By.CLASS_NAME, "ga")
    
    for name,wins,losses,gf,ga in zip(name,wins,losses,gf,ga):
        print(name.text+" || "+wins.text+" || "+losses.text+" || "+gf.text+" || "+ga.text)
        writer.writerow([id_counter,name.text,wins.text,losses.text,gf.text,ga.text])
        
        id_counter += 1
    try:
        print()
        print()
        print("Page "+ str(pagenum) + " printed.")
        print()
        print()
        pagenum += 1
        pagetoscrape.find_element(By.XPATH, "//a[@aria-label='Next']").click()
        
        

    except NoSuchElementException:
        break
    
  
    
    #code to scrape data from different pages into a csv file and then add them to a new table on a database