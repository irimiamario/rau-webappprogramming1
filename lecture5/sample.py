variable1 = 10
this_is_a_variable = 20
this_is_another_variable = 20.5
this_is_my_fourth_variable = 122.21

string1 = 'this is my first string'
string2 = "this is my second string"
string3 = f"this is my third string. Variable1 = {variable1}"

print(string3.split("."))

list1 = [10, 'string2', variable1, string2]
element1 = list1[0]
element3 = list1[2]
print(f"list1 = {list1}")
list1[0] = 20
list1[3] = "test"
print(f"list1 = {list1}")

list1.append(19)
list1.append([1,2,3,4])
list1.append('string')
print(list1)
list1[5].append(20)
print(list1)
other_string = list1[-1].upper()
print(list1)
print(other_string)
list1.append(other_string)
print(list1)
list2 = [5,1,2,6]
list2.sort(reverse=True)
print(list2)
list2.pop()
print(list2)
print(list2.index(5))

t = (1, 2, 'stest', list2)
print(t)
t[-1].append(20)
print(t)

s1 = {1,3,4,0,1,1,1,1,1,1}
s2 = {1,2,2,2,2,2}
s3 = s1.difference(s2)
print(s3)

# key: value
d1 = {
    "name": "andrei",
    "age": 32,
    "country": "romania"
}
print(d1)
d1["name"] = "liviu"
d1["new_key"] = "new_value"
print(d1)
k = list(d1.keys())
print(k)
v = list(d1.values())
print(v)

# logical op
# and, or 
# ==, !=, >, <, <=, >=
# not 
# True, False
print(variable1 == this_is_a_variable)
print(True != False)

variable1 = this_is_a_variable
if variable1 == this_is_a_variable:
    print("they are equal")
elif variable1 == this_is_another_variable:
    print("v1 and another var are equal")
else:
    print("they are not equal")

n = input()
n = int(n)
print(n+1)

for el in list1:
    print(el)
    print(el, el, el)

a = 10
while a > 0:
    print(a)
    a = a - 1




