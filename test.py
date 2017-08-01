import unittest
import sys
import os
import copy


class TestCheckpointExcersise(unittest.TestCase):

    # Addreses tests

    def test_step01_address_person(self):
        self.assertEqual("Jan Kowalski", self.get_address().person)

    def test_step02_get_full_address(self):
        self.assertEqual('Jan Kowalski, Kraków, ul. Daszyńskiego 15/31',
                         self.get_address().get_full_address())

    def test_step03_address_eq(self):
        from address import Address
        first = Address("Jan Kowalski", "Kraków",
                        "ul. Daszyńskiego", "15/31")
        second = Address("Jan Kowalski", "Kraków",
                         "ul. Daszyńskiego", "15/31")
        self.assertEqual(first, second)

    def test_step04_address_not_eq(self):
        from address import Address
        first = Address("Jan Kowalski", "Kraków",
                        "ul. Daszyńskiego", "15/31")
        second = Address("Jan Kowalski", "Kraków",
                         "ul. Daszyńskiego", "16/31")
        self.assertNotEqual(first, second)

    def test_step05_work_address_person(self):
        self.assertEqual("Adam Adamski", self.get_work_address().person)

    def test_step06_company(self):
        self.assertEqual("Mordor sp. z o.o.", self.get_work_address().company)

    def test_step07_get_full_work_address(self):
        self.assertEqual(
                         'Adam Adamski, Warszawa, ul.' +
                         ' Domaniewska 6/66, Mordor sp. z o.o.',
                         self.get_work_address().get_full_address())

    def test_step08_work_address_eq(self):
        from work_address import WorkAddress
        first = WorkAddress("Adam Adamski", "Warszawa",
                            "ul. Domaniewska", "6/66", "Mordor sp. z o.o.")
        second = WorkAddress("Adam Adamski", "Warszawa",
                             "ul. Domaniewska", "6/66", "Mordor sp. z o.o.")
        self.assertEqual(first, second)

    def test_step09_work_address_not_eq(self):
        from work_address import WorkAddress
        first = WorkAddress("Adam Adamski", "Warszawa",
                            "ul. Domaniewska", "6/66", "Mordor sp. z o.o.")
        second = WorkAddress("Adam Adamski", "Warszawa",
                             "ul. Domaniewska", "6/66", "Hobbit sp. z o.o.")
        self.assertNotEqual(first, second)

    def test_step10_work_and_address_not_eq(self):
        from address import Address
        from work_address import WorkAddress
        first = Address("Adam Adamski", "Warszawa",
                        "ul. Domaniewska", "6/66")
        second = WorkAddress("Adam Adamski", "Warszawa",
                             "ul. Domaniewska", "6/66", "Hobbit sp. z o.o.")
        self.assertNotEqual(first, second)

    # AddressBook

    def test_step11_address_book_name(self):
        from address_book import AddressBook
        self.my_book = AddressBook("friends")
        self.assertEqual("friends", self.my_book.name)

    def test_step12_address_book_add_address(self):
        self.add_addresses_to_book()
        self.assertEqual(2, len(self.my_book.addresses))

    def test_step13_address_book_type_error(self):
        from address_book import AddressBook
        book = AddressBook("Test")
        with self.assertRaises(TypeError, msg="Test dupy się nie powiódł ;("):
            book.add_address("dupa")

    def test_step14_address_book_find_returns_empty(self):
        self.add_addresses_to_book()
        self.assertListEqual([], self.my_book.find("XXX"),
                             msg="Should return empty list")

    def test_step15_address_book_find_returns_one(self):
        self.add_addresses_to_book()
        expected = [self.my_book.addresses[0]]
        actual = self.my_book.find("Kraków")
        self.assertListEqual(expected, actual)

    def test_step16_address_book_find_returns_many(self):
        self.add_addresses_to_book()
        expected = self.my_book.addresses
        actual = self.my_book.find("ski")
        self.assertListEqual(expected, actual)

    def test_step17_address_book_find_case_insensitive(self):
        self.add_addresses_to_book()
        expected = [self.my_book.addresses[1]]
        actual = self.my_book.find("adam")
        self.assertListEqual(expected, actual,
                             msg="Search should be case insensitive")

    def test_step18_sort(self):
        import address_book
        address_book.sorted = None  # remove sorted function
        self.add_addresses_to_book()
        expected = [self.get_work_address(), self.get_address()]
        self.my_book.sort()
        self.assertListEqual(expected, self.my_book.addresses)

    def test_step19_sort_2(self):
        import address_book
        address_book.sorted = None  # remove sorted function
        expected = self.create_address_book()
        actual = copy.deepcopy(expected)
        actual.sort()
        expected.sort()
        self.assertListEqual(expected.addresses, actual.addresses)

    def test_step20_builtin_sort(self):
        with open("address_book.py", "r") as f:
            content = f.read()
            self.assertEqual(content.find("addresses.sort"), -1,
                             msg="Don't use built in sort function!")


    # 2nd part tests

    def test_step21_create_from_csv_length(self):
        from address_book import AddressBook
        book = AddressBook.create_from_csv("book_name", "addresses.csv")
        self.assertIsInstance(book, AddressBook)
        self.assertEqual(5, len(book.addresses))

    def test_step22_create_from_csv_name(self):
        from address_book import AddressBook
        book_name = "book_name"
        book = AddressBook.create_from_csv("book_name", "addresses.csv")
        self.assertEqual("book_name", book.name)

    def test_step23_create_from_csv_addresses(self):
        from address_book import AddressBook
        expected = self.create_address_book().addresses
        book = AddressBook.create_from_csv("book_name", "addresses.csv")
        actual = book.addresses
        self.assertListEqual(expected, actual)

    def test_step24_save_to_csv(self):
        from address_book import AddressBook
        book_name = "book_name"
        book = AddressBook.create_from_csv("book_name", "addresses.csv")

        # remove old file so that we have a guarantee that a file is generated
        try:
            os.remove(book.name + ".csv")
        except:
            pass

        book.save_to_csv()

        with open("addresses.csv") as org, open(book.name + ".csv") as copy:
            are_equal = org.readlines() == copy.readlines()

        self.assertTrue(are_equal, msg="Loaded and saved files are not equal")

    # helper methods
    def get_address(self):
        from address import Address
        return Address("Jan Kowalski", "Kraków", "ul. Daszyńskiego", "15/31")

    def get_work_address(self):
        from work_address import WorkAddress
        return WorkAddress("Adam Adamski", "Warszawa", "ul. Domaniewska",
                           "6/66", "Mordor sp. z o.o.")


    def add_addresses_to_book(self):
        from address_book import AddressBook
        self.my_book = AddressBook("friends")
        self.my_book.add_address(self.get_address())
        self.my_book.add_address(self.get_work_address())

    def create_address_book(self):
        from address_book import AddressBook
        from address import Address
        from work_address import WorkAddress

        expected = AddressBook("expected")
        expected.add_address(Address("Jane Weaver", "Tugusirna",
                                     "Rowland", "1877/2"))
        expected.add_address(Address("Rebecca Cunningham", "Murzuq",
                                     "Heffernan", "2/3"))
        expected.add_address(Address("Steven Pierce", "Matsena",
                                     "Mariners Cove", "153/4"))
        expected.add_address(WorkAddress("Jerzy Mardaus", "Kraków",
                                         "Ślusarska", "9/1",
                                         "Codecool Poland Sp. z o.o."))
        expected.add_address(Address("Betty Jenkins", "Tirmiz",
                                     "Hollow Ridge", "011/5"))

        return expected

if __name__ == '__main__':
    unittest.main(module=__name__, verbosity=2, buffer=True, exit=False)
