# 1.
name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
total_number = 0
with open("numbers.txt") as in_file:
    for i in range(2):
        number = int(in_file.readline())
        total_number += number
print(total_number)

# 4.
total_number = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        number = int(line)
        total_number += number
print(total_number)
