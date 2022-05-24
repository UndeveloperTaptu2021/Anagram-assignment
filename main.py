first_word= input("Welcome to the ultimate Anagram Checker \n Enter your first word here: ")
print("confirm that "  + first_word + " is your first word")


second_word= input("Enter your second word here: ")
print(second_word)

if(sorted(first_word.lower())==sorted(second_word.lower())) : print(True)
else: print(False)
