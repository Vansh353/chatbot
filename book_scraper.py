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
    driver = webdriver.Chrome(options=options)  # Ensure you have chromedriver installed and in PATH

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

def main():
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
    
    # Add more custom responses based on the description
    if "mystery" in description.lower():
        print("Looks like this book is a mystery! Enjoy the thrill of solving it!")
    elif "romance" in description.lower():
        print("Ah, a romantic tale! Prepare to be swept off your feet!")
    elif "adventure" in description.lower():
        print("An adventurous journey awaits! Get ready for an exciting ride!")
    elif "fantasy" in description.lower():
        print("Welcome to a world of fantasy and magic! Let your imagination soar!")
    elif "inspirational" in description.lower():
        print("Prepare to be inspired! This book is sure to uplift your spirits!")
    
    elif "suspenseful" in description.lower():
        print("Get ready for a suspenseful and thrilling ride!")
    elif "heartwarming" in description.lower():
        print("This heartwarming tale will leave you with a smile!")
    elif "thought-provoking" in description.lower():
        print("Prepare to delve into deep thoughts and reflections!")
    elif "humorous" in description.lower():
        print("Get ready to laugh out loud with this humorous adventure!")
    elif "captivating" in description.lower():
        print("Get ready to be captivated from beginning to end!")
   
    
    # More custom responses based on themes or elements found in the description
    elif "epic" in description.lower():
        print("Embark on an epic journey with this book!")
    elif "gripping" in description.lower():
        print("Hold on tight! This gripping tale will keep you on the edge of your seat!")
    elif "emotional" in description.lower():
        print("Prepare for an emotional rollercoaster ride!")
    elif "enchanting" in description.lower():
        print("Experience the enchantment of this mesmerizing story!")
    elif "mind-bending" in description.lower():
        print("Get ready for a mind-bending adventure that will challenge your perceptions!")
    else:
        print("Immerse yourself in the world of this book and let it transport you!")

if __name__ == "__main__":
    main()
