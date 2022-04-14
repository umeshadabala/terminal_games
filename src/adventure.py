import time
print('''
 █████╗ ██████╗ ██╗   ██╗███████╗███╗   ██╗████████╗██╗   ██╗██████╗  ██████╗ ██╗   ██╗███████╗
██╔══██╗██╔══██╗██║   ██║██╔════╝████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔═══██╗██║   ██║██╔════╝
███████║██║  ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝██║   ██║██║   ██║███████╗
██╔══██║██║  ██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗██║   ██║██║   ██║╚════██║
██║  ██║██████╔╝ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                                                               
''')
time.sleep(1)

start = str(input("Do you want to enter the world's dangerous and adventurous island alone (y/n): "))
if start == "y":
    print("you have entered the island")
    left_right = str(input('''
Now you have two doors one on the left another on the right
on the right door there is  a lion which did not have food for 2 months and
on the left  door there is  a poisonous gas which can kill you in 2 seconds
now choose left or right door (left/right): '''))
    if left_right == 'right':
        print("Good Choice  the lion is not alive because any living thing cannot live without food for 2 months. ")
        tsunami = str(input("Now your being hit by a tsunami, choose a option to survive (run/building)"))
        if tsunami == "building":
            print('You escaped the tsunami')
            escape = str(input("You have two things to do make a boat and escape the island or escape by using the swimming survival kit (boat/swim)"))
            if escape == "boat":
                print("Congrats you escaped the island")
                time.sleep(5)
            elif escape == "swim":
                print("You were killed by the sharks while swimming")
                time.sleep(5)
            else:
                quit()
        elif tsunami == "run":
            print("You were killed by the tsunami")
            time.sleep(5)
        else:
            quit()
    elif left_right == "left":
        print("You were killed by the poisonous gas")
        time.sleep(5)
    else:
        quit()
elif start =="n":
    print("I know you are  Scared about this 🤣")
    time.sleep(5)
else:
    quit()
