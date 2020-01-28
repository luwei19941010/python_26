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

bracket=re.compile('\([^()]+\)')
div_mul=re.compile(r'\d+(\.\d+)?[*/]-?\d+(\.\d+)?')
add_del=re.compile(r'\d+(\.\d+)?[-+]-?\d+(\.\d+)?')
only=re.compile(r'(-?\d+(.\d+)?)')
def Div_mul(s):#(3+5-3*-0.2-3.3*2.2-8.5/2.4)
    exp=re.split('([/*])',div_mul.search(s).group())
    if exp[1]=='*':
        return s.replace(div_mul.search(s).group(),str(float(exp[0])*float(exp[2])))
    elif exp[1]=='/':
        return s.replace(div_mul.search(s).group(), str(float(exp[0]) / float(exp[2])))
def Add_del(s):
    # print(s)
    exp = re.split('([+-])', add_del.search(s).group())
    # print(exp)
    if exp[1] == '+':
        return s.replace(add_del.search(s).group(), str(float(exp[0]) + float(exp[2])))
    elif exp[1] == '-':
        return s.replace(add_del.search(s).group(), str(float(exp[0]) - float(exp[2])))
def Only(s):
    exp=re.split('[()]',s)
    return exp[1]

def calc():
    while True:
        s = input('Please input the expression(q for quit):')  # 例：'1+2- (3*  4-3/2+ (   3-2*(3+  5 -3*  -0.2-3.3*2.2 -8.5/ 2.4 )+10) +10)'
        # s='1+2- (3*  4-3/2+ (   3-2*(3+  5 -3*  -0.2-3.3*2.2 -8.5/ 2.4 )+10) +10)'
        #s='( -2.201666666666667)'
        if s.lower() == 'q':
            break
        else:
            s = ''.join(i for i in re.split('\s+', s))
        if not s.startswith('('):
            s=('(%s)'%s)
        # s=(1+2-(3*4-3/2+(3-2*(3+5-3*-0.2-3.3*2.2-8.5/2.4)+10)+10))
        while bracket.search(s):
            s=s.replace('--','+')
            s_search=bracket.search(s).group()#(3+5-3*-0.2-3.3*2.2-8.5/2.4)
            if div_mul.search(s_search):
                s=s.replace(s_search,Div_mul(s_search))
            elif add_del.search(s_search):
                s=s.replace(s_search,Add_del(s_search))
            elif only.search(s_search):
                s = s.replace(s_search, Only(s_search))
        print('The answer is: %.2f' % (float(s)))


if __name__=='__main__':
# print(Div_mul('(3+5-3*-0.2-3.3*2.2-8.5/2.4)'))
    calc()



