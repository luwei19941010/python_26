#-*-coding:utf-8-*-
# Author:Lu Wei
'''
9、大作业：计算器
1)如何匹配最内层括号内的表达式
2)如何匹配乘除法
3)考虑整数和小数
4)写函数，计算‘23’ ‘10/5’
5)引用4)中写好的函数，完成'23/4'计算
'''

# '1+2- (3*  4-3/2+ (   3-2*(3+  5 -3*  -0.2-3.3*2.2 -8.5/ 2.4 )+10) +10)'
import re
# s=''.join(i for i in re.split('\s+',s))
# print(re.search('\([^()]+\)',s))

bracket=re.compile('\([^()]+\)')
div_mul=re.compile(r'\d+(\.\d+)?[*/]-?\d+(\.\d+)?')
# a='(3-2*(3+5-3*-0.2-3.3*2.2-8.5/2.4)'
#
# print(div_mul.search(a))
def Div_mul(s):


def calc():
    while True:
        # s = input('Please input the expression(q for quit):')  # 例：'1+2- (3*  4-3/2+ (   3-2*(3+  5 -3*  -0.2-3.3*2.2 -8.5/ 2.4 )+10) +10)'
        s='1+2- (3*  4-3/2+ (   3-2*(3+  5 -3*  -0.2-3.3*2.2 -8.5/ 2.4 )+10) +10)'
        if s == 'q':
            break
        else:
            s = ''.join(i for i in re.split('\s+', s))
        if not s.startswith('('):
            s=('(%s)'%s)
        while bracket.search(s):
            s.replace('--','+')
            s_search=bracket.search(s).group()
            if div_mul.search(s_search):
                s_search=s




if __name__=='__main__':
    calc()



