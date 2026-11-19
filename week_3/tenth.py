#List in python
nums = [ 25, 12, 36, 95,14 ]

nums[1] = 13
#print(nums)

for i in nums:
    print(i)

nums.append(37)
nums.insert(1,14)
nums.remove(14)
#nums.clear()

nums.extend([ 29, 12, 14, 26])
print(nums)

print(nums.pop())
print(min(nums))
print(max(nums))
#print(nums.sort())