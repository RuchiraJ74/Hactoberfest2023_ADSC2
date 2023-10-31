input("Enter the students name : ")


sub1=int(input("Enter the marks of subject 1 : "))
sub2=int(input("Enter the marks of subject 2 : "))
sub3=int(input("Enter the marks of subject 3 : "))


average=(sub1+sub2+sub3)/3
print("Average marks of the student : ",average)

if average>=90 and average<=100:
  print("Grade obtained by student is O.")
  print("Student is Pass with distinction.")

elif average>=80 and average<=89:
  print("Grade obtained by student is A.")
  print("Student is Pass with distinction.")

elif average>=70 and average<=79:
  print("Grade obtained by student is B.")
  print("Student is Pass with distinction.")

elif average>=60 and average<=69:
  print("Grade obtained by student is C.")
  print("Student is Pass with distinction.")

elif average>=40 and average<=59:
  print("Grade obtained by student is D.")
  print("Student is Pass.")

else:
  print("Grade obtained by student is F.")
  print("Student is Fail.")
