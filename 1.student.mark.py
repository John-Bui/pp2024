def get_number_of_students():
    return int(input("Enter the number of students: "))

num_students = get_number_of_students()

def get_student_information():
    student_records = {}
    for _ in range(num_students):
        student_id = input("Enter the student ID: ")
        student_name = input("Enter student name: ")
        date_of_birth = input("Enter date of birth: ")
        student_records[student_id] = {'student_name': student_name, 'date_of_birth': date_of_birth}
    return student_records

def get_number_of_courses():
    return int(input("Enter the number of courses: "))

num_courses = get_number_of_courses()

def get_course_information():
    course_records = {}
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        course_records[course_id] = course_name
    return course_records

def get_student_marks(student_records, course_records):
    marks_records = {}
    for course_id in course_records:
        marks_records[course_id] = {}
        print(f'Enter the marks for {course_records[course_id]}')
        for student_id in student_records:
            mark = float(input(f"Enter mark for {student_records[student_id]['student_name']} (ID: {student_id}): "))
            marks_records[course_id][student_id] = mark
    return marks_records

students_info = get_student_information()
courses_info = get_course_information()
marks_info = get_student_marks(students_info, courses_info)

# Print all values
print("Student Information:")
for student_id, student_info in students_info.items():
    print("Student ID:", student_id)
    for key, value in student_info.items():
        print(key + ":", value)
    print()

print("Course Information:")
for course_id, course_name in courses_info.items():
    print("Course ID:", course_id)
    print("Course Name:", course_name)
    print()

print("Student Marks:")
for course_id, course_marks in marks_info.items():
    print("Course ID:", course_id)
    for student_id, mark in course_marks.items():
        print(f"Student ID: {student_id}, Mark: {mark}")
    print()
