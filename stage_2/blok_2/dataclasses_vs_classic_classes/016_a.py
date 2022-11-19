# how to store a comment in web application

# What to do if we have two different endpoints?
# one with author and one without?
# Let's check what we can do within one model.
from dataclasses import dataclass, field
from typing import Optional, cast

from dataclasses_json import dataclass_json, config, LetterCase, Undefined

from simulated_rest_api.api import get_comment_with_author, get_comment, get_comment_with_lots_of_other_data


def possible_non_existent():
    sentinel = cast(object, None)
    return field(default=sentinel, metadata=config(exclude=lambda x: x is sentinel))


# Python naming conventions in class get automatically transformed to JSON compliant
# Undefined.EXCLUDE throws away any data not defined in this dataclass but present in json
@dataclass_json(letter_case=LetterCase.CAMEL,
                undefined=Undefined.EXCLUDE)
@dataclass(frozen=True, order=True)
class Comment:
    comment_id: int = field(metadata=config(field_name="id"))  # create an alias for the field actually in json
    text: str
    author: Optional[str] = possible_non_existent()
    replies: list = field(default_factory=list, compare=False, init=False, hash=False)


for source in [get_comment_with_author, get_comment, get_comment_with_lots_of_other_data]:
    comments_list = []
    for _ in range(10):
        comment = source()
        comments_list.append(Comment.from_dict(comment))

    first, *rest, last = comments_list
    print(comments_list[0])
    print(comments_list[0].to_json())
    # with sentinel value defined it sets Author to None if there is no author passed in the JSON
    # as a additional trick it leaves the "Author" if there is not one out of creating json
    #  withoutthe sentinel value we'd have "Author" : null" within the JSON
