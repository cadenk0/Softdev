def first_last6(nums):
  if nums[0] == 6:
    return True
  if nums[len(nums)-1]==6:
    return True
    
  return False

print(first_last6([1, 2, 3, 4, 5, 6]))

def same_first_last(nums):
  if len(nums) >= 1:
    if nums[0] == nums[-1]:
      return(True)
    else:
      return(False)
  else:
    return(False)


def make_pi():
  a = [3, 1, 4]
  return(a)


def common_end(a, b):
  if a[0]==b[0] or a[-1]==b[-1]:
    return(True)
  else:
    return(False)

def sum3(nums):
  sum = 0
  for i in nums:
    sum += i
  return sum

def rotate_left3(nums):
  nums.append(nums.pop(0))
  return nums

def reverse3(nums):
  count = 2
  result = []
  for i in range(3):
    result.append(nums.pop(count))
    count -= 1
  return result

def max_end3(nums):
  m = max(nums[0], nums[len(nums)-1])
  for i in range(len(nums)):
    nums[i-1] = m
  return nums

def sum2(nums):
  return sum(nums[:2])

def middle_way(a, b):
  result = []
  result.append( a[1]) 
  result.append(b[1])
  return result

def make_ends(nums):
  result = []
  result.append(nums[0])
  result.append(nums[len(nums)-1])
  return result

def has23(nums):
  return(2 in nums or 3 in nums)

