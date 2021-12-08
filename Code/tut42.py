# Time Module in Python
import time

# initial = time.time()
# k = 0
# while (k < 20):
#     print("This is a line")
#     k += 1

# print(f"Time Taken for While Loop to run {time.time() - initial} Seconds\n")

# initial2 = time.time()
# for i in range(20):
#     print("This is a line")

# print(f"Time taken by For Loop {time.time() - initial2} Seconds")

# localtime = time.asctime(time.localtime(time.time()))
# print (localtime)

n = 0
while (n < 10):
    print("This is a line")
    time.sleep(1)  # It will stop the code for 1 second
    n += 1
