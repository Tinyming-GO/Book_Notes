# 基础

## 注释

`print('hello	world')	# 注意到 print 是一个函数`

## 字面常量
## 数字
## 字符串
- 单引号
- 双引号
- 三引号：你可以通过使用三个引号—— """ 或 ''' 来指定多行字符串。

```python
'''这是一段多行字符串。这是它的第一行。
This is	the	second line.
"What's	your name?," I asked.
He said "Bond, James Bond."
'''
```
## 字符串是不可变的
## 格式化方法

构建字符串，使用`format()`方法。

```python
age  = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this	book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
```

输出:

```
Swaroop was 20 years old when he wrote this book
Why is Swaroop playing with that python?
```

注意数字只是一个可选选项:

```python
age  = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this	book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
```

`format()` 方法 更详细的格式,例如:

```python
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本,并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

输出:

```
0.333
___hello___
Swaroop wrote A Byte of Python
```

※ print 总是会以一个不可见的“新一行”字符( \n )。为防止打印过程中出现这一换行符,你可以通过 end 指定其应以空白结尾:

```python
print('a', end='')
print('b', end='')
```

输出:

```
ab
```

## 转义序列
## 原始字符串

在字符串前增加`r`或`R`来指定一个 原始(Raw) 字符串：

```python
r"Newlines are indicated by \n"  # \n 将不会被转义
```

## 变量
## 标识符命名

变量是标识符的一个例子。标识符(Identifiers)	是为	某些东西	提供的给定名称。

- 第一个字符必须是字母表中的字母或下划线( _ )。
- 标识符的其它部分可以由字符下划线( _ )、数字(0~9)组成。
- 标识符名称区分大小写。例如, myname 和 myName 并不等同。

## 数据类型
## 对象

需要记住的是 , Python 将程序中的任何内容统称为`对象(Object)`。

## 案例:使用变量与字面常量

```python
# 文件名:var.py
i = 5
print(i)
i = i + 1
print(i)
s = '''This is a multi-line string.
This is the second line.'''
print(s)
```

输出:

```
5
6
This is a multi-line string.
This is the second line.
```

## 逻辑行与物理行

尽量保证 一 物理行 对应一个 逻辑行（不使用分号；）。

如果你有一行非常长的代码,你可以通过使用反斜杠将其拆分成多个物理行。这被称作`显式行连接`

```python
s = 'This is a string. \
This continues the string.'
print(s)
```

输出：

```
This is a string. This continues the string.
```

## 缩进

每一组这样的语句被称为 `块(block)`。Python 将始终对块使用缩进,并且绝不会使用大括号。

# 运算符与表达式

表达式可以拆分成`运算符(Operators)`与`操作数(Operands)`。

## 运算符

- \+ (加)
- \- (减)
- \* (乘)
- \*\* (乘方) eg： 3 \*\* 4 输出 81 (即 3 \* 3 \* 3 * 3 )。
- / (除)
- // (整除) eg： 13 // 3 输出 4 。
- % (取模)
- << (左移)
- - 将数字的位向左移动指定的位数。(每个数字在内存中以二进制数表示,即 0 和 1 )
- - 2 << 2 输出 8 。 2 用二进制数表示为 10 。
- - 向左移 2 位会得到 1000 这一结果,表示十进制中的 8 。
- \>> (右移)
- & (按位与)
- - 5 & 3 输出 1 。
- | (按位或)
- - 5 | 3 输出 7 。
- ^	(按位异或)
- - 5 ^ 3 输出 6 。
- ~ (按位取反)
- - x 的按位取反结果为 -(x+1)。
- - ~5 输出 -6 。
- < (小于) 比较可以任意组成组成链接: 3 < 5 < 7 返回 True 。（所有的比较运算符返回的结果均为 True 或 False ）
- \> (大于)
- <= (小于等于)
- \>= (大于等于)
- == (等于)
- != (不等于)
- not (布尔“非”)
- and (布尔“与”)  作短路计算
- or (布尔“或”)

## 数值运算与赋值的快捷方式

`a = a * 3	<==>  a *= 3`

## 求值顺序 运算符的优先级

## 改变运算顺序  使用括号

## 结合性  同优先级的运算符从左至右依次求值

## 表达式

```python
length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))
```

输出:

```
Area is 10
Perimeter is 14
```

# 控制流

## 	if 语句

```python
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新块在这里结束
elif guess < number:
    # 另一代码块
    print('No,	it	is	a	little	higher	than	that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No,	it	is	a	little	lower	than	that')
    # 你必须通过猜测一个大于(>)设置数的数字来到达这里。
print('Done')
# 这最后一句语句将在
# if 语句执行完毕后执行。
```

输出:

```
Enter an integer : 50
No, it is a little lower than that
Done
```

一个最小规模且有效的 `if 语句` 是这样的:

```python
if True: # 注意：True首字母一定是大写！
 	print('Yes, it is true')
```

## while 语句

`while 语句`同样可以拥有`else 子句`作为可选选项！！！！

```python
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations,	you	guessed	it.')
        # 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No,	it	is	a	little	higher	than	that.')
    else:
        print('No,	it	is	a	little	lower	than	that.')
else:
    print('The	while	loop	is	over.')  # 跳出循环时，就一定会执行这句
# 在这里你可以做你想做的任何事
print('Done')
```

输出:

```
$ python while.py
Enter an integer	:	50
No,	it	is	a	little	lower	than	that.
Enter an integer	:	22
No,	it	is	a	little	higher	than	that.
Enter an integer	:	23
Congratulations,	you	guessed	it.
The	while loop is over.
Done
```

## 	for 循环

```python
for i in range(1, 5): # range(1,5) 将输出序列 [1, 2, 3, 4] 。 range(1,5,2) 将会输出 [1, 3] 。
    print(i)
else:
    print('The for loop is over')
```

输出:

```
$ python for.py
1
2
3
4
The for loop is over
```

另外需要注意的是,`range()`每次只会生成一个数字,如果你希望获得完整的数字列表,要在使用`range()`时调用`list()`。例如下面这样: `list(range(5))`,它将会返回 [0, 1, 2, 3, 4] 。

```python
print(range(1, 5)) # python2 输出：range(1, 5)
print(range(1, 5)) # python3 输出：[1, 2, 3, 4]
print(list(range(1, 5))) # python2 python3 都输出：[1, 2, 3, 4]
```

## 	break 语句

## 	continue 语句

# 函数

函数可以通过关键字`def`来定义。

```python
def say_hello():
    # 该块属于这一函数
    print('hello world')
# 函数结束

say_hello()  # 调用函数
say_hello()  # 再次调用函数
```

输出:

```
$ python function1.py
hello world
hello world
```

## 函数参数

要注意在此使用的术语——在定义函数时给定的名称称作`“形参”(Parameters)`,在调用函数时你所提供给函数的值称作`“实参”(Arguments)`。

```python
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# 直接传递字面值
print_max(3, 4)
x = 5
y = 7
# 以参数的形式传递变量
print_max(x, y)
```

输出:

```
$ python function_param.py
4 is maximum
7 is maximum
```

## 局部变量

所有变量的`作用域`是它们被定义的`块`

## global 语句

你可以在同一句 global 语句中指定不止一个的全局变量,例如`global	x, y, z`。

## 默认参数值

要注意到,默认参数值应该是`常数`！！！更确切地说,默认参数值应该是`不可变的`！！！

```python
def say(message, times=1):
    print(message * times)
```

>※ 只有那些位于参数列表末尾的参数才能被赋予默认参数值,意即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前。
>
>这是因为值是按参数所处的位置依次分配的。举例来说,`def func(a, b=5)`是有效的,但 def func(a=5, b) 是无效的。

## 关键字参数

我们使用命名(关键字)而非位置(一直以来我们所使用的方式)来指定函数中的参数。

这样做有两大优点——其一,我们不再需要考虑参数的顺序,函数的使用将更加容易。其二,我们可以只对那些我们希望赋予的参数以赋值,只要其它的参数都具有默认参数值。

```python
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)


func(3, 7)
func(25, c=24)  # 注意这顺序是乱的
func(c=50, a=100)  # 注意这顺序是乱的
```

输出:

```python
$ python function_keyword.py
a is 3 and b is 7 and c is 10
a is 25 and b is 5 and c is 24
a is 100 and b is 5 and c is 50
```

## 可变参数

想定义的函数里面能够有任意数量的变量,也就是参数数量是可变的

```python
def total(a=5, *numbers, **phonebook):

    print('a', a)

    # 遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项目
    for first_part, second_part in phonebook.items(): # .items() 一定要加！！
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))  # 函数没有显式的return，默认return None
```

输出:

```
$ python function_varargs.py
a 10
single_item 1
single_item 2
single_item 3
Inge 1560
John 2231
Jack 1123
None
```

## 	return 语句

如果 return 语句没有搭配任何一个值则代表着`返回 None`。每一个函数都在其末尾隐含了一句 return None ,除非你写了你自己的 return 语句。

```python
def some_function():
    pass
```

※ Python 中的 pass 语句用于指示一个没有内容的语句块。

## DocStrings

Python 有一个甚是优美的功能称作文档字符串(Documentation	Strings),在称呼它时通常会使用另一个短一些的名字docstrings。

```python
def print_max(x, y):
    '''打印两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能,将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
```

输出:

```
$ python function_docstring.py
5 is maximum
打印两个数值中的最大数。

 这两个数都应该是整数

```

这里要注意文档字符串也适用于后面相关章节将提到的`模块(Modules)`与`类(Class)` 。

强烈推荐你为你编写的所有重要的函数配以文档字符串。

# 模块

如何使用标准库模块：

```python
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
```

输出:

```
$ python module_using_sys.py we are arguments
The command line arguments are:
module_using_sys.py
we
are
arguments
The PYTHONPATH is ['/tmp/py',
# many entries here, not shown here
'/Library/Python/2.7/site-packages',
'/usr/local/lib/python2.7/site-packages']
```

当 Python 运行 import sys 这一语句时,它会开始寻找 sys 模块。在这一案例中,由于其是一个内置模块,因此 Python 知道应该在哪里找到它。如果它不是一个已编译好的模块,即用 Python 编写的模块,那么 Python 解释器将从它的`sys.path`变量所提供的目录中进行搜索。

※ sys.path 内包含了导入模块的字典名称列表！！

另外要注意的是当前目录指的是程序启动的目录。你可以通过运行`import os; print(os.getcwd())`来查看你的程序目前所处在的目录。

## 按字节码编译的 .pyc 文件

注意:这些 .pyc 文件通常会创建在与对应的 .py 文件所处的目录中。如果 Python 没有相应的权限对这一目录进行写入文件的操作,那么 .pyc 文件将不会被创建。

## from..import 语句

如果你希望直接将`argv`变量导入你的程序(为了避免每次都要输入`sys.`),那么你可以通过使用`from sys import argv`语句来实现这一点。

- 警告:一般来说,你应该尽量避免使用 from...import 语句,而去使用 import 语句。这是为了避免在你的程序中出现名称冲突,同时也为了使程序更加易读。

案例:

```python
from math import sqrt

print("Square	root	of	16	is", sqrt(16))
```

## 模块的 __name__

```python
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
```

输出:

```
$ python module_using_name.py
This program is being run by itself

$ python
>>> import module_using_name
I am being imported from another module
>>>
```

每一个 Python 模块都定义了它的`__name__`属性。如果它与`__main__`属性相同则代表这一模块是由用户独立运行的,因此我们便可以采取适当的行动。

## 编写你自己的模块

你还可以使用:

```python
from mymodule import * # 这将导入诸如 say_hi 等所有公共名称,但不会导入 __version__ 名称,因为后者以双下划线开头。
```

## dir 函数

内置的`dir()`函数能够返回由对象所定义的名称列表。 如果这一对象是一个模块,则该列表会包括函数内所定义的函数、类与变量。

该函数接受参数。 如果参数是模块名称,函数将返回这一指定模块的名称列表。 如果没有提供参数,函数将返回当前模块的名称列表。

```python
$ python
>>> import sys
# 给出 sys 模块中的属性名称
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# 此处只展示部分条目
# 给出当前模块的属性名称
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__','sys']
# 创建一个新的变量 'a'
>>> a = 5
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
# 删除或移除一个名称
>>> del a
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```

## 包

现在,你必须开始遵守用以组织你的程序的层次结构。变量通常位于函数内部,函数与全局变量通常位于模块内部。如果你希望组织起这些模块的话,应该怎么办?这便是包(Packages)应当登场的时刻。

包是指一个包含模块与一个特殊的`__init__.py`文件的文件夹,后者向 Python 表明这一文件夹是特别的,因为其包含了 Python	模块。

让我们这样设想: 你想创建一个名为“world”的包,其中还包含着 “asia”、“africa” 等其它子包,同时这些子包都包含了诸如“india”、“madagascar”等模块。

下面是你会构建出的文件夹的结构:

```
- <some folder present in the sys.path>/
  - world/
    - __init__.py
    - asia/
      - __init__.py
      - india/
        - __init__.py
        - foo.py
      - africa/
        - __init__.py
        - madagascar/
          - __init__.py
          - bar.py
```

包是一种能够方便地分层组织模块的方式。你将在 标准库 中看到许多有关于此的实例。

# 数据结构

Python	中有四种内置的数据结构——`列表(List)`、`元组(Tuple)`、`字典(Dictionary)`和`集合(Set)`。

## 列表

列表是一种可变的(Mutable)数据类型

```python
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana'] # 你可以向列表中添加任何类型的对象,包括数字,甚至是其它列表。
print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist: # 使用 for...in 循环来遍历列表中的每一个项目。
    print(item, end=' ') # 使用 end 参数,这样就能通过一个空格来结束输出工作,而不是通常的换行。

print('\nI also have to buy rice.')
shoplist.append('rice') # 通过列表对象中的 append 方法向列表中添加一个对象。
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()  # 列表的 sort 方法对列表进行排序。这里要着重理解到这一方法影响到的是列表本身,而不会返回一个修改过的列表——这与修改字符串的方式并不相同。同时,这也是我们所说的,列表是可变的(Mutable)而字符串是不可变的(Immutable)。
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
```

输出:

```
$ python ds_using_list.py
I have 4 items to purchase.
These items are: apple mango carrot banana
I also have to buy rice.
My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
I will sort my list now
Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
The first item I will buy is apple
I bought the apple
My shopping list is now ['banana', 'carrot', 'mango', 'rice']
```

## 有关对象与类的快速介绍

列表是使用对象与类的实例。当我们启用一个变量`i`并将整数 5 赋值给它时,你可以认为这是在创建一个`int`类(即类型)之下的对象(即实例)`i`。

## 元组

元组的一大特征类似于字符串,它们是不可变的,也就是说,你不能编辑或更改元组。

```python
#	我会推荐你总是使用括号
#	来指明元组的开始与结束
#	尽管括号是一个可选选项。
#	明了胜过晦涩,显式优于隐式。
zoo = ('python', 'elephant', 'penguin')  # 这是一个元组
print('Number	of	animals	in	the	zoo	is', len(zoo)) # `len`函数用来获取元组的长度。

new_zoo = 'monkey', 'camel', zoo
print('Number	of	cages	in	the	new	zoo	is', len(new_zoo))
print('All	animals	in	new	zoo	are', new_zoo)
print('Animals	brought	from	old	zoo	are', new_zoo[2]) # 使用方括号的形式被称作索引(Indexing)运算符
print('Last	animal	brought	from	old	zoo	is', new_zoo[2][2]) # new_zoo 元组中的第三个项目中的第三个项目
print('Number	of	animals	in	the	new	zoo	is',
      len(new_zoo) - 1 + len(new_zoo[2]))
```

输出:

```
$ python ds_using_tuple.py
Number of animals in the zoo is 3
Number of cages in the new zoo is 3
All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))
Animals brought from old zoo are ('python', 'elephant', 'penguin')
Last animal brought from old zoo is penguin
Number of animals in the new zoo is 5
```

- 包含 0 或 1 个项目的元组
- - 一个空的元组由一对圆括号构成,就像`myempty = ()`这样。然而,一个只拥有一个项目的元组并不像这样简单。你必须在第一个(也是唯一一个)项目的后面加上一个逗号来指定它,如此一来 Python 才可以识别出在这个表达式想表达的究竟是一个元组还是只是一个被括号所环绕的对象,也就是说,如果你想指定一个包含项目 2 的元组,你必须指定`singleton = (2, )`。

## 字典

通过使用符号构成`d = {key : value1 , key2 : value2}`这样的形式,来成对地指定键值与值。

```python
# “ab”是地址(Address)簿(Book)的缩写

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值—值配对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items(): # 字典的items()方法将返回一份包含元组的列表，每一元组中则包含了每一对相应的信息——键值以及其相应的值。
    print('Contact {} at {}'.format(name, address))

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab: # 使用`in`运算符来检查某对键值—值配对是否存在。
    print("\nGuido's address is", ab['Guido'])
```

输出:

```
$ python ds_using_dict.py
Swaroop's address is swaroop@swaroopch.com
There are 3 contacts in the address-book
Contact Swaroop at swaroop@swaroopch.com
Contact Matsumoto at matz@ruby-lang.org
Contact Larry at larry@wall.org
Guido's address is guido@python.org
```

要想了解有关`dict`类的更多方法,请参阅`help(dict)`。

## 序列

列表、元组和字符串可以看作序列(Sequence)的某种表现形式。序列的主要功能是资格测试(Membership Test)(也就是 in 与 not	in 表达式)和索引操作(Indexing Operations),它们能够允许我们直接获取序列中的特定项目。

上面所提到的序列的三种形态——列表、元组与字符串,同样拥有一种切片(Slicing)运算符,它能够允许我们序列中的某段切片——也就是序列之中的一部分。
```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation	#
# 索引或“下标(Subscription)”操作符	#
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])  # 负数从后面开始
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:]) # 切片操作！数字可选，冒号是必填的！中括号！包含开始，不包含结尾！
# 从某一字符串中切片	#
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
# 修改切片的步长（step）
print('Item is', shoplist[1:3:2])
```

输出:

```bash
$ python ds_seq.py
Item 0 is apple
Item 1 is mango
Item 2 is carrot
Item 3 is banana
Item -1 is banana
Item -2 is carrot
Character 0 is s
Item 1 to 3 is ['mango', 'carrot']
Item 2 to end is ['carrot', 'banana']
Item 1 to -1 is ['mango', 'carrot']
Item start to end is ['apple', 'mango', 'carrot', 'banana']
characters 1 to 3 is wa
characters 2 to end is aroop
characters 1 to -1 is waroo
characters start to end is swaroop
Item is ['mango']
```

序列的一大优点在于你可以使用同样的方式访问元组、列表与字符串。

## 集合

```bash
>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True
>>> 'usa' in bri
False
>>> bric = bri.copy()
>>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}
```

## 引用

```python
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist
# 我购买了第一项项目,所以我将其从列表中删除
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到	shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表,以此我们确认
# 它们指向的是同一个对象
print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在两份列表已出现不同
```

输出:

```
$ python ds_reference.py
Simple Assignment
shoplist is ['mango', 'carrot', 'banana']
mylist is ['mango', 'carrot', 'banana']
Copy by	making a full slice
shoplist is ['mango', 'carrot', 'banana']
mylist is ['carrot', 'banana']
```

你要记住如果你希望创建一份诸如序列等复杂对象的副本(而非整数这种简单的对象(Object)),你必须使用切片操作来制作副本。如果你仅仅是将一个变量名赋予给另一个名称,那么它们都将“查阅”同一个对象,如果你对此不够小心,那么它将造成麻烦。

## 有关字符串的更多内容

你在程序中使用的所有字符串都是`str 类`下的对象。你可以查阅`help(str)`。

```python
# 这是一个字符串对象
name = 'Swaroop'
if name.startswith('Swa'):  # startswith 方法用于查找字符串是否以给定的字符串内容开头。
    print('Yes, the string starts with "Swa"')
if 'a' in name:   # in 运算符用以检查给定的字符串是否是查询的字符串中的一部分。
    print('Yes, it contains the string "a"')
if name.find('war') != -1: # find 方法用于定位字符串中给定的子字符串的位置。
    print('Yes it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
```

输出:

```
$ python ds_str_methods.py
Yes, the string starts with "Swa"
Yes, it contains the string "a"
Yes, it contains the string "war"
Brazil_*_Russia_*_India_*_China
```

# 解决问题

## 文件备份=>backup_ver1.py

## 软件开发流程

# 面向对象编程

对象可以使用属于它的普通变量来存储数据。这种从属于对象或类的变量叫作`字段(Field)`。对象还可以使用属于类的函数来实现某些功能,这种函数叫作`类的方法(Method)`。这两个术语很重要,它有助于我们区分`函数与变量`,哪些是独立的,哪些又是属于类或对象的。总之,`字段与方法通称类的属性(Attribute)`。

字段有两种类型——它们属于某一类的各个实例或对象,或是从属于某一类本身。它们被分别称作`实例变量(Instance Variables)`与`类变量(Class Variables)`。

通过`class`关键字可以创建一个类。

## 	self

假设你有一个 MyClass 的类,这个类下有一个实例 myobject 。当你调用一个这个对象的方法,如 myobject.method(arg1,	arg2)		时,Python 将会自动将其转换成 MyClass.method(myobject,	arg1, arg2) ——这就是 self 的全部特殊之处所在。

这同时意味着,如果你有一个没有参数的方法,你依旧必须拥有一个参数——`self`。

## 类

最简单的类(Class):

```python
class Person:
    pass  # 一个空的代码块

p = Person()
print(p)
```

## 方法

```python
class Person:
    def say_hi(self): # 要注意到 say_hi 这一方法不需要参数,但是依旧在函数定义中拥有 self 变量。
        print('Hello, how are you?')

p = Person()
p.say_hi()
#	前面两行同样可以写作
#	Person().say_hi()
```

输出:

```
$ python oop_method.py
Hello, how are you?
```

## `__init__` 方法

`__init__ 方法`会在类的对象被实例化(Instantiated)时立即运行。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# 前面两行同时也能写作
# Person('Swaroop').say_hi()
```

输出:

```
$ python oop_init.py
Hello, my name is Swaroop
```

## 类变量与对象变量

```python
#coding=UTF-8
class Robot:
    """表示有一个带有名字的机器人。"""

    #一个类变量,用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name   # 这个变量属于对象！！ 注意跟PHP的区别
        print("(Initializing {})".format(self.name))
        # 当有人被创建时,机器人
        # 将会增加人口数量
        Robot.population += 1  # 这个变量属于类！！ 最好使用self.__class__.population。

    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
        没问题,你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod  # 将下面的方法how_many定义为类方法！所有对象共享该方法！
    def how_many(cls):  # 定义一个属于类的方法！！未加前缀__的类方法都是公开的
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()
```

输出:

```
$ python oop_objvar.py
(Initializing R2-D2)
Greetings, my masters call me R2-D2.
We have 1 robots.
(Initializing C-3PO)
Greetings, my masters call me C-3PO.
We have 2 robots.
Robots can do some work here.
Robots have finished their work. So let's destroy them.
R2-D2 is being destroyed!
There are still 1 robots working.
C-3PO is being destroyed!
C-3PO was the last one.
We have 0 robots.
```

- 我们通过 `Robot.population` 而非 self.population 引用 population `类变量`。对于类变量，还可以使用`self.__class__.population`
- 我们对于 name `对象变量`采用 `self.name` 标记法加以称呼。
- 注意当一个对象变量与一个类变量名称相同时,类变量将会被隐藏。
- 我们使用装饰器(Decorator)将 how_many 方法标记为类方法。你可以将装饰器想象为调用一个包装器(Wrapper)函数的快捷方式,因此启用 @classmethod 装饰器等价于调用: `how_many	= classmethod(how_many)`
- 我们可以在运行时通过 `Robot.__doc__` 访问类的 文档字符串,对于方法的文档字符串,则可以使用 `Robot.say_hi.__doc__` 。
- 所有的类成员都是公开的。但有一个例外:如果你使用数据成员并在其名字中使用双下划线作为前缀,形成诸如 `__privatevar` 这样的形式,Python 会使用名称调整(Name-mangling)来使其有效地成为一个私有变量。
- 任何在类或对象之中使用的变量其命名应以下划线开头,其它所有非此格式的名称都将是公开的,并可以为其它任何类或对象所使用。请记得这只是一个约定,Python	并不强制如此(除了双下划线前缀这点)。

## 继承

```Python
# coding=UTF-8
class SchoolMember:
    '''代表任何学校里的成员。'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):  # 这个方法被子类覆盖了，所以没有被调用
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):  # SchoolMember 被称为 基类/超类 ， Teacher 被称为 子类/派生类
    '''代表一位老师。'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # 显式地调用基类的同名方法
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
    '''代表一位学生。'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# 打印一行空白行
print()
members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()
```

输出:

```
$ python oop_subclass.py
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)
Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75"
```

这里有一条有关术语的注释——如果继承元组(Inheritance Tuple)中有超过一个类,这种情况就会被称作多重继承(Multiple Inheritance)。

# 输入与输出

## 用户输入内容

```python
def reverse(text):
    return text[::-1]  # 使用切片功能翻转文本

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
```

输出:

```
$ python3 io_input.py
Enter text: sir
No, it is not a palindrome
$ python3 io_input.py
Enter text: madam
Yes, it is a palindrome
$ python3 io_input.py
Enter text: racecar
Yes, it is a palindrome
```

## 文件

```python
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
 use Python!
'''
# 打开文件以编辑('w'riting)
f = open('poem.txt', 'w') # 常用的打开模式是阅读模式( 'r' ),写入模式( 'w' )和追加模式( 'a' )。更多模式查看 help(open)
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()
# 如果没有特别指定,
# 将假定启用默认的阅读('r'ead)模式
f = open('poem.txt')  # 默认即是阅读模式，不需要指定
while True:
    line = f.readline()  # 读取一行，同时结尾还包含了换行符！
    # 零长度指示 EOF
    if len(line) == 0:  # 空字符串返回时，表示到达了文件末尾
        break
    # 每行(`line`)的末尾
    # 都已经有了换行符
    # 因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close() # ※
```

输出:

```
$ python3 io_using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
 use Python!
```

## Pickle

Python 提供了一个叫作 的标准模块,通过它你可以将任何纯 Python 对象存储到一个文件中,并在稍后将其取回。这叫作`持久地(Persistently)存储对象`。

```python
import pickle

# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']
# 准备写入文件
f = open(shoplistfile, 'wb') # 写入、二进制模式
# 转储对象至文件
pickle.dump(shoplist, f)  # 这过程称为封装
f.close()
# 清除 shoplist 变量
del shoplist
# 重新打开存储文件
f = open(shoplistfile, 'rb')
# 从文件中载入对象
storedlist = pickle.load(f)  # 这过程称为拆封
print(storedlist)
```

输出:

```
$ python io_pickle.py
['apple', 'mango', 'carrot']
```

## Unicode

> 注意:如果你正在使用 Python 2,我们又希望能够读写其它非英语语言,我们需要使用`unicode`类型,它全都以字母`u`开头,例如`u"hello	world"`	。

```python
# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")  # 指定编码为utf-8
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)
```

# 异常

## 错误
## 异常
## 处理异常

我们可以通过使用`try..except`来处理异常状况。

```python
try:
    text = input('Enter something --> ')
except EOFError:  # 至少一个except字句
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:  # else 子句将在没有发生异常的时候执行。
    print('You entered {}'.format(text))
```

输出:

```
# Press ctrl + d
$ python exceptions_handle.py
Enter something --> Why did you do an EOF on me?
# Press ctrl + c
$ python exceptions_handle.py
Enter something --> ^CYou cancelled the operation.
$ python exceptions_handle.py
Enter something --> No exceptions
You entered No exceptions
```

## 抛出异常

你可以通过`raise`语句来引发一次异常。引发的错误或异常必须是直接或间接从属于`Exception`(异常) 类的派生类。

```python
# encoding=UTF-8

class ShortInputException(Exception): # 必须继承Exception基类
    '''一个由用户定义的异常类'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3) # 抛出文本长度小于最小长度限制的异常
# 其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex: #  ex 是 ShortInputException 的别名!
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))  # 调用异常类对象的字段
else:
    print('No exception was raised.')  # 无异常抛出进入else

```

输出:

```
$ python exceptions_raise.py
Enter something --> a
ShortInputException: The input was 1 long, expected at least 3
$ python exceptions_raise.py
Enter something --> abc
No exception was raised.
```

## Try ... Finally

能确保读取文件时，无论是否发生异常，都可以正确关闭！

```python
import sys
import time

f = None
try:
    f = open("poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()  # 读取一行
        if len(line) == 0:  # 判断是否到达文件结尾
            break
        print(line, end='')
        sys.stdout.flush() # 使得上一个print能立即打印到屏幕
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        time.sleep(2)  # 休眠2秒
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:  # 无论是否有异常抛出 都会进入finally
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
```

输出:

```
$ python exceptions_finally.py
Programming is fun
Press ctrl+c now
^C!! You cancelled the reading from the file.
(Cleaning up: Closed the file)
```

## 	with 语句

在`try`块中获取资源,然后在`finally`块中释放资源是一种常见的模式。因此,还有一个`with`语句使得这一过程可以以一种干净的姿态得以完成。

```python
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
```

我们将关闭文件的操作交由`with open`来自动完成。它总会在代码块开始之前调用`thefile.__enter__`函数,并且总会在代码块执行完毕之后调用`thefile.__exit__`。因此,我们在`finally`代码块中编写的代码应该格外留心`__exit__`方法的自动操作。这能够帮助我们避免重复显式使用`try..finally`语句。

# 标准库

## sys 模块

`sys 模块`包括了一些针对特定系统的功能。

## 日志模块

```python
import os  # os 模块用以和操作系统交互
import platform # platform 模块用以获取平台——操作系统——的信息
import logging # logging 模块用来记录(Log)信息。

# 通过检查platform.platform()，来确定使用的操作系统
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),  # 主驱动盘
                                os.getenv('HOMEPATH'),  # 主文件夹
                                'test.log')  # 用于存储信息的文件名
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')
print("Logging to", logging_file) # 打印日志即将保存的位置路径
#以特定格式记录日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug("Start of the program")  # 调试信息
logging.info("Doing something")  # 提醒信息
logging.warning("Dying now")  # 警告信息，还有很多
```

输出:

```python
$ python stdlib_logging.py
Logging to /Users/swa/test.log
$ cat /Users/swa/test.log
2014-03-29 09:27:36,660 : DEBUG : Start of the program
2014-03-29 09:27:36,660 : INFO : Doing something
2014-03-29 09:27:36,660 : WARNING : Dying now
```

## 每周模块系列

进一步探索标准库的最好方法是阅读由 Doug Hellmann 撰写的优秀的`Python Module of the Week`系列(你还可以阅读它的实体书或是阅读 Python 官方文档)。

# 更多

## 传递元组

从一个函数中返回两个不同的值：

```bash
>>> def get_error_details():
...     return (2, 'details')
...
>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'details'
```

要注意到`a,	b = <some expression>`的用法会将表达式的结果解释为具有两个值的一个元组。

这也意味着在 Python 中交换两个变量的最快方法是:

```bash
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
```

## 特殊方法

诸如`__init__`和`__del__`等一些方法对于类来说有特殊意义。

下面的表格列出了一些有用的特殊方法。如果你想了解所有的特殊方法,请参阅手册。

- `_init__(self, ...)` 这一方法在新创建的对象被返回准备使用时被调用。
- `__del__(self)` 这一方法在对象被删除之前调用(它的使用时机不可预测,所以避免使用它)
- `__str__(self)` 当我们使用 print 函数时,或 str() 被使用时就会被调用。
- `__lt__(self,	other)` 当小于运算符(<)被使用时被调用。类似地,使用其它所有运算符(+、> 等等)时都会有特殊方法被调用。
- `__getitem__(self, key)`  使用 x[key] 索引操作时会被调用。
- `__len__(self)` 当针对序列对象使用内置 len() 函数时会被调用


## 单语句块

如果你的语句块只包括单独的一句语句,那么你可以在同一行指定它,而不使用缩进

```bash
>>> flag = True
>>> if flag: print('Yes')
...
Yes
```

## Lambda 表格

`lambda 语句`可以创建一个新的函数对象。从本质上说,lambda 需要一个参数,后跟一个表达式作为函数体,这一表达式执行的值将作为这个新函数的返回值。

```python
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y']) #lambda后面第一个i是传入函数体的形参，：后面的是函数体； 本例中 i 是list中的一个字典
print(points)
```

输出:

```
$ python more_lambda.py
[{'y': 1, 'x': 4}, {'y': 3, 'x': 2}]
```

要注意到一个 list 的 sort 方法可以获得一个 key 参数,用以决定列表的排序方式(通常我们只知道升序与降序)。在我们的案例中,我们希望进行一次自定义排序,为此我们需要编写一个函数,但是又不是为函数编写一个独立的 def 块,只在这一个地方使用,因此我们使用	Lambda	表达式来创建一个新函数。

## 列表推导

列表推导(List Comprehension)用于从一份现有的列表中得到一份新列表。想象一下,现在你已经有了一份数字列表,你想得到一个相应的列表,其中的数字在大于 2 的情况下将乘以2。列表推导就是这类情况的理想选择。

```python
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2] # 并不会改变listone
print(listtwo)
```

输出:

```
$ python more_list_comprehension.py
[6, 8]
```

在本案例中,当满足了某些条件时( if	i >	2 ),我们进行指定的操作( 2*i ),以此来获得一份新的列表。要注意到原始列表依旧保持不变。使用列表推导的优点在于,当我们使用循环来处理列表中的每个元素并将其存储到新的列表中时时,它能减少样板(Boilerplate)代码的数量。

## 在函数中接收元组与字典

有一种特殊方法,即分别使用`*`或`**`作为元组或字典的前缀,来使它们作为一个参数为函数所接收。当函数需要一个可变数量的实参时,这将颇为有用。

```bash
>>> def powersum(power, *args):
... '''Return the sum of each argument raised to the specified power.'''
... total = 0
... for i in args:
... total += pow(i, power)
... return total
...
>>> powersum(2, 3, 4)
25
>>> powersum(2, 10)
100
```

因为我们在`args`变量前添加了一个`*`前缀,函数的所有其它的额外参数都将传递到`args`中,并作为一个元组予以储存。如果采用的是`**`前缀,则额外的参数将被视为字典的键值—值配对。

## assert 语句

`assert 语句`用以断言(Assert)某事是真的。例如说你非常确定你正在使用的列表中至少包含一个元素,并想确认这一点,如果其不是真的,就抛出一个错误, assert 语句就是这种情况下的理想选择。当语句断言失败时,将会抛出`AssertionError`。

```bash
>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
AssertionError
```

你应该明智地选用`assert 语句`。在大多数情况下,它好过捕获异常,也好过定位问题或向用户显示错误信息然后退出。

## 装饰器

装饰器(Decorators)是应用包装函数的快捷方式。这有助于将某一功能与一些代码一遍又一遍地“包装”。举个例子,我为自己创建了一个 retry 装饰器,这样我可以将其运用到任何函数之中,如果在一次运行中抛出了任何错误,它就会尝试重新运行,直到最大次数 5 次,并且每次运行期间都会有一定的延迟。这对于你在对一台远程计算机进行网络调用的情况十分有用:

```python
from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log = logging.getLogger("retry")


def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt	%s/%s	failed	:	%s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical("All	%s	attempts	failed	:	%s",
                     MAX_ATTEMPTS,
                     (args, kwargs))

    return wrapped_f


counter = 0


@retry  # 装饰器的语法糖 类似于 save_to_database = retry(save_to_database)
def save_to_database(arg):
    print("Write	to	a	database	or	make	a	network	call	or	etc.")
    print("This	will	be	automatically	retried	if	exception	is	thrown.")
    global counter
    counter += 1
    #	这将在第一次调用时抛出异常
    #	在第二次运行时将正常工作(也就是重试)
    if counter < 2:
        raise ValueError(arg)


if __name__ == '__main__':
    save_to_database("Some	bad	value")
```

输出:

```
$	python	more_decorator.py
Write	to	a	database	or	make	a	network	call	or	etc.
This	will	be	automatically	retried	if	exception	is	thrown.
ERROR:retry:Attempt	1/5	failed	:	(('Some	bad	value',),	{})
Traceback	(most	recent	call	last):
		File	"more_decorator.py",	line	14,	in	wrapped_f
				return	f(*args,	**kwargs)
		File	"more_decorator.py",	line	39,	in	save_to_database
				raise	ValueError(arg)
ValueError:	Some	bad	value
Write	to	a	database	or	make	a	network	call	or	etc.
This	will	be	automatically	retried	if	exception	is	thrown.
```

它是如何工作的

请参阅:

https://foofish.net/python-decorator.html

http://toumorokoshi.github.io/dry-principles-through-python-decorators.html


# 如何翻译本书

本书的完整源代码可在	https://github.com/swaroopch/byte-of-python	获得。





