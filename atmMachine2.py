card_no = (input('Enter your card_no\n'))
password = (input('Enter your password\n'))

fhand = open('card_pin.txt')
red = fhand.read()
if (password[0:4] == red[11:15]) and (card_no[0:4] == red[27:31]):
    balance = float(red[42:])
    print('==========     WELCOME     ==========\n     ')
    while 1:
        print('1.BALANCE ENQUIRY')  # mainoption
        print('2.WITHDRAWAL')
        print('3.SERVICE')
        print('4.FAST CASH')
        print('5.EXIT')
        print("=================================")
        ch = int(input('Enter appropriate number for further operation\n'))
        if ch == 1:  # to check balance
            print('BALANCE=', balance)
        elif ch == 2:  # withdrawal
            amount = int(input('ENTER THE AMOUNT: MULTIPLE OF 100 or 500\n'))
            balance = balance - amount
            bln = str(balance)
            fh2 = open("card_pin.txt", "a")
            fh2.write('\n'+bln)
            if balance < 500:
                balance = balance + amount
                print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT\n')
                print('YOUR CURRENT BALANCE IS\n', balance)
            else:

                print('PLEASE COLLECT YOUR CASH\n')
                print('YOUR CURRENT BALANCE IS\n', balance)
        elif ch == 3:
            print("===================")
            print('CHANGE PASSWORD')
            print('CHANGE NUMBER')
            print('ABOUT')
            print('EXIT')
            print("===================")
        elif ch == 4:
            print("===================")
            print('1.500\t\t2.2000')
            print('3.5000\t\t4.10000')
            print('5.20000')
            print("===================")
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