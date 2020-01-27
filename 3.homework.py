#-*-coding:utf-8-*-
# Author:Lu Wei
import re,sys,os
#1.匹配一篇英文文章的标题 类似 The Voice Of China
# ret=re.findall('[a-zA-Z\s]+','The Voice Of China',flags=re.S)
# print(ret)

#2.匹配一个网址
# 类似 https://www.baidu.com http://www.cnblogs.com
# ret=re.findall(r'http[s]?://www.\w+.com','http://www.cnblogs.com')
# print(ret)

#3.匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06
# ret=re.findall(r'\d{4}[-/.]\d[0-2][-/.][0-3]\d','2018.12.06')
# print(ret)

#4.匹配15位或者18位身份证号
# ret=re.findall(r'\d{15}(?:\d{3}|\d{2}x)?','33018419941010501x')
# print(ret)

#5.从lianjia.html中匹配出标题，户型和面积，结果如下：
#[('金台路交通部部委楼南北大三居带客厅 单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]


# 6、1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
# ret=re.findall(r'((?:[-+*/]?\d+)+)','1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))')
# # ret=re.findall(r'([-+/*]?/d)','(20-20)')
# print(ret)

#7.从类似9-25/3+7/399/42998+10568/14的表达式中匹配出乘法或除法
# ret=re.findall('\d+(?:[/*]\d+)+','9-25/3+7/399/42998+10568/14')
# print(ret)
# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '老男孩': {},
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }
#
# lst=[menu]
# while lst:
#     for key in lst[-1]:
#         print(key)
#     inp = input('inputsome:')
#     if inp.upper()=='Q':
#         break
#     if inp.upper()=='B':
#         lst.pop()
#         continue
#     dict = lst[-1].get(inp)
#     lst.append(dict)

path1=r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan'

size=0
l=[path1]
while l:
    path=l.pop()
    lst=os.listdir(path)
    for i in lst:
        file_path=os.path.join(path,i)
        if os.path.isdir(file_path):
            l.append(file_path)
            print(l)
        elif os.path.isfile(file_path):
            s=os.path.getsize(file_path)
            size+=s
print(size)






