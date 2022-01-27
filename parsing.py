from selenium import webdriver
import os
import time
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.flashscore.ru/basketball/brazil/nbb-2020-2021/results/'
chromedriver = "/Users/Mvideo/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

'''
driver.get(url)
time.sleep(10)
soup = BeautifulSoup(driver.page_source, "html.parser")


team_home_soup = soup.find_all('div', ["event__participant event__participant--home", "event__participant event__participant--home fontBold"])
team_away_soup = soup.find_all('div', ["event__participant event__participant--away", "event__participant event__participant--away fontBold"])
team_home = []
team_away = []
for tag in team_home_soup:
    team_home.append(tag.get_text())
for tag in team_away_soup:
    team_away.append(tag.get_text())


total_home_soup = soup.find_all('div', class_="event__score event__score--home")
total_away_soup = soup.find_all('div', class_="event__score event__score--away")
total_home = []
total_away = []
for tag in total_home_soup:
    total_home.append(int(tag.get_text()))
for tag in total_away_soup:
    total_away.append(int(tag.get_text()))


firstp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--1")
firstp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--1")
firstp_home = []
firstp_away = []
for tag in firstp_home_soup:
    firstp_home.append(int(tag.get_text()))
for tag in firstp_away_soup:
    firstp_away.append(int(tag.get_text()))


secondp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--2")
secondp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--2")
secondp_home = []
secondp_away = []
for tag in secondp_home_soup:
    secondp_home.append(int(tag.get_text()))
for tag in secondp_away_soup:
    secondp_away.append(int(tag.get_text()))


thirdp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--3")
thirdp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--3")
thirdp_home = []
thirdp_away = []
for tag in thirdp_home_soup:
    thirdp_home.append(int(tag.get_text()))
for tag in thirdp_away_soup:
    thirdp_away.append(int(tag.get_text()))


fourthp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--4")
fourthp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--4")
fourthp_home = []
fourthp_away = []
for tag in fourthp_home_soup:
    fourthp_home.append(int(tag.get_text()))
for tag in fourthp_away_soup:
    fourthp_away.append(int(tag.get_text()))
tech = []
for i in range(len(total_home)):
    if (total_home[i] == 0 and total_away[i] == 20) or (total_home[i] == 20 and total_away[i] == 0):
        tech.insert(0, i)
for i in tech:
    total_home.pop(i)
    total_away.pop(i)
    team_home.pop(i)
    team_away.pop(i)
'''

final_dataset = pd.DataFrame()

def make_dataset(url):
    driver.get(url)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    team_home_soup = soup.find_all('div', ["event__participant event__participant--home",
                                           "event__participant event__participant--home fontBold"])
    team_away_soup = soup.find_all('div', ["event__participant event__participant--away",
                                           "event__participant event__participant--away fontBold"])
    team_home = []
    team_away = []
    for tag in team_home_soup:
        team_home.append(tag.get_text())
    for tag in team_away_soup:
        team_away.append(tag.get_text())

    total_home_soup = soup.find_all('div', class_="event__score event__score--home")
    total_away_soup = soup.find_all('div', class_="event__score event__score--away")
    total_home = []
    total_away = []
    for tag in total_home_soup:
        total_home.append(int(tag.get_text()))
    for tag in total_away_soup:
        total_away.append(int(tag.get_text()))

    firstp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--1")
    firstp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--1")
    firstp_home = []
    firstp_away = []
    for tag in firstp_home_soup:
        firstp_home.append(int(tag.get_text()))
    for tag in firstp_away_soup:
        firstp_away.append(int(tag.get_text()))

    secondp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--2")
    secondp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--2")
    secondp_home = []
    secondp_away = []
    for tag in secondp_home_soup:
        secondp_home.append(int(tag.get_text()))
    for tag in secondp_away_soup:
        secondp_away.append(int(tag.get_text()))

    thirdp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--3")
    thirdp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--3")
    thirdp_home = []
    thirdp_away = []
    for tag in thirdp_home_soup:
        thirdp_home.append(int(tag.get_text()))
    for tag in thirdp_away_soup:
        thirdp_away.append(int(tag.get_text()))

    fourthp_home_soup = soup.find_all('div', class_="event__part event__part--home event__part--4")
    fourthp_away_soup = soup.find_all('div', class_="event__part event__part--away event__part--4")
    fourthp_home = []
    fourthp_away = []
    for tag in fourthp_home_soup:
        fourthp_home.append(int(tag.get_text()))
    for tag in fourthp_away_soup:
        fourthp_away.append(int(tag.get_text()))
    tech = []
    for i in range(len(total_home)):
        if (total_home[i] == 0 and total_away[i] == 20) or (total_home[i] == 20 and total_away[i] == 0):
            tech.insert(0, i)
    for i in tech:
        total_home.pop(i)
        total_away.pop(i)
        team_home.pop(i)
        team_away.pop(i)

    data = {'team_home': team_home,
            'team_away': team_away,
            'total_home': total_home,
            'total_away': total_away,
            'firstp_home': firstp_home,
            'firstp_away': firstp_away,
            'secondp_home': secondp_home,
            'secondp_away': secondp_away,
            'thirdp_home': thirdp_home,
            'thirdp_away': thirdp_away,
            'fourthp_home': fourthp_home,
            'fourthp_away': fourthp_away
            }
    dataset = pd.DataFrame(data)
    return dataset


final_dataset = pd.concat([final_dataset, make_dataset('https://www.flashscore.ru/basketball/brazil/nbb-2016-2017/results/')])
final_dataset = pd.concat([final_dataset, make_dataset('https://www.flashscore.ru/basketball/brazil/nbb-2017-2018/results/')])
final_dataset = pd.concat([final_dataset, make_dataset('https://www.flashscore.ru/basketball/brazil/nbb-2018-2019/results/')])
final_dataset = pd.concat([final_dataset, make_dataset('https://www.flashscore.ru/basketball/brazil/nbb-2019-2020/results/')])
final_dataset = pd.concat([final_dataset, make_dataset('https://www.flashscore.ru/basketball/brazil/nbb-2020-2021/results/')])


final_dataset.to_csv('full.csv')