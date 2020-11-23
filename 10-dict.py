# 类似于 js 对象, 查找速度快，用空间换取时间
dog = {
  'age': 10,
  'name': '小黄'
}
# dog.pop('say') error
print(dog)

cn ={}
cn.setdefault('123',[]).append('123')
print(cn)
cn.setdefault('123',[]).append('456')
print(cn)