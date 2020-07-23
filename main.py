
#TopRowKeys
SP = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_"]

#Letters on the Keyword
LRS = ['z', 'x', 'c', 'v', 'b', 'n', 'm', 'a', 's',
'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w', 'e', 'r', 't','y', 'u', 'i', 'o', 'p']

#Numbers
NRS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

word = str(input("Enter a password: "))


found = False

while found == False:

  if len(word) > 8:
    print("Try again")
