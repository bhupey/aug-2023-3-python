# union()
s1 = {1,2,3,4}
s2 = {3,4,5,6}

result = s1.union(s2)
print(result)  #{1,2,3,4,5,6}
print(s1|s2) #{1,2,3,4,5,6}


#intersection()
result.s1.intersection(s2)
print(result)  #{3,4}
print(s1 & s2) #{3,4}


#difference()
result.s1.difference(s2)
print(result)  #{1,2}
print(s1-s2)  #{1,2}


#issubset() and issuperser()
s1={1,2,3,4,5,6}
s2={3,4,5,6}

print(s1.issubset(s2))  #False
print(s2.issubset(s1))  #True
print(s2.issuperset(s1))  #False
print(s1.issuperset(s2))  #True




#symmetric_diffrence()
s1={1,2,3,4,5,6}
s2={3,4,5,6}
result = s1.symmetric_difference(s2)
print(result) #{1,2,5,6}
print(s1^s2) #{1,2,5,6}


# symmetric_diffrence_update()
s1.symmetric_difference_update(s2)
print(s1) #{1,2,5,6}
