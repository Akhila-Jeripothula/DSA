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

class Solution:
    def rotate(self,nums,k):
        k=k%len(nums)
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
            reverse(0,len(nums)-1)
            reverse(0,k-1)
            reverse(k,len(nums)-1)