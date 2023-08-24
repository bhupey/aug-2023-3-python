student = {"name":"jane", "age": 30, "address": "KTM"}
student["roll_no"] = 21
print(student) #{"name":"jane", "age": 30, "address": "KTM", "roll_no": 21}

student["name"] = "jon"
print(student)  #{"name":"jon", "age": 30, "address": "KTM", "roll_no": 21}


other = {"institute": "broadway", "phone_no": 95666555}
student.update(other)
print(student) 
#{'name': 'jon', 'age': 30, 'address': 'KTM', 'roll_no': 21, 'institute': 'broadway', 'phone_no': 95666555}


student.update(lastname="ABC")
print(student)
#{'name': 'jon', 'age': 30, 'address': 'KTM', 'roll_no': 21, 'institute': 'broadway', 'phone_no': 95666555, 'lastname': 'ABC'}
