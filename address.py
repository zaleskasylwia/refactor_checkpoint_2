class Address:
    def __init__(self, person, city, street, house_no):
        self.person = person
        self.city = city
        self.street = street
        self.house_no = house_no

    def get_full_address(self):
        return "{}, {}, {} {}".format(self.person, self.city, self.street, self.house_no)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__