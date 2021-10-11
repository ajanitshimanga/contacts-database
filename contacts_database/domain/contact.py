from dataclasses import dataclass
from uuid import UUID

from contacts_database.domain.person import Person


@dataclass(frozen=True)
class Contact:

    uuid: UUID
    person: Person
    phone_number: int
