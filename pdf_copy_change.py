#原作者： https://blog.csdn.net/weixin_39278265/article/details/84194996
import time
import sys
import os
import re
sys.path.append(os.path.abspath("SO_site-packages"))
import pyperclip  # 引入模块

recent_value = ""
tmp_value="" # 初始化（应该也可以没有这一行，感觉意义不大。但是对recent_value的初始化是必须的）

while True:
    tmp_value = pyperclip.paste() 			# 读取剪切板复制的内容
    
    try:
        if tmp_value != recent_value:				 #如果检测到剪切板内容有改动，那么就进入文本的修改
            recent_value = tmp_value
            changed = out = re.sub("\r\n", " ", recent_value) 	#将文本的换行符去掉，变成一个空格
            pyperclip.copy(changed) 							#将修改后的文本写入系统剪切板中
            print("\n Value changed: %s" % str(changed))  	# 输出已经去除换行符的文本
        time.sleep(0.3)
    except KeyboardInterrupt:  # 如果有ctrl+c，那么就退出这个程序。  （不过好像并没有用。无伤大雅）
        break