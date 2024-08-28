import sys
def initial_slambook():
  row = int(input("Enter the number of people that will be answering the questions: "))
  cols = 6
  slam_book = []
  print(slam_book)
  for i in range(row):
    print("\nEnter contact %d details in the following order (ONLY): "% (i+1))
    print("NOTE: * indicates madatory fields")
    temp =[]
    for j in range(cols):
      if j == 0:
        temp.append(str(input("Enter name: ")))
        if temp[j] == '' or temp[j] == ' ':
          sys.exit("Name is a mandatory field. Processing exit due to blank field...")

      if j ==1 :
        temp.append(str(input("Enter age: ")))
      if j ==2:
        temp.append(str(input("Enter you hobbies: ")))
        if temp[j] == '' or temp[j] == ' ':
          temp[j] = None
           
      if j==3: 
        temp.append(str(input("Enter your favorite color, animal, number, sport, B.F.F, and grade: ")))
        if temp[j] == '' or temp[j] == ' ':
          temp[j] = None
      if j ==4:
        temp.append(str(input("Enter something you hate and like about the person who made this slambook: ")))
        if temp[j] == '' or temp[j] == ' ':
          temp[j] = None
      slam_book.append(temp)  
   
  print(slam_book)
  return slam_book

def thanks():
  print("***********************************************************************************")
  print("Thank you for checking out the slam book")
  print("Please visit again!")
  print("***********************************************************************************")
  sys.exit("Goodbye, have a nice day!")

def main():
  print("..................................................................................")
  print("Hello dear friend, welcome to my slam book")
  print("You may now proceed to explore my slam book")
  print("..................................................................................")

  choice = 1
  while choice in (1,2):
    choice = menu()
    if (choice == 1):
      pb = initial_slambook()
    else:
      thanks()

def menu():
  print("***********************************************************************************")
  print("\t\t\t\t\tSLAM BOOK DIRECTORY")
  print("***********************************************************************************")
  print("\tYou can now perform the following operators in this slam book\n")
  print("1. Answer question")
  print("Other numer. Exit slambook")
  choice = int(input("Please enter your choice: "))
  return choice

  

main()
menu()
  