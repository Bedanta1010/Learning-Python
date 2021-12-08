# Multilevel Inheritance in Python
class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def isDance(self):
        return f"Yes I dance {self.dance} no. of times."


class Grandson(Son):
    dance = 6

    def isDance(self):
        return f"Yes I dance awesomely {self.dance} no. of times."   # This will override the Son class


rohan = Dad()
larry = Son()
harry = Grandson()

print(harry.isDance())
print(harry.basketball)   # It will still work since Son inheriting Dad Class
