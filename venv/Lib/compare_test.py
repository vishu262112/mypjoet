abc = '7'
ap = input('enter a string')
if abc == ap:
    print('equal')
else:
    print(type(abc))
    fhand = open('card_pin.txt')
    str = fhand.read()
    print(type(str))
    print(str)


if str[0:4] == card_no[0:4]:
    print('yes')
else:
    print("not equal")