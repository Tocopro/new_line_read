# Reading a line requested by the user from a file
sonnets = open("C:\\Users\\NEAK\\Documents\\Sonnets\\reprints.txt")
user = int(input("Enter a Line NUmber: "))
if 0 < user > 14:
    print("Not Valid Entry")
else:
    user = user - 1
    lines_read = sonnets.readlines()
    print("Line requested is " + str(user + 1))
    print(lines_read[user])
    
