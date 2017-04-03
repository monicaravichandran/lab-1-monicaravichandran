#* Section 1 (Git)
persnickety
#* Section 2 (Data Definitions)

#* 1)
class Celsius:
   def __init__(self,celsius):
      self.celsius = celsius
   def __eq__(self, other):
      return self.celsius == other.celsius
   def __repr__(self):
      return("Celsius(%r)" % (self.celsius))
class Farenheit:
   def __init__(self,farenheit):
      self.farenheit = farenheit
   def __eq__(self,other):
      return self.farenheit == other.farenheit
   def __repr__(self): 
      return("Farenheit(%r)" % (self.farenheit))
def main():
   celsius = float(input("Celsius:"))
   c = Celsius(celsius)
   f = Farenheit(c.celsius*1.8+32)
   print(f)
if  __name__ == '__main__':
   main()

#* 2)

#* 3)

#* 4)

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

