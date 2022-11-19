# how to store a comment in web application

# I think I forgot something...
# Oh. The Author. Dammit.
# The API guy forgot it, but added it now, and I have to fix bunch of stuff...
# So let's add Author as a field,
# add it's property, change, the __repr__, __hash__ and all comparison functions.....
import copy
from pprint import pprint

from dataclasses_vs_classic_classes.simulated_rest_api.api import get_comment_with_author


class Comment:
    def __init__(self, comment_id: int, text: str, author: str):
        self.__author = author
        self.__comment_id = comment_id
        self.__text = text

    @property
    def comment_id(self):
        return self.__comment_id

    @property
    def text(self):
        return self.__text

    @property
    def author(self):
        return self.__author

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.__comment_id}, text={self.__text}, author={self.__author})"

    def __eq__(self, other):  # because we don't want to compare objects of different classes here
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text, self.__author) == (other.comment_id, other.text, other.author)
        else:
            raise TypeError(f"Don't compare {self.__class__.__name__,} to {other.__class__.__name__,}")

    # optional - for improving performance
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.__class__, self.__comment_id, self.__text, self.__author))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text, self.__author) < (other.comment_id, other.text, other.author)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text, self.__author) <= (other.comment_id, other.text, other.author)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text, self.__author) > (other.comment_id, other.text, other.author)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.__comment_id, self.__text, self.__author) >= (other.comment_id, other.text, other.author)
        else:
            return NotImplemented


comments_list = []
for _ in range(10):
    comment = get_comment_with_author()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text'], author=comment['author']))

#  Let's check if we didn't break anything....
print("Natural order of comments:")
print(comments_list)
print("Sorted order of comments:")
print(sorted(comments_list))
print(sorted(comments_list, reverse=True))

# as a final check, let's try make our Comment a tuple or dictionary
print((comments_list[0].comment_id, comments_list[0].text, comments_list[0].author))
print(comments_list[0].__dict__)
# not extremely beautiful...
