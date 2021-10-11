from dataclasses import asdict

from contacts_database.domain.contact import Contact
from contacts_database.domain.contact_document import ContactDocument
from contacts_database.repository.contact_repository import ContactRepository
from contacts_database.service.elasticsearch_service import ElasticsearchService


class ElasticsearchContactRepository(ContactRepository):

    def __init__(self, elasticsearch_service: ElasticsearchService) -> None:
        self._es = elasticsearch_service

    def write_contact(self, contact: Contact) -> None:
        contact_document = ContactDocument(
            uuid=contact.uuid,
            first_name=contact.person.first_name,
            last_name=contact.person.last_name,
            phone_number=contact.phone_number
        )
        self._es.index_document(
            document=asdict(contact_document)
        )
