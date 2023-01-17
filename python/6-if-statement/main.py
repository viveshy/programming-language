# Find if user can caste vote
age = int(input('Enter your age:'))

if age >= 18:
    print('You are eligible to caste vote.')
else:
    print('You are not eligible to cate vote.')

 
# Select and find your interest
percentage = float(input('Enter your percentage:'))

if percentage >= 70:
    print("Great!")
elif percentage < 70 and percentage >= 50:
    print("Good job!")
else:
    print("Work hard!")