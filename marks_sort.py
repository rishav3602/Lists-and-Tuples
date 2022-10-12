"""
Write a program to accept marks of six students and display them in a sorted manner.
"""

mark_stu1 = int(input("Enter you marks :"))
mark_stu2 = int(input("Enter you marks :"))
mark_stu3 = int(input("Enter you marks :"))
mark_stu4 = int(input("Enter you marks :"))
mark_stu5 = int(input("Enter you marks :"))
mark_stu6 = int(input("Enter you marks :"))

marks_list = [mark_stu1,mark_stu2,mark_stu3,mark_stu4,mark_stu5,mark_stu6]
marks_list.sort()
print(marks_list)