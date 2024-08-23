sub_1=int(input("Enter Marks: "))
sub_2=int(input("Enter Marks: "))
sub_3=int(input("Enter Marks: "))

total_percentage=((sub_1+sub_2+sub_3)/3)

if(total_percentage>=40 and sub_1>=33 and sub_2>=33 and sub_3>=33):
    print("You're Passed:",total_percentage)

else:
    print("You're Failed:",total_percentage)




