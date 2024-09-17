def count_evens(nums):
  total=0
  for i in nums:
    if i % 2 == 0:
      total+=1
  return(total)


def big_diff(nums):
  return(max(nums)-min(nums))

def centered_average(nums):
  nums=nums[:nums.index(max(nums))] + nums[nums.index(max(nums))+1:]
  nums=nums[:nums.index(min(nums))] + nums[nums.index(min(nums))+1:]
  total=0
  for i in nums:
    total+=i
  av = total / len(nums)
  return(av)

def sum13(nums):
  total=0
  if len(nums) == 0:
    return(0)
  else:
    for i in nums:
      if 13 in nums:
        nums=nums[:nums.index(13)] + nums[nums.index(13)+2:]
    for i in nums:
      total+=i
  return(total)


def sum67(nums):
    in_section = False
    sum = 0
    for num in nums:
        if num == 6:
            in_section = True
        elif num == 7 and in_section:
            in_section = False
        elif not in_section:
            sum += num
    return sum



def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False


