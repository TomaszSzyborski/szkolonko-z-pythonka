from selene import query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def get_game_id():
    return browser.driver.current_url.split("/")[-2]


def get_language_dependence():
    return s("[item-poll-button='languagedependence'] .ng-binding").get(query.text)

def unfold_language_dependence_poll():
    return s("[item-poll-button='languagedependence'] button").click()
