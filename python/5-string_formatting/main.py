# Numbers
prime = 2
composite = 4 

# PREVIOUS
print('prime number is', prime, 'and composite number is', composite)

# ____________STRING FORMATTING__________
#1. Using Format method
print('prime number is {0} and composite number is {1}'.format(prime, composite))

decimal_num = 3.142546
print('decimal number with 3 precision is {0:.3}'.format(decimal_num))

print('decimal number till 3 decimal places is {0:.3f}'.format(decimal_num))

#2. Using f-string
print(f'prime number is {prime} and composite number is {composite}')
print(f'decimal number till 3 precision is {decimal_num:.3}')
print(f'decimal number till 3 decimal places is {decimal_num:.3f}')