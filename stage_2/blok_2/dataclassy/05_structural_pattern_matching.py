import base64
import string

import dataclasses_json
import requests as r
from dataclasses_json import dataclass_json, LetterCase, Undefined, CatchAll, config


def get_invoices(url):
    response = r.get(url)
    response.raise_for_status()
    return response.json()


from dataclasses import dataclass, field
from typing import Optional


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


def process_raw_recipient(raw_recipient):
    match raw_recipient:
        case {"company": company, "address": address, "country_code": country_code}:
            return Company(company=company, address=address, country_code=country_code)
        case _:
            raise ValueError(f"Cannot parse invoice recipient {raw_recipient}")


def process_raw_invoice(raw_invoice):
    match raw_invoice:
        case {
            "invoice_id": invoice_id,
            "currency": currency,
            "amount": amount,
            "sku": sku,
        }:
            return Invoice(
                invoice_id=invoice_id,
                currency=currency,
                amount=amount,
                sku=sku,
                recipient=None,
            )
        case _:
            raise ValueError(f"Cannot parse invoice {raw_invoice}")


def process_raw_records(records):
    invoices = []
    for record in records:
        match record:
            case {"recipient": raw_recipient, **raw_invoice}:
                recipient = process_raw_recipient(raw_recipient)
                invoice = process_raw_invoice(raw_invoice)
                invoice.recipient = recipient
                invoices.append(invoice)
            case _:
                raise ValueError(f"Cannot parse structure {record}")
    return invoices


if __name__ == '__main__':
    data = get_invoices('https://demo.inspiredpython.com/invoices')
    print(data[0])
    # {'recipient': {'company': 'Schuchhardt GmbH & Co. OHG', 'address': 'Philip-Plath-Gasse 4\n39694 Olpe',
    #                'country_code': 'DE'}, 'invoice_id': 34809, 'currency': 'GBP', 'amount': 639.16,
    #  'sku': 'PROPANE-ACCESSORIES'}
    #
    some_invoice = None
    for result in process_raw_records(get_invoices("https://demo.inspiredpython.com/invoices/")):
        print(result)
        some_invoice = result

    print(some_invoice.to_json(ensure_ascii=False))
    some_data = {"invoice_id": "3",
                 "currency": "GBP",
                 "amount": "10000",
                 "sku": 123,
                 "recipient": None,
                 "SQL_INJECTION": "SELECT * FROM USERS;"}

    invoice = Invoice.from_dict(some_data)
    print(invoice)
    print(isinstance(invoice, Invoice))
