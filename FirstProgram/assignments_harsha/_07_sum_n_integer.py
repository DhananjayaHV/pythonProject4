user_input = int(input('Enter the nth number >> '))


for i in range(user_input):
    sum_n = user_input*(user_input+1)/2

print("The sum of the first", user_input, "positive integers is",sum_n)
