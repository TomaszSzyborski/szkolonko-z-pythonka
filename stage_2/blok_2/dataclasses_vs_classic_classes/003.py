# how to store a comment in web application

# Since previous version printed gibberish...
# or rather not gibberish but a place of object at memory
# we want to change it to be more human readable
# so we have to implement __repr method
from pprint import pprint

from dataclasses_vs_classic_classes.simulated_rest_api.api import get_comment


class Comment:
    def __init__(self, comment_id: int, text: str):
        self.comment_id = comment_id
        self.text = text

    # In case we have to use the representation... like print or log something.....
    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.comment_id}, text={self.text})"


comments_list = []
for _ in range(10):
    comment = get_comment()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text']))


for comment in comments_list:
    pprint(comment)
    # Ok... prints fine...