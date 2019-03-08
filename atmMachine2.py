pin = 9916
balance = 2000
card_no = int(input('Enter your card_no\n'))
if(card_no==9916):
    print('==========     WELCOME     ==========\n     ')
    print('1.BALANCE ENQUIRY')
    print('2.WITHDRAWAL')
    print('3.SERVICE')
    print('4.FAST CASH')
    ch = int(input('Enter appropriate number for further operation\n'))
    if ch == 1:
        print('BALANCE=100000')
    elif ch == 2 :
        amount = int(input('ENTER THE AMOUNT\n'))
        balance = balance - amount
        if(balance<=500):
            print('SORRY YOUR BALANCE IS BELOW OF MINIMUM AMOUNT')
        else:

            print('PLEASE COLLECT YOUR CASH')
            print('YOUR CURRENT BALANCE IS',balance
                  )

else:
    print('wrong pin')acSAccXczcZ