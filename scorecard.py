from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://crex.live"
def get_scorecard(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service('C:/Users/sarth/Desktop/lifeease/chromedriver-win64/chromedriver-win64/chromedriver.exe') 
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = f"{BASE_URL}{url}"
    driver.get(url) 
    batting_table = driver.find_elements(By.CSS_SELECTOR, "table.bowler-table")[0].find_element(By.CSS_SELECTOR, 'tbody').find_elements(By.CSS_SELECTOR, 'tr')
    batting_data = []
    
    for row in batting_table:

        decision = row.find_element(By.CSS_SELECTOR, 'div.decision').text
        player_name = row.find_element(By.CSS_SELECTOR, 'span.player-name').text
        runs = row.find_element(By.CSS_SELECTOR, 'div.run-highlight').text
        bowls = row.find_elements(By.CSS_SELECTOR, 'td')[2].find_element(By.CSS_SELECTOR, 'div').text
        fours = row.find_elements(By.CSS_SELECTOR, 'td')[3].find_element(By.CSS_SELECTOR, 'div').text
        sixs = row.find_elements(By.CSS_SELECTOR, 'td')[4].find_element(By.CSS_SELECTOR, 'div').text
        sr = row.find_elements(By.CSS_SELECTOR, 'td')[5].find_element(By.CSS_SELECTOR, 'div').text
        batting_data.append({
            'player_name': player_name,
            'decision': decision,
            'runs': runs,
            'bowls': bowls,
            'fours': fours,
            'sixs': sixs,
            'sr': sr
        })

    extras = driver.find_elements(By.CSS_SELECTOR, 'div.c-rate-or-extras')[1].find_elements(By.CSS_SELECTOR, 'span')[0].text
    extras += '('+driver.find_elements(By.CSS_SELECTOR, 'div.c-rate-or-extras')[1].find_elements(By.CSS_SELECTOR, 'span')[1].text+')'

    bowling_data = []
    bowling_table = driver.find_elements(By.CSS_SELECTOR, "table.bowler-table")[1].find_element(By.CSS_SELECTOR, 'tbody').find_elements(By.CSS_SELECTOR, 'tr')
    for row in bowling_table:
        player_name = row.find_element(By.CSS_SELECTOR, 'span.player-name').text
        overs = row.find_element(By.CSS_SELECTOR, 'div.run-highlight').text
        runs = row.find_elements(By.CSS_SELECTOR, 'td')[2].find_element(By.CSS_SELECTOR, 'div').text
        wickets = row.find_elements(By.CSS_SELECTOR, 'td')[3].find_element(By.CSS_SELECTOR, 'div').text
        econ = row.find_elements(By.CSS_SELECTOR, 'td')[4].find_element(By.CSS_SELECTOR, 'div').text
        bowling_data.append({
            'player_name':player_name,
            'overs':overs,
            'runs':runs,
            'wickets':wickets,
            'econ':econ
        })
    fow_data = []
    fow_table = driver.find_elements(By.CSS_SELECTOR, "table.bowler-table")[2].find_element(By.CSS_SELECTOR, 'tbody').find_elements(By.CSS_SELECTOR, 'tr')
    for row in fow_table:
        batsman = row.find_element(By.CSS_SELECTOR, 'span.player-name').text
        score = row.find_element(By.CSS_SELECTOR, 'div.run-highlight').text
        overs = row.find_elements(By.CSS_SELECTOR, 'td')[2].find_element(By.CSS_SELECTOR, 'div').text
        fow_data.append({
            'batsman': batsman,
            'score': score,
            'overs': overs
        })

    yet_to_bat = []
    upcoming = driver.find_elements(By.CSS_SELECTOR, 'div.player-data')
    for player in upcoming:
        yet_to_bat.append((player.find_element(By.CSS_SELECTOR, 'div').text,player.find_element(By.CSS_SELECTOR, 'span').text))

    partnerships = []
    partnershipsec = driver.find_elements(By.CSS_SELECTOR, 'div.p-section-wrapper')
    for part in partnershipsec:
        wicket = part.find_element(By.CSS_SELECTOR, 'div.p-wckt-info').text
        name1 = part.find_element(By.CSS_SELECTOR, 'p').text
        score1 = part.find_elements(By.CSS_SELECTOR, 'p')[1].text
        runs = part.find_element(By.CSS_SELECTOR, 'p.p-runs').text
        name2 = part.find_element(By.CSS_SELECTOR, 'p.p-right').text
        score2 = part.find_elements(By.CSS_SELECTOR, 'p.p-right')[1].text
        partnerships.append({
            'wicket':wicket,
            'name1':name1,
            'score1':score1,
            'runs':runs,
            'name2':name2,
            'score2':score2
        })

    return {
        'batting_table': batting_data,
        'bowling_table': bowling_data,
        'fow_data': fow_data,
        'yet_to_bat': yet_to_bat,
        'partnerships':partnerships
    }
    
