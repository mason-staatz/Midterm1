"""
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
"""

import CourseClass as cc


def main():

    name = "MIS 4322 - Advanced Python"
    crn = "250309"
    seats = 4
    status = "open"
    students = ["John", "James", "Jill", "Jack", "Joanne"]

    courses = cc.Course(name, crn, seats, status)
    registers = cc.Register(name, crn)

    for i in students:
        print(registers.get_name())
        print("Course Name: ", courses.get_name())
        print("CRN: ", courses.get_crn())
        courses.update_seat_count()
        print("Seats Left: ", courses.get_seats())
        print(
            "Sorry ",
            registers.get_name(),
            "registration is",
            courses.get_status(),
            "for",
            courses.get_name(),
        )


# print('Student Name: ', registers.get_name())

main()
