#Arrays:(1st part)





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
# nums=[1,2,3,4,5,6,9]
# count=0
# for num in nums:
#     if num%3==0:
#         count+=1
# print(count)




#LINEAR SEARCH

#15. find the target element

# nums=[1,2,3,4,5,6,34,52,12,11]
# target=11
# found=False
# for num in nums:
#     if(num==target):
#         found=True
#         break
# if found:
#     print("FOUND BABY")
# else:
#     print("NOT FOUND BABY")





#16.
# nums=[10,20,30,40]
# for index,num in enumerate(nums):
#     print(index,num)



#17. index
# nums=[10,20,30,40]
# target=30
# found=False
# for index,num in enumerate(nums):
#     if(num==target):
#         found=True
#         break
# if found:
#     print(index)
# else:
#     print("Element not found")




#18.

# nums = [4,8,15,16,23,42]
# target = 23
# found=False
# for index,num in enumerate(nums):
#     if target==num:
#         found=True
#         break
# if(found):
#     print(index)
# else:
#     print("element not found")




#19. count occurences
# nums=[1,2,3,4,2,4,2]
# target=2
# count=0
# for num in nums:
#     if(target==num):
#         count+=1
# print(count)



#20.find the first occurence

# nums=[1,2,3,4,5,3,6,3]
# target=3
# found=False
# for index,num in enumerate(nums):
#     if num==target:
#         found=True
#         break
# if found:
#     print(f"Element found at index{index}")
# else:
#     print("not found")




#21.find the last occurence
# nums=[1,2,3,4,3,2,4,3]
# target=3
# last_index=-1
# for index,num in enumerate(nums):
#     if(target==num):
#         last_index=index
# print(last_index)






#largest
# nums = [8, 15, 3, 21, 10]
# largest=nums[0]
# for num in nums:
#     if(num>largest):
#         largest=num
# print(largest)



#second largest

# nums=[8,15,3,21,10]
# largest=float("-inf")
# secondlargest=nums[-1]
# for num in nums:
#     if(num>largest):
#         secondlargest=largest
#         largest=num
#     elif(num>secondlargest and num!=largest):
#         secondlargest=num
# print(secondlargest)




#reverse of an array:


# nums=[10,20,30,40,50]
# for i in range(len(nums)-1,-1,-1):
#     print(nums[i])


#method 1:
# nums=[10,20,30,40,50]
# rev=[]
# for i in range(len(nums)-1,-1,-1):
#     rev.append(nums[i])
# print(rev)
    

#method2:(Two pointer approach)    ********************************

# nums=[1,2,3,4,5,6]
# left=0
# right=len(nums)-1
# while left<right:
#     temp=nums[left]
#     nums[left]=nums[right]
#     nums[right]=temp
#     left+=1
#     right-=1

# print(nums)


#sorted array
# nums=[1,3,5,7,2,23,18]
# sorted_array=True
# for i in range(len(nums)-1):
#     if(nums[i]>nums[i+1]):
#         sorted_array=False
#         break
# print(sorted_array)






# LEETCODE - 1929 ***

# nums=[1,2,1]
# ans=[]
# for num in nums:
#     ans.append(num)
# for num in nums:
#     ans.append(num)
# print(ans)




#move zeroes   ************************


#method 1- by creating an array

# nums=[0,5,2,0]
# res=[]
# for num in nums:
#     if(num!=0):
#         res.append(num)
# for i in range(nums.count(0)):
#     res.append(0)

# print(res)




#method 2 - two pointer approach

# nums=[1,0,2,3,0,4]
# left=0
# for right in range(len(nums)):
#     if nums[right]!=0:
#         temp=nums[left]
#         nums[left]=nums[right]
#         nums[right]=temp
#         left+=1
# print(nums)




#leet code : remove duplicates in a sorted array:

# nums=[1,1,2,2,3,3,4,4]
# left=0
# for right in range(1,len(nums)):
#     if nums[right]!=nums[left]:
#         left+=1
#         nums[left]=nums[right]

# print(nums)
# print(left+1)







# New Topic : Rotate Arrayyyy **

# nums=[1,2,3,4,5,6]
# k=2
# nums[:]=nums[-k:]+nums[:-k]
# print(nums)



#OR


# Leet code 189 solution

# class Solution:
#     def rotate(self,nums,k):
#         k=k%len(nums)
#         def reverse(left,right):
#             while left<right:
#                 nums[left],nums[right]=nums[right],nums[left]
#                 left+=1
#                 right-=1
#             reverse(0,len(nums)-1)
#             reverse(0,k-1)
#             reverse(k,len(nums)-1)





#*****
# Next topic : Running sum in 1D array ( Prefix sum)



#method 1: by creating a new array :
# nums=[1,2,5,7]
# res=[]
# total=0
# for num in nums:
#     total+=num
#     res.append(total)
# print(res)



#method 2:
# nums = [5, 2, 7, 1]
# for i in range(1, len(nums)):
#     nums[i] = nums[i] + nums[i-1]
# print(nums)






# new concept : Prefix sum with range queries

#prefix sum
# nums=[1,2,3,4,5,6,7,8]
# prefix=[0]*len(nums)
# prefix[0]=nums[0]
# for i in range (1,len(nums)):
#     prefix[i]=prefix[i-1]+nums[i]
# print(prefix)


#range queries
# left=2
# right=4
# if(left==0):
#     answer=prefix[right]
# else:
#     answer=prefix[right]-prefix[left-1]
# print(answer)





#  PIVOT INDEX:
# nums=[1,7,3,6,5,6]
# total=sum(nums)
# left_sum=0
# for i in range(len(nums)):
#     right_sum=total-left_sum-nums[i]
#     if(left_sum==right_sum):
#         print(i)
#     left_sum+=nums[i]






# MISSING NUMBER :

#1.

# nums=[3,0,1,4]
# n=len(nums)
# expected_sum=n*(n+1)//2
# actual_sum=sum(nums)
# missing=expected_sum-actual_sum
# print(missing)



#2.
# nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# n=len(nums)
# x=n*(n+1)//2
# y=sum(nums)
# z=x-y
# print(z)



# leetcode 268
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n=len(nums)
#         expected_sum=n*(n+1)//2
#         actual_sum=sum(nums)
#         missing=expected_sum - actual_sum
#         return missing






# NEXT TOPIC : MAJORITY ELEMENT

# nums=[2,2,1,1,1,2,2]
# count={}
# for num in nums:
#     if num in count:
#         count[num]+=1
#     else:
#         count[num]=1
# for num in count:
#     if count[num]>len(nums)//2:
#        print(num)
        
#booyer moore method:
# nums=[2,2,1,1,1,2,2]
# candidate=None
# count=0
# for num in nums:
#     if count==0:
#         candidate=num
#     if num==candidate:
#         count+=1
#     else:
#         count-=1
# print(candidate)



# #leetcode: 169

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count={}
#         for num in nums:
#             if num in count:
#                 count[num]+=1
#             else:
#                 count[num]=1
#         for num in count:
#             if count[num]>len(nums)//2:
#                 return num
        

#other method: Booyer Moore method:

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate=None
#         count=0
#         for num in nums:
#             if count==0:
#                 candidate=num
#             if num==candidate:
#                 count+=1
#             else:
#                 count-=1
#         return candidate






#Another Topic: Best time to buy and sell stock:

# prices=[1,3,5,2,7]
# min_price=prices[0]
# max_profit=0
# for price in prices:
#     if price<min_price:
#         min_price=price
#     profit=price-min_price
#     if profit>max_profit:
#         max_profit=profit
# print(max_profit)




# Another Topic: TWO SUM **********

#BRUTE FORCE APPROACH:
# nums=[1,2,3,6,4]
# target=10
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print([i,j])


#leet code 1:
# class Solution:
#     def twoSum(self,nums,target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]



#optimal approach:
# nums=[3,2,4]
# target=6
# seen={}
# for i in range(len(nums)):
#     complement=target-nums[i]
#     if complement in seen:
#         print([seen[complement],i])
#     seen[nums[i]]=i


        

# TOPIC : CONTAINS DUPLICATE
# nums=[1,2,3,1]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]==nums[j]:
#             print(True)
# print(False)


#optimal:
# class Solution:
#     def containDuplicates(self,num):
#         nums=[1,2,1]
#         seen=set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False



# TOPIC : Product of Array except itself
nums=[1,2,3,4]
res=[]

for i in range(len(nums)):
    product=1
    for j in range(len(nums)):
        if(i!=j):
            product*=nums[j]
    res.append(product)
print(res)
    
