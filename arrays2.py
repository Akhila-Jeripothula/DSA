# Arrays part 2

#3 sum:


# class Solution:
#     def threeSum(self, nums):
#         nums.sort()
#         answer = []

#         for i in range(len(nums) - 2):

#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue

#             left = i + 1
#             right = len(nums) - 1

#             while left < right:

#                 total = nums[i] + nums[left] + nums[right]

#                 if total < 0:
#                     left += 1

#                 elif total > 0:
#                     right -= 1

#                 else:
#                     answer.append([nums[i], nums[left], nums[right]])

#                     left += 1
#                     right -= 1

#                     while left < right and nums[left] == nums[left - 1]:
#                         left += 1

#                     while left < right and nums[right] == nums[right + 1]:
#                         right -= 1

#         return answer


#optimal code






#next topic: leetcode 560
#max subarray 
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count=0
#         for i in range(len(nums)):
#             total=0
#             for j in range(i,len(nums)):
#                 total+=nums[j]
#                 if total==k:
#                     count+=1
#         return count        






#LEETCODE 128 - Longest consequtive sequence:

# nums=[100,67,11,4,12,13]
# longest = 0

# for num in nums:
#     current = num
#     count = 1

#     while current + 1 in nums:
#         current += 1
#         count += 1

#         longest = max(longest, count)

# print(longest)


#optimal:
# class Solution:
#     def longestConsecutive(self, nums):
#         num_set = set(nums)
#         longest = 0

#         for num in num_set:
#             if num - 1 not in num_set:
#                 current = num
#                 count = 1

#                 while current + 1 in num_set:
#                     current += 1
#                     count += 1

#                 longest = max(longest, count)

#         return longest






#leetcode 2 :
# class Solution:
#     def addTwoNumbers(self, l1, l2):

#         # Convert first linked list into a number
#         num1 = 0
#         place = 1

#         while l1:
#             num1 = num1 + l1.val * place
#             place = place * 10
#             l1 = l1.next

#         # Convert second linked list into a number
#         num2 = 0
#         place = 1

#         while l2:
#             num2 = num2 + l2.val * place
#             place = place * 10
#             l2 = l2.next

#         # Add the two numbers
#         total = num1 + num2

#         # Convert the result back into a linked list
#         dummy = ListNode(0)
#         current = dummy

#         if total == 0:
#             return dummy.next

#         while total > 0:
#             digit = total % 10

#             current.next = ListNode(digit)
#             current = current.next

#             total = total // 10

#         return dummy.next
