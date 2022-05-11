from tkinter import *
from tkinter.filedialog import *
from tkinter.colorchooser import *
from tkinter import messagebox

root=Tk( )
root.propagate(5)
root.configure(bg="white")
t1=Toplevel( )



scr=Scrollbar(root,width=26,relief=RIDGE)
scr.pack(side="right",fill=Y)
t=Text(root,yscrollcommand=scr.set,width=40,height=34)
#t.place(x=0,y=0)
t.pack(expand=True,fill="both")
t.propagate(0)


def openfile( ):

	

	file=askopenfile(mode='r',filetypes=[('python files','*.py*'),('txt files','*.txt'),('all files','*.*')])
	content=file.read( )

	
	
	t.delete(0.0,END)
	t.insert(END,content)

	
	scr.config(command=t.yview)
#Creating all the functions in notepad	
def savefile( ):
	file = asksaveasfile(mode='w', defaultextension=".txt")

	if file:
	    file.write(str(t.get(0.0,END)))
	    file.close()
	    
def new( ):
	m=messagebox.askquestion("Are you sure","Are you sure you want to make a New File?\n Please save the current File if have not saved it.",icon='warning')
	if m== 'yes':
		t.delete(0.0,END)
		
	else:
		messagebox.showinfo("closed","closed")
	
def fontx( ):
	t.config(font=("courier",15))
	
def Helv( ):
	t.config(font=("helvetica",7))
def Cour( ):
	t.config(font=("Courier",7))
def Times( ):
	t.config(font=("Times",9))
	
def changecolor( ):
	col=askcolor( )
	colour=col[1]
	t.config(bg=colour)

def textcolour( ):
	col=askcolor( )
	color=col[1]
	t.config(fg=color)
def fontsize(size):
	t.config(font=("helvetica",size))
	
def cut( ):
	global cutted
	cuts=t.selection_get( )
	cutted=cuts
	
def copy( ):
	global copied
	copys=t.get(0.0,END)
	copied=copys
	
def copy_paste( ):
	t.insert(0.0,copied)
	
def cut_paste( ):
	t.insert(0.0,cutted)
	
def dark( ):
	t.config(bg="black",fg="white")
	root.configure(bg="black")
	scr.configure(bg="gray13")
def white( ):
	t.config(bg="white",fg="black")
	scr.configure(bg="white")

def selectall( ):
	t.tag_add('sel',1.0,END)

def Lg( ):
	t.config(fg="limegreen",bg="black")
	t.configure(bg="black")
	

	
	
	
	
	
	

menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
#creating file menu
menu.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="New",command=new)
filemenu.add_separator( )
filemenu.add_command(label="Exit",command=exit)

editmenu=Menu(menu)
submenu=Menu(editmenu)

submenu.add_radiobutton(label="Helvetica",command=Helv)
submenu.add_radiobutton(label="Courier",command=Cour)
submenu.add_radiobutton(label="Times",command=Times)







#creating edit menu
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_cascade(label="Font",menu=submenu)
editmenu.add_command(label="Background Colour",command=changecolor)
editmenu.add_command(label="Text colour",command=textcolour)
#creating tools menu
toolsmenu=Menu(menu)

menu.add_cascade(label="Tools",menu=toolsmenu)
toolsmenu.add_command(label="Cut",command=cut)
toolsmenu.add_command(label="Copy",command=copy)
toolsmenu.add_command(label="Copy-paste",command=copy_paste)
toolsmenu.add_command(label="Cut-paste",command=cut_paste)
toolsmenu.add_separator( )
toolsmenu.add_command(label="Select All",command=selectall)

#Creating the theme menu
Thememenu=Menu(menu)

menu.add_cascade(label="Themes",menu=Thememenu)

Thememenu.add_command(label="Dark Theme",command=dark)
Thememenu.add_command(label="White Theme",command=white)
Thememenu.add_command(label="Hacker's Choice",command=Lg)







root.mainloop( )