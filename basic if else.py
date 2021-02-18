#basic-if-else

money=int(input('คุณมีเงินเท่าไร?:  '))
from pprint import pprint #pretty print
import random
restaurant={'high':[{'name':'shitsuka sushi','price':200},
			 {'name':'peporoni','price':500}],
	  'medium':[{'name':'เสวย','price':200},
	  		 {'name':'รสดี','price':250}],
	  'low':[{'name':'ป๊าส้ม','price':40},
	        {'name':'ป๊าเล็กกระเพรา','price':50}]}

# pprint(restaurant)

# money=1000

if money>=500:
	select=random.choice(restaurant['high'])
	print('คุณท่านทานร้าน {} ดีมั้ยครับ? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))
	# print('shitsuka'+'อร่อยมาก')
elif money>=250:
	select=random.choice(restaurant['medium'])
	print('คุณพี่ทานร้าน {} ดีมั้ยครับ? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))
	# print('เสวย'+'รสชาดดีลองมาแล้ว')
else:
	select=random.choice(restaurant['low'])
	print('พี่ทานร้าน {} ดีมั้ยครับ? ราคาเริ่มต้น {} บาท'.format(select['name'],select['price']))
	# print('ป๊าส้ม'+'ถูกดี')


