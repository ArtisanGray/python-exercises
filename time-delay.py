# This program will count to 10 with a second pause in between.
import time

count = 0
for x in range(0, 10):
	count+= 1
	time.sleep(1)
	print(count)
