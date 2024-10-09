grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = list(students)
a.sort()
print(a)
A = sum(grades[0]) / len(grades[0])
B = sum(grades[1]) / len(grades[1])
J = sum(grades[2]) / len(grades[2])
K = sum(grades[3]) / len(grades[3])
S = sum(grades[4]) / len(grades[4])
print(a[0],':', A, a[1],':', B, a[2],':',J, a[3],':', K, a[4],':', S)