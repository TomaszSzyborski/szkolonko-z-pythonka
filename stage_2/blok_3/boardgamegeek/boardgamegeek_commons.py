import csv
from collections import namedtuple
from typing import List

from selene.support.shared import browser
from selene.support.shared.jquery_style import s

Game = namedtuple("Game", ["title", "ownership"])

browser.config.browser_name = 'chrome'
browser.config.base_url = 'https://www.boardgamegeek.com/'
browser.config.timeout = 10


def login():
    user_name = ""
    password = ""

    browser.open(browser.config.base_url)
    browser.config.driver.maximize_window()

    s("//*[text()='Sign In']").click()
    s("#inputUsername").type(user_name)
    s("#inputPassword").type(password).press_enter()


def go_to_collection():
    s(".mygeek-dropdown-username").click()
    s("//a[@class='dropdown-item' and text()='Collection']").click()


def fetch_games_from_file(file_name="games.csv") -> List[Game]:
    games = []
    with open(file_name) as file:
        for game_data in csv.DictReader(file, delimiter=","):
            games.append(Game(game_data["Title"], game_data["Do I Have It?"]))
    return games

