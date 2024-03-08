import time
from time import sleep
import pandas as pd
import csv

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

def Scrapper(job_role, counter):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                            options=option)
    
    sleep(2)
    driver.get(page_url.format(job_role))
    sleep(3)
    break_ = 0

    while break_ != -1:
        try:
            close_pop_btn = driver.find_element(By.XPATH, "//*[@id='mosaic-desktopserpjapopup']/div[1]/button")
            close_pop_btn.click()
            print("POP CLOSED!\n")
        except NoSuchElementException:
            print("NO POP UP!\n")
        
        job_page = driver.find_element(By.ID,"mosaic-jobResults")
        jobs = job_page.find_elements(By.CLASS_NAME,"job_seen_beacon") 

        for job in jobs:
            print("job counter", counter)
            #extarcting job details
            job_title = job.find_element(By.CLASS_NAME, 'jobTitle')
            title = job_title.text
            
            location = job.find_element(By.CLASS_NAME,"company_location").text,

            #extracting salary
            try: 
                salary = job.find_element(By.CLASS_NAME,"salary-snippet-container").text
            except NoSuchElementException: 
                try: 
                    salary = job.find_element(By.CLASS_NAME,"estimated-salary").text
                except NoSuchElementException:
                    salary = "None"

            #extracting job description
            job_title.click()
            sleep(2)
            try: 
                description = driver.find_element(By.ID,"jobDescriptionText").text
            except: 
                description = "None"
            
            print("Title: ", title)
            print("Location: ", location)
            print("Salary: ", salary)
            print("Description", description)
            print("\n")
                
            job_details = ([counter, job_role, title, location, salary, description])

            #adding data to csv file
            data_file = '/Users/ayankumar/Desktop/SkillQuest/data-base/data.csv'
            csv_writer(job_details)
            counter += 1
            
        try:
            print("Next Page\n")
            next_page_btn = driver.find_element(By.XPATH, f"//a[@data-testid='pagination-page-next']")
            next_page_btn.click()
        except NoSuchElementException:
            print("All Jobs Extracted!! \nMoving to next JOB ROLE")
            break_ = -1

    driver.quit()

    return counter

#adding data to csv file
def csv_writer(job_detaiils):
    data_file = '/Users/ayankumar/Desktop/SkillQuest/data-base/data.csv'
    with open(data_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(['Id', 'Job Category', 'Job Title', 'Location', 'Salary', 'Job Description'])
        #writer.writerow([counter, job_title, title, location, salary, desicription])
        writer.writerows([job_detaiils])



job_search_keyword = ['Data+Scientist', 'Data+Engineer', 'Data+Analyst', 'Machine+Learning',
                      'Software+Developer', 'Full+Stack+Developer', 'Frontend+Developer', 'Backend+Developer', 
                      'Devops+Engineer', 'UI/UX+Designer', 'Business+Analyst', 'System+Administrator', 
                      'Network+Administrator', 'Cloud+Engineer']

page_url = 'https://in.indeed.com/jobs?q={}'

counter = 0

for jobs in job_search_keyword:
    counter = Scrapper(jobs, counter + 1)