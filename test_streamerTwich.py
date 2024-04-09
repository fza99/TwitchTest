import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Sets up a Chrome WebDriver in mobile emulation mode."""
    mobile_emulation = {"deviceName": "Pixel 2"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_twitch_stream(driver):
    """Searches for a StarCraft II stream on Twitch, handles pop-ups, and takes screenshots."""
    #1 Go to twitch
    driver.get("https://www.twitch.tv")

    #2 Click in the search icon
    search_icon = driver.find_element(By.XPATH, "//a[contains(@href, '/search')]")
    search_icon.click()

    #input StarCraft II
    search_box = driver.find_element(By.XPATH, "//input[@type='search' and @placeholder='Rechercher...']")
    search_box.send_keys("StarCraft II")
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".CoreText-sc-1txzju1-0.lckOBr")))

    # scroll down 2 times
    for _ in range(2):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", driver.execute_script("return document.body"))

    #Select one streamer
    streamer_card = driver.find_element(By.CSS_SELECTOR, "a.ScCoreLink-sc-16kq0mq-0.kakgCs.tw-link[href*='/esl_sc2']")
    streamer_card.click()

    #On the streamer page wait until all is load and take a screenshot
    wait = WebDriverWait(driver, 15) 

    try:
        # More specific element for waiting
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "video.player-video__element")))
    except :
        # Handle potential loading issues gracefully
        print("Streamer video might not have loaded. Continuing...")
        pass

    try:
        # More specific pop-up detection
        popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-backdrop")))
        popup.find_element(By.CLASS_NAME, "modal-close").click()
    except :
        print("No pop-up found")
        pass

    time.sleep(2)
 
    #Take a screenshot
    screenshot_name = f"twitch_streamer_{time.time()}.png"
    driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved as: {screenshot_name}")