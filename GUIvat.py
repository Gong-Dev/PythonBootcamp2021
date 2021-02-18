#GUIvat.py
from tkinter import *
from tkinter import ttk

GUI=Tk()
GUI.geometry('700x600')
GUI.title('โปรแกรมVAT โดย ก๊องแก๊ง')

###config
font1=('TH SarabunPSK',20)

###ช่องกรอก ชื่อสินค้า###

l=ttk.Label(GUI,text='ชื่อสินค้า',font=font1)
l.pack()
prod=StringVar() #ตัวแปร เก็บชื่อสินค้าตอนพิมพ์
e1=ttk.Entry(GUI,textvariable=prod,font=font1)
e1.pack(pady=20)

###ช่องกรอก ราคาสินค้า###
ttk.Label(GUI,text='ราคาสินค้า',font=font1).pack()
price=StringVar() #ตัวแปร เก็บราคาสินค้าตอนพิมพ์
e2=ttk.Entry(GUI,textvariable=price,font=font1).pack(pady=20)

###ช่องกรอก จำนวนสินค้า###
ttk.Label(GUI,text='จำนวน',font=font1).pack()
amou=StringVar() #ตัวแปร เก็บจำนวนสินค้าตอนพิมพ์
e3=ttk.Entry(GUI,textvariable=amou,font=font1)
e3.pack(pady=20)

###ปุ่มคำนวณ###
def calc(event=None):    #(event คือให้สามารถกดคีย์สั่งได้ =none เพื่อให้สามารถใช้คู่กับbutton ได้)
	print('radio: ',v_radio.get())
	# print(type(int(price.get())))
	price1=int(price.get())
	amou1=int(amou.get()) #int() คำสั่งแปลงข้อความเป็นตัวเลข เช่น '100' --> 100
	total=price1*amou1
	prod1=prod.get()

	if v_radio.get()=='ic':
		vat7=total*(7/107)
		netto=total*(100/107)
		# print(('ราคาก่อน vat: {:.2f} (vat7%:{:.2f})').format(netto,vat7))    #:.2f คือให้เป็นทศนิยม 2 ตำแหน่ง
		result.set(' สินค้า : {} จำนวน {} ชิ้น \n ชิ้นละ: {} บาท รวมเป็นเงิน {} บาท\n Net : {:.2f}.- Vat7% : {:.2f}.- '.format(prod1,amou1,price1,
																													total,netto,vat7))																								                
	elif v_radio.get()=='av':
		vat7=total*(7/100)
		netto=total
		sumto=total+vat7																				               
		result.set(' สินค้า : {} จำนวน {} ชิ้น \n ชิ้นละ: {:.2f} บาท รวมเป็นเงิน {:.2f} บาท\n Net : {:.2f}.- Vat7% : {:.2f}.- '.format(prod1,amou1,price1+(vat7/amou1),
																													sumto,netto,vat7))																						               
	else:
		result.set(' สินค้า : {} จำนวน {} ชิ้น \n ชิ้นละ: {} บาท รวมเป็นเงิน {} บาท\n '.format(prod1,amou1,price1,total))
																																																			               


b1=ttk.Button(GUI,text='คำนวณ',command=calc)
b1.pack(pady=20,ipadx=20)
e3.bind('<Return>',calc)
###ผลลัพธ์จากการคำนวร###
result=StringVar()
result.set('<<<ผลลัพธ์ที่ได้>>>') #โชว์ข้อมูลเริ่มต้น
r1=ttk.Label(GUI,textvariable=result,font=font1)
r1.pack()

f1=Frame(GUI)
f1.pack(pady=10)

v_radio=StringVar()

ra1=ttk.Radiobutton(f1,text='ราคารวม vat แล้ว',variable=v_radio,value='ic')
ra1.grid(row=0,column=0)
ra1.invoke() #ให้ra1เป็นdefault

ra2=ttk.Radiobutton(f1,text='ราคา + vat7% ',variable=v_radio,value='av')
ra2.grid(row=0,column=1)

ra3=ttk.Radiobutton(f1,text='ราคาไม่รวม vat',variable=v_radio,value='nic')
ra3.grid(row=0,column=2)


GUI.mainloop()