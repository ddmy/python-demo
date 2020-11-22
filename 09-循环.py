nums = list(range(21))
print(nums)
result = 0
for x in nums:
  result += nums[x]
print(result)

n = 1
total = 0
while n <= 1000:
  if n > 100: break
  total += n
  n += 1
print(total)


x = 0
while x < 20:
  x += 1
  if x % 2 == 0: continue
  print(x)