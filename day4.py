'''day-4 class
List is mutable,duplicate value
TUPLE is unchangable,immutable
Dictionary is collection of item(key:value)'''
#Input of student details in list,tuple,dictionary

a = []
b = ()
c = {}

name = input("Enter the name: ").title()
usn = input("Enter the USN: ").upper()
branch = input("Enter the branch: ")
sem = input("Enter the semester: ")

a.extend([name, usn, branch, sem])

b = (name, usn, branch, sem)

c["Name"] = name
c["USN"] = usn
c["Branch"] = branch
c["Semester"] = sem


print(a)
print(b)
print(c)


print(type(a))
print(type(b))
print(type(c))
