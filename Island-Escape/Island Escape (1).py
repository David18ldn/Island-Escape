import time
import os
import random
global auth
global Stamina
global current_day
global Task1
global Task2
global Task3
global Task4
global Task5
global Location
global backpack

backpack=str()
current_day=(15)
Stamina=(12)
auth=("0")
Location=("")
Task1=(0)
Task2=(0)
Task3=(0)
Task4=(0)
Task5=(0)


usernames_txt=("usernames.txt")
read_username=open(usernames_txt,"r")
write_username=open(usernames_txt, "a")
fileContent_U=read_username.readlines()

filename=("passwords.txt")
read_password=open(filename, "r")
write_password=open(filename, "a")
fileContent_P=read_password.readlines()



def clear():
        os.system("cls")

def introduction():
        x=input("Press Y to see the introduction.\n")
        if x ==(""):
                scene_1_caban()
        while x ==("y")or("Y"):
                
                clear()
                print("""                               On an island teenagers have arrived for the challenge "summer camp" """)
                print("""  This has been organized by the ruling Labour Party for schools to reward kids who scored good results in their exams.""")
                time.sleep(10)
                clear() 
                print("""       Because the organizers want to offer students the chance of making friends and open up to socializing""")
                print("""                 Phones are not allowed to make sure that students interact more.""")
                time.sleep(10)
                clear()
                print("         However there is a criminal who arrived in the port that wants to kill all the students")
                print("          In 15 days someone will come to collect the students and teachers from the sea port")
                time.sleep(10)
                clear()
                print("Survive 15 days!")
                time.sleep(3)
                clear()
                scene_1_caban()
def Register():
        username=input("Please enter your user-name\n")
        write_username.write(username)
        write_username.write("\n")
        write_username.close()
        password=input("Please enter your password\n")
        write_password.write(password)
        write_password.write("\n")
        write_password.close()
        print("Your account has been successfully created")
        time.sleep(3)
        clear()
        main_menu()
def Login():
        global auth
        username=input("Please enter your username\n")
        password=input("Please enter your password\n")
        if username in open("usernames.txt").read() and password in open("passwords.txt").read():
                print("Login successfully")
                auth=("1")
                time.sleep(3)
                clear()
                main_menu()
        else:
                print("Incorrect user-name or password\n\n")
                Login()
def main_menu():
        clear()
        print("           _  _             _  ________________________________ 0==EXIT ")
        print("   .       /\\/%\       .   /%\/%\     .                                                 ")
        print("       __.<\\%#//\,_       <%%#/%%\,__  .                                                ")
        print(" .    <  /|\\%%%#///\    /^%#%%\///%#\\                                                  ")
        print("           /%/\ \'//|    |   // /\// //                  ")                              
        print("  .     L/'`   \ \  `    O   / /  ```")
        print("         `      \ \     .   / /       .                                                  ")
        print("  .       .      \ \       / /  .                                                                ")
        print("         .        \ \     / /          .                                                 ")
        print("    .      .    ..:\ \:::/ /:.     .     .                                               ")
        print(" ______________/ \__;\___/\;_/\_______________ESCAPE THE ISLAND")
        print(" YwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYwYw\n\n")
        #-------------------------------------------------------------------------------------------------------------------

        num=input("1==Register\n2==Login\n3=Play ESCAPE THE ISLAND                              \n\n ")
        

        if num ==("1"):
                Register()
        elif num ==("2"):
                Login()
        elif num ==("3"):
                if auth == "1":
                        introduction()
                if auth ==("0"):
                        print("You are not logged in")
                        Login()
        elif num ==("0"):
                print("Thank you for playing ESCAPE THE ISLAND")

def ending_manger():

        def day_expired():
                global Task1
                global Task2
                global Task3
                global Task4
                global Task5
                
                clear()
                print(Location)
                if Task1 or Task2 or Task3 or Task4 or Task5 ==(0):
                        print("You survived However you didn't had a weapon prepared to defend yourself")
                        print("The killer found you and broke your legs")
        if Stamina ==(0):
                print("You tired to move but you had insufficient stamina")
                time.sleep(3)
                print("The killer found you and broke your head")

        if current_day ==(0):
                day_expired()

def scene_1_caban():
        clear()
        global Location
        global current_day
        global Stamina
        global Task1
        global backpack
        if current_day ==(0) or Stamina==(0):
                ending_manger()
        else:

                Location=("Cabin")
                print("")
                print("Location cabin-----DAY",current_day,"\n")


                choice=input("1==Rest under the bed\n2==Grab food\n3==Run to the forest\n4==Check Stamina\n5==Check backpack\n99==Help")
                if choice==(""):
                        scene_1_caban()
                if choice ==("1"):
                        Stamina=Stamina+4
                        current_day=current_day-1
                        scene_1_caban()

                if choice ==("2"):
                        if Task1==(1):
                                print("Item already collected!")
                                time.sleep(3)
                                scene_1_caban()
                                
                        else:
                                Stamina=Stamina-1
                                Task1=(1)
                                backpack=(backpack+("FOOD--"))
                                scene_1_caban()
                
                if choice ==("3"):
                        Stamina=Stamina-2
                        current_day=current_day-1
                        scene_2_forest()

                if choice ==("4"):

                        print("--------Stamina-------")
                        print("---------",Stamina,"---------","\n")
                        x=input()
                        if x ==(""):
                                clear
                        scene_1_caban()

                if choice == ("5"):
                        print(backpack)
                        x=input()
                        if x ==(""):
                                scene_1_caban()

                if choice ==("99"):
                        print("-------Help------------")
                        print("Option 1 allows you to rest in order to increase the stamina and skip a day.")
                        print("Option 2 allows you to add food to a backpack which is a task that is required for the player to win")
                        print("Option 3 allows you to move to diferent locations")
                        print("Option 4 allows you to check the players stamina")
                        print("Option 5 allows you  to check the backpack contents")
                        print("Press enter when you've finished reading")
                        x=input()
                        if x ==(""):
                                 clear()
                                 scene_1_caban()

def scene_2_forest():
        clear()
        global backpack
        global current_day
        global Stamina
        global Task2
        global Location
        if current_day ==(0) or Stamina==(0):
                ending_manger()
        else:

                Location=("forest")
                print("")
                print("Location forest-----DAY",current_day,"\n")
                choice=input("1==Rest in the cave\n2==Grab sticks\n3==Run to the sea port\n4==Run to cabin \n5==Check Stamina\n6==Check backpack\n99==Help")
                
                if choice ==(""):
                        scene_2_forest()

                if choice ==("1"):
                        Stamina=Stamina+5
                        current_day=current_day-1
                        scene_2_forest()

                if choice ==("2"):

                        if Task2==(1):
                                print("Item already collected!")
                                time.sleep(3)
                                scene_2_forest()
                                
                        else:
                                Stamina=Stamina-2
                                Task2=(1)
                                backpack=backpack+("STICKS--")
                                scene_2_forest()

                if choice ==("3"):
                        current_day=current_day-1
                        Stamina=Stamina-1
                        scene_3_sea_port()
                
                if choice ==("4"):
                        current_day=current_day-1
                        Stamina=Stamina-2
                        scene_1_caban()

                if choice ==("5"):
                        print("--------Stamina-------")
                        print("---------",Stamina,"---------","\n")
                        
                        x=input()
                        if x ==(""):
                                scene_2_forest()

                if choice == ("6"):
                        print(backpack)
                        x=input()
                        if x ==(""):
                                scene_2_forest()

                if choice ==("99"):
                        print("-------Help------------")
                        print("Option 1 allows you to rest in order to increase the stamina and skip a day.")
                        print("Option 2 allows you to add stick to a backpack which is a task that is required for the player to win")
                        print("Option 3 allows you to move to diferent locations")
                        print("Option 4 allows you to check the players stamina")
                        print("Option 5 allows you  to check the backpack contents")
                        print("Press enter when you've finished reading")
                        x=input()
                        if x ==(""):
                                 clear()
                                 scene_2_forest()

def scene_3_sea_port():
        clear()
        Location=("Sea port")
        
        global current_day
        global Stamina
        global Task3
        global backpack
        if current_day ==(0) or Stamina==(0):
                ending_manger()

        else:
                print("")
                print("Location sea port-----DAY",current_day,"\n")
                question=("1==Rest in a boat\n2==Grab rope\n3==Run to the forest\n4==Run to tents\n5==Check Stamina\n6==Check backpack\n99==Help")
                choice=input(question)
                if choice==(""):
                        scene_3_sea_port()
                if choice ==("1"):
                        Stamina=Stamina+5
                        current_day=current_day-1
                        scene_3_sea_port()
                
                if choice ==("2"):

                        if Task3==(1):
                                print("Item already collected!")
                                time.sleep(3)
                                scene_3_sea_port()
                                
                        else:
                                backpack=backpack+("ROPE--")
                                Stamina=Stamina-2
                                Task3=(1)
                                scene_3_sea_port()              

                if choice ==("3"):
                        current_day=current_day-1
                        Stamina=Stamina-2
                        scene_2_forest()
                if choice ==("4"):
                        current_day=current_day-1
                        Stamina=Stamina-2
                        scene_4_tents()

                if choice ==("5"):

                        print("--------Stamina-------")
                        print("---------",Stamina,"---------","\n")
                        x=input()
                        if x ==(""):
                                scene_3_sea_port()
                if choice == ("6"):
                        print(backpack)
                        x=input()
                        if x ==(""):
                                scene_3_sea_port()

                if choice ==("99"):
                        print("-------Help------------")
                        print("Option 1 allows you to rest in order to increase the stamina and skip a day.")
                        print("Option 2 allows you to grab the rope and put it into a backpack which is a task that is required for the player to win")
                        print("Option 3 allows you to move to diferent locations")
                        print("Option 4 allows you to move to diferent locations")
                        print("Option 5 allows you to check the players stamina")
                        print("Option 6 allows you  to check the backpack contents")
                        print("Press enter when you've finished reading")
                        x=input()
                        if x ==(""):
                                 clear()
                                 scene_3_sea_port()


def scene_4_tents():
        clear()
        Location=("Tents")
        
        global current_day
        global Stamina
        global Task4
        global backpack

        if current_day ==(0) or Stamina==(0):
                ending_manger()

        else:
                print("")
                print("Location tents-----DAY",current_day,"\n")
                choice=input("1==Rest in a sleep-bag\n2==Grab knife\n3==Run to the reception\n4==Run to sea port\n5==Check Stamina\n6==Check backpack\n99==Help")
                if choice==(""):
                        clear()
                        scene_4_tents()
                if choice ==("1"):
                        Stamina=Stamina+5
                        current_day=current_day-1
                        scene_4_tents()
                
                if choice ==("2"):

                        if Task4==(1):
                                print("Item already collected!")
                                time.sleep(3)
                                scene_4_tents()
                                
                        else:
                                backpack=backpack+("KNIFE--")
                                Stamina=Stamina-2
                                Task4=(1)
                                scene_4_tents()         

                if choice ==("3"):
                        current_day=current_day-1
                        Stamina=Stamina-2
                        scene_5_reception()

                if choice ==("4"):
                        current_day=current_day-1
                        Stamina=Stamina-2
                        scene_3_sea_port()

                if choice ==("5"):

                        print("--------Stamina-------")
                        print("---------",Stamina,"---------","\n")
                        x=input()
                        if x ==(""):
                                scene_4_tents()
                if choice == ("6"):
                        print(backpack)
                        x=input()
                        if x ==(""):
                                scene_4_tents()

                if choice ==("99"):
                        print("-------Help------------")
                        print("Option 1 allows you to rest in order to increase the stamina and skip a day.")
                        print("Option 2 allows you to grab a knife which is a task that is required for the player to win")
                        print("Option 3 allows you to move to diferent locations")
                        print("Option 4 allows you to move to diferent locations")
                        print("Option 5 allows you to check the players stamina")
                        print("Option 6 allows you  to check the backpack contents")
                        print("Press enter when you've finished reading")
                        x=input()
                        if x ==(""):
                                 clear()
                                 scene_4_tents()

def scene_5_reception():

        clear()
        Location=("Tents")
        
        global current_day
        global Stamina
        global Task5
        global backpack

        if current_day ==(0) or Stamina==(0):
                ending_manger()

        else:
                print("")
                print("Location tents-----DAY",current_day,"\n")
                choice=input("1==Rest under a desk\n2==Grab battery\n3==Run to the tents\n4==Run to sea port\n5==Check Stamina\n6==Check backpack\n99==Help")
                if choice==(""):
                        clear()
                        scene_5_reception()
                if choice ==("1"):
                        Stamina=Stamina+5
                        current_day=current_day-1
                        scene_5_reception()
                
                if choice ==("2"):

                        if Task5==(1):
                                print("Item already collected!")
                                time.sleep(3)
                                scene_5_reception()
                                
                        else:
                                backpack=backpack+("BATTERY")
                                Stamina=Stamina-2
                                Task5=(1)
                                scene_5_reception()             

                if choice ==("3"):
                        current_day=current_day-1
                        Stamina=Stamina-2
                        scene_4_tents()

                if choice ==("4"):
                        current_day=current_day-1
                        Stamina=Stamina-2
                        scene_3_sea_port()

                if choice ==("5"):

                        print("--------Stamina-------")
                        print("---------",Stamina,"---------","\n")
                        x=input()
                        if x ==(""):
                                scene_5_reception()

                if choice == ("6"):
                        print(backpack)
                        x=input()
                        if x ==(""):
                                scene_5_reception()

                if choice ==("99"):
                        print("-------Help------------")
                        print("Option 1 allows you to rest in order to increase the stamina and skip a day.")
                        print("Option 2 allows you to grab battery which is a task that is required for the player to win")
                        print("Option 3 allows you to move to diferent locations")
                        print("Option 4 allows you to move to diferent locations")
                        print("Option 5 allows you to check the players stamina")
                        print("Option 6 allows you  to check the backpack contents")
                        print("Press enter when you've finished reading")
                        x=input()
                        if x ==(""):
                                 clear()
                                 scene_5_reception()
main_menu()
