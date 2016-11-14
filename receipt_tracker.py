from tkinter import *
import sqlite3 as lite
from random import *
from math import *

class App(Frame):
	def __init__(self,master):
		Frame.__init__(self,master, height = 100, width = 100)
		self.label_store = Label(self, text = 'Store Name: ')
		self.label_store.grid(row=1, column =1)
		self.entry_store = Entry(self)
		self.entry_store.grid(row = 1, column=2)
		self.label_tax = Label(self, text = 'Tax paid: ')
		self.label_tax.grid(row=2, column =1)
		self.entry_tax = Entry(self)
		self.entry_tax.grid(row = 2, column=2)
		self.label_balance = Label(self, text = 'Balance: ')
		self.label_balance.grid(row=3, column =1)
		self.entry_balance = Entry(self)
		self.entry_balance.grid(row = 3, column=2)	
		self.label_date = Label(self, text = 'Date: ')
		self.label_date.grid(row=4, column =1)
		self.entry_date = Entry(self)
		self.entry_date.grid(row = 4, column=2)
		self.upload_button = Button(self, text ='Upload', command = self.input_data).grid(row=5, column =2)
		self.item_button = Button(self, text='Add Items', command = self.makeform).grid(row=5, column =1)
	
	# Display input on item window. *****
	
	def input_data(self):
		con = lite.connect('reciept_data.db')
		x = random() * 10000000
		self.y = int(x)
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO trip_data(id, store, tax_paid, balance, date) VALUES(?,?,?,?,?);", (self.y, self.entry_store.get(), self.entry_tax.get(), self.entry_balance.get(), self.entry_date.get()))
		self.entry_store.delete(0,'end')
		self.entry_tax.delete(0,'end')
		self.entry_balance.delete(0,'end')
		self.entry_date.delete(0,'end')
		self.entry_store.focus()
		
	def makeform(self):
		root = Tk()
		self.label_name = Label(root, text = 'Item Name: ')
		self.label_name.grid(row =2, column =1)
		self.entry_name = Entry(root)
		self.entry_name.focus()
		self.entry_name.grid(row=2, column=2)
		self.label_price = Label(root, text = 'Item Price: ')
		self.label_price.grid(row=3, column=1)
		self.entry_price = Entry(root)
		self.entry_price.grid(row=3, column=2)
		self.input_button = Button(root, text='Upload', command = self.input_text)
		self.input_button.grid(row=4, column=2)
		root.mainloop()
	
		
	def input_text(self):
		con = lite.connect('grocery_data.db')
		self.entry_name.focus()
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO item_data(id, item_name, item_price) VALUES(?,?,?);", (self.y,self.entry_name.get(),self.entry_price.get()))
		print('Sucess')
		self.entry_name.delete(0,'end')
		self.entry_price.delete(0,'end')

def main():
	root = Tk()
	App(root).pack(expand=True, fill='both')
	root.mainloop()

if __name__ == "__main__":
	main()

#***sqlite table schema:***
#CREATE TABLE item_data(id INTEGER, item_name TEXT, item_price INTEGER, FOREIGN KEY(id) REFERENCES trip_data(id));
#CREATE TABLE trip_data(id INTEGER PRIMARY KEY, store TEXT NOT NULL, tax_paid INTEGER, balance INTEGER, date INTEGER); 



