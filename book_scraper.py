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

    # Create a WebDriver instance without specifying executable_path
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
