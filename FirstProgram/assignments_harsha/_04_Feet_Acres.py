lenght = float(input("Enter the lenght of the former's land in feets : "))
width = float(input("Enter the width of the former's land  in feets : "))

area=lenght*width
print(area)

area_acre = area/43560
print(f'The total area of the field is {area_acre} acres')