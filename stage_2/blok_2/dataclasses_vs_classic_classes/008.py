# how to store a comment in web application

# We're awesome. We have everything we need.
# but... let's fiddle around a bit...

import copy
from pprint import pprint

from dataclasses_vs_classic_classes.simulated_rest_api.api import get_comment


class Comment:
    def __init__(self, comment_id: int, text: str):
        self.comment_id = comment_id
        self.text = text

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.comment_id}, text={self.text})"

    def __eq__(self, other):  # because we don't want to compare objects of different classes here
        if other.__class__ is self.__class__:
            return (self.comment_id, self.text) == (other.comment_id, other.text)
        else:
            raise TypeError(f"Don't compare {self.__class__.__name__,} to {other.__class__.__name__,}")

    # optional - for improving performance
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.__class__, self.comment_id, self.text))


comments_list = []
for _ in range(10):
    comment = get_comment()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text']))

comment_to_be_checked = copy.deepcopy(comments_list[0])
assert comment_to_be_checked in comments_list
# awesome, assertion passes

# assert get_comment() in comments_list
# shit. But we're good... were good.

assert comment_to_be_checked == comments_list[0]
assert comment_to_be_checked != comments_list[1]

# Good. now lets create a dictionary
comments_to_behaviour = {comment_to_be_checked: "The one I check"}
print(comments_to_behaviour)
print(comments_to_behaviour[comment_to_be_checked])
# prints nicely now...

# let's be evil again
comment_to_be_checked.comment_id = 1

print(comments_to_behaviour)
print(comments_to_behaviour[comment_to_be_checked])

# Fuck.
# KeyError: Comment(id=1, text=Stay owner experience just sign. Difference house fire box training. Hear
# attention nice turn read. Throw night relate manager. Parent you itself our. Become song want time may. Group sound
# music.)

