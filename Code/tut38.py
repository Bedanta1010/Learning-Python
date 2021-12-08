# Python external and built-in modules
import random
import sklearn   # need to fix pip by downloading python 3.9.5 again
import platform

# ranNum = random.randint(0, 7)
# print(ranNum)

# rand = random.random()  # It will generate any number between 0 and 1
# rand = random.random() * 100   # Will generate any number till 100
# print(rand)

# lst = ["CW Network", "Aaj Tak", "BBC News", "CodeWithHarry"]
# choice = random.choice(lst)
# print(choice)

print("My processor is:", platform.processor())
print("My system build is:", platform.version())
print("My system is:", platform.system())
print("My architecture is:", platform.architecture())
