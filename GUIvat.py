#GUIvat.py
from tkinter import *
from tkinter import ttk

GUI=Tk()
GUI.geometry('500x600')
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
e3=ttk.Entry(GUI,textvariable=amou,font=font1).pack(pady=20)

###ปุ่มคำนวณ###
def calc():
	print(type(int(price.get())))
	price1=int(price.get())
	amou1=int(amou.get()) #int() คำสั่งแปลงข้อความเป็นตัวเลข เช่น '100' --> 100
	total=price1*amou1
	result.set('ราคาสิ้นค้า {} ชิ้น {} บาท ({}/ชิ้น )'.format(amou1,total,price1))


b1=ttk.Button(GUI,text='คำนวณ',command=calc)
b1.pack(pady=20,ipadx=20)

###ผลลัพธ์จากการคำนวร###
result=StringVar()
result.set('<<<ผลลัพธ์ที่ได้>>>') #โชว์ข้อมูลเริ่มต้น
r1=ttk.Label(GUI,textvariable=result,font=font1)
r1.pack()


GUI.mainloop()