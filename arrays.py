#Arrays:

#1. Finding the largest number in an array

# nums=[1,2,3,4,5,6]
# largest=nums[0]
# for num in nums:
#     if(num>largest):
#         largest=num
# print(num)




#2.Finding  the smallest number in an array

# nums=[1,2,3,4,5,6]
# smallest=nums[0]
# for num in nums:
#     if(smallest>num):
#         smallest=num
# print(smallest)



#3. Total or sum of numbers in an array

# nums=[1,2,3,4,5,6]
# total=0
# for num in nums:
#     total+=num
# print(total)




#4. sum of even numbers
# nums=[1,2,3,4,5,6]
# total=0
# for num in nums:
#     if(num%2==0):
#         total+=num
# print(total)






#5. sum of odd
# nums=[1,2,3,4,5]
# total=0
# for num in nums:
#     if(num%2!=0):
#         total+=num
# print(total)





#6.sum of numbers greater than 10
# nums=[1,2,6,7,12,15]
# total=0
# for num in nums:
#     if(num>10):
#         total+=num
# print(total)




#7.average of elements
# nums=[2,4,6,8]
# total=0
# for num in nums:
#     total+=num
# print(total/len(nums))





#8.count even numbers:
# nums=[1,2,3,4]
# count=0
# for num in nums:
#     if(num%2==0):
#         count+=1
# print(count)



#9.count odd numbers:
# nums=[1,2,3,4,5]
# count=0
# for num in nums:
#     if(num%2!=0):
#         count+=1
# print(count)




#10.count positive integers:
# nums=[1,2,3,4,-2]
# count=0
# for num in nums:
#     if num>0:
#         count+=1
# print(count)



#11.count negative integers
# nums=[1,2,3,4,-2]
# count=0
# for num in nums:
#     if num<0:
#         count+=1
# print(count)



#12.count zeroes
# nums=[1,2,3,4,0,0,0,0,0]
# count=0
# for num in nums:
#     if(num==0):
#         count+=1
# print(count)





#13.count numbers greater than 10
# nums=[1,2,5,99]
# count=0
# for num in nums:
#     if(num>10):
#         count+=1
# print(count)





#14.count numbers divisible by 3
nums=[1,2,3,4,5,6,9]
count=0
for num in nums:
    if num%3==0:
        count+=1
print(count)