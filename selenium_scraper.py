import pandas as pd
import time
from driver_service import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils import scroll_until_found
import os


class LazadaScrapper:

    def __init__(self, url):
        self.url = url
        self.driver = get_driver()
        self.data = []
        self.author_classes = ".mod-reviews .item .middle span:first-child"
        self.date_classes = ".mod-reviews .item .top span"
        self.review_body_classes = ".mod-reviews .item .content"
        self.empty_star_path = "//laz-img-cdn.alicdn.com/tfs/TB18ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"

    def get_webpage(self):
        try:
            self.driver.get(self.url)
        except TimeoutException:
            print("Page load timed out but continuing with the script.")
    
    def find_element(self, class_name):
        try:
            element = scroll_until_found(driver=self.driver, class_name=class_name)
            return element
        except Exception as e:
            print("Error finding element:", str(e))
            return None

    def get_totalPages(self):
        try:
            if self.find_element("next-pagination-list") is None:
                return 0
            review_pages = self.find_element("next-pagination-list")
            total_pages = int(review_pages.text.split("...")[-1])
            return total_pages
        except Exception as e:
            print("Error getting total pages:", str(e))
            return 0

    def get_reviews(self):
        total_pages = self.get_totalPages()
        full_star_path = "https://laz-img-cdn.alicdn.com/tfs/TB19ZvEgfDH8KJjy1XcXXcpdXXa-64-64.png"
        iteration = 1
        wait = WebDriverWait(self.driver, 10)

        while iteration <= total_pages:
            try:
                # Wait for the reviews container to load once per page
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".mod-reviews")))
                reviews = self.driver.find_elements(By.CSS_SELECTOR, ".mod-reviews .item")
                
                for review in reviews:
                    # Directly fetch required elements without redundant waits
                    try:
                        author = review.find_element(By.CSS_SELECTOR, self.author_classes).text
                        date = review.find_element(By.CSS_SELECTOR, self.date_classes).text
                        review_body = review.find_element(By.CSS_SELECTOR, self.review_body_classes).text
                        # Optimized star rating calculation
                        star_rating = len([x for x in review.find_elements(By.CSS_SELECTOR, ".star") if x.get_attribute("src") == full_star_path])
                        
                        row = {"review": review_body, "author": author, "date": date, "star_rating": star_rating}
                        self.data.append(row)
                    except NoSuchElementException:
                        print("Error finding review details.")
                    
                # Attempt to click the next page button
                next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next-btn.next")))
                next_button.click()
                print("Navigated to next page.")
            except TimeoutException as e:
                print("Timeout waiting for elements or next page button:", str(e))
                break  # Exit the loop if elements or button not found
            except Exception as e:
                print("General error:", str(e))
                break  # Exit the loop on unexpected error

            iteration += 1
            # Implicit wait before the next iteration, consider adjusting or removing based on actual page load times
            time.sleep(2)


    def close_browser(self):
        self.driver.quit()
    
    def export_data(self):
        df = pd.DataFrame(self.data)
        df.to_csv("lazada_reviews.csv", index=False)
        print(df)
        return df

    def run(self):
        self.get_webpage()
        self.get_reviews()
        self.export_data()
        self.close_browser()

url = os.getenv("LAZADA_URL")

lazada_scrapper = LazadaScrapper(url).run()