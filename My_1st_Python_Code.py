name = input("Enter your name: ")
age = int(input("Enter your age: "))
full_marks = int(input("Total Marks Per Subject: "))

# Define an empty dictionary
marks = {}

while True:
    marks['english'] = int(input("Enter English Marks Obtained: "))
    if marks['english'] > full_marks:
        print("You cannot enter more than your Full Marks")
        continue

    marks['maths'] = int(input("Enter Math Marks Obtained: "))
    if marks['maths'] > full_marks:
        print("You cannot enter more than your Full Marks")
        continue

    marks['social'] = int(input("Enter Social Marks Obtained: "))
    if marks['social'] > full_marks:
        print("You cannot enter more than your Full Marks")
        continue

    marks['science'] = int(input("Enter Science Marks Obtained: "))
    if marks['science'] > full_marks:
        print("You cannot enter more than your Full Marks")
        continue

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