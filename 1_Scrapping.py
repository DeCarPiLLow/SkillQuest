import time
from time import sleep
from random import randint
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

job_search_keyword = ['Data+Scientist', 'Data+Engineer', 'Data+Analyst', 'Machine+Learning', 
                      'Software+Developer', 'Full+Stach+Developer', 'Frontend+Developer', 
                      'Backend+Developer', 'Devops+Engineer', 'Business+Analyst']

page_url = 'https://in.indeed.com/jobs?q={}'

start = time.time()

job_lst=[]
job_description_list=[]
salary_list = []

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                          options=option)
sleep(3)
counter = 1
br = 0

for job_title in job_search_keyword:
    
    driver.get(page_url.format(job_title))
    driver.get(page_url.format("data analyst"))
    sleep(3)

    while br != -1:
        try:
            close_pop_btn = driver.find_element(By.XPATH, "//*[@id='mosaic-desktopserpjapopup']/div[1]/button")
            close_pop_btn.click()
        except NoSuchElementException:
            print("page closed")
        
        job_page = driver.find_element(By.ID,"mosaic-jobResults")
        jobs = job_page.find_elements(By.CLASS_NAME,"job_seen_beacon") 

        for jj in jobs:
            print("job counter", counter)
            counter += 1

            job_title = jj.find_element(By.CLASS_NAME,"jobTitle")

            job_lst.append([job_title.text,
            job_title.find_element(By.CSS_SELECTOR,"a").get_attribute("href"),
            job_title.find_element(By.CSS_SELECTOR,"a").get_attribute("id"),           
            jj.find_element(By.CLASS_NAME,"company_location").text,
            job_title.find_element(By.CSS_SELECTOR,"a").get_attribute("href")])

            try: 
                salary_list.append(jj.find_element(By.CLASS_NAME,"salary-snippet-container").text)

            except NoSuchElementException: 
                try: 
                    salary_list.append(jj.find_element(By.CLASS_NAME,"estimated-salary").text)
                
                except NoSuchElementException:
                    salary_list.append(None)
    
            # job_title.click()
            # sleep(randint(3, 5))
            # try: 
            #     job_description_list.append(driver.find_element(By.ID,"jobDescriptionText").text)
            # except: 
            #     job_description_list.append(None)
            
        try:
            print("clicking next page")
            next_page_btn = driver.find_element(By.XPATH, f"//a[@data-testid='pagination-page-next']")
            next_page_btn.click()
        except NoSuchElementException:
            br = -1

    driver.quit()


