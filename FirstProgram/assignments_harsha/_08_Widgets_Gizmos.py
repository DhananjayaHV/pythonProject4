nur_widgets = int(input("Enter the total number of widgets >> "))
nur_gizmos = int(input("Enter the total number of Gizmos >> "))

weight_widgets =75
weight_gizmos = 112

total_weight = weight_widgets*nur_widgets + weight_gizmos*nur_gizmos
print(f'Total weight of the order is {total_weight} grams')