from time import sleep

from bs4 import BeautifulSoup
import requests as r
from selene import query
from selene.support.shared.jquery_style import s, ss

import bgg_collection_manipulation as collection
import bgg_game as game_page
import boardgamegeek_commons as bgg

bgg.login()
bgg.go_to_collection()
games = bgg.fetch_games_from_file("lotsa_games.csv")

# for game in games:
#     collection.add_game(game)

# sleep(5)  # for observability

# option to remove everything
# collection.remove_all_games()
#
# option to remove just thinks specified in a file
# for game in games:
#     collection.remove_game(game)
#
collection.go_to_random_game()

language_dependence_from_web = game_page.get_language_dependence()
print(f"{language_dependence_from_web=}")

# game_id = game_page.get_game_id()
game_page.unfold_language_dependence_poll()

list_of_votes = ss("//tr[@ng-controller='PollResultElement']//td[last()]")
votes = [int(element.get(query.text).strip()) for element in list_of_votes]
index_of_voted_answer = votes.index(max(votes))
dependence_in_poll = ss("//tr[@ng-controller='PollResultElement']//th")\
    .element(index_of_voted_answer)\
    .get(query.text)

print(f"{language_dependence_from_web=}")
print(f"{dependence_in_poll=}")


# votes_list = []
# for element in list_of_votes:
#     votes_list.append(element)

# endpoint = f"xmlapi/boardgame/{game_id}"
#
# fetched_xml = r.get(f"{bgg.browser.config.base_url}{endpoint}").text
# print(f"{fetched_xml=}")
#
# soup = BeautifulSoup(fetched_xml, 'lxml')
#
# print(soup.prettify())
#
# print(80 * "=")
# language_dependence_poll = soup.boardgames.boardgame.find("poll", {"name": "language_dependence"})
# # all results
# print(f"{language_dependence_poll=}")
#
# # all results
# print(f"{language_dependence_poll.results.find_all('result')=}")
#
# # just one result - the first one
# print(f"{language_dependence_poll.results.find('result')=}")
#
# # searching for max voted option
# print([result["numvotes"] for result in language_dependence_poll.results.find_all("result")])
#
# # finding max value
# max_voted_option = max([int(result["numvotes"]) for result in language_dependence_poll.results.find_all("result")])
# print(max_voted_option)
#
# most_voted_api = language_dependence_poll.results.find(numvotes=f"{max_voted_option}")["value"]
#
# print(f"{most_voted_api=}")
# print(f"{language_dependence_from_web=}")
#
# assert most_voted_api == language_dependence_from_web
# print("Success!!!")
