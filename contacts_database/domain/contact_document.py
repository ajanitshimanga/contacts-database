from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ContactDocument:

    uuid: UUID
    first_name: str
    last_name: str
    phone_number: int
