from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login():
    driver = webdriver.Chrome()

    try:
        # Navigate to URL
        driver.get("https://www.saucedemo.com/")

        # Maximize screen
        driver.maximize_window()

        # Check document state
        print("\n"+f"Document readyState: {driver.execute_script('return document.readyState;')}")

        # Set implicit wait ONCE
        driver.implicitly_wait(5)

        # Verify URL
        assert driver.current_url == "https://www.saucedemo.com/"

        # Input Username
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        # Input Password
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        # Click Login button
        login = driver.find_element(By.XPATH, "//input[@type='submit']")
        login.click()


        # Wait for login to complete
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        # Print current page info after login
        print(f"After login URL: {driver.current_url}")
        print(f"Page title: {driver.title}")

        # Find all "Add to cart" buttons
        add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        count = 0
        # Print text of all buttons
        for value in add_to_cart_buttons:

            count+=1
            print(f"Button text:{count}- {value.text}")

        # Click the second "Add to cart" button (index 1)
        if len(add_to_cart_buttons) > 1:
            add_to_cart_buttons[1].click()
            print("Clicked second 'Add to cart' button")
        else:
            print("Less than 2 buttons found!")

        # Click on cart link 
        cart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart.click()

        # Wait for cart page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        # Verify cart page URL
        print(f"Cart page URL: {driver.current_url}")
        print(f"Cart page title: {driver.title}")
        assert driver.current_url == "https://www.saucedemo.com/cart.html"

        print("Test completed successfully!")

    except Exception as e:
        print(f"Test failed: {e}")
        raise

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_login()