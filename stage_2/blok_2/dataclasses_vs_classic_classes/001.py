# how to store a comment in web application

# Simplest choice is dict.
from pprint import pprint

from dataclasses_vs_classic_classes.simulated_rest_api.api import get_comment

comments_list = []
for _ in range(10):
    comments_list.append(get_comment())

pprint(comments_list)
