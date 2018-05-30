import random
pass_len = input('How long do you want your password to be?')
pass_len_int = int(pass_len)
# Declare a list of characters for your password
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","y","v","x","y","z"]
a_num = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","y","v","x","y","z","1","2","3","4","5","6","7","8","9","0"]
a_num_sym = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','y','v','x','y','z','1','2','3','4','5','6','7','8','9','0','!','?','.',',','-']
# Ask the user what type of password they want
print("Enter [1] for letters only\n")
print("Enter [2] for numbers and letters\n")
print("Enter [3] for numbers, letters, and symbols\n")
pass_type = input()

pass_type_int = int(pass_type)
if pass_type_int == 1:
  password =' '
  for x in range(pass_len_int):
    password += random.choice(alpha)
  else:
    print (password)
elif pass_type_int == 2:
  password = ''
  for x in range(pass_len_int):
    password += random.choice(a_num)
  else:
    print (password)
elif pass_type_int == 3:
 password =''
 for x in range(pass_len_int):
    password += random.choice(a_num_sym)  
 else:
    print(password)
else:
  exit()
# print the random password.


