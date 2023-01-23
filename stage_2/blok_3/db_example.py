import dataclasses

from dataclasses_json import dataclass_json, LetterCase
from tinydb import TinyDB, Query

db = TinyDB("todo_db.json")
new_item = {"name": "Book", "quantity": 5}

db.insert(new_item)
print(db.all())

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclasses.dataclass
class Item:
    name: str
    quantity: int

db.insert(Item("Pen", 420).to_dict())

print(db.all())

items = [
         {"name": "Cake", "quantity": 1},
         {"name": "Candles", "quantity": 10},
         {"name": "Balloons", "quantity": 50},
         {"name": "Confetti", "quantity": 234565555672},
         {"name": "Glass", "quantity": 231004565555672},
         {"name": "Fireworks", "quantity": 10e7},
     ]
db.insert_multiple(items)
print(db.all())

print("Querying the db")
q = Query()
lots_of_items = db.search(q.quantity > 40)
print(lots_of_items)

# print("Clearing the database")
# db.drop_tables()
# print("After clearing")
# print(db.all())

