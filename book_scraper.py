import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_book_info(book_title):
    """
    Fetch book description and URL of the book page from the provided Goodreads book URL using Selenium.
    """
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Set the PATH environment variable to include the directory containing chromedriver
    os.environ["PATH"] += ":/home/vansh/.cache/selenium/chromedriver/linux64/121.0.6167.184/"

    # Create a WebDriver instance
    driver = webdriver.Chrome(options=options)

    try:
        # Construct the Goodreads search URL
        search_url = f"https://www.goodreads.com/search?q={book_title.replace(' ', '+')}"
        driver.get(search_url)

        # Get the URL of the first search result
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'bookTitle'))
        )
        book_url = first_result.get_attribute('href')
        driver.get(book_url)

        # Wait for the description element to be loaded
        description_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='description']"))
        )
        description = description_element.text.strip()
    finally:
        driver.quit()

    return description, book_url

if __name__ == "__main__":
    book_title = input("Enter the title of the book: ")
    description, book_url = fetch_book_info(book_title)
    
    if description:
        print("Here is a brief summary of the book:")
        print(description) 
   
    else:
        print("Sorry, I couldn't find a description for that book.")
        
    if book_url:
        print("You can find more information about the book here:", book_url)
    else:
        print("Sorry, I couldn't find a link for that book.")
