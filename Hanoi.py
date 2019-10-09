from time import sleep

######################
####### CONFIG #######
######################

CLEAR_SCREEN = True     # default true
disk_num = 7            # default 7
disk_speed = 0.12       # default 0.12

######################
### Initialization ###
######################

# Optional import (don't import if not needed)
if(CLEAR_SCREEN):
    import os

# Stacks
stacka = []
stackb = []
stackc = []

######################
###### Methods #######
######################

# Functions
def move(source, destination):
    # Moves disks
    global stacka
    global stackb
    global stackc
    global disk_speed
    #print("Move disk from " + source + " to " + destination)

    # Receive
    if(source == "A"):
        data = stacka.pop()
    elif(source == "B"):
        data = stackb.pop()
    elif(source == "C"):
        data = stackc.pop()
    
    # Send
    if(destination == "A"):
        stacka.append(data)
    elif(destination == "B"):
        stackb.append(data)
    elif(destination == "C"):
        stackc.append(data)
    if(CLEAR_SCREEN):
        os.system('clear' if os.name =='posix' else 'cls')
    printstacks()
    sleep(disk_speed)


def moveVia(num, src, lyv, dst):
    # Recursive algorithm for solving the puzzle
    if(num != 0):
        moveVia(num-1, src, dst, lyv)
        move(src, dst)
        moveVia(num-1, lyv, src, dst)


def printstacks():
    # Print the stacks in a sensible way
    global stacka
    global stackb
    global stackc
    global disk_num

    # Establish print string
    data = ""

    # Lengths
    lena = len(stacka)
    lenb = len(stackb)
    lenc = len(stackc)

    # Print each disk height
    for k in range(0, disk_num):
        i = disk_num - 1 - k
        # 0 0 1
        if(lena <= i and lenb <= i and lenc > i):
            data = data + ("{:10}{:10}{:10}\n".format("", "", stackc[i]))
        # 0 1 0
        elif(lena <= i and lenb > i and lenc <= i):
            data = data + ("{:10}{:10}{:10}\n".format("", stackb[i], ""))
        # 0 1 1
        elif(lena <= i and lenb > i and lenc > i):
            data = data + ("{:10}{:10}{:10}\n".format("", stackb[i], stackc[i]))
        # 1 0 0
        elif(lena > i and lenb <= i and lenc <= i):
            data = data + ("{:10}{:10}{:10}\n".format(stacka[i], "", ""))
        # 1 0 1
        elif(lena > i and lenb <= i and lenc > i):
            data = data + ("{:10}{:10}{:10}\n".format(stacka[i], "", stackc[i]))
        # 1 1 0
        elif(lena > i and lenb > i and lenc <= i):
            data = data + ("{:10}{:10}{:10}\n".format(stacka[i], stackb[i], ""))
        # 1 1 1
        elif(lena > i and lenb > i and lenc > i):
            data = data + ("{:10}{:10}{:10}\n".format(stacka[i], stackb[i], stackc[i]))
        # 0 0 0
        else:
            data = data + "\n"
    
    data = data + ("         A         B         C\n")
    if(not CLEAR_SCREEN):
        data = data + "-" * 39 + "\n"
    print(data)
            
######################
######## Main ########
######################

if(__name__ == "__main__"):
    print("-" * 50)
    for i in range(1, disk_num+1):
        stacka.append(i)
    printstacks()
    moveVia(disk_num, 'A', 'B', 'C')