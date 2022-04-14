import time
print('''
███████╗██╗  ██╗ ██████╗  ██████╗ ████████╗███████╗██████╗ 
██╔════╝██║  ██║██╔═══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗
███████╗███████║██║   ██║██║   ██║   ██║   █████╗  ██████╔╝
╚════██║██╔══██║██║   ██║██║   ██║   ██║   ██╔══╝  ██╔══██╗
███████║██║  ██║╚██████╔╝╚██████╔╝   ██║   ███████╗██║  ██║
╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                           
''')
time.sleep(1)
enemies = 4
start = str(input("Do you wanna enter the game(y/n)"))
if start == "y":
    print("starting... task kill the enemies")
    enemy1 = str(input("your enemy is next to you, do you wanna shoot him or wait for him to shoot(y/n)"))
    if enemy1 == "y":
        print("you shot him")
        enemies -= 1
        enemy2 = str(input("you cannot  see  a enemy near you do you wanna move forward to find a enemy (y/n)"))
        if enemy2 == "y":
            print("you found a enemy")
            enemy3 = str(input("do you wanna shoot him (y/n)"))
            if enemy3 == "y":
                print("you shot him")
                enemies -= 1
                enemy4 = str(input("Enemy in the left do you wanna shoot him by turning left or shoot the enemy far away from you with  the sniper 's' for sniper 'l' for turning left "))
                if enemy4 == "s":
                    print("the enemy in the left shooted you and then you died")
                   
                elif enemy4 == "l":
                    print("you killed the enemy")
                    enemy5 = str(input("Do you wanna shot him with the sniper(y/n) "))
                    if enemy5 == "y":
                        print('All enemies  died and you Win')
                    elif enemy5 == "n":
                        print("The enemy spotted you and killed you")
                    else:
                        print("Invalid Input")
                else:
                    print("Invalid Input")
                    exit()

            elif enemy3 == "n":
                print("you missed him, moved forward, steeped on the landmine and died")
            else:
                print("Invalid input")
        elif enemy2 == "n":
            print("A enemy far away from you shot you with a sniper and you died")
        else:
            print("Invalid input")
            exit()
    elif enemy1 == "n":
        print("he shot you")
        print("you have died")
    else:
        print("Invalid input")
        exit()

elif start == "n":
    print("Goodbye")
    time.sleep(5)
else:
    print("Invalid input")
    exit()
