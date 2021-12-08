# Enumerate Function
l1 = ["Bhindi", "Mango", "Chow", "Roti", "Pizza"]

for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"Please buy {item}")
