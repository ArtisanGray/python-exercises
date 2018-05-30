# create a function to check for duplicates in an array
test_array = [5,51,3,3,1,2,89,54,3,5,41,4,65,12,77,321,4]   #Use this array in your program.

test_array_fixed  = list(dict.fromkeys(test_array))
print (test_array_fixed)
