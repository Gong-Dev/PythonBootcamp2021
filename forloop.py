#รันซ้ำตามตัวเลขที่ต้องการ
import time
for i in range(10):
	print(i)
	time.sleep(1)
	print('---')
print('==========')
for i in range(1,20,3):
	print(i)
	time.sleep(1)
	print('---')
print('==========')
friend=['tom','anne','jane','mike']
for f in friend:
	print(f)
print('==========')

for f in friend:
	if f=='anne':
		print(f)
print('==========')	