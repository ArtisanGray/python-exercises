#check how to read and open a file from A20
def longestWord():
  
  with open("alice.txt", "rU") as file_name:
    file_read = list(file_name.readlines())
    words = []
    for line in file_read:
    
      words += line.split()
    print (max(words, key=len))

longestWord()
#Mr. Faulkner, i do need help with this. the text file supports newline, i opened the file in a new way to see if that would work, but it didnt. i guess it's REPL.it's fault. Tomorrow ill try it in IDLE
