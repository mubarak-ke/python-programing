day_of_week=["monday","tuesday","wednesday","thursady","friday","saturday","sunday"]
day_of_week[0]='friday'
day_of_week.append("monday")
# day_of_week.clear()
list=day_of_week.copy()
print(day_of_week.count("ttt"+"monday"))
list1=[1,2,3,4,5]
day_of_week.extend(list1)
print(day_of_week.index("tuesday"))
# print(day_of_week)
day_of_week.insert(1,"june")
print(day_of_week)
day_of_week.pop()
print(day_of_week)
day_of_week.reverse()
print(day_of_week)
list.sort()
print(list)

numbers=[1,2,3,4,[10,20,30], 5,6,7,8]
print(numbers[4][1])

#updating elements in a list
numbers[0]=100
