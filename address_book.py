from address import Address
from work_address import WorkAddress
import csv


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
            for index in range(length):
                if self.addresses[index] > self.addresses[index + 1]:
                    sorted = False
                    self.addresses[index], self.addresses[index + 1] = self.addresses[index + 1], self.addresses[index]

        return (self.addresses)

    @classmethod
    def create_from_csv(cls, list_name, csv_path):
        address_book = cls(list_name)
        with open(csv_path) as csvfile:
            address_reader = csv.reader(csvfile)
            next(address_reader)  # skip heades
            for data in address_reader:
                company = data[4]
                if company:
                    address_book.add_address(WorkAddress(data[0], data[1], data[2], data[3], data[4]))
                else:
                    address_book.add_address(Address(data[0], data[1], data[2], data[3]))
        return address_book

    def save_to_csv(self):
        HEADERS = ['person', 'city', 'street', 'house_no', 'company']
        with open('{}.csv'.format(self.name), 'w', newline='') as csvfile:
            addresswriter = csv.writer(csvfile)
            addresswriter.writerow(HEADERS)
            for a in self.addresses:
                if isinstance(a, WorkAddress):
                    addresswriter.writerow([a.person, a.city, a.street, a.house_no, a.company])
                else:
                    addresswriter.writerow([a.person, a.city, a.street, a.house_no, ''])
