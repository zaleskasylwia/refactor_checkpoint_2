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

    @classmethod
    def create_from_csv(cls, list_name, csv_path):
        address_book = cls(list_name)

        with open(csv_path, 'r') as address_data:
            next(address_data)
            lines = address_data.readlines()
        table_with_addresses = [element.strip().split("\n") for element in lines]

        for line in table_with_addresses:
            if len(line) == 4:
                address = Address(line[0], line[1], line[2], line[3])
                address_book.add_address(address)

            elif len(line) == 5:
                address = WorkAddress(line[0], line[1], line[2], line[3], line[4])
                address_book.add_address(address)

        return address_book
