#!/usr/bin/python3

# -*- coding: utf-8 -*-
# @Time    : 2019-04-08 17:06
# @Author  : liushiyi
# @Email   : liushiyi1027@gmail.com
# @File    : 1.3-保留最后N个元素.py
# @Software: PyCharm

"""
问题：
在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？
"""

"""
解决方案：
保留有限历史记录正式"collections.deque"大显身手的时候。
比如，下面的代码在多行上面做简单的文本匹配，并返回匹配所在行的最后N行。
"""


from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)
if __name__ == '__main__':
    with open(r'../../cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

"""
在写查询元素的代码时，通常会使用包含 yield 表达式的生成器函数，也就是我们上面示例代码中的那样。 这样可以将搜索过程代码和使用搜索结果代码解耦。
"""

"""
扩展：
使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉。
"""