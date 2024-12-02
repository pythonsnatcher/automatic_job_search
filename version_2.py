from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import threading
import subprocess
import time
import threading


# Function to run caffeinate in the background
def keep_screen_active():
    subprocess.Popen(["caffeinate"])  # Prevent system from going into sleep mode
    while True:
        time.sleep(60)  # Keep running the caffeinate process


# Run the function in a separate thread
thread = threading.Thread(target=keep_screen_active)
thread.daemon = True
thread.start()

# Your existing script continues here...


# Function to move the mouse slightly every 60 seconds

# Load environment variables from the .env file
load_dotenv()

# Get email, password, keywords, and location from environment variables MANDATORY TO HAVE A '.ENV' FILE PREPARED
email_address = os.getenv("email_address")
password = os.getenv("password")
keywords = os.getenv("keywords")
location = os.getenv("location")

number_of_pages_to_search = 1000
number_of_cycles_per_page = 1
retry_limit = 50  # Set the retry limit for the first button

# Prompt the user for the remote work option
remote_work_preference = (

    input("Would you like to filter for remote work jobs? (yes/no): ").strip().lower()
    # 'no'
)

# Set up Chrome options
chrome_options = Options()
# Uncomment and specify if needed:
# chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Set up Chrome WebDriver using webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Navigate to Reed website
url = "https://www.reed.co.uk"
driver.get(url)

# Wait to ensure the page is fully loaded
time.sleep(3)
print("Navigated to Reed.co.uk")


# Function to click the consent button
def click_consent_button():
    try:
        consent_button = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        consent_button.click()
        print("Consent button clicked.")
        return True
    except Exception as e:
        print(f"Error clicking consent button: {e}")
        return False


# Click the consent button
if click_consent_button():
    print("Consent button clicked successfully!")
else:
    print("Failed to click the consent button.")

# Wait for a moment
time.sleep(1)


# Function to click the sign-in button
def click_sign_in_button():
    try:
        sign_in_button = driver.find_element(By.XPATH, '//*[@id="site-header"]/div[2]/div[1]/ul/li[2]/a')
        sign_in_button.click()
        print("Sign-in button clicked.")
        return True
    except Exception as e:
        print(f"Error clicking sign-in button: {e}")
        return False


# Click the sign-in button
if click_sign_in_button():
    print("Sign-in button clicked successfully!")
else:
    print("Failed to click the sign-in button.")

# Wait for the sign-in form to load
time.sleep(3)


# Function to insert email and password
def insert_email_and_password(email, password):
    try:
        # Find the email input field and insert the email
        email_input = driver.find_element(By.XPATH, '//*[@id="signin_email"]')
        email_input.send_keys(email)
        print(f"Email address {email} inserted successfully.")

        # Find the password input field and insert the password
        password_input = driver.find_element(By.XPATH, '//*[@id="signin_password"]')
        password_input.send_keys(password)
        print("Password inserted successfully.")
        return True
    except Exception as e:
        print(f"Error with email/password insertion: {e}")
        return False


# Insert email and password
if insert_email_and_password(email_address, password):
    print("Email and password entered successfully.")
else:
    print("Failed to enter email and/or password.")


# Function to click the continue button
def click_continue_button():
    try:
        continue_button = driver.find_element(By.XPATH, '//*[@id="signin_button"]')
        continue_button.click()
        print("Continue button clicked.")
        return True
    except Exception as e:
        print(f"Error clicking continue button: {e}")
        return False


# Click the continue button
if click_continue_button():
    print("Continue button clicked successfully!")
else:
    print("Failed to click the continue button.")

# Wait for the main search form to load
time.sleep(15)


# Function to insert keywords
def insert_keywords(keywords):
    try:
        keywords_input = driver.find_element(By.XPATH, '//*[@id="keywords"]')
        keywords_input.click()
        keywords_input.send_keys(keywords)
        print(f"Keywords '{keywords}' inserted successfully.")
        return True
    except Exception as e:
        print(f"Error inserting keywords: {e}")
        return False


# Insert keywords
if insert_keywords(keywords):
    print("Keywords inserted successfully!")
else:
    print("Failed to insert keywords.")


# Function to insert location
def insert_location(location):
    try:
        location_input = driver.find_element(By.XPATH, '//*[@id="location"]')
        location_input.click()
        location_input.send_keys(location)
        print(f"Location '{location}' inserted successfully.")
        return True
    except Exception as e:
        print(f"Error inserting location: {e}")
        return False


# Insert location
if insert_location(location):
    print("Location inserted successfully!")
else:
    print("Failed to insert location.")


# Function to click the search button
def click_search_button():
    try:
        search_button = driver.find_element(By.XPATH, '//*[@id="main-search"]/div[1]/div[3]/button')
        search_button.click()
        print("Search button clicked.")
        return True
    except Exception as e:
        print(f"Error clicking search button: {e}")
        return False


# Click the search button
if click_search_button():
    print("Search button clicked successfully!")
else:
    print("Failed to click the search button.")

time.sleep(5)


# Function to click the Easy Apply checkbox
def click_easy_apply_checkbox():
    try:
        # Check if the checkbox is already selected
        easy_apply_checkbox = driver.find_element(By.XPATH, '//*[@id="isEasyApply"]')

        if easy_apply_checkbox.is_selected():
            print("Easy Apply checkbox is already selected.")
            return True

        # Try to click using the first XPath method
        try:
            easy_apply_checkbox.click()
            print("Easy Apply checkbox clicked using XPath.")
            return True
        except Exception as e:
            print(f"Error clicking checkbox with XPath: ")

        # Try using CSS selector method
        try:
            easy_apply_checkbox = driver.find_element(By.CSS_SELECTOR, "#isEasyApply")
            easy_apply_checkbox.click()
            print("Easy Apply checkbox clicked using CSS selector.")
            return True
        except Exception as e:
            print(f"Error clicking checkbox with CSS selector:")

        # Try using JavaScript click if other methods fail
        try:
            driver.execute_script("arguments[0].click();", easy_apply_checkbox)
            print("Easy Apply checkbox clicked using JavaScript.")
            return True
        except Exception as e:
            print(f"Error clicking checkbox with JavaScript: ")

        # Fallback - report failure
        print("Failed to click Easy Apply checkbox after all attempts.")
        return False

    except Exception as e:
        print(f"Error locating Easy Apply checkbox: ")
        return False


# Attempt to click the Easy Apply checkbox with multiple methods
if click_easy_apply_checkbox():
    print("Easy Apply checkbox clicked successfully before applying for jobs.")
else:
    print("Failed to click Easy Apply checkbox.")

# Wait to observe the results
time.sleep(8)


# Function to click the Work from Home checkbox
def click_work_from_home_checkbox():
    try:
        # Locate the Work from Home checkbox using multiple strategies
        work_from_home_checkbox = driver.find_element(By.XPATH, '//*[@id="remoteWorkingOption"]')

        # Check if the checkbox is already selected
        if work_from_home_checkbox.is_selected():
            print("Work from Home checkbox is already selected.")
            return True

        # Try to click using the XPath
        try:
            work_from_home_checkbox.click()
            print("Work from Home checkbox clicked using XPath.")
            return True
        except Exception as e:
            print(f"Error clicking Work from Home checkbox with XPath: {e}")

        # Try using CSS Selector
        try:
            work_from_home_checkbox = driver.find_element(By.CSS_SELECTOR, "#remoteWorkingOption")
            work_from_home_checkbox.click()
            print("Work from Home checkbox clicked using CSS Selector.")
            return True
        except Exception as e:
            print(f"Error clicking Work from Home checkbox with CSS Selector: {e}")

        # Try using JavaScript click as a fallback
        try:
            driver.execute_script("arguments[0].click();", work_from_home_checkbox)
            print("Work from Home checkbox clicked using JavaScript.")
            return True
        except Exception as e:
            print(f"Error clicking Work from Home checkbox with JavaScript: {e}")

        # Fallback - report failure
        print("Failed to click Work from Home checkbox after all attempts.")
        return False

    except Exception as e:
        print(f"Error locating Work from Home checkbox: {e}")
        return False


# If the user wants to filter for remote work, click the checkbox
if remote_work_preference in ["yes", "y"]:
    print("You have chosen to filter for remote work jobs.")
    if click_work_from_home_checkbox():
        print("Work from Home checkbox clicked successfully.")
    else:
        print("Failed to click Work from Home checkbox. Continuing without this filter.")
else:
    print("You chose not to filter for remote work jobs. Proceeding as normal.")


def click_easy_apply_buttons_for_jobs():
    applied_jobs = []  # List to track applied jobs

    # Static XPaths for the second and third buttons (no need to change these)
    second_button_xpath = '//*[@id="__next"]/div[3]/div[2]/div[1]/div/div/div/div[2]/div/button'
    third_button_xpath = '//*[@id="__next"]/div[3]/div[2]/div[1]/div/div/div/span/button'

    # XPaths for the unchecked and checked buttons
    unchecked_button_xpath = "//button[@data-qa='applyJobBtn' and text()='Easy apply']"
    checked_button_xpath = "//button[@data-qa='applyJobBtn' and @disabled]"

    try:
        # Define a function to apply to jobs and return a list of applied jobs
        def apply_to_jobs():
            applied_this_round = []  # Track applied jobs in this round

            retry_count = 0  # Initialize retry counter

            # Locate all Easy Apply buttons on the page
            apply_buttons = driver.find_elements(By.XPATH, unchecked_button_xpath)
            print(f"Found {len(apply_buttons)} Easy Apply buttons that are unchecked.")

            # Iterate through the apply_buttons in cycles of first, second, and third button clicks
            num_buttons = len(apply_buttons)
            for idx in range(0, num_buttons):  # Iterate over all the first buttons
                try:
                    # First button (Easy Apply)
                    first_button = apply_buttons[idx]

                    # Retry clicking the first button until it works or retry limit is reached
                    while retry_count < retry_limit:
                        try:
                            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
                                                  first_button)
                            first_button.click()
                            # print(f"Clicked first Easy Apply button for Job {idx + 1}.")
                            break  # Exit the retry loop if successful
                        except Exception as e:
                            retry_count += 1
                            driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
                                                  first_button)
                            # print(f"Retry {retry_count}/{retry_limit} failed: . Trying again...")

                    # If after retries, it still didn't work, print a message and move to next job
                    if retry_count >= retry_limit:
                        # print(f"Failed to click Easy Apply button for Job {idx + 1} after {retry_limit} retries.")
                        retry_count = 0
                        continue  # Skip this job and move to the next one

                    # Wait for the second button to appear and click it
                    time.sleep(2)
                    second_button = driver.find_element(By.XPATH, second_button_xpath)
                    second_button.click()
                    # print(f"Clicked the second Easy Apply button for Job {idx + 1}.")

                    # Track this as a successful application after clicking the second button
                    applied_this_round.append(idx + 1)

                    # Wait for the third button to appear and click it
                    time.sleep(2)

                    try:
                        third_button = driver.find_element(By.XPATH, third_button_xpath)
                        third_button.click()
                        time.sleep(1)
                        third_button.click()  # Double click for confirmation
                        # print(f"Clicked the third Easy Apply button for Job {idx + 1}.")
                    except Exception as e:
                        third_button = driver.find_element(By.XPATH, third_button_xpath)
                        third_button.click()
                        # print("Continuing...")

                    # Add job index to applied_jobs list
                    applied_jobs.append(idx + 1)

                except Exception as e:
                    # print(f"Failed to process Easy Apply buttons for Job {idx + 1}. Error: ")
                    continue  # Continue with the next set of buttons if one fails
            time.sleep(3)
            print(applied_this_round)
            return applied_this_round

        # Loop through pages 1 to 10
        for page_number in range(1, number_of_pages_to_search):
            print(f"Processing Page {page_number}...")

            # Apply to jobs x times on the current page
            for _ in range(number_of_cycles_per_page):
                applied_jobs += apply_to_jobs()
                print(f"Applied for {len(applied_jobs)} jobs on Page {page_number}.")
                print('')

                # Scroll to the top of the page after applying
                driver.execute_script("window.scrollTo(0, 0);")

            # If it's not the last page, try to navigate to the next page using aria-label
            if page_number < number_of_pages_to_search:
                next_page_clicked = False
                retry_count = 0  # Initialize retry counter
                max_retries = 100  # Maximum number of retries

                next_page_selector = f'a[aria-label="Goto Page {page_number + 1}"]'

                while retry_count < max_retries and not next_page_clicked:
                    try:
                        next_page_button = WebDriverWait(driver, 2).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, next_page_selector))
                        )
                        actions = ActionChains(driver)
                        actions.move_to_element(next_page_button).perform()
                        time.sleep(1)

                        next_page_button.click()
                        print(f"Navigated to Page {page_number + 1}.")
                        next_page_clicked = True
                    except Exception as e:
                        retry_count += 1
                        next_page_button = WebDriverWait(driver, 2).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, next_page_selector))
                        )
                        actions = ActionChains(driver)
                        actions.move_to_element(next_page_button).perform()
                        time.sleep(1)

                        next_page_button.click()
                        print(f"Attempt {retry_count} failed: {e}. Retrying...")

                        time.sleep(1)

                        if retry_count >= max_retries:
                            print(f"Failed to navigate to Page {page_number + 1} after {max_retries} attempts.")

                            try:
                                exit_button = driver.find_element_by_xpath(
                                    '//*[@id="__next"]/div[3]/div[2]/div[1]/div/div/header/button')
                                exit_button.click()
                                print("Clicked the 'Exit' button using XPath.")
                            except Exception as xpath_error:
                                print(f"Failed to click 'Exit' button using XPath: {xpath_error}")
                                exit_button = driver.find_element_by_xpath(
                                    '//*[@id="__next"]/div[3]/div[2]/div[1]/div/div/header/button')
                                exit_button.click()

                                try:
                                    driver.execute_script(
                                        "document.querySelector('#__next > div.layout_content__49Kn9.layout_content_searchPage__nLFQv > div:nth-child(3) > div.modal.overflow-auto.fade.apply-job-modal_modal__Y8QOR.show.d-block > div > div > header > button').click()"
                                    )
                                    print("Clicked the 'Exit' button using JavaScript.")
                                    exit_button = driver.find_element_by_xpath(
                                        '//*[@id="__next"]/div[3]/div[2]/div[1]/div/div/header/button')
                                    exit_button.click()
                                except Exception as js_error:
                                    print(f"Failed to click 'Exit' button using JavaScript: {js_error}")
                                    exit_button = driver.find_element_by_xpath(
                                        '//*[@id="__next"]/div[3]/div[2]/div[1]/div/div/header/button')
                                    exit_button.click()

                            print(f"Skipping to next page after failing to exit loop on Page {page_number}.")
                            break

                    if not next_page_clicked:
                        print(f"Failed to navigate to the next page after Page {page_number}. Exiting.")
                        break

                    time.sleep(3)

        print(f"Total applied jobs: {len(applied_jobs)}")
        print(applied_jobs)
        return applied_jobs

    except Exception as e:
        print(f"Error finding Easy Apply buttons: {e}")
        return []  # Return empty list if error occurs



# Call the function to click the Easy Apply buttons and track applied jobs
applied_jobs = click_easy_apply_buttons_for_jobs()

# Print the jobs that were successfully applied for
if applied_jobs:
    print(f"Successfully applied for the following jobs: {', '.join(map(str, applied_jobs))}")
else:
    print("No jobs were successfully applied for.")

time.sleep(3)
