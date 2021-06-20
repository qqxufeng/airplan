# -*- coding: utf-8 -*-
"""
1.if
  elif
  else
  条件循环语句
2. '%.2f' % 保留2位小数
"""

money = float (input("请输入机票价格："))
pay_1 = (money - 10000) * .3
pay_2 = (money - 20000) * .7 + 3000
pay_3 = (money - 25000)  + 6500
if money <= 10000 :
    print('你回国机票公司承担！')
elif money <= 20000 :
    print('你回国，自行应付机票:','%.2f' %(pay_1))
elif money <= 25000 :
    print('你回国，自行应付机票:','%.2f' %(pay_2))
else:
    print('你回国，自行应付机票:','%.2f' %(pay_3))
    
    
    
    
    
