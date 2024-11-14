import requests
from bs4 import BeautifulSoup

BASE_URL = "https://crex.live"


def get_match_schedule(url):
    global matches
    get_url = f"{BASE_URL}{url}"
    response = requests.get(get_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    left_container = soup.find('div', class_='info-left-wrapper')
    right_container = soup.find('div', class_='info-right-wrapper')
    left_sections = left_container.find_all('div')
    league = left_sections[0].find('a').find('img').get('alt')
#     match_number = left_sections[0].find('a').find('div',class_='s-format').text
#     venue_detail_section = left_container.find('div', class_='venue-detail')
    
#     date = venue_detail_section.find('div', class_='match-date').find('div').text
#     team1 = left_container.find_all('div',class_='form-team-name')[0].text
#     team2 = left_container.find_all('div',class_='form-team-name')[1].text
#     format_match = left_container.find_all('div',class_='format-match')[0]
#     form_signs = format_match.find('div', class_='align-center')
#     signs = form_signs.find_all('div',class_='match')
#     last_matches_team1 = []
#     for sign in signs:
#         last_matches_team1.append(sign.text)
#     format_match2 = left_container.find_all('div',class_='format-match')[1]
#     form_signs2 = format_match2.find('div', class_='align-center')
#     signs2 = form_signs2.find_all('div',class_='match')
#     last_matches_team2 = []
#     for sign in signs2:
#         last_matches_team2.append(sign.text)

#     table1 = left_container.find_all('app-match-info-table')[0]
#     trs1 = table1.find_all('tr')
#     team_comparison = []
    
#     temp = left_container.find('div',class_='weather-temp').text
#     venue_match_cnt = left_container.find('div',class_='match-count').text
#     win_bat_first = left_container.find_all('span', class_='match-win-per')[0].text
#     win_bowl_first = left_container.find_all('span', class_='match-win-per')[1].text
#     avg_first_score = left_container.find_all('span',class_='venue-avg-val')[0].text
#     avg_sec_score = left_container.find_all('span',class_='venue-avg-val')[1].text
#     highest_total = left_container.find_all('span',class_='venue-score')[0].text if left_container.find_all('span',class_='venue-score') else ""
#     lowest_total = left_container.find_all('span',class_='venue-score')[1].text if left_container.find_all('span',class_='venue-score') else ""
#     highest_chased = left_container.find_all('span',class_='venue-score')[2].text if left_container.find_all('span',class_='venue-score') else ""
#     lowest_chased = left_container.find_all('span',class_='venue-score')[3].text if left_container.find_all('span',class_='venue-score') else ""
#     toss = right_container.find_all('div')[0].find('p').text
#     players = right_container.find_all('div',class_='playingxi-card-row')
#     playing_xi = []
#     for player in players:
#         pname = player.find('div', class_='p-name')
#         playing_xi.append(pname.text)

#     recent_matches = []
#     first_team = left_container.find_all('div', class_='global-match-team')
#     decisions = left_container.find_all('div', class_='match-dec-text')
#     second_team = left_container.find_all('div', class_='global-match-end')

#     for i in range(len(first_team)):
#         recent_matches.append(
#             f"{first_team[i].find('div', class_='team-name').text} ({first_team[i].find('div', class_='team-score').text},{first_team[i].find('div', class_='team-over').text}) VS {second_team[i].find('div', class_='team-name').text} ({second_team[i].find('div', class_='team-score').text},{second_team[i].find('div', class_='team-over').text}), Result - {decisions[i].text}"
#         )

#     match_info.append({
#         'league' : league,
#         'match_number' : match_number,
#         # 'venue' : venue,
#         'date' : date,
#         'team1' : team1,
#         'team2' : team2,
#         'last_matches_team1' : last_matches_team1,
#         'last_matches_team2' : last_matches_team2,
#         'temp' : temp,
#         'venue_match_cnt' : venue_match_cnt,
#         'win_bat_first' : win_bat_first,
#         'win_bowl_first' : win_bowl_first,
#         'avg_first_score' : avg_first_score,
#         'avg_sec_score' : avg_sec_score,
#         'highest_total' : highest_total,
#         'lowest_total' : lowest_total,
#         'highest_chased' : highest_chased,
#         'lowest_chased' : lowest_chased,
#         'toss' : toss,
#         'playing_xi' : playing_xi,
#         'recent_matches' : recent_matches
#     })

    try:
        match_number = left_sections[0].find('a').find('div', class_='s-format').text
    except Exception:
        match_number = ""

    try:
        venue_detail_section = left_container.find('div', class_='venue-detail')
        date = venue_detail_section.find('div', class_='match-date').find('div').text
    except Exception:
        date = ""

    try:
        team1 = left_container.find_all('div', class_='form-team-name')[0].text
    except Exception:
        team1 = ""

    try:
        team2 = left_container.find_all('div', class_='form-team-name')[1].text
    except Exception:
        team2 = ""

    try:
        format_match = left_container.find_all('div', class_='format-match')[0]
        form_signs = format_match.find('div', class_='align-center')
        signs = form_signs.find_all('div', class_='match')
        last_matches_team1 = [sign.text for sign in signs]
    except Exception:
        last_matches_team1 = []

    try:
        format_match2 = left_container.find_all('div', class_='format-match')[1]
        form_signs2 = format_match2.find('div', class_='align-center')
        signs2 = form_signs2.find_all('div', class_='match')
        last_matches_team2 = [sign.text for sign in signs2]
    except Exception:
        last_matches_team2 = []

    try:
        temp = left_container.find('div', class_='weather-temp').text
    except Exception:
        temp = ""

    try:
        venue_match_cnt = left_container.find('div', class_='match-count').text
    except Exception:
        venue_match_cnt = ""

    try:
        win_bat_first = left_container.find_all('span', class_='match-win-per')[0].text
    except Exception:
        win_bat_first = ""

    try:
        win_bowl_first = left_container.find_all('span', class_='match-win-per')[1].text
    except Exception:
        win_bowl_first = ""

    try:
        avg_first_score = left_container.find_all('span', class_='venue-avg-val')[0].text
    except Exception:
        avg_first_score = ""

    try:
        avg_sec_score = left_container.find_all('span', class_='venue-avg-val')[1].text
    except Exception:
        avg_sec_score = ""

    try:
        highest_total = left_container.find_all('span', class_='venue-score')[0].text if left_container.find_all('span', class_='venue-score') else ""
    except Exception:
        highest_total = ""

    try:
        lowest_total = left_container.find_all('span', class_='venue-score')[1].text if left_container.find_all('span', class_='venue-score') else ""
    except Exception:
        lowest_total = ""

    try:
        highest_chased = left_container.find_all('span', class_='venue-score')[2].text if left_container.find_all('span', class_='venue-score') else ""
    except Exception:
        highest_chased = ""

    try:
        lowest_chased = left_container.find_all('span', class_='venue-score')[3].text if left_container.find_all('span', class_='venue-score') else ""
    except Exception:
        lowest_chased = ""

    try:
        toss = right_container.find_all('div')[0].find('p').text
    except Exception:
        toss = ""

    try:
        players = right_container.find_all('div', class_='playingxi-card-row')
        playing_xi = [player.find('div', class_='p-name').text for player in players]
    except Exception:
        playing_xi = []

    try:
        recent_matches = []
        first_team = left_container.find_all('div', class_='global-match-team')
        decisions = left_container.find_all('div', class_='match-dec-text')
        second_team = left_container.find_all('div', class_='global-match-end')

        for i in range(len(first_team)):
            recent_matches.append(
                f"{first_team[i].find('div', class_='team-name').text} ({first_team[i].find('div', class_='team-score').text},{first_team[i].find('div', class_='team-over').text}) VS {second_team[i].find('div', class_='team-name').text} ({second_team[i].find('div', class_='team-score').text},{second_team[i].find('div', class_='team-over').text}), Result - {decisions[i].text}"
            )
    except Exception:
        recent_matches = []

    return {
        'league': league,
        'match_number': match_number,
        'date': date,
        'team1': team1,
        'team2': team2,
        'last_matches_team1': last_matches_team1,
        'last_matches_team2': last_matches_team2,
        'temp': temp,
        'venue_match_cnt': venue_match_cnt,
        'win_bat_first': win_bat_first,
        'win_bowl_first': win_bowl_first,
        'avg_first_score': avg_first_score,
        'avg_sec_score': avg_sec_score,
        'highest_total': highest_total,
        'lowest_total': lowest_total,
        'highest_chased': highest_chased,
        'lowest_chased': lowest_chased,
        'toss': toss,
        'playing_xi': playing_xi,
        'recent_matches': recent_matches
    }


  
