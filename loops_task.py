# #number one
# num=list(range(1,51))
# print(num)
# #number two
# num2=[]
# for num in numbers:
#      if num%7==0 or num%5==0:
#           num2.append(num)
#           print(num2)
        
# #number three
# numbers=list(range(10,41))
# sum=0
# average=[]
# for i in numbers:
#      sum=sum+i
#      average.append(i)
# print(sum)
# avg=sum/len(average)
# print(avg)
# #mode
# #median

#number four
odd_numbers=[]
for number in range(10,51):
     if number %2!=0:
          odd_numbers.append(number)
odd_numbers1=odd_numbers[0:10]
print(odd_numbers1)

#number five
# numbers=int(input("enter number"))
# print(f"multiplication table for{numbers}:")
# for i in range(1,11):
#      result= numbers*i
#      print(f"{numbers} x {i} = {result}")
num=list(range(1,11))
number=float(input("enter number:"))
for i in num:
     mult=i*number
     result=f"{number}x{i}={mult}"
     print(result)

#number five
even_numbers=[]
for number in range(1,51):
     if number %2==0:
          even_numbers.append(number)
even_numbers1=even_numbers[0:10]
print(even_numbers1)     