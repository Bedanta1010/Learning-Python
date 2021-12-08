# f = open("tut27i.txt", "w")  # Write mode
# f.write("The universe is huge !")
# f.close()
# f = open("tut26i.txt", "a")  # Append mode
# f.write("\nThe universe is huge !")
# f.close()

# f = open("tut27i.txt", "w")
# a = f.write("The universe is huge !")
# print(a)
# f.close()

f = open("tut27j.txt", "r+")  # Read and write mode
print(f.read())
a = f.write("Thank you")
f.close()
