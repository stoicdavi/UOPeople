import time
name = ('David', 'Beckham')
names= ('john', 'Dan', 'David')
# concatenation of two tuples
names1 = name + names
print(names1)
time.sleep(3)
age = [45, 46]


for p in zip(names1, age):
    print(p)