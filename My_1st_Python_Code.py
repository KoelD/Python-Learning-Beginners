name = input("Enter your name: ")
full_marks = int(input("Full Marks Per Subject: "))
while full_marks < 1:
    print(f"Full marks cannot be less than 1")
    full_marks = int(input("Full Marks Per Subject Again: "))

# Define Subject List
subjects = ['English', 'Maths', 'Social', 'Science', 'Hindi', "Computer Science"]

# Define an empty dictionary to store marks of each subject
marks = {}

# Print Total subject & marks
print(f"Total subject: {len(subjects)}")
print(f"Total marks: {tot_marks}")

# Calculate percentage scored
percent = int(tot_marks / (len(subjects) * full_marks) * 100)
print(f"Percentage scored : {percent}%")

    marks['social'] = int(input("Enter Social Marks Obtained: "))
    if marks['social'] > full_marks:
        print("You cannot enter more than your Full Marks")
        continue

    # Check by element dict key value in range to compare with percent
    if int(gr_dic['s']) <= percent <= int(gr_dic['e']):
        print(f"{name} has scored grade : {gr_dic['grade']}")

    marks['hindi'] = int(input("Enter Hindi Marks Obtained: "))
    if marks['hindi'] > full_marks:
        print("You cannot enter more than your Full Marks")
        continue

    break

print(f"Total subject: {len(marks)}")
percentage = ((marks["english"] + marks["maths"] + marks["social"] + marks["science"] + marks["hindi"]) / (len(marks) * full_marks) * 100)
print(f"Received Marks: {percentage}%")

if percentage > 90:
    print(name, "has obtained Grade A+")
elif percentage > 80 and percentage <= 90:
    print(name, "has obtained Grade A")
elif percentage > 70 and percentage <= 80:
    print(name, "has obtained Grade B")
elif percentage > 60 and percentage <= 70:
    print(name, "has obtained Grade C")
elif percentage > 50 and percentage <= 60:
    print(name, "has obtained Grade D")
elif percentage > 40 and percentage <= 50:
    print(name, "has obtained Grade E")
else:
    print(name, "has obtained Grade F")