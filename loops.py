# # write number between 0 and 1000
# numbers=list(range(0,1000))
# print(numbers)


# #syntax for for loops
# for i in numbers:
#     if i%2==0:
#      print(i)

# # save numbers betwwen 1000 and 2000 divisble by 7
# nums_divisible_by_seven = []
# numbers=list(range(1000,2001))
# for j in numbers:
#          if j%7==0:
#             nums_divisible_by_seven.append(j)

# print(nums_divisible_by_seven) 

#save numbers that are only divisible by 5 and 7 and between 0 and 500 in alist
nums_divisible_only_by_five_and_seven =[]

for k in range(0,501):
    if (k % 5 == 0 and k % 7 == 0):
        nums_divisible_only_by_five_and_seven.append(k)
print(nums_divisible_only_by_five_and_seven)

fruits=["cherry","mango","apple","orange"]
for fruit in fruits:
    if fruit=="apple":
      print("available")
#write a program that calculates the sum of
#for numbers from 1 to 100 using a for loop
      sum=0
      for num in range(1,101):
          sum+=num
          print(sum)
    