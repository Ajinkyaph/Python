from selenium import webdriver
import time
import pytest

path = r"E:\Software\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://demowebshop.tricentis.com/login")

@pytest.mark.dependency()
def test_login():
    # click Login
    time.sleep(2)
    driver.find_element("xpath", "//a[@class='ico-login']").click()
    # click Email
    time.sleep(2)
    driver.find_element("xpath", "//input[@id='Email']").send_keys("Priyankar.sarkar66@gmail.com")

    # click Password
    time.sleep(2)
    driver.find_element("xpath", "//input[@id='Password']").send_keys("PK1234")
    # click Remember_me
    time.sleep(2)
    driver.find_element("xpath", "//input[@id='RememberMe']").click()

    # click Register Button
    time.sleep(2)
    driver.find_element("xpath", "//input[@value='Log in']").click()

    


def test_log_out():
    time.sleep(2)
    driver.find_element("xpath", "//a[@class='ico-logout']").click()

# Loading the image
    driver.get_screenshot_as_file("screenshot.png")
