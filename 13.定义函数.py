# def 定义函数

def isAdult(age):
  return age >= 18

xiaoming = {
  'age': 10
}

print(xiaoming['age'])
age = xiaoming['age']
info = '他成年了!' if (isAdult(xiaoming['age'])) else '他没成年呢！'

# print(info)
# print(f'小明{xiaoming['age']}岁,')  error
print(f'小明{age}岁,', info)