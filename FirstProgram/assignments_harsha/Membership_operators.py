l1=[1,2,3,4,5,6,7]
l2=[9,8,10,1,2]
l=l1+l2
numb = []

for i in l1:
    if i not in l2:
        numb.append(i)


for i in l2:
    if i not in l1:
        numb.append(i)


print(numb)