line1 = ['###', '  #', '###', '###', '# #', '###', '###', '###', '###', '###']
line2 = ['# #', '  #', '  #', '  #', '# #', '#  ', '#  ', '  #', '# #', '# #']
line3 = ['# #', '  #', '###', '###', '###', '###', '###', '  #', '###', '###']
line4 = ['# #', '  #', '#  ', '  #', '  #', '  #', '# #', '  #', '# #', '  #']
line5 = ['###', '  #', '###', '###', '  #', '###', '###', '  #', '###', '###']


def display_led(num):

    num_str = str(num)

    for lines in range(1, 6):
        for item in num_str:
            print(globals()['line%s' % lines][int(item)], end=" ")
        print("")


try:
    display = int(input("Please insert any integer to convert to LED simulation \n"))
except ValueError:
    print("You are inserting invalid format of integer")

try:
    display_led(display)
except NameError:
    print("Cannot display your LED conversion due to invalid integer input")