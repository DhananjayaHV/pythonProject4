nur_container = int(input("Enter the total number of container : "))
size_container = float(input("Enter the size of the cotainer in ltrs : "))


if size_container<=1:
    refund = nur_container*0.10
    print(f'Total amount refunded is {refund}$')

else:
    refund= nur_container*0.25
    print(f'Total amount refunded is {refund}$')