data = [2,4,5,6]
result = []
for i in data:
    result.append(i**2)
print(result)


result = [i**2 for i in data]
print(result)

result= [i for i in range(15) if i %2 ==0]
print(result)

data = [("name", "jon"), ("age", 30), ("address", "KTM")]
dict = {}
for key,values in data:
    dict[key] = values
print(dict)


count = 0
num = 0
while count != 20:
    if num % 2 == 0:
        print(num)
        count += 1
    num += 1
 