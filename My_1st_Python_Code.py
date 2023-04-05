name = str(input("Enter your name : "))
age = int(input("Enter your Age : "))
marks = {} # Define marks as dict
marks['english'] = int(input("Enter English Marks Obtained : "))
marks['maths'] = int(input("Enter Math Marks Obtained : "))
marks['social'] = int(input("Enter Social Marks Obtained : "))
marks['science'] = int(input("Enter Science Marks Obtained : "))
marks['hindi'] = int(input("Enter Hindi Marks Obtained : "))
full_marks = int(input("Total Marks Per Subject : "))
print(f"Total subject : {len(marks)}")
percentage = ((marks["english"] + marks["maths"] + marks["social"] + marks["science"] + marks["hindi"])/(len(marks)*full_marks)*100)
print(f"Received Marks : {percentage}%") 
# percentage > 90
# print(name, "has obtained Grade A+")
# percentage>80 and <=90
# print(name, "has obtained Grade A")
# percentage>70 and <=80
# print(name, "has obtained Grade B")
# percentage>60 and <=70
# print(name, "has obtained Grade C")
# percentage>50 and <=60
# print(name, "has obtained Grade D")
# percentage>40 and <=50
# print(name, "has obtained Grade E")
# percentage<=40
# print(name, "has obtained Grade F")
=======
Name=int(input("Enter your Name"))
Age=int(input("Enter your Age"))
Eng=int(input("Enter English Marks"))
Mat=int(input("Enter Maths Marks"))
Soc=int(input("Enter Social Marks"))
Sci=int(input("Enter Science Marks"))
Hin=int(input("Enter Hindi Marks"))
Per=(Eng+Mat+Soc+Sci+Hin)/5
Per>90
  print(Name, "has obtained Grade A+")
  Per>80 and <=90
  print(Name, "has obtained Grade A")
  Per>70 and <=80
  print(Name, "has obtained Grade B")
  Per>60 and <=70
  print(Name, "has obtained Grade C")
  Per>50 and <=60
  print(Name, "has obtained Grade D")
 Per>40 and <=50
  print(Name, "has obtained Grade E")
 Per<=40
  print(Name, "has obtained Grade F")
>>>>>>> 9ef756bc9f327dab8a1692dc03cb013a8a5bddec
