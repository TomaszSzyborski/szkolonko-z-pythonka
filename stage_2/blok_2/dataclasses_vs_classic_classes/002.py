# how to store a comment in web application

# However dict may only good to have within the same file
# and hopefully within 20-30 lines of code for easier access to the kyes - which are strings
# this may lead to human error - misspelling the key, which ends up with error AT RUNTIME
# so this is way to late - the test may fail on pipeline if not executed locally.
# the proposition is to create a class representing a model of the object
from pprint import pprint

from dataclasses_vs_classic_classes.simulated_rest_api.api import get_comment


class Comment:
    # observe that id is a built in keyword so the variable name should be
    # for example comment_id
    def __init__(self, comment_id: int, text: str):
        self.comment_id = comment_id
        self.text = text


comments_list = []
for _ in range(10):
    # fails because of Comment.__init__() got an unexpected keyword argument 'id'
    # comments_list.append(Comment(**get_comment()))
    comment = get_comment()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text']))


pprint(comments_list)
# Dammit it just prints:
# [<__main__.Comment object at 0x104637b50>,
#  <__main__.Comment object at 0x1048b6710>,
#  <__main__.Comment object at 0x1048b67a0>,
#  <__main__.Comment object at 0x1054c1e10>,
#  ...