def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print(item)

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Gavin','Joe','Jebb']

print(list(map(splicer,names)))

def check_even(num):
    return num%2 == 0

print(list(filter(check_even,my_nums)))

square = lambda num: num ** 2

print(square(5))

print(list(map(lambda num:num**2,my_nums)))

print(list(filter(lambda num:num%2 == 0,my_nums)))

# return index 0 for each name in names
print(map(lambda name:name[0],names))

