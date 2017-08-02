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

    def sort(self):
        sorted = False
        length = len(self.addresses) - 1

        while not sorted:
            sorted = True
            for address in range(length):
                if self.addresses[address].get_full_address() > self.addresses[address + 1].get_full_address():
                    sorted = False
                    self.addresses[address], self.addresses[address + 1] = self.addresses[address + 1], self.addresses[address]

        return (self.addresses)