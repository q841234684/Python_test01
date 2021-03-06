m1 = {'name': '小明', 'age': 13, 'score': 95}
print(m1)
print(m1["name"])
print(len(m1))
m1['sex'] = '男'
print(m1)
m2 = {'color': 'red', 'price': 12.423}
m1.update(m2)
print(m1)
m1.pop("price")
print(m1)
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
if 'price' in m1:
    print(m1['price'])
else:
    print('不含price')
for key in m1.keys():
    print('键:' + key + ' 值：', m1[key])
for value in m1.values():
    print(value)
for entry in m2:
    print('entry:', entry)
for key, value in m2.items():
    print('key:', key, 'value', value)
m1.clear()
print(m1)
m2 = {'name': {'first': 'Johney', 'last': 'Lee'}, 'age': 13}
print(m2['name']['first'])

# 创建字典有以下三种方法
# dict(a=1, b=2, c=2)
# dict([(a,1), (b,2), (c,3)])
# dict({a:1, b:2, c:3})
