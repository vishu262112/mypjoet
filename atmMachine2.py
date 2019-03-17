pin = 9916
balance = 2000
card_no = int(input('Enter your card_no\n'))
if card_no == 9916:
    print('==========     WELCOME     ==========\n     ')
    while 1:
        print('1.BALANCE ENQUIRY')#main option
        print('2.WITHDRAWAL')
        print('3.SERVICE')
        print('4.FAST CASH')
        print('5.EXIT')
        ch = int(input('Enter appropriate number for further operation\n'))
        if ch == 1:#to check balance
            print('BALANCE=2000')
        elif ch == 2:#withdawal
            amount = int(input('ENTER THE AMOUNT: MULTIPLE OF 100 or 500\n'))
            balance = balance - amount
            if balance < 500:
                balance = balance + amount
                print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                print('YOUR CURRENT BALANCE IS', balance)
            else:

                print('PLEASE COLLECT YOUR CASH')
                print('YOUR CURRENT BALANCE IS', balance)
        elif ch == 3:
            print('CHANGE PASSWORD')
            print('CHANGE NUMBER ')
            print('ABOUT  ')
            print('EXIT ')
        elif ch == 4:
            print('1.500')
            print('2.2000')
            print('3.5000')
            print('4.10000')
            print('5.20000')
            fast_cash = int(input("Enter the number for withdrawal"))
            if fast_cash == 1:
                balance = balance - 500
                if balance <= 500:
                    balance = balance + 500
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH')
                    print('YOUR CURRENT BALANCE IS', balance)
            elif fast_cash == 2:
                balance = balance - 2000
                if balance <= 500:
                    balance = balance + 2000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH')
                    print('YOUR CURRENT BALANCE IS', balance)
            elif fast_cash == 3:
                balance = balance - 5000
                if balance <= 500:
                    balance = balance + 5000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH')
                    print('YOUR CURRENT BALANCE IS', balance)
            elif fast_cash == 4:
                balance = balance - 10000
                if balance <= 500:
                    balance = balance + 10000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH')
                    print('YOUR CURRENT BALANCE IS', balance)
            elif fast_cash == 5:
                balance = balance - 20000
                if balance <= 500:
                    balance = balance + 20000
                    print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
                    print('YOUR CURRENT BALANCE IS', balance)
                else:
                    print('PLEASE COLLECT YOUR CASH')
                    print('YOUR CURRENT BALANCE IS', balance)
        elif ch == 5:
            exit(0)
else:
    print('wrong pin')
