grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
day_1 = {"Mary", "Jake", "Sam", "Alex", "Percy", "Jessica", "Trent", "Mahmoud"}
day_2 = {"Jake", "Sam", "Alex", "Percy", "Mahmoud", "Trent", "Caleb", "Zayne"}
a = len(grades)
b = max(grades)
c = min(grades)
d = (sum(grades))/len(grades)
e = (len(day_1.union(day_2)))
f = day_1.intersection(day_2)
g = day_1.symmetric_difference(day_2)#OR (day_1-day_2).union(day_2-day_1)
print(a,"Students took the exam.")
print ("The highest grade was a", b)
print("The lowest grade was a ", c)
print("The average grade for the exam was a ", d)
print(e,"students attended the class.")
print(f, "attended both class days.")
print(g,"attended one class day.")