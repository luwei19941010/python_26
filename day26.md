day26

### 今日内容

- re模块
  - python中方法
  - python中的方法+正则表达式的新内容
    - 分组
    - 分组命名
    - 引用分组
  - 爬虫的小列子

#### 1.re模块

##### 1.1 re.findall('\d+','luwei123' )

​	findall 会匹配字符串中所有符合规则项，并返回一个列表[ ]，如果没有匹配到则返回空列表[ ]。

##### 1.2re.search('\d+','luwei123' )

```
ret=re.search('\d+','luwei123' )
print(ret)#是一个对象，如果能匹配上返回一个对象，如果不能匹配上返回None
print(ret.group)#如果是对象，那么这个对象内部实现了group，所以可以取值
			   #如果是None，那么这个对象不可能实现了group方法，所以报错
			   #加if 判断避免
#会从头到尾，匹配字符串中取出第一个符合条件的项。
```

##### 1.3re.match('/d','luwei123')

```
ret=re.match('/d','luwei123')#返回一个对象
print(ret)
#效果类似search但是差别在于match是从第一个字符开始是否符合匹配规则，类似匹配规则前有个^
#match=seach+^正则
```

#### 2.进阶方法

- 时间复杂度（效率）
  - complie()
  - 在同一个正则表达式重复使用多次的时候使用能够减少时间的开销
- 空间复杂度（内存占用率)
  - finditer()
  - 在查询的结果超过1个情况下，能够有效的减少内存，降低空间复杂度从而降低时间复杂度
- 用户体验

##### 2.1 re.finditer('/d','saasadafdsaf'*2000000)

```
ret=re.finditer('/d','saasadafdsaf'*2000000)#ret是迭代器。
for i in ret:	#迭代出来每一项都是一个对象。
	print(i.group())#通过group来取值。
```

##### 2.2re.compile( )

```
ret=re.compile('\d+')#编译正则表达式
ret.findall('ASDASDWQsdasd')
#\d+ 正则表达式 ----> 字符串
	#\d str
		#循环str，找到所有的数字
```

结合：

```
ret=re.compile('\d+')#
ret2=ret.finditer('asdasbdkjkj123')
for i in ret2:
	print(i.group())
```

##### 2.3re.sub('\d','D','asdasd124wqe3132w12qe')

```
ret=re.sub('\d','D','asdasd124wqe3132w12qe',1)#只替换1个，返回字符串
print(ret)
```

```
ret=re.subn('\d','D','asdasd124wqe3132w12qe')#返回元组
print(ret)
```

##### 2.4re.split( '\d','alex83taibai872')

```
ret=re.split( '\d+','alex83taibai82luwei19')#返回列表
ret=re.split( '(\d+)','alex83taibai82luwei19')#默认自动保留分组中的内容
print(ret)
```

#### 3.分组与re模块结合

##### 3.1分组应用

```
s1=<h1>wahaha</h1>
import re
ret=re.search('<(\w+)>(.*?)(</\w+>)',s1)
print(ret.group(0))#group参数默认为0，表示取整个正则匹配的结果。
print(ret.group(1))#取第一个分组中的内容
print(ret.group(2))#取第二个分组中的内容
ret=re.search('<(？P<tag>\w+)>(？P<cont>.*?)(</\w+>)',s1)
```

##### 3.2分组命名表达式

```
(?P<名字>正则表达式)
search group('组名')
```

3.3引用分组

```
(?P=组名)表示这个组中的内容必须和之前已经存在的一组匹配到的内容完全一致
ret=re.search('<(?P<tag>\w+)>(?P<cont>.*?)(</(?P=tag)>)',s1)
ret=re.search('<(?P<tag>\w+)>(?P<cont>.*?)</\1>',s1)#\1为取第一个分组
```

##### 3.4findall与分组

```
s1='1.2312+2.123+3'
ret=re.findall('\d+(\.\d+)?',s1)
print(ret)#['.2312','.123',' ']
#findall遇到正则表达式中的分组，会优先显示分组中的内容
#取消分组优先显示 ?:
ret=re.findall('\d+(?:\.\d+)?',s1)
```

##### 3.5split与分组

```
#split遇到正则表达式中分组，会保留分组中本应该被删除的内容
```



应用方法：

1.当想匹配的内容包含了不想匹配的内容中，这个时候只需要把不想匹配的先匹配出来，在通过手段去除