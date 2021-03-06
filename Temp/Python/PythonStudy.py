#! /usr/bin/env python
#coding=utf-8

##################################################################################################
# Python 可进行系统调用的解释型脚本语言。通常用来作为“可执行的伪码”(pseudocode)，
#   可用C重写python扩展, 拥有一致的接口，从而提高特定部分的性能。
#   PyRex 工具允许C和Python混合编程。
#
# IDE比较(推荐 Eric 和 Ulipad、eclipse + pydev)
# Python有Windows扩展(PythonWin)，可创建Win32程序，其中包含WinAPI和COM扩展，可使用MFC做原型开发验证
# Web应用框架 -- Django 和 Turbogears
#
# 源码为 .py, 可显示地编译成字节码，扩展名为 .pyc 或 .pyo
# Python提倡简洁的代码设计，高效的数据结构和模块化的组件
# 内存管理由python解释器负责，通过引用计数进行内存管理，变量都是引用
#
#
#Python 中未指定返回值得函数全自动返回None，等价与NULL
#
#print 变量名 -- 显示变量值，等价于 xxx.str()
#变量名 -- 等价于 xxx.repr()
#
#print 可用格式字符串(%)进行字符串替换，print "%s is number %d" % ("one",1) => "one is number 1"
#print 默认每次输出后都会换行，在 输出语句最后加逗号(,)则会继续输出(好像会打印一个空格?)
#
#变量=raw_input(提示信息) -- 通过标准输入获取信息
#文档字符串(生成在线文档),在函数开始处用双引号括起的字符串，可在运行时访问
#运算符：//-地板除法?； / -- 传统除法？ ** -- 乘方运算符  <== from future import division
#不等于有两种方式 !=(推荐) 和 <> (淘汰), 判断是否等于用 ==
#逻辑运算符: and, or, not
#
#动态类型语言，变量的类型和值在赋值得那一刻被初始化
#基本数字类型： int, long(L,python的长整型只受限于内存大小 -- 可轻松表达很大的整数), bool, float, complex(复数, 如 6.2+5.1j)，Decimal(十进制浮点数类型，高精度，常用于处理金钱)
#字符串：可包含在成对的单引号或双引号之间，三个引号可用来包含特殊字符(如 xml/html等)，字符索引为 [0,len()-1] ，反向索引是 [-len, -1]
#  "+"号用于字符串连接，"*"号用于字符串重复， 如'-'*20 表示20个'-'字符
#
#tuple(元组) -- 只读列表， aTuple=(1,2,3,4)
#list(列表) -- 可保存任意数量任意数据类型的python对象，个数和元素值可变， aList=[1,2,3,4]，有 append,remove等方法
#dict(字典) -- 映射数据类型， aDict= { 'one':1 ; 'two':2 } ，有 keys，values 等方法
#  for key in aDict -- 类似shell脚本的foreach迭代，每次迭代其中的一个元素
#range(n) -- 可生成一个范围内的列表[0,n-1]，for i in range(len(str)): print str[i], '[%d] % i  <== 通过 len 和 range 遍历字符串
#新语法(可同时循环索引和元素) -- for i, ch in enumerate(str): ...
#if 表达式: 
#  语句
#else:
#  语句
#
#
#切片运算符[start:stop-1] 可得到子字符串
#
#代码块通过缩进对齐方式来表达代码逻辑，而不是使用括号或关键字
#
#
#文件 -- 打开open(文件名,"模式,r/w/a|+(读写)b(二进制)"; 关闭close; 
#fObj=open('/tmp/mylog.txt', 'r'); for eachline in fObj: print eachLine; fObj.close();
#
#异常 -- 通过 try-except 进行处理，通过 raise 抛出异常， finally ?：
#  try: 
#  except IOError, e:
#    print 'Some Error', e
#  else: 
#    xxx
#
#for xxx else (如for中无break时执行?)
#
#函数，使用小括号调用，如无return，会自动返回None对象 -- 通过引用调用，函数内对参数的改变会影响到原始对象，参数可有默认值
#  def 函数名([参数]:
#    """可选文档字符串"""
#    函数体
#  def myAdd(x,y):
#    """this is add"""
#    return x+y
#
#类 -- 在类定义中可声明静态变量(类定义中直接写的)，构造中可通过self设置成员变量()
#  class 类名(基类):
#    "文档字符串"
#    int 静态变量 <== 静态变量定义？
#    def 方法名(self,参数): 
#      self.xxxx <== 使用或设置成员变量
#    def __init__(self[,参数])  -- 类似构造函数，会自动调用进行初始化
#  创建类变量： obj=类名(参数)
#