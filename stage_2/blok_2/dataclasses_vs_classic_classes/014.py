# how to store a comment in web application

# See! I thought that the guy changed the requirements.
# Now it has to have list of replies in the thread...
# easy peasy

from dataclasses import dataclass, field

from dataclasses_vs_classic_classes.simulated_rest_api.api import get_comment_with_author


@dataclass(frozen=True, order=True)
class Comment:
    comment_id: int
    text: str
    author: str
    replies: list = field(default_factory=list, compare=False, init=False, hash=False)
    # we want to get rid of replies from hashing, comparing and being put as initializer parameter


comments_list = []
for _ in range(10):
    comment = get_comment_with_author()
    comments_list.append(Comment(comment_id=comment["id"], text=comment['text'], author=comment['author']))

first, *rest, last = comments_list

print(f"Replies to first comment: {first.replies=}")
print(f"Replies to last comment: {last.replies=}")

# So far so good.
first.replies.append("This comment sucks!")
print(f"Replies to first comment: {first.replies=}")
print(f"Replies to last comment: {last.replies=}")  # We're good.
