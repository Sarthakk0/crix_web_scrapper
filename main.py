import requests
import schedule
import time
from bs4 import BeautifulSoup
from matchschedule import get_match_schedule
from livescore import get_live_score
from playing11 import get_playing11
from scorecard import get_scorecard



base_url='https://crex.live'
url = 'https://crex.live/fixtures/match-list'  # actual URL



result = []

def get_data():
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    match_links = []

    # matches = soup.find_all('li', class_='match-card-container')
    dates = [i.get_text(strip=True) for i in soup.find_all('div',class_='date')]
    data = soup.find_all('ul',class_='match-list-wrapper')
    i=0
    for date_wise in data:
        print("Date - ",dates[i])
        matches = date_wise.find_all('li', class_='match-card-container')
        for match in matches:
            print("*"*50)
            match_link = match.find('a', href=True)['href']
            match_links.append(match_link)
            match_status = match.find('div',class_='match-details')
            print(base_url+match_link)
            match_details_text = match_status.get_text(strip=True,separator = " ")
            print(match_details_text)
            print("*"*50)
            match_link = match_link.split("/")
            match_link.pop()
            match_link = "/".join(match_link)
            if "Live" in match_details_text:
                try:
                    livescore = get_live_score(match_link+"/live")
                    print(livescore)
                except:
                    livescore = "NA"
                    print("Unable to get live score try again later")
                try:
                    match_info = get_match_schedule(match_link+"/info")
                    print(match_info)
                except:
                    match_info = "NA"
                    print("Unable to get match schedule try again later")
                try:
                    p11 = get_playing11(match_link+"/info")
                    print(p11)
                except:
                    p11 = "NA"
                    print("Unable to get match info try again later")
                try:
                    scorecard = get_scorecard(match_link+"/scorecard")
                    print(scorecard)
                except:
                    scorecard = "NA"
                    print("Unable to get scorecard try again later")
                    
            else:
                try:
                    match_info = get_match_schedule(match_link+"/info")
                    print(match_info)
                except:
                    match_info = "NA"
                    print("Unable to get match schedule try again later")
            result.append(
                {
                    "match_info" : match_info ,
                    "livescore" : livescore,
                    "playing11" : p11,
                    "scorecard" : scorecard
                }
            )
        i+=1

if __name__ == "__main__":
    
    schedule.every(5).minutes.do(get_data)
    while True:
        schedule.run_pending()
        time.sleep(1)
