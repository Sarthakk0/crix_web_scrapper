from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://crex.live"

def fetch_playingxi(driver):
    playing=[]
    playerssec = driver.find_element(By.CSS_SELECTOR, 'div.playingxi-card')
    players = playerssec.find_elements(By.CSS_SELECTOR, 'div.p-name')
    for player in players:
        playing.append(player.text)
    return playing

def get_playing11(url):
    url = f"{BASE_URL}{url}"
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service('C:/Users/sarth/Desktop/lifeease/chromedriver-win64/chromedriver-win64/chromedriver.exe') 
    driver = webdriver.Chrome(service=service,options=chrome_options)

    driver.get(url)  
    driver.execute_script("document.querySelector('ins.adsbygoogle').style.display = 'none';")

    
    results = []
  
    playing_xi1=[]
    playing_xi2 = []
    btn = driver.find_elements(By.CSS_SELECTOR, "button.playingxi-button")[1]
    time.sleep(1)
    btn.click()
    time.sleep(1)
    playing_xi2 = fetch_playingxi(driver)
    btn = driver.find_elements(By.CSS_SELECTOR, "button.playingxi-button")[0]
    head = driver.find_element(By.CSS_SELECTOR, 'div.playingxi-header')
    driver.execute_script("arguments[0].scrollIntoView(true);", head)
    time.sleep(1)
    btn.click()
    time.sleep(1)
    playing_xi1 = fetch_playingxi(driver)

    header = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.playingxi-card"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", header)
    if playing_xi1 or playing_xi2:
        results =({
            'team1':playing_xi1,
            'team2':playing_xi2,
            })
    else:
        results = ("Could not retrieve live score.")
        
    return results
