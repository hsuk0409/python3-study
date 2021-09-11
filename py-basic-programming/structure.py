# list
students = ["친구1", "친구4", "친구2", "친구3"]

print(students)
print(len(students))
students.append('친구5')
print(students)
students.remove(students[2])
print(students)
students.insert(1, '친구1.5')
print(students)

cnt = 1
for student in students:
    print('{0}번째 학생={1}'.format(cnt, student))
    cnt += 1

students.sort()
print(students)

students.sort(reverse=True)
print(students)

students_slicing = students[1:3]
print(students_slicing)

students.clear()
print(students)

# dictionary
dic = {'name': 'justin'}
print(dic)
print(dic.get('name'))