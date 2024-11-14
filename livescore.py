from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://crex.live"

def get_live_score(url):
    url = f"{BASE_URL}{url}"
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    service = Service('C:/Users/sarth/Desktop/lifeease/chromedriver-win64/chromedriver-win64/chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    innings_break = False
    text = driver.find_element(By.CSS_SELECTOR, 'div.result-box').text.strip()
    innings_break = (text == 'Innings Break') or (text == 'Players Entering')

    if not innings_break:
        try:
            player_name_element = driver.find_elements(By.CSS_SELECTOR, "div.batsmen-name")[0].find_element(By.CSS_SELECTOR, 'p')
        except:
            print('player 1 not found')
        try:
            player_name_element2 = driver.find_elements(By.CSS_SELECTOR, "div.batsmen-name")[1].find_element(By.CSS_SELECTOR, 'p')
        except:
            print('player 2 not found')
        try:
            bowler_element = driver.find_elements(By.CSS_SELECTOR, "div.batsmen-partnership")[2]
        except:
            print('bowler not found')
        try:
            bowler_name = bowler_element.find_element(By.CSS_SELECTOR, 'div.batsmen-name').find_element(By.CSS_SELECTOR, 'p').text
        except:
            print('bowler name not found')
        player_name1 = player_name_element.text
        player_name2 = player_name_element2.text
        batsman1_score = driver.find_elements(By.CSS_SELECTOR, "div.batsmen-score")[0]
        runs1 = batsman1_score.find_elements(By.CSS_SELECTOR, 'p')[0].text
        balls1 = batsman1_score.find_elements(By.CSS_SELECTOR, 'p')[1].text

        batsman2_score = driver.find_elements(By.CSS_SELECTOR, "div.batsmen-score")[1]
        runs2 = batsman2_score.find_elements(By.CSS_SELECTOR, 'p')[0].text
        balls2 = batsman2_score.find_elements(By.CSS_SELECTOR, 'p')[1].text

        batsman3_score = driver.find_elements(By.CSS_SELECTOR, "div.batsmen-score")[2]
        bowler_score = batsman3_score.find_elements(By.CSS_SELECTOR, 'p')[0].text
        bowler_overs = batsman3_score.find_elements(By.CSS_SELECTOR, 'p')[1].text

        batting_team = driver.find_element(By.CSS_SELECTOR, 'div.team-1').text
        runs = driver.find_element(By.CLASS_NAME, 'f-runs').find_elements(By.CSS_SELECTOR,'span')[0].text
        overs = driver.find_element(By.CLASS_NAME, 'f-runs').find_elements(By.CSS_SELECTOR,'span')[1].text
        

    last_ball = driver.find_element(By.CSS_SELECTOR, 'div.result-box').find_element(By.CSS_SELECTOR,'span').text
    required = driver.find_element(By.CSS_SELECTOR, 'div.final-result').text

    try:
        crr = driver.find_element(By.CSS_SELECTOR, 'div.team-run-rate').find_elements(By.CSS_SELECTOR,'span.data')[0].text
    except:
        crr = 'NA'
    try:
        rrr = driver.find_element(By.CSS_SELECTOR, 'div.team-run-rate').find_elements(By.CSS_SELECTOR,'span.data')[1].text
    except:
        rrr = 'NA'
    last_balls=[]

    


    return {
        'status':text,
        'crr':crr,
        'rrr':rrr,
        'required':required,
        'last_ball':last_ball,
        'runs': runs,
        'overs':overs,
        'bat_team': batting_team,
        "batsman1":player_name1,
        'batsman2': player_name2,
        'bowler': bowler_name,
        'runs1':runs1,
        'balls1':balls1,
        'runs2':runs2,
        'balls2':balls2,
        'bowler_score':bowler_score,
        'bowler_overs':bowler_overs
    }

