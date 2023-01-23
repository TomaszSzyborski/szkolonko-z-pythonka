import random

from selene import be, have
from selene import query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

from boardgamegeek_commons import Game

def add_game(game: Game):

    s("a [alt='Add a Game']").click()
    s("input[name='geekitemname']").type(game.title)
    ss(".searchbox_results_title + *") \
        .wait_until(have.size_greater_than_or_equal(1))
    ss(".searchbox_results_title + *").first \
        .click()
    own_checkbox = s("#addowned")
    if own_checkbox.get(query.attribute("checked")) and game.ownership == "No":
        own_checkbox.click()
    elif not own_checkbox.get(query.attribute("checked")) and game.ownership == "Yes":
        own_checkbox.click()
    s("#addgame input[type='button']").click()
    s(".searchbox_results_title").wait_until(be.absent)


def remove_game(game: Game):
    s(f"//tr[.//td[contains(normalize-space(),'{game.title}')]]//*[@alt='remove']") \
        .hover().click()
    browser.switch_to.alert.accept()
    browser.driver.refresh()


def remove_all_games():
    games_to_be_removed = len(ss("td [alt='remove']"))
    print(games_to_be_removed)
    for _ in range(games_to_be_removed):
        remove_icon = s("img[alt='remove']")
        remove_icon.hover().click()
        browser.switch_to.alert.accept()
        browser.driver.refresh()


def go_to_random_game():
    size = len(ss("[id*='results_objectname'] a"))
    ss("[id*='results_objectname'] a")\
        .element(random.randint(0, size))\
        .click()
