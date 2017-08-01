# Address Book in OOP way
**Please read this document carefully!**
========================================

## Final result expectation

Console application that allows user to manage his contacts.

Sample usage:
```
$python main.py

Welcome to your Awesome OOP Address Book Manager!

What would you like to do?
  1. Create new address book
  2. Open address book from file
  0. Exit
Option: 2

Please provide a name of an address book:
Friends

**Friends**
What would you like to do?
  1. List addresses
  2. Add a new address
  3. Remove an address
  4. Search for an address
  5. Save this address book
  0. Back to main menu
Option: 1

Address List:
#1 - Jan Kowalski, Kraków, ul. Daszyńskiego 15/31
#2 - Adam Adamski, Warszawa, ul. Domaniewska 6/66, Mordor sp. z o.o.
```

# Specification
Below you'll find specifications of classes that you should implement in order to pass the tests. Have in mind that this specification does not contain implementation details. **It is your responsibility to decide which methods should be static or where to use inheritance and etc.** Remember that you can implement more classes to make your code better.

Specification is divided into three parts. First two are mandatory and the third one is optional (12pts). This means that you don't have to implement the UI in order to pass this exercise.

## General rules
* do not modify addresses.csv file because you might break the tests
* you don't have to write docstrings during this assignment because time is short
* even though you work alone please commit often and properly, make pushes after each part of the exercise
* test your code often

## 1st part - classes

### `Address` class

#### Attributes:

* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number

#### Methods

##### `__init__`

Parameters:
* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number

##### `get_full_address`

This method should __return__ full address as a string in the following form:
`{person}, {city}, {street} {house_no}`

##### `__eq__`

This method should compare an instance of Address with other Address object using its attributes and return True if addresses are equal

Parameters:
* `self` - first Address object
* `other` - second Address object


### `WorkAddress` class

#### Attributes:

* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number
* `company` - string, name of the company

#### Methods

##### `__init__`

Parameters:
* `person` - string, full name of address owner
* `city` - string, city name
* `street` - string, street name
* `house_no` - string, house number
* `company` - string, name of the company

##### `get_full_address`

This method should __return__ full address as a string in the following form:
`{person}, {city}, {street} {house_no}, {company}`

##### `__eq__`

This method should compare an instance of WorkAddress with other WorkAddress object using its attributes and return True if addresses are equal

Parameters:
* `self` - first WorkAddress object
* `other` - second WorkAddress object

### `AddressBook` class

#### Attributes:

* `name` - name of the address book
* `addresses` - list containing addresses (`Address` or `WorkAddress` objects)

#### Methods

##### `__init__`

Parameters:
* `name` - name of the address book

##### `add_address`
Adds given `Address` or `WorkAddress` to the list of addresses. Raises TypeError when something else is added.

Parameters:
* `address` - `Address` or `WorkAddress` object

##### `find`
Searches through address book for a given phrase and returns a list of matching objects. This method should be case insensitive.

Parameters:
* `search_phrase` - string, that we're looking for


##### `sort`
Sorts addresses in `addresses` list alphabetically by full address in ascending order. You should implement your own sorting algorithm. Don't use built in `sort` and `sorted` functions.

### _please git push now_

## 2nd part - persistence
### `create_from_csv`

Write `create_from_csv` method in `AddressBook` class. It should take 2 parameters:

* `list_name` - name of the address book.
* `csv_path` - path to CSV file.

This method should return `AddressBook` instance with list of items from CSV file.

First row in CSV file contains column headers.

Have in mind that CSV file could contain both home and work addresses.

### `save_to_csv`
Write `save_to_csv` method in AddressBook that saves all addresses in address book to a .csv file named `name`.csv

### _please git push now_

## 3rd part - user interface - optional
### main menu
* `1. Create new address book` - asks for address book name and creates a new one, starts Address book menu.
* `2. Open address book from file` - asks for address book name, loads address book from file, starts Address book menu.
* `0. Exit` - closes the program.

### address book menu
* `1. List addresses` - displays all addresses.
* `2. Add a new address` - asks for a new address data and adds it to the address book.
* `3. Remove an address` - asks which address should be removed and removes it.
* `4. Search for an address` - asks for a search phrase and than displays all matching addresses.
* `5. Save this address book` - saves address book to a file named `name`.csv.
* `0. Back to main menu` - moves back to main menu.
