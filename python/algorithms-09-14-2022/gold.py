# Retrieve a book from the library
from random import randrange

bookName = str(input("Which book would you like to retrieve?\n"))
isLibraryOpen = randrange(0, 100)
isBookAvailable = randrange(0, 100)

if isLibraryOpen < 20: print("Library is closed! Try again later."); exit()
if isBookAvailable < 40: print("Looks like that book isn't available! Try again another time."); exit()

print(f"Successfully retrieved \"{bookName}\"!")