from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime, timedelta
from marshmallow import fields

@dataclass_json
@dataclass
class DataClassWithIsoDatetime:
    created_at: datetime = field(
        metadata=config(
            encoder=datetime.isoformat,
            decoder=datetime.fromisoformat,
            mm_field=fields.DateTime(format='iso')
        )
    )


just_now = DataClassWithIsoDatetime(datetime.now())
print(just_now)
print(just_now.to_dict())
print(just_now.to_json())

# end_date = datetime.now() - timedelta(days=10,hours=7)
# print(end_date)

from_date = DataClassWithIsoDatetime.from_dict({"created_at": "2022-06-25 16:41:33"})
print(from_date)

from_date = DataClassWithIsoDatetime.from_json('{"created_at": "2022-06-05"}')
print(from_date)