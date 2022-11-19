# how to store a comment in web application

# Great, so now we have basics covered, I'd like to sort comments
# becasue I like them to be displayed in certain manner

import copy
from pprint import pprint

from simulated_rest_api.api import get_comment


class Comment:
    def __init__(self, comment_id: int, text: str):
        self.__comment_id = comment_id
        self.__text = text

    @property
    def comment_id(self):
        return self.__comment_id

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.__comment_id}, text={self.__text})"

    def __eq__(self, other):  # because we don't want to compare objects of different classes here
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text) == (other.__comment_id, other.__text)
        else:
            raise TypeError(f"Don't compare {self.__class__.__name__,} to {other.__class__.__name__,}")

    # optional - for improving performance
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.__class__, self.__comment_id, self.__text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text) < (other.comment_id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text) <= (other.comment_id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text) > (other.comment_id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text) >= (other.comment_id, other.text)
        else:
            return NotImplemented

comments_list = []
for _ in range(10):
    comment = get_comment()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text']))


print("Natural order of comments:")
print(comments_list)
print("Sorted order of comments:")
print(sorted(comments_list))


