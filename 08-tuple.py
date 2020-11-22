print('tuple 是不可变的，类似于ES6 const')

people = ('张三', [])

print(people, '尝试修改一下')

name = input('你的名字?\n')

people[1].append(name)

print('结果是', people)
