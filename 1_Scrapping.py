from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

job_search_keyword = ['Data+Scientist', 'Data+Engineer', 'Data+Analyst', 'Machine+Learning', 
                      'Software+Developer', 'Full+Stach+Developer', 'Frontend+Developer', 
                      'Backend+Developer', 'Devops+Engineer', 'Business+Analyst']

