# airplan
在非洲打工，疫情回不去了，本来公司说是包机票，现在机票3-4万，公司来了 阶梯报销法则

只能自己DIY 计算了，学习python

目标  
1. 本地计算

2. 打包exe
      
3. 打包apk
      
4. 网页查询
      
5. 添加自助查询机票价格并计算，选择航班线路
      
以上目标

主体逻辑完成后很长时间没动力了。。。
继续完善吧，把python程序转换成exe  用了 pyinstaller
需要pip 安装 pyinstaller

完成后 直接在py程序目录 运行cmd
pyinstaller -F *.py
dist 目录下就是生成的exe
第一次运行会闪退，原因，没有GUI
先加个暂停吧
