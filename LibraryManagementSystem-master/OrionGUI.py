#Konnichiwa,ganbateh! O_O
from tkinter import *
import tkinter.font
import datetime
import tkinter.messagebox
from datetime import timedelta

def login_in():
	global id_input
	global password_input
	global login_menu

	login_menu=Tk()
	login_menu.wm_title("Login")
	login_menu.minsize(250,80)
	login_menu.maxsize(250,80)
	login_menu.resizable(0,0)
	k_font = tkinter.font.Font(family='Times new roman', size=10, weight=tkinter.font.BOLD)

	id_label=Label(login_menu,text="Your ID")
	password_label=Label(login_menu,text="Password")
	id_input=Entry(login_menu)
	password_input=Entry(login_menu)
	loginbutton1=Button(login_menu,command=login_check,text=" Login ",bg='light blue',height=1,width=7,font=k_font)
	password_input.config(show="*")

	id_label.grid(row=0,sticky=E)
	id_input.grid(row=0,column=1)
	password_label.grid(row=1,sticky=E)
	password_input.grid(row=1,column=1)
	loginbutton1.grid(columnspan=2)

	login_menu.mainloop()


def login_check():
	global id
	user_id = []
	user_password = []
	id=id_input.get()
	password=password_input.get()
	f = open ('Userprofile.txt')
	line = f.readline()
	norecord = int(line)
	z=0
	verification=0
	while line!="":
		line = f.readline()
		if z==0:
			user_id.append(line.rstrip('\n'))
			z=z+1

		elif z==1:
			user_password.append(line.rstrip('\n'))
			z=0

	while True:
		if  user_id[0] == id and user_password[0] == password :
			verification=2
			break

		elif user_id[1] == id and user_password[1] == password:
			verification=1
			break

		elif user_id[2]== id and user_password[2] == password:
			verification=1
			break

		elif user_id[3] == id and user_password[3] == password :
			verification=1
			break

		elif user_id[4] == id and user_password[4] == password:
			verification=1
			break
		else:
			tkinter.messagebox.showinfo("Login"," The student ID or Password that you have entered is incorrect.Please reenter")
			return(login_in)
	if verification==1:
		tkinter.messagebox.showinfo("Login","Login Successful!")
		login_menu.destroy()
		Main_Menu()
	else:
		tkinter.messagebox.showinfo("Login","Greetings!Feedbacks from users are listed here")
		feedback_read()

def Main_Menu():
	base = Tk()
	#Window title and size optimization
	base.wm_title("CENTRAL LIBRARY")
	base.minsize(600,600)

	but_font = tkinter.font.Font(family='Helvetica', size=15, weight=tkinter.font.BOLD)
	in_font = tkinter.font.Font(family='Lucida Calligraphy', size=15, weight=tkinter.font.BOLD)
	current_time1=datetime.datetime.now()
	current_time=str(current_time1)
	#Bunch of labels
	status = Label(base,text=("Date and time logged in: " + current_time),bd=1,relief=SUNKEN,anchor=W,bg='light pink')
	orionLabel=Label(base, text="CENTRAL LIBRARY",bg='dark orange',font=("Castellar", "50","bold","italic","underline"),fg="black")
	welcomeLabel=Label(base,text=("Welcome! "+id),font=("Freestyle Script","50","bold"))
	imageLibrary = PhotoImage(file="giphy.gif")
	topFrame=Frame(base)
	bottomFrame=Frame(base)

	#Positioning of labels
	status.pack(side=BOTTOM,fill=X)
	orionLabel.pack(fill=X)
	welcomeLabel.pack()
	Label(base, image=imageLibrary).pack()
	topFrame.pack()
	bottomFrame.pack(side=BOTTOM)

	#Buttons
	borrow_but=Button(bottomFrame,bg="black",fg="white",text="Borrow books",font=in_font,height=5,width=15,command=borrow_in)
	return_but=Button(bottomFrame,bg="dark orange",text="Return books",font=in_font,height=5,width=15,command=return_in)
	search_but=Button(bottomFrame,bg="black",fg="white",text="Search for books",font=in_font,height=5,width=15,command=search_in)
	store_but=Button(bottomFrame,bg="dark orange",text="Shop",font=in_font,height=5,width=15,command=shop_in)
	feedback_but=Button(bottomFrame,bg="black",fg="white",text="Feedback",font=in_font,height=5,width=15,command=feedback_in)

	#Positioning of buttons
	borrow_but.pack(side=LEFT)
	return_but.pack(side=LEFT)
	search_but.pack(side=LEFT)
	store_but.pack(side=LEFT)
	feedback_but.pack(side=LEFT)

	base.mainloop()




def borrow_in():
	global borrow_entry1
	global bookborrow
	global borrow_menu

	borrow_menu=Tk()

	borrow_menu.wm_title("Borrow")
	borrow_menu.minsize(900,500)
	borrow_menu.maxsize(900,500)
	borrow_menu.resizable(0,0)


	Title = []
	Author = []
	Availability = []

	f = open ("Bookdata.txt")#read the number of records that specified in the first line of text file
	line = f.readline()
	norecord =int(line)#Read records of file and store them into the array

	b = 0
	while line!="":
		line = f.readline()
		if b == 0:
			Title.append(line.rstrip('\n'))
			b = b + 1
		elif b == 1:
			Author.append(line.rstrip('\n'))
			b = b + 1
		else:
			Availability.append(line.rstrip('\n'))
			b = 0



	borrow_list=Listbox(borrow_menu,height=50,width=50)
	borrow_list2=Listbox(borrow_menu,height=50,width=50)
	borrow_list3=Listbox(borrow_menu,height=50,width=50)


	for num in range(0,norecord):
		borrow_list.insert(0,Title[num])
		borrow_list2.insert(0,Author[num])
		borrow_list3.insert(0,Availability[num])

	borrow_list.configure(background="pink")
	borrow_list2.configure(background="pink")
	borrow_list3.configure(background="light grey")
	borrow_label1=Label(borrow_menu,text="<<< Please enter the book title that you wish to borrow >>>",font=("Times", "20","bold","italic"),bg="light blue")
	borrow_label2=Label(borrow_menu,text="Title")
	borrow_label3=Label(borrow_menu,text="Author")
	borrow_label4=Label(borrow_menu,text="Availability")

	borrow_entry1=Entry(borrow_menu,width=50)
	borrow_button1=Button(borrow_menu,text="Borrow",command=borrow_check,font=("Times new roman","10","bold"),bg="light blue")

	borrow_label1.grid(row=0,columnspan=20)
	borrow_label2.grid(row=3,column=1)
	borrow_label3.grid(row=3,column=4)
	borrow_label4.grid(row=3,column=7)

	borrow_entry1.grid(row=1,columnspan=20)
	borrow_button1.grid(row=2,columnspan=20)
	borrow_list.grid(row=4,column=1)
	borrow_list2.grid(row=4,column=4)
	borrow_list3.grid(row=4,column=7)
	borrow_menu.mainloop()

def borrow_check():

	book = open("Bookdata.txt",'r')
	bookborrow = book.readlines()
	book.close()
	date = datetime.date.today()
	enddate = date + timedelta(days = 7)
	bbook=(borrow_entry1.get().upper() + ('\n'))
	bbook=str(bbook)
	if (bbook in bookborrow):
		numline_book = bookborrow.index(bbook)
		Avail = numline_book + 2
		if bookborrow[Avail] == str("Unavailable\n"):
			tkinter.messagebox.showinfo("Borrow","This book is currently unavailable, please select another book")
			borrow_menu.lift()
			u = 1
		else:
			bookborrow[Avail] = str("Unavailable\n")
			with open("Bookdata.txt",'w') as file:
				file.writelines(bookborrow)
			tkinter.messagebox.showinfo("Borrow","The book you have selected has been successfully borrowed. Please return it by:" +'\n'+ str(enddate) )

			rec = open("Record.txt","r")
			record = rec.readlines()
			rec.close()
			log = id +("\n")
			if (log in record):
				numline = record.index(log)
				BB = numline + 1
				record[BB] = str("\n"+ bbook)
			with open("Record.txt",'w') as file:
				file.writelines(record)
			Done2=tkinter.messagebox.askyesno("Borrow","Do you want to borrow another book?")
			if Done2==True:
				borrow_menu.destroy()
				borrow_in()
			else:
				borrow_menu.destroy()



	else:
		tkinter.messagebox.showinfo("Borrow","The book that you had entered is not in our database,sorry,please enter a different book")
		borrow_menu.lift()

def return_in():
	global return_entry1
	global return_menu
	global record_verification
	return_menu=Tk()
	return_menu.minsize(400,400)
	return_menu.maxsize(400,400)
	return_menu.wm_title("Return")
	return_menu.resizable(0,0)

	record_list=Listbox(return_menu,height=25,width=70)

	Title = []
	Author = []
	Availability = []
	##uses data from reader.py. Will work when compiled
	#User_id = []
	#Borrow = []
	f = open ("Bookdata.txt")
	#read the number of records that specified in the first line of text file
	line = f.readline()
	norecord = int(line)
	#Read records of file and store them into the array
	b = 0
	while line!="":
		line = f.readline()
		if b == 0:
			Title.append(line.rstrip('\n'))
			b = b + 1
		elif b == 1:
			Author.append(line.rstrip('\n'))
			b = b + 1
		else:
			Availability.append(line.rstrip('\n'))
			b = 0
	record_verification=[None]
	record_verification_num=0
	recording = open ("Record.txt","r+")
	user_book = recording.readlines()
	recording.close()
	verification2=0
	log=id+("\n")
	if (log in user_book):
		bookline = user_book.index(log)
	while verification2==0:
		try:
			bookarrange = bookline+1
			user_book[bookarrange]=int(user_book[bookarrange])
			break
		except ValueError:
			record_verification_num=record_verification_num+1
			record_verification.append(user_book[bookarrange])
			record_list.insert(bookline,user_book[bookarrange])
			bookline=bookline+1


	record_list.configure(background="light grey")
	return_button1=Button(return_menu,text="Return",command=return_check,font=("Times new roman","10","bold"),bg="dark orange")
	return_entry1=Entry(return_menu,width=50)
	return_label1=Label(return_menu,text=" Please enter the book title that you wish to return ",font=("Times", "12","bold","italic"),bg="light blue")
	return_label2=Label(return_menu,text=id+"'s borrowing record",font=("Times","10","bold"))
	return_label1.grid(row=0,columnspan=20)
	return_entry1.grid(row=1,columnspan=20)
	return_label2.grid(row=3,column=5)
	return_button1.grid(row=2,columnspan=20)
	record_list.grid(row=4,column=5)


	return_menu.mainloop()



def return_check():
	import datetime as dt
	from datetime import timedelta
	date = dt.date.today()
	bbook =(return_entry1.get().upper() + ('\n'))
	book = open("Bookdata.txt")
	bookborrow = book.readlines()
	book.close()
	if (bbook in bookborrow)and (bbook in record_verification):
		numline_book = bookborrow.index(bbook)
		Avail = numline_book + 2
		if bookborrow[Avail] == str("Available\n"):
			tkinter.messagebox.showinfo("This book has been returned, please select another book")

		else:
			bookborrow[Avail] = str("Available\n")
			with open("Bookdata.txt",'w') as file:
				file.writelines(bookborrow)
			tkinter.messagebox.showinfo("Return","The book you have selected has been successfully returned on"+'\n'+str(date))

			rec = open("Record.txt","r+")
			record = rec.readlines()
			rec.seek(0)
			for log in record:
				if log != bbook:
					rec.write(log)
			rec.truncate()
			rec.close()

			Done3=tkinter.messagebox.askyesno("Return","Do you want to return another book?")
			if Done3==True:
				return_menu.destroy()
				return_in()
			else:
				return_menu.destroy()
	else:
		tkinter.messagebox.showinfo("Return","The book that you had entered is invalid.Please reenter a different book")
		return_menu.lift()

def shop_in():
	global shop_entry1
	global shop_entry2
	global shop_entry3
	global shop_entry4
	global shop_entry5
	global shop_menu

	#The shop main menu
	shop_menu=Tk()
	shop_menu.wm_title("Shop")
	shop_menu.resizable(0,0)
	tkinter.messagebox.showinfo("Shop","Get 10% off from your total purchase when you purchase more than RM50")
	shop_menu.lift()

	f=open("item.txt","r")
	line=f.read().splitlines()
	f.close()
	shop_menu.minsize(350,300)
	shop_menu.maxsize(350,300)

	#Defining variables >.<
	itemleft1=int(line[0])
	itemleft2=int(line[1])
	itemleft3=int(line[2])
	itemleft4=int(line[3])
	itemleft5=int(line[4])

	#These strings are meant to be placed in the listbox "shop_list"
	kitemleft1=str(itemleft1)
	kitemleft2=str(itemleft2)
	kitemleft3=str(itemleft3)
	kitemleft4=str(itemleft4)
	kitemleft5=str(itemleft5)

	#Creating listbox,entries,labels and "purchase" button
	shop_list=Listbox(shop_menu,width=60,height=7)
	shop_button1=Button(shop_menu,text="Purchase",command=shop_in_check,bg="dark orange")
	shop_entry1=Entry(shop_menu,width=5)
	shop_label1=Label(shop_menu,text="MMU T-Shirt")
	shop_entry2=Entry(shop_menu,width=5)
	shop_label2=Label(shop_menu,text="MMU lanyard")
	shop_entry3=Entry(shop_menu,width=5)
	shop_label3=Label(shop_menu,text="MMU Student Handbook")
	shop_entry4=Entry(shop_menu,width=5)
	shop_label4=Label(shop_menu,text="MMU Student Card")
	shop_entry5=Entry(shop_menu,width=5)
	shop_label5=Label(shop_menu,text="MMU Academic Calendar")
	shop_label6=Label(shop_menu,text="Quantity")

	#Postioning listbox,entries,labels and "purchase" button
	shop_list.grid(rowspan=7,columnspan=60)
	shop_entry1.grid(row=8,column=3)
	shop_entry2.grid(row=9,column=3)
	shop_entry3.grid(row=10,column=3)
	shop_entry4.grid(row=11,column=3)
	shop_entry5.grid(row=12,column=3)
	shop_label1.grid(row=8,column=2,sticky=E)
	shop_label2.grid(row=9,column=2,sticky=E)
	shop_label3.grid(row=10,column=2,sticky=E)
	shop_label4.grid(row=11,column=2,sticky=E)
	shop_label5.grid(row=12,column=2,sticky=E)
	shop_label6.grid(row=7,column=3)
	shop_button1.grid(row=13,column=3)

	#Inserting stuff into the listbox >.<
	shop_list.insert(0,"No | Item |                                                | Price                  | Stocks left|")
	shop_list.insert(1,"1.     MMU T-shirt                                     RM37.90		              "+kitemleft1)
	shop_list.insert(2,"2.     MMU lanyard                                   RM1.80			                 "+kitemleft2)
	shop_list.insert(3,"3.     MMU Student Handbook               RM10.50			              "+kitemleft3)
	shop_list.insert(4,"4.     MMU Student Card                        RM50.00			                "+kitemleft4)
	shop_list.insert(5,"5.     MMU Academic Calendar              RM5.30			                 "+kitemleft5)

	shop_menu.mainloop()

def shop_in_check(): #This module is to check if the user's input is a valid integer or not
	global quantity1
	global quantity2
	global quantity3
	global quantity4
	global quantity5

	try:
		quantity1=(shop_entry1.get())
		quantity1=int(quantity1)
		quantity2=(shop_entry2.get())
		quantity2=int(quantity2)
		quantity3=(shop_entry3.get())
		quantity3=int(quantity3)
		quantity4=(shop_entry4.get())
		quantity4=int(quantity4)
		quantity5=(shop_entry5.get())
		quantity5=int(quantity5)
	except ValueError:
		tkinter.messagebox.showinfo("Shop","One or more of your entries is not a valid input.Please reenter :D ")
		shop_menu.lift()
		return(shop_in)

	shop_check()


def shop_check():
	totalprice=0
	f=open("item.txt","r")
	line=f.read().splitlines()
	f.close()
	price1=quantity1*37.90
	itemleft1=int(line[0])-quantity1
	if itemleft1<0:
		itemleft1=itemleft1+quantity1
		price1=0
		tkinter.messagebox.showinfo("Shop","Sorry it seems like we don't have enough MMU T-Shirt in stock.We apologize for the inconvenience caused")
		shop_menu.lift()
		return(shop_in)
	price2=quantity2*1.80
	itemleft2=int(line[1])-quantity2
	if itemleft2<0:
		itemleft2=itemleft2+quantity2
		price2=0
		tkinter.messagebox.showinfo("Shop","Sorry it seems like we don't have enough MMU lanyard in stock.We apologize for the inconvenience caused")
		shop_menu.lift()
		return(shop_in)
	price3=quantity3*10.50
	itemleft3=int(line[2])-quantity3
	if itemleft3<0:
		itemleft3=itemleft3+quantity3
		price3=0
		tkinter.messagebox.showinfo("Shop","Sorry it seems like we don't have enough MMU Student Handbook in stock.We apologize for the inconvenience caused")
		shop_menu.lift()
		return(shop_in)
	price4=quantity4*50.00
	itemleft4=int(line[3])-quantity4
	if itemleft4<0:
		itemleft4=itemleft4+quantity4
		price4=0
		tkinter.messagebox.showinfo("Shop","Sorry it seems like we don't have enough MMU Student Card in stock.We apologize for the inconvenience caused")
		shop_menu.lift()
		return(shop_in)
	price5=quantity5*5.30
	itemleft5=int(line[4])-quantity5
	if itemleft5<0:
		itemleft5=itemleft5+quantity5
		price5=0
		tkinter.messagebox.showinfo("Shop","Sorry it seems like we don't have enough MMU Academic Calendar in stock.We apologize for the inconvenience caused")
		shop_menu.lift()
		return(shop_in)
	totalprice=totalprice+price1+price2+price3+price4+price5
	if totalprice>50:
		totalprice=totalprice-(totalprice*1/10)
	Done=tkinter.messagebox.askyesno("Shop","Do you wish to checkout?")
	if Done== True:
		pass
	else:
		tkinter.messagebox.showinfo("Shop","Please fill the quantity(s) again.")
		totalprice=0
		itemleft1=itemleft1+quantity1
		itemleft2=itemleft2+quantity2
		itemleft3=itemleft3+quantity3
		itemleft4=itemleft4+quantity4
		itemleft5=itemleft5+quantity5
		shop_menu.lift()
		return (shop_in)

	f=open ("item.txt","w+")
	f.write(str(itemleft1)+'\n')
	f.write(str(itemleft2)+'\n')
	f.write(str(itemleft3)+'\n')
	f.write(str(itemleft4)+'\n')
	f.write(str(itemleft5)+'\n')
	f.close()
	totalprice=str(totalprice)
	tkinter.messagebox.showinfo("Shop","Your bill and item(s) is ready."+"Payment= RM"+totalprice+" .Kindly collect your items at our service counter during working hours.Thank you.")
	shop_menu.destroy()

def search_in():
	global search_entry
	global search_menu
	search_menu=Tk()

	search_menu.maxsize(500,100)
	search_menu.maxsize(500,100)
	search_menu.wm_title("Search")
	search_menu.resizable(0,0)

	search_label1=Label(search_menu,text="Search through our database to check if your desired book is available",font=("Times", "12","bold","italic"),bg="light blue")
	search_label1.pack(side=TOP)

	search_entry = Entry(search_menu,width=50)
	search_entry.pack(side=TOP)

	search_button=Button(search_menu,text="Search",command=search_check,font=("Times new roman","10","bold"),bg="dark orange")
	search_button.pack(side=TOP)

	search_menu.mainloop()


def search_check():
	file = open ('Bookdata.txt', 'r')
	booklist = file.readlines()
	file.close()
	search_word=(search_entry.get().upper()+('\n'))
	search_menu.destroy()
	if (search_word in booklist):
		search_menu2=Tk()
		search_menu2.wm_title("Search")
		search_menu2.attributes("-topmost",True)
		tkinter.messagebox.showinfo("Search","It is in our database!")

		search_result=Listbox(search_menu2,height=10,width=50)
		numline_book = booklist.index(search_word)
		book=str(booklist[numline_book])
		author=str(booklist[numline_book + 1])
		availability=str(booklist[numline_book + 2])

		search_result.insert(1,"Name:" + book)
		search_result.insert(2,"Author:" +author)
		search_result.insert(3,"Availability:" +availability)

		search_result.pack()
		search_menu2.mainloop()
	else:
		tkinter.messagebox.showinfo("Search","Sorry,this book does not exist in our database")

def feedback_in():
	global feedback_bar
	global feedback_menu
	global feedback_input

	feedback_menu=Tk()
	feedback_menu.wm_title("Feedback")
	feedback_menu.maxsize(800,200)
	feedback_menu.resizable(0,0)

	feedback_bar=Entry(feedback_menu,width=100)
	feedback_label=Label(feedback_menu,text= "We improve from your valuable feedback.Thank you!",font=("Monotype corsiva","15","italic"),bg="light blue")
	button1=Button(feedback_menu, text="Submit feedback",command=feedback_check,font=("Times new roman","10","bold"),bg="dark orange")

	feedback_bar.pack(side=TOP)
	feedback_label.pack(side=TOP)
	button1.pack(side=TOP)
	feedback_menu.mainloop()

def feedback_check():
	user_feedback=feedback_bar.get()
	if len(feedback_bar.get())==0:
		tkinter.messagebox.showinfo("Feedback","You did not type anything O_O")
		feedback_menu.lift()
		return(feedback_in)
	else:
		tkinter.messagebox.showinfo("Feedback","Thank you for your valuable feedback! >_<")
		file = open('Feedback.txt', 'a')
		file.write(user_feedback + "\n")
		file.close()
		feedback_menu.destroy()


def feedback_read():
	login_menu.destroy()
	read_feedback_menu=Tk()
	read_feedback_menu.minsize=(1000,1000)
	read_feedback_menu.minsize=(1000,1000)
	read_feedback_menu.wm_title("Users' feedback")

	list=Listbox(read_feedback_menu)
	file = open('Feedback.txt' , 'r')
	num_feedback = len(file.readlines())
	file.close()
	file = open('Feedback.txt' , 'r')
	count = 1
	feedback = file.readlines()
	for i in range(0, num_feedback):
		list_feedback =str(count) + ('.') + (feedback[count - 1])
		list.insert(count,list_feedback)
		count += 1

	list.pack(side=LEFT,fill=BOTH,expand=YES)
	read_feedback_menu.mainloop()

login_in()
