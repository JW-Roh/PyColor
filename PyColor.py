from textwrap import wrap
from termcolor import colored
from sty import fg, bg, ef, rs, RgbFg

def rgbToHex(int1, int2, int3):
    a = str(hex(int1)).replace("0x", "")
    b = str(hex(int2)).replace("0x", "")
    c = str(hex(int3)).replace("0x", "")

    if len(a) == 1:
        a = "0"+a
    if len(b) == 1:
        b = "0"+b
    if len(c) == 1:
        c = "0"+c

    hexInString = "#"+a+b+c
    return hexInString

def hexToRGB(hex):
    int1 = None
    int2 = None
    int3 = None
    hexInList = wrap(hex.replace("#", ""), 2)
    rgbFrame = "{0}, {1}, {2}"

    for string in hexInList:
        if not int1:
            int1 = str(int(string, 16))
        elif not int2:
            int2 = str(int(string, 16))
        elif not int3:
            int3 = str(int(string, 16))

    return rgbFrame.format(int1, int2, int3)

def ask():
    textP = colored("P", "red")
    textY = colored("y", "cyan")
    textC = colored("C", "yellow")
    textO1 = colored("o", "green")
    textL = colored("l", "blue")
    textO2 = colored("o", "white")
    textR = colored("r", "magenta")
    mode = input(textP+textY+textC+textO1+textL+textO2+textR+"\n\n1: RGB to Hex\n2: Hex to RGB\n3: Exit\n\nenter: ")

    if int(mode) == 1:  # rgb to hex
        rgbRequest = input("Enter RGB ex.(255, 255, 255)\n\nenter:")
        if rgbRequest.count(", ") == 2:
            int1 = None
            int2 = None
            int3 = None
            splitedRGB = str(rgbRequest).split(", ")
            for num in splitedRGB:
                if not int1:
                    int1 = str(num)
                elif not int2:
                    int2 = str(num)
                elif not int3:
                    int3 = str(num)
            print(colored("Hex: " + rgbToHex(int(int1), int(int2), int(int3)), "green"))
        else:
            print(colored("Invalid type of rgb.\n\n\n", "red"))
            ask()
    elif int(mode) == 2:  # hex to rgb
        hexRequest = input("Enter Hex ex.(#ffffff)\n\nenter:")
        if len(hexRequest) == 7:
            if hexRequest.startswith("#"):
                print(colored("RGB: " + hexToRGB(str(hexRequest)), "green"))
            else:
                print(colored("Hex needs to start with '#'.\n\n\n", "red"))
                ask()
        else:
            print(colored("Invalid type of hex.\n\n\n", "red"))
            ask()
    elif int(mode) == 3:  # exit
        exit()
    else:
        print(colored("Please enter 1, 2 or 3.\n\n\n", "red"))
        ask()

    again = input(colored("Again? (y/n)\n\n\n", "blue"))
    if again == "y":
        ask()
    else:
        exit()

ask()