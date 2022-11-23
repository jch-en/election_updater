# program to pull number & percentage of votes from clarity elections

import schedule
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from git import Repo

# global variables of voting data
turnout_num = None
turnout_pct = None
robert_jonsen_num = None
robert_jonsen_pct = None
kevin_jensen_num = None
kevin_jensen_pct = None
veenker_num = None
veenker_pct = None
comsa_num = None
comsa_pct = None
summa_num = None
summa_pct = None
hamachek_num = None
hamachek_pct = None
forssell_num = None
forssell_pct = None
lythcotthaims_num = None
lythcotthaims_pct = None
lauing_num = None
lauing_pct = None
dharap_num = None
dharap_pct = None
campos_num = None
campos_pct = None
chiuwang_num = None
chiuwang_pct = None
segal_num = None
segal_pct = None


# webscraping function
def get_data(url, raw_path, percent_path):
    # creates driver instance
    s = Service("C:\Windows\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    # adds link to be web-scraped
    driver.get(url)
    # wait for raw data
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, raw_path)))
    # store the raw data
    raw_data = driver.find_element(By.CSS_SELECTOR, raw_path).text
    # wait for percent data
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, percent_path)))
    # store the percent data
    percent_data = driver.find_element(By.CSS_SELECTOR, percent_path).text
    # closes the driver
    driver.quit()
    return raw_data, percent_data


# voting turnout data
voting_turnout_url = "https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/turnout"
voting_turnout_raw_path = ".text"
voting_turnout_percent_path = "div[class='col'] div[class='value']"

# SC County sheriff election 2022 data, with the URL and CSS paths (acquired through selectorshub)
sheriff_url = "https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/detail/70"
robert_jonsen_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)"
robert_jonsen_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(2) > enr-bar:nth-child(3) > div:nth-child(2)"
kevin_jensen_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)"
kevin_jensen_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(3) > enr-bar:nth-child(3) > div:nth-child(2)"

# Palo Alto City Council election 2022 data, with the URL and CSS paths (acquired through selectorshub)
city_council_url = "https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/detail/84"
veenker_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)"
veenker_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(2) > enr-bar:nth-child(3) > div:nth-child(2)"
comsa_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)"
comsa_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(3) > enr-bar:nth-child(3) > div:nth-child(2)"
summa_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)"
summa_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(4) > enr-bar:nth-child(3) > div:nth-child(2)"
hamachek_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2)"
hamachek_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(5) > enr-bar:nth-child(3) > div:nth-child(2)"
forssell_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(2)"
forssell_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(6) > enr-bar:nth-child(3) > div:nth-child(2)"
lythcotthaims_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(7) > div:nth-child(2)"
lythcotthaims_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(7) > enr-bar:nth-child(3) > div:nth-child(2)"
lauing_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(8) > div:nth-child(2)"
lauing_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(8) > enr-bar:nth-child(3) > div:nth-child(2)"

# PAUSD School Board elections 2022 data, with the URL and CSS paths (acquired through selectorshub)
PAUSD_school_board_url = "https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/detail/43"
dharap_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)"
dharap_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(2) > enr-bar:nth-child(3) > div:nth-child(2)"
campos_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2)"
campos_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(3) > enr-bar:nth-child(3) > div:nth-child(2)"
chiuwang_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)"
chiuwang_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(4) > enr-bar:nth-child(3) > div:nth-child(2)"
segal_raw_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(2)"
segal_percent_path = "body > enr-root:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > enr-detail:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ngb-tabset:nth-child(2) > div:nth-child(2) > div:nth-child(1) > enr-areabreakdown-choices-results:nth-child(1) > div:nth-child(1) > div:nth-child(5) > enr-bar:nth-child(3) > div:nth-child(2)"


def update_vote_count():
    # turnout data
    global turnout_num, turnout_pct
    turnout_num, turnout_pct = get_data(voting_turnout_url, voting_turnout_raw_path, voting_turnout_percent_path)

    # jonsen data
    global robert_jonsen_num, robert_jonsen_pct
    robert_jonsen_num, robert_jonsen_pct = get_data(sheriff_url, robert_jonsen_raw_path, robert_jonsen_percent_path)

    # jensen data
    global kevin_jensen_num, kevin_jensen_pct
    kevin_jensen_num, kevin_jensen_pct = get_data(sheriff_url, kevin_jensen_raw_path, kevin_jensen_percent_path)

    # veenker data
    global veenker_num, veenker_pct
    veenker_num, veenker_pct = get_data(city_council_url, veenker_raw_path, veenker_percent_path)

    # comsa data
    global comsa_num, comsa_pct
    comsa_num, comsa_pct = get_data(city_council_url, comsa_raw_path, comsa_percent_path)

    # summa data
    global summa_num, summa_pct
    summa_num, summa_pct = get_data(city_council_url, summa_raw_path, summa_percent_path)

    # hamachek data
    global hamachek_num, hamachek_pct
    hamachek_num, hamachek_pct = get_data(city_council_url, hamachek_raw_path, hamachek_percent_path)

    # forssell data
    global forssell_num, forssell_pct
    forssell_num, forssell_pct = get_data(city_council_url, forssell_raw_path, forssell_percent_path)

    # lythcott-haims data
    global lythcotthaims_num, lythcotthaims_pct
    lythcotthaims_num, lythcotthaims_pct = get_data(city_council_url, lythcotthaims_raw_path, lythcotthaims_percent_path)

    # lauing data
    global lauing_num, lauing_pct
    lauing_num, lauing_pct = get_data(city_council_url, lauing_raw_path, lauing_percent_path)

    # dharap data
    global dharap_num, dharap_pct
    dharap_num, dharap_pct = get_data(PAUSD_school_board_url, dharap_raw_path, dharap_percent_path)

    # campos data
    global campos_num, campos_pct
    campos_num, campos_pct = get_data(PAUSD_school_board_url, campos_raw_path, campos_percent_path)

    # chiu-wang data
    global chiuwang_num, chiuwang_pct
    chiuwang_num, chiuwang_pct = get_data(PAUSD_school_board_url, chiuwang_raw_path, chiuwang_percent_path)

    # segal data
    global segal_num, segal_pct
    segal_num, segal_pct = get_data(PAUSD_school_board_url, segal_raw_path, segal_percent_path)


def last_updated():
    # creates datetime object
    dt = datetime.now()
    # get current day of week
    weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = weekday_list[dt.weekday()]
    # get current month
    month_list = ["Jan. ", "Feb. ", "March ", "April ", "May ", "June", "July", "Aug. ", "Sept. ", "Oct. ", "Nov. ", "Dec. "]
    month = month_list[dt.month - 1]
    # get numerical day
    day = dt.day
    # get current time, in AP format
    hours = dt.strftime('%I')
    if hours[0] == '0':
        hours = hours[1:]
    time = hours + ':' + dt.strftime('%M')
    if dt.strftime('%p') == 'AM':
        time = time + ' a.m.'
    if dt.strftime('%p') == 'PM':
        time = time + ' p.m.'

    statement = "Last updated " + str(day_of_week) + ", " + str(month) + str(day) + " at " + str(time)
    return statement


# use String format method to alter html
def get_html_string():
    my_string = '''<!DOCTYPE html>
    <span class="storycontent"><p><i><span style="font-weight: 400;">{html_last_updated}</span></i></p>
    <p><span style="font-weight: 400;">Here are the live results of this year's elections so far from {html_turnout_num} ballots cast, accounting for {html_turnout_pct} of <a href="https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/turnout">registered voters</a></span><span style="font-weight: 400;">.&nbsp;</span></p>
    <p><a href="https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/detail/70"><b>Sheriff</b></a><b> (one open seat)</b></p>
    <p><span style="font-weight: 400;">Robert 'Bob' Jonsen: {html_robert_jonsen_num}</span></p>
    <p>{html_robert_jonsen_pct}</p>
    <p><span style="font-weight: 400;">Kevin Jensen: {html_kevin_jensen_num}</span></p>
    <p>{html_kevin_jensen_pct}</p>
    <p><a href="https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/detail/84"><b>City Council</b></a><b> (three open seats)</b></p>
    <p><span style="font-weight: 400;">Vicki Veenker: {html_veenker_num}</span></p>
    <p><span style="font-weight: 400;">{html_veenker_pct}</span></p>
    <p><span style="font-weight: 400;">Ed Lauing: {html_lauing_num}</span></p>
    <p><span style="font-weight: 400;">{html_lauing_pct}</span></p>
    <p><span style="font-weight: 400;">Julie Lythcott-Haims: {html_lythcotthaims_num}</span></p>
    <p><span style="font-weight: 400;">{html_lythcotthaims_pct}</span></p>
    <p><span style="font-weight: 400;">Lisa Forssell: {html_forssell_num}</span></p>
    <p>{html_forssell_pct}</p>
    <p><span style="font-weight: 400;">Doria Summa: </span>{html_summa_num}</p>
    <p><span style="font-weight: 400;">{html_summa_pct}</span></p>
    <p><span style="font-weight: 400;">Alex Comsa: {html_comsa_num}</span></p>
    <p><span style="font-weight: 400;">{html_comsa_pct}</span></p>
    <p><span style="font-weight: 400;">Brian Hamachek: {html_hamachek_num}</span></p>
    <p><span style="font-weight: 400;">{html_hamachek_pct}</span></p>
    <p><a href="https://results.enr.clarityelections.com/CA/Santa_Clara/115971/web.307039/#/detail/43"><b>School Board</b></a><b> (two open seats)</b></p>
    <p><span style="font-weight: 400;">Shana Segal: {html_segal_num}</span></p>
    <p>{html_segal_pct}</p>
    <p><span style="font-weight: 400;">Shounak Dharap: {html_dharap_num}</span></p>
    <p><span style="font-weight: 400;">{html_dharap_pct}</span></p>
    <p><span style="font-weight: 400;">Nicole Chiu-Wang: {html_chiuwang_num}</span></p>
    <p>{html_chiuwang_pct}</p>
    <p><span style="font-weight: 400;">Ingrid Campos: {html_campos_num}</span></p>
    <p>{html_campos_pct}</p>
    </span>
    '''.format(
        html_last_updated=last_updated(),
        html_turnout_num=turnout_num,
        html_turnout_pct=turnout_pct,
        html_robert_jonsen_num=robert_jonsen_num,
        html_robert_jonsen_pct=robert_jonsen_pct,
        html_kevin_jensen_num=kevin_jensen_num,
        html_kevin_jensen_pct=kevin_jensen_pct,
        html_veenker_num=veenker_num,
        html_veenker_pct=veenker_pct,
        html_lauing_num=lauing_num,
        html_lauing_pct=lauing_pct,
        html_lythcotthaims_num=lythcotthaims_num,
        html_lythcotthaims_pct=lythcotthaims_pct,
        html_forssell_num=forssell_num,
        html_forssell_pct=forssell_pct,
        html_summa_num=summa_num,
        html_summa_pct=summa_pct,
        html_comsa_num=comsa_num,
        html_comsa_pct=comsa_pct,
        html_hamachek_num=hamachek_num,
        html_hamachek_pct=hamachek_pct,
        html_segal_num=segal_num,
        html_segal_pct=segal_pct,
        html_dharap_num=dharap_num,
        html_dharap_pct=dharap_pct,
        html_chiuwang_num=chiuwang_num,
        html_chiuwang_pct=chiuwang_pct,
        html_campos_num=campos_num,
        html_campos_pct=campos_pct
    )
    return my_string


# override html file with updated content
def write_to_html():
    f = open("index.html", "w")
    f.write(get_html_string())
    f.close()


# setting up for automated git push
PATH_OF_GIT_REPO = r"C:/Users/jonat/PycharmProjects/election_updater"  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from automated python script'


# automate push to git
def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except Exception:
        print('Some error occured while pushing the code')


# repeatable function that updates the HTML file
def complete_update_website():
    update_vote_count()
    write_to_html()
    git_push()


# update html file every hour
schedule.every(1).hour.do(complete_update_website)

while True:
    schedule.run_pending()
    time.sleep(1)

