import re
from subprocess import call

# Main Loop

running = True

while running == True:
    option = input("\nWhat do you want to do?: [Get data : Add data]\n")
    if option == "Add data":
        # Adding Data(Price, Item Bought) to the file Data.txt, and Data.py

        print("\n")
        Expense = float(input("\nHow much you paid:  \n"))
        Item = input("What did you bought:  ")
        if Expense <= 50 :
            print("\nNot bad price!")
        elif Expense > 50:
            print("Save money bro!")

        with open('Data.txt', 'a') as f:
            f.write(f"Money spent: {Expense} SAR | Item bought:  {Item} \n")
            print("Done!")

        with open('Data.py', 'a') as f: 
            f.write(f"print(\"Money spent: {Expense} SAR | Item bought: {Item}\")\n")

        # Asking to loop the while loop again or not

        ask = input("\nDo you want to continue the program?: [Yes : No] ")
        if ask == "Yes":
            running = True
        elif ask == "No":
            running = False
        else:
            print("Invalid Option!")
            running = False

    elif option == "Get data":
        # Reading Data(Price, Item Bought) from the file Data.txt, and Data.py

        print("\n")
        def open_filename():
            call(["python", "Data.py"])
        open_filename()
        with open('data.txt', 'r') as file:
            text = file.read()
        amounts = re.findall(r'([\d.]+)\sSAR', text) # Takiing price(numbers) from the file Data.txt 
        total_spent = sum(map(float, amounts)) # Summing up all the price(numbers) in the file Data.txt 
        print("\nTotal money spent: {:.2f} SAR".format(total_spent))

        # Asking to loop the while loop again or not

        ask = input("\nDo you want to continue the program?: [Yes : No] ")
        if ask == "Yes":
            running = True
        elif ask == "No":
            running = False
        else:
            print("Invalid Option!")
            running = False
