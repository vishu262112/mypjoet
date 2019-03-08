num = int(input('Enter a number'))
dup = num
result = 0
while num  > 0:
    temp = num % 10
    num = num / 10
    result = result * 10 + temp

if dup == result:
    print("palindrome")
else:
    print('not palindrome')