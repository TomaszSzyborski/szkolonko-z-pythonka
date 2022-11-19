# how to store a comment in web application

# So we waqnt to fetch a comment and check if it's already in our database
# of... I don't know... Naughty comments?
# whatever...
# IN THE DATABASE
# to ensure we display everything right, or something in these lines.
import copy
from pprint import pprint

from simulated_rest_api.api import get_comment


class Comment:
    def __init__(self, comment_id: int, text: str):
        self.comment_id = comment_id
        self.text = text

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.comment_id}, text={self.text})"


comments_list = []
for _ in range(10):
    comment = get_comment()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text']))

comment_to_be_checked = comments_list[0]

# Let's check it - it has to be in the list, we just got it FROM the list, right?
assert comment_to_be_checked in comments_list

#  oof, that's awesome, let's check further
assert comment_to_be_checked == comments_list[0]

# wait... what if some hacker wants to do something malicious like...
# print(f"{comment_to_be_checked}")
# print(f"{comments_list}")
print(f"{comment_to_be_checked.comment_id=}")
print(f"{comments_list[1].comment_id=}")

# let's be evil and assign the same comment id
print("Prior ID swap")
print(f"Extracted comment id {comment_to_be_checked.comment_id}")
print(f"Listed comment id {comments_list[0].comment_id}")
print(f"Swapped comment id {comments_list[1].comment_id}")
comment_to_be_checked.comment_id = comments_list[1].comment_id

print("After swap")
print(f"{comment_to_be_checked}")
print(f"{comments_list[1]}")
print(f"{comment_to_be_checked.comment_id=}")
print(f"{comments_list[1].comment_id=}")
assert comment_to_be_checked == comments_list[0]  # WAIT WHAT?
# WTF JUST HAPPENED - I changed the value of a field and it doesn't fails the assertion?

comment_to_be_checked.text = comments_list[1].text

# huh...
assert comment_to_be_checked == comments_list[0]  # WAIT WHAT? it... passes? Let's print to doublecheck
print(f"{comment_to_be_checked}")
print(f"{comments_list[0]}")

# oh... oooooooohhhh, Let's pass value and not references right?
comment_to_be_checked = copy.deepcopy(comments_list[0])
assert comment_to_be_checked in comments_list  # yeah now what?
