#!/usr/bin/env python3

import sys


nums = sys.argv[1:]
nums = list(map(int,nums))
nums_sorted = sorted(nums)

# print(nums_sorted)
#count 
count = len(nums)
print('count='+str(count))
#unique
uniq = len(set(nums))
print('unique='+str(uniq))
#min
# def min (nums):
#     res = inf
#     for i in nums:
#         if int(i) <= res:
#             res = int(i) 
#     return res

min_num = min(nums)
print('minimun='+str(min_num))
#max 
max = max(nums)
print('maximun='+str(max))
#sum
# def sum (nums):
#     res = 0
#     for n in nums:
#         res += int(n)
#     return res
sum_num = sum(nums)

#mean
avag =  sum_num /count
if sum_num  % count == 0:
 avag = int (avag)
print('mean=',avag)
#mid 
index = (count-1)/2
mid = nums_sorted[int(index)]
print('median='+str(mid))
#mode 
def mode(nums):
    dict = {}
    for n in nums:
        if n not in dict.keys():
            dict[n] =1
        else:
            dict[n]+=1
    max_count = 0
    mode = 0
    for key, value in dict.items():
        if value > max_count:
            mode = key
            max_count = value
    return mode

mode_num = mode(nums)
print('mode='+str(mode_num))

print('sum='+str(sum_num))


#product
  
def multi(nums):
    res = 1
    for i in nums:
        res = res * int(i)
    return res
products = multi(nums)
print('product='+ str(products))
# print('product=',products)
# print('count=',count)
# print('unique=',uniq)
# print('minimun=',min)
# print('maximun=',max)
# print('mean=',avag)
# print('median=',mid)
# print('mode=',mode_num)
# print('sum=', sum)
# print('product=',products)