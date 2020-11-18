userInput = input('请输入你的年龄')
age = int(userInput)
print('您输入的是', age)
# int 把字符串转成 整数
if age >= 18:
  print('小伙子，你成年了！')
else:
  print('小屁孩，快长大!')