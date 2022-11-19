from dataclasses import dataclass
from typing import Optional

import requests as r
from dataclasses_json import dataclass_json, LetterCase, Undefined, CatchAll


def get_invoices(url):
    response = r.get(url)
    response.raise_for_status()
    return response.json()


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Company:
    company: str
    address: str
    country_code: str


@dataclass_json(letter_case=LetterCase.CAMEL, undefined=Undefined.INCLUDE)
@dataclass
class Invoice:
    invoice_id: int
    currency: str
    amount: float
    sku: str
    recipient: Optional[Company]
    unknown_things: CatchAll


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PureInvoice:
    invoice_id: int
    currency: str
    amount: float
    sku: str
    recipient: Optional[Company]


if __name__ == '__main__':
    data = get_invoices('https://demo.inspiredpython.com/invoices')
    print(data[0])
    print(isinstance(data[0], dict))
    some_invoice = Invoice.from_dict(data[0])
    print(some_invoice.to_json(ensure_ascii=True))

    some_data = {"invoice_id": "3",
                 "currency": "GBP",
                 "amount": "10000",
                 "sku": 123,
                 "recipient": None,
                 "SQL_INJECTION": "SELECT * FROM USERS;"}

    invoice = Invoice.from_dict(some_data)
    print(invoice)
    print(isinstance(invoice, Invoice))
    pure_invoice = PureInvoice.from_dict(some_data)
    print(pure_invoice)
    print(isinstance(pure_invoice, Invoice))
