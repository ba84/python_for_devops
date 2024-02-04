# Task 1

a = 5
b = 2

sum = a + b
sub = a - b
mul = a * b
div = a / b

# Task 2

less_than = a < b
great_than = a > b
equal = a == b
not_equal = a != b

# Task 3
x = True
y = False

op1 = 5 == (x and y)
op2 = 5 == (x or y)
#op3 = 6 == x not y

# Task 4

total = 10

total += 5
total -= 3
total *= 2
total /= 4

print(total)

# Task 6 (I skipped 5 because i am not familiar with bitewise)

my_list = ["one", 2, "three", 4, 5.5, 6, "7"]

same = type(my_list[0]) is type(my_list[2])
not_same = type(my_list[1]) is not type(my_list[4])
mem1 = 5.5 in my_list
mem2 = type(str) not in my_list

print(mem2)