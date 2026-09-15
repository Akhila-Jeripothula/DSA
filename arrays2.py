Arrays part 2
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
