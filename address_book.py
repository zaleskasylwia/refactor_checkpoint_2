from address import Address
from work_address import WorkAddress


class AddressBook:
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        if isinstance(address, Address):
            return self.addresses.append(address)
        else:
            raise TypeError

    def find(self, search_phrase):
        matching_addresses = []
        for address in self.addresses:
            if search_phrase.lower() in address.get_full_address().lower():
                matching_addresses.append(address)
        return matching_addresses