# how to store a comment in web application

# There's too much too handle...
#  What if the API guy changes or adds another thing?
# Let's introduce dataclasses
import copy
import dataclasses
import inspect
from dataclasses import asdict, astuple, dataclass
from pprint import pprint

from dataclasses_vs_classic_classes.simulated_rest_api.api import get_comment_with_author


@dataclass(frozen=True, order=True)
class Comment:
    comment_id: int
    text: str
    author: str


comments_list = []
for _ in range(10):
    comment = get_comment_with_author()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text'], author=comment['author']))

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
# comment_to_be_checked.comment_id = 1
# when we uncomment above line we get AttributeError: can't set attribute 'comment_id' as expected now

print(comments_to_behaviour)
print(comments_to_behaviour[comment_to_be_checked])

print("Natural order of comments:")
print(comments_list)
print("Sorted order of comments:")
print(sorted(comments_list))
print(sorted(comments_list, reverse=True))

# transform to be dict and tuple:
print(astuple(comment_to_be_checked))
print(asdict(comment_to_be_checked))
# MUCH better then previous

# so what's behind the curtains?
pprint(inspect.getmembers(Comment, inspect.isfunction))


# But default generates these:
@dataclass
class DefaultComment:
    comment_id: int
    text: str
    author: str


print("Default dataclass atogenerated functions:")
pprint(inspect.getmembers(DefaultComment, inspect.isfunction))
