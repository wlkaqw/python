import time
for i in range(101):
    print("\r{:1}%".format(i), end="")#\r回到行首
    time.sleep(0.1)