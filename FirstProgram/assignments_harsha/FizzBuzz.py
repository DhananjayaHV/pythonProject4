user_input = int(input("Enter the number >> "))

for i in range(100):
    if ((i % 3) == 0 and (i % 5) == 0):
        print("FIzzBuzz")
    elif (i%3)==0:
        print("Fizz")

    elif(i%5)==0:
        print("Buzz")
    else:
        print(i)




