# Dictionary is nothing but key value pairs
# d1 = {}
# print(type(d1))
d2 = {"Harry": "Burger", "Rohan": "Fish", "SkillF": "Roti", "Shubham": {"B": "Maggie", "L": "roti", "D": "Chicken"}}
# print(d2["Harry"])
# print(d2["Shubham"])
# print(d2["Shubham"]["D"])
# d2["Ankit"] = "Junk Food"
# d2["Aurangzeb"] = "Kebabs"
# d2[420] = "Kebabs"
# print(d2)
# del d2[420]
# d3 = d2
# d3 = d2.copy()
# del d3["Harry"]
# It will delete the index in d2 too so .copy() is better
print(d2)

# print(d2.get("Harry"))
# d2.update({"Leena": "Toffee"})
# print(d2)
print(d2.keys())
print(d2.items())
