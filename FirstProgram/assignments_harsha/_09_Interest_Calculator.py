amount = int(input('Enter the amount : '))
time=[1,2,3]
total_saving_amount = amount
saving_amount = []
for i in time:
    interest = 4
    total_amount=total_saving_amount*interest*i/100
    total_saving_amount = total_amount+amount
    saving_amount.append(total_saving_amount)


print(saving_amount)
