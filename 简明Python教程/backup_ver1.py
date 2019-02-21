# 先申明编码，不然中文会报错！
# -*- coding: utf-8 -*
import os
import time

"""
问题：我想要一款程序来备份我所有的重要文件。
分析：
- 需要备份的文件与目录应在一份列表中予以指定。
- 备份必须存储在一个主备份目录中。
- 备份文件将打包压缩成 zip 文件。
- zip 压缩文件的文件名由当前日期与时间构成。

第二版 修改将日期作为子目录 时间作为压缩文件名

第三版 给备份增加备注
"""

# 1.需要备份的文件与目录将被指定在一个列表中。
source = ['~/Desktop']

# 2.备份必须存储在一个主备份目录中。
target_dir = '/tmp/Desktop_backup'

# 如果目标目录不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 3. 备份文件将打包压缩成 zip	文件。
# 4. 将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# 添加一条来自用户的注释以创建
comment = input('Enter a comment --> ')
# 检查是否有评论键入
# zip 文件名称格式
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# 如果子目录不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 备份文件将打包压缩成 zip 文件。
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Bachup FAILED')

'''
其它待改进
1、允许额外的文件与目录传递到脚本中
答：我们可以从 sys.argv 列表中获得这些名称,然后我们可以通过 list 类提供的 extend 方法把它们添加到我们的 source 列表中.

2、最重要的改进方向是不使用 os.system 方法来创建归档文件,而是使用 zipfile 或 tarfile 内置的模块来创建它们的归档文件。这些都是标准库的一部分,随时供你在你的电脑上没有	zip	程
序作为没有外部依赖的情况下使用这些功能。
'''