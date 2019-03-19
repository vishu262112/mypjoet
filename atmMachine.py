card_no = (input('Enter your card_no\n'))
password = (input('Enter your password\n'))

fhand = open('card_pin.txt')
str = fhand.read()
if (password[0:4] == str[11:15]) and (card_no[0:4] == str[23:27]):
    fh2 = open('card_pin',"w")

    balance = float(str[35:])
    print('==========     WELCOME     ==========\n     ')
    while 1:
        print('1.BALANCE ENQUIRY')      #mainoption
        print('2.WITHDRAWAL')
        print('3.SERVICE')
        print('4.FAST CASH')
        print('5.EXIT')
        ch = int(input('Enter appropriate number for further operation\n'))
        if ch == 1:       #to check balance
            print('BALANCE=',(balance))
        elif ch == 2:      #withdrawal
            amount = int(input('ENTER THE AMOUNT: MULTIPLE OF 100 or 500\n'))
            balance = balance - amount
            if balance < 500:
                balance = balance + amount
                print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT\n')
                print('YOUR CURRENT BALANCE IS\n', balance)
            else:

                print('PLEASE COLLECT YOUR CASH\n')
                print('YOUR CURRENT BALANCE IS\n', balance)
        elif ch == 3:
            print('CHANGE PASSWORD\n')
            print('CHANGE NUMBER \n')
            print('ABOUT \n ')
            print('EXIT\n ')
        elif ch == 4:
            print('1.500')
            print('2.2000')
            print('3.5000')
            print('4.10000')
            print('5.20000')
            fast_cash = int(input("ENTER THE NUMBER TO WITHDRAWAL\n"))
            if fast_cash == 1:
                balance = balance - 500
                if balance <= 500:
                    balance = balance + 500
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS\n', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH\n')
                    print('YOUR CURRENT BALANCE IS\n', balance)
            elif fast_cash == 2:
                balance = balance - 2000
                if balance <= 500:
                    balance = balance + 2000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS\n', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH\n')
                    print('YOUR CURRENT BALANCE IS\n', balance)
            elif fast_cash == 3:
                balance = balance - 5000
                if balance <= 500:
                    balance = balance + 5000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS\n', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH\n')
                    print('YOUR CURRENT BALANCE IS\n', balance)
            elif fast_cash == 4:
                balance = balance - 10000
                if balance <= 500:
                    balance = balance + 10000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS\n', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH')
                    print('YOUR CURRENT BALANCE IS\n', balance)
            elif fast_cash == 5:
                balance = balance - 20000
                if balance <= 500:
                    balance = balance + 20000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS\n', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH')
                    print('YOUR CURRENT BALANCE IS\n', balance)
        elif ch == 5:
            print("THANK YOU FOR USING US")
            exit(0)
else:
    print('WRONG PIN')
    exit(0)



