from typing import List
from uuid import UUID

from contacts_database.domain.contact import Contact


class ContactRepository:

    def write_contact(self, contact: Contact) -> None:
        raise NotImplementedError

    def get_contacts_by_name(self) -> List[Contact]:
        raise NotImplementedError

    def get_contacts_by_number(self) -> List[Contact]:
        raise NotImplementedError

    def get_contact_by_uuid(self) -> Contact:
        raise NotImplementedError

    def update_contact(self, new_contact_info: Contact) -> None:
        # if the contact uuid is not in the data base. Just throw error? or call write_contact? choose one.
        raise NotImplementedError

    def delete_contact_by_uuid(self, contact_uuid: UUID) -> None:
        raise NotImplementedError
