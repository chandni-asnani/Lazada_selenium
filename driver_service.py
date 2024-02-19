import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

load_dotenv()

def get_driver():

    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Choose Chrome Browser
    driver = webdriver.Chrome(service=Service(os.getenv("DRIVER_PATH")), options=chrome_options)

    return driver