import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def scroll_until_found(driver, class_name, max_attempts=20):
    attempts = 0
    while attempts < max_attempts:
        # Scroll down
        driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(3)  # Wait for the page to load
        
        # Try to find the element
        try:
            element = driver.find_element(By.CLASS_NAME, class_name)
            print("Element found")
            return element  # Element found, return it
        except NoSuchElementException:
            # Element not found, increment attempts
            attempts += 1
            print(f"Attempt {attempts}/{max_attempts}: Element not found, scrolling more...")
        if attempts > 12:
            driver.execute_script("window.stop();")

    print("Reached max attempts, element not found")
    return None