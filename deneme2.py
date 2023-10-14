#This program find type of triangle by length.
length1 = input("Please enter the length1: ")
length2 = input("Please enter the length2: ")
length3 = input("Please enter the length3: ")

if length1.isnumeric() and length2.isnumeric() and length3.isnumeric():
    length1 = int(length1)>0
    length2 = int(length2)>0
    length3 = int(length3)>0
    if (length1+length2)>length3 and (length2+length3)>length1 and (length1+length3)>length2:
        print("triangle occurs")
        if length1==length2==length3:
            print(length1,length2,length3,"Equilateral Triangle")
        elif length1!=length2!=length3:   
            print(length1,length2,length3,"Isosceles Triangle")
        else:
            print(length1,length2,length3,"Scalene Triangle")

    else:
        print("The lengths you enter don't form a triangle")