## 1.1 省略结束标签的便利性
## 1.2 empty、isset、is_null的区别

- isset() 用来检测一个变量是否已声明且值不为NULL
- empty() 用来检测一个变量是否为空：空字符串，false，空数组[array()],NULL，0，''，以及被unset删除后的变量。
- is_null() 只针对已声明变量

## 1.3 布尔值的正确打开方式（TRUE/FALSE 建议大写，因为是常量）

## 1.4 变量作用域实践（函数体内访问外部变量 `global $globalName`）

## 1.5 多维数组排序

- 一维数组排序常用sort()、ksort()等
- 二维、多维数组排序，需要自定义排序函数:

`uasort()`函数接受两个参数，并且返回一个值表示那个参数应该排在前面。负数或者FALSE意味着第一个参数应该排在第二个参数之前。正数或者TRUE表示第二个参数应该排前面，如果值为0，则表示两个参数相等。

```php
<?php

//定义多维数组
$a = array(
    array('sky', 'blue'),
    array('apple', 'red'),
    array('tree', 'green'),
);
//自定义数组比较函数，按数组的第二个元素进行比较
function my_compare($a, $b) {
    if($a[1] < $b[1]) {
        return -1;
    } else if($a[1] == $b[1]) {
        return 0;
    } else {
        return 1;
    }
}

//排序
usort($a,'my_compare'); //PHP会把内层数组不断地发送给自定义函数
//输出结果
print_r($a);
```

## 1.6 超级全局数组

超级全局数组（super global array）是由PHP内置的，无须开发者重新定义。PHP执行脚本时会自动收集信息并赋值给这些数组。共有十多个分类。

| 名称 | 功能 |
|--------|--------|
| $_GET[]       |   取得用GET方法提交的表单内容，数组键和值分别对应元素名和值     |
| $_POST[]       |   取得用POST方法提交的表单内容，数组键和值分别对应元素名和值     |
| $_COOKIE[]       |   取得或设置当前站点的Cookie     |
| $_SESSION[]       |   取得当前用户访问的会话，以数组形式体现，如sessionid及自定义session数据     |
| $_ENV[]       |   当前PHP服务器的环境变量     |
| $_SERVER[]       |   当前PHP运行环境的服务器变量     |
| $_FILES[]       |   用户上传文件时提交到当前脚本参数     |
| $_REQUEST[]       |   包含当前脚本提交的所有请求，它包含了$_GET[]、$_POST[]、$_COOKIE[]、$_SESSION[]这些超级全局数组的全部内容     |
| $GLOBALS[]       |   该超级变量数组包含正在执行脚本时所有超级全局数组的内容     |

## 1.7 global 关键字与 global 数组的区别

`$GLOBALS['var']` 是外部的全局变量本身，`global $var` 是外部$var的同名引用或者指针，如：

- $GLOBALS['var']

```php
<?php

$var1 = 1;

function test() {
    unset($GLOBALS['var1']);
}

test();
echo $var1; //因为$var1变量被删除，所以没有内容显示出来
```

- global $var

```php
<?php

$var1 = 1;

function test() {
    global $var1;
    unset($var1);
}

test();
echo $var1; //输出 1
```

综上：
- $GLOBALS['var'] 是外部的全局变量本身
- global $var 是外部$var的同名引用或者指针

## 1.8 活用静态变量（静态变量 在函数执行完时不会销毁，脚本执行完时才销毁）

函数内部创建的局部变量，会在函数执行完毕时立即删除。有时为了保存上次局部变量执行的结果，以便下次执行时使用，这时就可以用静态变量来实现。

```php
<?php

function myFunction() {
    static $myVar = 0;
    echo ++$myVar;
}

myFunction(); // 1
myFunction(); // 2
myFunction(); // 3
```

## 1.9 require、require_once、include、include_once与autoload

- 没有once意味着允许多次执行
- include()、include_once()，包含失败会显示警告错误，然后还会继续执行。如果是require()、require_once(),包含文件失败后会抛出致命错误并中止脚本
- 生产环境中，注意千万不要把程序错误信息抛给用户，可在代码中使用error_reporting(0)禁止所有的错误显示，内部加入完善的错误及日志处理，显示给用户正常内容即可。
- require_once()要慢于require，使用autoload速度最快。

Apache为我们提供了ab工具，用来测试脚本性能，及并发。

`ab -c 10 -n 100000 localhost/index.php` 模拟了10万个请求，同一时间有10个并发请求

## 1.10 = 与 =\=、===的区别
## 1.11 HereDoc 与 NowDoc

```php
<?php

$a = 'hallo';

$hereDoc = <<<HEARDOC
 {$a} world;
HEARDOC;

$nowDoc = <<<'NOWDOC'
 {$a} world;
NOWDOC;

echo $hereDoc; // hallo world;
echo '\n';
echo $nowDoc; // {$a} world;
```

## 1.12 函数传值与引用

函数传值的两种方式：

- 传值

括号内加入相应变量名：

`function getUserInfo($f,$s,$t){}`

使用`func_get_arg()`函数来直接处理：

```php
function getUserInfo() {
    $f = func_get_arg(0);
    $s = func_get_arg(1);
    $t = func_get_arg(2);
}
```

如果还觉得繁琐，可以将`func_get_arg()`函数返回的内容交给数组，再进行处理：

```php
function getUserInfo() {
    $args = func_get_args();
    $f = $args(0);
    $s = $args(1);
    $t = $args(2);
}
```

※ 值传递，不是引用！举例：$a = $b; 删除$a，不影响$b;

- 引用


