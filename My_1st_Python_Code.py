name = input("Enter your name: ")
full_marks = int(input("Full Marks Per Subject: "))
while full_marks < 1:
    print(f"Full marks cannot be less than 1")
    full_marks = int(input("Full Marks Per Subject Again: "))

# Define Subject List
subjects = ['English', 'Maths', 'Social', 'Science', 'Hindi', "Computer Science"]

# Define an empty dictionary to store marks of each subject
marks = {}
# define int var
tot_marks = 0
for sub in subjects:
    marks[sub] = input(f"Please enter marks obtained in {sub} : ")
    while not marks[sub].isnumeric() or int(marks[sub]) > full_marks or int(marks[sub]) < 0 :
        print(f"Obtained marks should be between 0 to {full_marks}, and non-special character")
        marks[sub] = input(f"Please re-enter marks obtained in {sub} again : ")
    marks[sub] = int(marks[sub])
    tot_marks += int(marks[sub])

# Print Total subject & marks
print(f"Total subject: {len(subjects)}")
print(f"Total marks: {tot_marks}")

# Calculate percentage scored
percent = int(tot_marks / (len(subjects) * full_marks) * 100)
print(f"Percentage scored : {percent}%")

# Define the grade table
grade_range_percent = [
    {"grade": "A+", "s": 91, "e": 100},
    {"grade": "A", "s": 81, "e": 90},
    {"grade": "B", "s": 71, "e": 80},
    {"grade": "C", "s": 61, "e": 70},
    {"grade": "D", "s": 51, "e": 60},
    {"grade": "E", "s": 41, "e": 50},
    {"grade": "F", "s": 1, "e": 40}
]
# Loop thru the grade table list element 
for gr_dic in grade_range_percent:
    # Print my grade table
    # print(f"Grade {gr_dic['grade']} for marks between {gr_dic['s']}% to {gr_dic['e']}%")

    # Check by element dict key value in range to compare with percent
    if int(gr_dic['s']) <= percent <= int(gr_dic['e']):
        print(f"{name} has scored grade : {gr_dic['grade']}")

    # Another alternative example of how to find the grade
    # marks_range = range(int(gr_dic['s']), (int(gr_dic['e'])+1))
    # print(marks_range)
    # if percent in marks_range:
        # print(f"Grade scored : {gr_dic['grade']}")