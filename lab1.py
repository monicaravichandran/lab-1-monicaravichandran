import unittest
# * Section 1 (Git)
#persnickety


# * Section 2 (Data Definitions)

# * 1)
# a Celsius is a float representing temperature in Celsius
# a Fahrenheit is a float representing temperature in Fahrenheit and is what is outputted after calculations
class Celsius:
    def __init__(self, celsius):
        self.celsius = celsius  # is an int representing temperature in celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __repr__(self):
        return "Celsius(%r)" % (self.celsius)


class Fahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit  # is an int representing temperature in fahrenheit

    def __eq__(self, other):
        return self.fahrenheit == other.fahrenheit

    def __repr__(self):
        return "Fahrenheit(%r)" % (self.fahrenheit)


def get_temp():
    celsius = float(input("Celsius:"))
    c = Celsius(celsius)
    f = Fahrenheit(c.celsius * 1.8 + 32)
    print(f)


# * 2)
# a price is an int representing the price/cost amount for various items in a store in cents

# * 3)
# a PriceRecord represents the price record for the store and has an item name and a price
# an item name is a string representing the name of the item in the PriceRecord
# a price is an int representing the price/dollar amount for various items in a store in cents
class PriceRecord:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __eq__(self, other):
        return type(other) == PriceRecord and self.item == other.item and self.price == other.price

    def __repr__(self):
        return "PriceRecord(%r,%r)" % (self.item, self.price)


# * 4)
# an OpenTab represents an web browser that contains the URL and the most recent date it was loaded
# a Url represents a string containing the webname URL of the web browser
# a Date is a string of the most recent date the Url was accessed in the format of "xx/xx/xxxx" (month/day/year))
class OpenTab:
    def __init__(self, url, date):
        self.url = url  # is a string representing a url of a website
        self.date = date  # is a Date

    def __eq__(self, other):
        return self.url == other.url and self.date == other.date

    def __repr__(self):
        return "OpenTab(%r,%r)" % (self.url, self.date)

class Date:
    def __init__(self, month, day, year):
        self.month = month  # is an int representing the month of the date
        self.day = day  # is an int representing the day of the date
        self.year = year  # is an int representing the year of the date

    def __eq__(self, other):
        return self.month == other.month and self.day == other.day and self.year == other.year

    def __repr__(self):
        return "Date(%r/%r/%r)" % (self.month, self.day, self.year)


# * Section 3 (Signature, Purpose Statements, Headers)

# * 1)
# Signature: int float --> int
# Purpose Statement: returns the price added to the respective sales tax that was inputted along with the original price
def get_tax_price(price, tax):
    pass

# * 2)
# Signature: database string --> int
# Purpose Statement: returns the price for a named item in a store's database after finding the inputted item name string in the database.
def get_price(item_name):
    pass

# * 3)
# Signature: database string --> int
# Purpose Statement: returns the median income in a given geographic region using a database as input
def get_med_income(region):
    pass

# * 4)
# Signature: database string --> list of strings
# Purpose Statement: returns a list of string cities which overlap in the geographic region provided
def get_cities(geo_region):
    pass

# * Section 4 (Test Cases)

# * 1)
# Signature: float float float --> float
# Purpose Statement: returns the second largest float of the 3 inputted floats given
def get_second_largest(num1,num2,num3):
    pass

# * 2)
# Signature: string --> boolean
# Purpose Statement: returns a boolean of True if the string inputted has no capital letters and False otherwise
def check_capital(word):
    pass
# * 3)
# Signature: string string --> string
# Purpose Statement: returns the northernmost state (in relation to the north pole) of the two states provided/inputted

def get_furthest_north(state1,state2):
    pass

# TestCases for 1-3

class TestCases1(unittest.TestCase):

    def test_get_second_largest_1(self):
        self.assertEqual(get_second_largest(1,2,3),2.0)
        self.assertEqual(get_second_largest(1,2,2),1.0)
        self.assertEqual(get_second_largest(2,2,2),2.0)
        self.assertEqual(get_second_largest(10.2,3.4,15.3),10.2)
        self.assertEqual(get_second_largest(5.3,5.3,5.3),5.3)
        self.assertEqual(get_second_largest(9,7,4),7.0)

    def test_check_capital_1(self):
        self.assertEqual(check_capital("Monica"), False)
        self.assertEqual(check_capital("a4bc3"), True)
        self.assertEqual(check_capital("ACB$$D"), False)
        self.assertEqual(check_capital("&abCd"), False)
        self.assertEqual(check_capital("cat$"),True)
        self.assertEqual(check_capital("#444532***3%"),True)

    def test_furthest_north_1(self):
        self.assertEqual(get_furthest_north("Texas", "California"), "California")
        self.assertEqual(get_furthest_north("Texas", "Alaska"), "Alaska")
        self.assertEqual(get_furthest_north("Alaska", "Nevada"), "Alaska")
        self.assertEqual(get_furthest_north("Alaska", "California"), "Alaska")


# * Section 5 (Whole Functions)

# * 1)
# Signature: float/int --> float
# Purpose Statement: returns the amount of feet in meters
def f2m(feet):
    meter = feet/3.28 # feet represent the inputted feet
    return float("%.3f" % meter) # meter represents the amount of feet in meters formatted to the 3rd decimal

# * 2)
# MusicalNote represents a musical note in a musical record and has pitch and duration

class MusicalNote:
    def __init__(self, duration, pitch):
        self.duration = duration # is the time in seconds the musical note is held for
        self.pitch = pitch # is the pitch represented as a frequency in Hz
    def __eq__(self,other):
        return self.duration == other.duration and self.pitch == other.pitch
    def __repr__(self):
        return "MusicalNote(%r,%r)" % (self.duration, self.pitch)

# * 3)
# note is a MusicalNote representing a musical note that has a pitch (frequency in Hz) and a duration in seconds
# Signature: MusicalNote --> MusicalNote
# Purpose Statement: returns a new note that is higher by one octave meaning its frequency has doubled
def up_one_octave(note):
    newNote = MusicalNote(note.duration, (note.pitch)*2)
    return newNote # is a MusicalNote that has the same duration as the inputted note but a frequency that has been doubled

# * 4)
# note is a MusicalNote representing a musical note that has a pitch (frequency in Hz) and a duration in seconds
# Signature: MusicalNote --> None
# Purpose Statement: returns None after doubling the frequency of the inputted MusicalNote
def up_one_octave_m(note):
    note.pitch = note.pitch*2
    return None

# Test Cases for #1,3,4:

class TestCases2(unittest.TestCase):
    def test_f2m(self):
        self.assertEqual(f2m(1),0.305)
        self.assertEqual(f2m(3.4), 1.037)
        self.assertEqual(f2m(-10.3), -3.14)
        self.assertEqual(f2m(0),0.0)
        self.assertEqual(f2m(12934.39482), 3943.413)
        self.assertEqual(f2m(328), 100.0)
    def test_up_one_octave(self):
        self.assertEqual(up_one_octave(MusicalNote(5,4)), MusicalNote(5,8))
        self.assertEqual(up_one_octave(MusicalNote(3.2, 5.6)), MusicalNote(3.2, 11.2))
        self.assertEqual(up_one_octave(MusicalNote(0,0)), MusicalNote(0,0))
        self.assertEqual(up_one_octave(MusicalNote(123,345.3)), MusicalNote(123, 690.6))
        self.assertEqual(up_one_octave(MusicalNote(234.5, 246)), MusicalNote(234.5,492))
    def test_up_one_octave_m(self):
        note = MusicalNote(5,4)
        returnedNone = up_one_octave_m(note)
        self.assertEqual(returnedNone, None)
        self.assertTrue(note.pitch == 8)

        note2 = MusicalNote(293.4,193.5)
        returnedNone2 = up_one_octave_m(note2)
        self.assertEqual(returnedNone2,None)
        self.assertTrue(note2.pitch == 387.0)

        note3 = MusicalNote(0,0)
        returnedNone3 = up_one_octave_m(note3)
        self.assertEqual(returnedNone3,None)
        self.assertTrue(note3.pitch == 0)

        note4 = MusicalNote(10,40)
        returnedNone4 = up_one_octave_m(note4)
        self.assertEqual(returnedNone4, None)
        self.assertTrue(note4.pitch == 80)

        note5 = MusicalNote(39,3)
        returnedNone5 = up_one_octave_m(note5)
        self.assertEqual(returnedNone5, None)
        self.assertFalse(note.pitch == 10)


if __name__ == '__main__':
    unittest.main()
