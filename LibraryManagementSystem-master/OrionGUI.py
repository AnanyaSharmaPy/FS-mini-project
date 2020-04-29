from tkinter import *
import tkinter.font
import datetime
import tkinter.messagebox
from datetime import timedelta
import os
import hashlib

user_id = 1000000

def login_in():
	global id_input_login
	global password_input_login
	global login_menu

	login_menu=Tk()
	login_menu.wm_title("Login")
	login_menu.minsize(250,150)
	login_menu.maxsize(250,150)
	login_menu.resizable(0,0)
	k_font = tkinter.font.Font(family='Times new roman', size=10, weight=tkinter.font.BOLD)

	id_label=Label(login_menu,text="Your ID")
	password_label=Label(login_menu,text="Password")
	id_input_login=Entry(login_menu)
	password_input_login=Entry(login_menu)
	loginbutton1=Button(login_menu,command=login_check,text=" Login ",bg='light blue',height=1,width=7,font=k_font)
	registerbutton=Button(login_menu,command=register_in,text=" Register ",bg='dark blue',height=1,width=7,font=k_font)
	password_input_login.config(show="*")

	id_label.grid(row=0,sticky=E)
	id_input_login.grid(row=0,column=1)
	password_label.grid(row=1,sticky=E)
	password_input_login.grid(row=1,column=1)
	loginbutton1.grid(columnspan=2)
	registerbutton.grid(columnspan=2)

	login_menu.mainloop()

#changed it from checking for each case hard-coded to a loop
def login_check():
	global id
	id=id_input_login.get()
	password=password_input_login.get()

	if(id == 'admin' and password == 'admin'):
		tkinter.messagebox.showinfo("Login","Greetings!Feedbacks from users are listed here")
		feedback_read()

	f1 = open ('index.txt', 'r')
	
	# salt = 2812738
	# key = hashlib.pbkdf2_hmac(
	# 	'sha256',
	# 	password.encode('utf-8'),
	# 	salt, 
	# 	100000
	# )

	flag = False
	for line in f1:
		line = line.rstrip('\n')
		words = line.split('|')
		if(words[0] == id):
			f2 = open ('Userprofile.txt', 'r')
			pos = words[1]
			f2.seek(int(pos))
			l = f2.readline()
			l = l.rstrip('\n')
			word = l.split('|')
			if(word[1] == password):
				flag = True
				tkinter.messagebox.showinfo("Login","Login Successful!")
				login_menu.destroy()
				Main_Menu()
				break
	if(flag == False):
		tkinter.messagebox.showinfo("Login"," The student ID or Password that you have entered is incorrect.Please reenter")
		return(login_in)


def register_in():
	global id_input
	global name_input
	global email_input
	global password_input
	global register_menu

	register_menu=Tk()
	register_menu.wm_title("Register")
	register_menu.minsize(250,350)
	register_menu.maxsize(250,350)
	register_menu.resizable(0,0)
	k_font = tkinter.font.Font(family='Times new roman', size=10, weight=tkinter.font.BOLD)

	id_label=Label(register_menu,text="Your ID")
	name_label=Label(register_menu,text="Full Name")
	email_label=Label(register_menu,text="Email")
	password_label=Label(register_menu,text="Password")
	id_input=Entry(register_menu)
	name_input=Entry(register_menu)
	email_input=Entry(register_menu)
	password_input=Entry(register_menu)
	loginbutton1=Button(register_menu,command=login_in,text=" Login ",bg='light blue',height=1,width=7,font=k_font)
	registerbutton=Button(register_menu,command=register_check,text=" Register ",bg='dark blue',height=1,width=7,font=k_font)
	password_input.config(show="*")

	id_label.grid(row=0,sticky=E)
	id_input.grid(row=0,column=1)
	name_label.grid(row=1,sticky=E)
	name_input.grid(row=1,column=1)
	email_label.grid(row=2,sticky=E)
	email_input.grid(row=2,column=1)
	password_label.grid(row=3,sticky=E)
	password_input.grid(row=3,column=1)
	registerbutton.grid(columnspan=2)
	loginbutton1.grid(columnspan=2)

	register_menu.mainloop()

def register_check():
	global id
	
	# user_name = []
	# user_password = []
	id=id_input.get()
	name=name_input.get()
	email=email_input.get()
	password=password_input.get()

	f1 = open('index.txt', 'r')
	#if id is already present then ask to login
	for line in f1:
		if line[:7] == id:
			tkinter.messagebox.showinfo("Register","Already registered")
			register_menu.destroy()
			#since login window will already be open.. it's not necessary to open it again
	f1.close()

	# salt = 2812738 # a random number
	# key = hashlib.pbkdf2_hmac(
	# 	'sha256', # The hash digest algorithm for HMAC
	# 	password.encode('utf-8'), # Convert the password to bytes
	# 	salt, # Provide the salt
	# 	100000 # 100,000 iterations of SHA-256 
	# )

	f2 = open ('Userprofile.txt', 'a')
	pos = f2.tell()
	f3 = open ('index.txt', 'a')
	#store hashed passwords which is key
	buf = id + '|' + password + '|' + name + '|' + email + '#'
	f2.write(buf)
	f2.write('\n')
	buf = id + '|' + str(pos)
	f3.write(buf)
	f3.write('\n')
	# key_sort('index.txt')
	f3.close()
	f2.close()
	tkinter.messagebox.showinfo("Register","Registration Successful!")
	register_menu.destroy()

def key_sort(fname):
	t=list()
	fin=open(fname,'r')
	for line in fin:
		line=line.rstrip('\n')
		words=line.split('|')
		t.append((words[0],words[1])) #0-key,1-other, sortin based on key.
		#print(t)
	fin.close()
	t.sort()
	with open("temp.txt",'w') as fout:
		for pkey,addr in t:
			pack=pkey+"|"+addr
			fout.write(pack+'\n')
	os.remove(fname)
	os.rename("temp.txt",fname)


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
	feedback_but=Button(bottomFrame,bg="dark orange",fg="white",text="Feedback",font=in_font,height=5,width=15,command=feedback_in)

	#Positioning of buttons
	borrow_but.pack(side=LEFT)
	return_but.pack(side=LEFT)
	search_but.pack(side=LEFT)
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
