#* Section 1 (Git)
persnickety
#* Section 2 (Data Definitions)

#* 1)
# a Celsius is a float representing temperature in Celsius
# a Fahrenheit is a float representing temperature in Fahrenheit
class Celsius:
   def __init__(self,celsius):
      self.celsius = celsius # is an int representing temperature in celsius
   def __eq__(self, other):
      return self.celsius == other.celsius
   def __repr__(self):
      return("Celsius(%r)" % (self.celsius))
class Fahrenheit:
   def __init__(self,farenheit):
      self.fahrenheit = fahrenheit # is an int representing temperature in fahrenheit
   def __eq__(self,other):
      return self.fahrenheit == other.fahrenheit
   def __repr__(self): 
      return("Fahrenheit(%r)" % (self.fahrenheit))
def get_temp():
   celsius = float(input("Celsius:"))
   c = Celsius(celsius)
   f = Fahrenheit(c.celsius*1.8+32)
   print(f)

#* 2)
# a Price is a float representing the price/dollar amount for various items in a store in cents

#* 3)
# a PriceRecord represents the price record for the store and has in ItemName and a Price
# an ItemName is a string representing the name of the Item in the PriceRecord
# a Price is a float representing the price/dollar amount for various items in a store in cents

#* 4)
# an OpenTab represents an web browser that contains the URL and the most recent date it was loaded
# a Url represents a string containing the webname URL of the web browser
# a Date is a string of the most recent date the Url was accessed
class OpenTab:
   def __init__(self,url,date):
      self.url = url #is a Url
      self.date = date #is a Date
   def __eq__(self,other):
      return self.url == other.url and self.date == other.date
   def __repr__(self):
      return("OpenTab(%r,%r)" % (self.url, self.date))

class Url:
   def __init__(self,webname):
      self.webname = webname # a string representing the URL
   def __eq__(self,other):
      return self.webname == other.webname
   def __repr__(self):
      return("Url(%r)" % (self.url)

class Date:
   def __init__(self, month, day, year):
      self.month = month # is an int representing the month of the date
      self.day = day # is an int representing the day of the date
      self.year = year # is an int representing the year of the date
   def __eq__(self, other):
      return self.month == other.month and self.day == other.day and self.year == other.year
   def __repr__(self):
      return ("Date(%r/%r/%r)" % (self.month, self.day, self.year))

#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)

#* 2)

#* 3)

#* 4)

#* Section 4 (Test Cases)

#* 1)

#* 2)

#* 3)

#* Section 5 (Whole Functions)

#* 1)

#* 2)

#* 3)

#* 4)

