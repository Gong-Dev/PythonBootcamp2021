money=998
transfer=2000

# print(money<transfer)
print('ต้องการโอน',transfer,'(มีค่าบริการ 15 บาท)')
while money<(transfer+15):
	print('คุณมีเงิน',money)
	print('please deposit to account')
	getm=int(input('how much deposit?:'))
	money=money+getm #998+xxx
	print('---')
print('คุณมีเงิน',money)
print('โอนเงินได้เลย')
print('เหลือเงินในบัญชี:',money-(transfer-15))