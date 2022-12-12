names = ["Anis", "niloy", "nabil", "rohit"]

for i in names:
    print("you are invited to dinner at my house " + i)

pop_name = names.pop()
print(pop_name + " wont make it tonight")
names.append("adnan")

for i in names:
    print("you are invited to dinner at my house " + i)


names.insert(0, 'ayon')
names.insert(5, 'marium')
names.append('shamol')
print("\n")
for i in names:
    print("you are invited to dinner at my house " + i)