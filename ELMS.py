from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

root = Tk()
root.title("EMPLOYEE LEAVE MONITORING SYSTEM")
root.config(background='#7a7473')

root.geometry("1250x900")
f1= Font(family="times")
lvar = []
lvar1 = []
lvar3 = []
def admin():
    global adminentryu,adminentryp,new
    new = Toplevel(root)
    new.title(" Admin ")
    new.geometry('1000x700')
    new.config(bg='#7a7473')
    adminlabel=Label(new,text='ENTER THE PASSWORD AND USERNAME TO CONTINUE',font=f1,bg='#7a7473')
    adminlabel.grid(row=0,columnspan=7,padx=120)
    adminlabelu=Label(new,text='USERNAME',font=f1,bg='#7a7473')
    adminlabelu.grid(row=1,column=1,pady=60)
    adminlabelp=Label(new,text='PASSWORD',font=f1,bg='#7a7473')
    adminlabelp.grid(row=2, column=1,)
    adminentryu = Entry(new,width=35)
    adminentryu.grid(row=1, column=2)
    adminentryp = Entry(new, width=35)
    adminentryp.grid(row=2, column=2)
    adminbuttons=Button(new,text='submit',font=f1,command=check_registration,width=20 )
    adminbuttons.grid(row=3,column=2,pady=30)
    adminbuttonc = Button(new, text='Cancel', font=f1,command=new.destroy,width=20)
    adminbuttonc.grid(row=4, column=2,pady=10)
    adminbuttonr = Button(new, text='REGISTER', font=f1, command=admin_register,width=15)
    adminbuttonr.grid(row=5, column=2,pady=10)

def admin_register():
    global adminentry_pass,adminentry_user,adminentry_scode,new4
    new4 = Toplevel(root)
    new4.config(bg='#7a7473')
    new4.title(" REGISTER ")
    new4.geometry('500x700')
    adminlabelr = Label(new4, text='REGISTER', font=f1,bg='#7a7473',padx=70)
    adminlabelr.grid(row=0, columnspan=9,pady=40)
    adminlabel_user = Label(new4, text='USERNAME', font=f1,bg='#7a7473')
    adminlabel_user.grid(row=1, column=1,padx=40,pady=40)
    adminlabel_pass = Label(new4, text='PASSWORD', font=f1,bg='#7a7473')
    adminlabel_pass.grid(row=2, column=1,padx=40,pady=40)
    adminentry_user = Entry(new4, width=35)
    adminentry_user.grid(row=1, column=2)
    adminentry_pass = Entry(new4, width=35)
    adminentry_pass.grid(row=2, column=2)
    adminbutton_sub = Button(new4, text='submit', font=f1, command=register_)
    adminbutton_sub.grid(row=4,column=2, pady=10)
    adminbutton_can = Button(new4, text='Cancel', font=f1, command=new4.destroy)
    adminbutton_can.grid(row=5, column=2, pady=10)
    adminlabel_scode= Label(new4,text='Security code',font=f1,bg='#7a7473',padx=40,pady=40)
    adminlabel_scode.grid(row=3,column=1)
    adminentry_scode = Entry(new4, width=35)
    adminentry_scode.grid(row=3, column=2)



def register_():
    global lvar,lvar1
    rvar = StringVar()
    rvar2=StringVar()
    rvar1=StringVar()
    rvar = adminentry_user.get()
    rvar1 = adminentry_pass.get()
    rvar2 = adminentry_scode.get()
    if rvar2 == '1234' and rvar != None and rvar1 != None:
        new.destroy()
        lvar.append(rvar)
        lvar1.append(rvar1)
        messagebox.showinfo("hello", 'success')
        new4.destroy()
        admin()
    else:
        messagebox.showinfo("wrong security code","please enter correct one")
        new4.destroy()


def check_registration():
    rvar3 = StringVar()
    rvar4 = StringVar()
    rvar3 = adminentryu.get()
    rvar4 = adminentryp.get()
    if (rvar3 in lvar) and (rvar4 in lvar1) :
        messagebox.showinfo("hello",'success')
        admin_submit()
    else:
        messagebox.showinfo('hello','please enter correct one')


def apply():
    global apply_text, ape,new1

    apply_text = StringVar()
    new1 = Toplevel(root)
    new1.title("Apply leave")
    new1.config(bg='#7a7473')
    new1.geometry('1300x700')
    apply_label = Label(new1, text="Give Your Reason", font=('times', '20', 'bold'),bg='#7a7473')
    apply_label.grid(row=0, columnspan=4)
    apply_text = Text(new1,height=40)
    apply_text.grid(rowspan=4, column=1,padx=70,pady=30)
    apply_label1 = Label(new1, text="Enter Your Name:", font=f1,bg='#7a7473')
    apply_label1.grid(row=2, column=2, pady=30, padx=30)
    ape = Entry(new1, font=f1)
    ape.grid(row=2, column=3)
    apply_bu = Button(new1, text="Submit", command=open_file, font=f1,width=30)
    apply_bu.grid(row=3, column=3)
    apply_bu1 = Button(new1, text="Exit", font=f1, command=new1.destroy,width=30)
    apply_bu1.grid(row=4, column=3,pady=40)



def open_file():
    var1 = StringVar()
    var1 = ape.get()
    var2 = (var1+".txt")
    file = open(var2, 'w')
    apply_d = apply_text.get(1.0, END)
    file.write(apply_d)
    file.close()
    lvar3.append(var1)
    ape.delete(0, END)
    apply_text.delete(1.0, END)
    messagebox.showinfo('apply','success')
    new1.destroy()


def admin_submit():
    global listbox1
    new5 = Toplevel(root)
    new5.title(" Admin ")
    new5.config(bg='#7a7473')
    new5.geometry('1000x700')
    listbox1 = Listbox(new5, height=30, width=70)
    listbox1.pack(padx=20, pady=20)
    ch_button = Button(new5, text="submit", font=f1,command = adminfile_open)
    ch_button.pack(padx=10)
    aa1=0
    while(aa1 <len(lvar3)):
        listbox1.insert(aa1,lvar3[aa1])
        aa1+=1
def adminfile_open():
    global sub_text1,sub_text,adtext
    new6 = Toplevel(root)
    new6.title(" Admin ")
    new6.geometry('1000x700')
    new6.config(bg='#7a7473')
    sub_text = listbox1.get(ANCHOR)
    sub_text1=(sub_text + '.txt')
    adminfile1=open(sub_text1,'r')
    arvar = adminfile1.read()
    adminfile1.close()
    adtext=Text(new6,height=40,width=90)
    adtext.pack(padx=20,pady=20)
    adtext.insert(END,arvar)
    adtxbutton=Button(new6,text="Approve",font=f1,command=approve)
    adtxbutton.pack(padx=20)
    adtxbutton = Button(new6, text="REJECTED", font=f1,command=reject,pady=20)
    adtxbutton.pack(padx=20)

def approve():
    approvefile=open(sub_text1,'a')
    approvefile.write("\n \n \n \n")
    approvefile.write("YOUR LEAVE HAS BEEN PERMITTED\n")
    approvefile.close()
    lvar3.remove(sub_text)
    listbox1.delete(ANCHOR)
    adtext.delete(1.0,END)
    leave_on()


def reject():
    approvefile = open(sub_text1, 'a')
    approvefile.write("\n \n \n \n")
    approvefile.write("YOUR LEAVE IS NOT GRANTED\n")
    approvefile.close()
    lvar3.remove(sub_text)
    listbox1.delete(ANCHOR)
    adtext.delete(1.0, END)
    admin_submit()

def leave_on():
    global leave_onentry
    new7 = Toplevel(root)
    new7.title(" Admin ")
    new7.config(bg='#7a7473')
    new7.geometry('1000x700')
    leavelable = Label(new7,text='ENTER THE DATE',font=f1,bg='#7a7473',pady=20)
    leavelable.pack(pady=10)
    leave_onentry =Entry(new7,font=f1)
    leave_onentry.pack(padx=10)
    leave_onentry.insert(0,"dd-mm-yyyy")
    leave_onbut = Button(new7,text='submit',font=f1,command=filein,pady=20)
    leave_onbut.pack(padx=10)


def filein():
    fileinv=leave_onentry.get()
    fileinv1=(fileinv+'.txt')
    f=open(fileinv1,'a')
    f.write("\n ")
    f.write(sub_text)
    f.close()
    leave_onentry.delete(0,END)

def check():
    new2 = Toplevel(root)
    new2.title("Check status")
    new2.geometry('1000x700')
    new2.config(bg='#7a7473')
    global check_entry, check_text
    check_lab = Label(new2, text="Check Your Status", font=f1,bg='#7a7473')
    check_lab.grid(row=0, columnspan=2)
    check_text = Text(new2, width=100,height=40)
    check_text.grid(rowspan=7, column=1, padx=20, pady=20)
    check_lab1 = Label(new2, text="Enter your name:", font=f1,bg='#7a7473')
    check_lab1.grid(row=2, column=2, padx=40)
    check_entry = Entry(new2, font=f1)
    check_entry.grid(row=2, column=3, padx=40)
    Button(new2, text="check", font=f1, command=check_file,width=20).grid(row=3, column=3)
    Button(new2, text="Exit", font=f1, command=new2.destroy,width=20).grid(row=4, column=3, pady=20)


def check_file():
    cvar = StringVar()
    check_text.delete(1.0, END)
    cvar = check_entry.get()
    cvar1 = (cvar+".txt")
    check_file = open(cvar1, 'r')
    check_text.insert(END, check_file.read())
    check_file.close()
    messagebox.showinfo('message','success')


def leave():
    global inleaveentry,inleavetext
    new3 = Toplevel(root)
    new3.title("Employee in Leave")
    new3.geometry('1000x700')
    new3.config(bg='#7a7473')
    inleavelable = Label(new3, text='Employees In Leave ',font=f1,bg='#7a7473')
    inleavelable.grid(row=0, columnspan=8)
    inleavetext = Text(new3, height=40)
    inleavetext.grid(rowspan=9,column=0, padx=20,pady=30)
    inleaveentrylable= Label(new3, text='Enter the date',padx=10,pady=10,font=f1,bg='#7a7473')
    inleaveentrylable.grid(row=1,column=1,padx=50)
    inleaveentry=Entry(new3, width=40)
    inleaveentry.grid(row=1,column=2,padx=20)
    inleaveentry.insert(0,'DD-MM-YEAR')
    inleavebutton=Button(new3,text='submit',command=inleave_open,font=f1,width=20)
    inleavebutton.grid(row=2,column=2)
    inleavebutton = Button(new3, text='clear', command=inleave_clear, font=f1,width=20)
    inleavebutton.grid(row=3, column=2,pady=10)
    inleaveexbutton=Button(new3,text='Exit',font=f1,command= new3.destroy,width=20)
    inleaveexbutton.grid(row=4,column=2,pady=10,padx=20)

def inleave_open():
    inleavevar = StringVar()
    inleavevar = inleaveentry.get()
    inleavevar1 = (inleavevar + '.txt')
    inleavefile = open(inleavevar1,'r')
    inleavetext.insert(END,inleavefile.read())
    inleavefile.close()

def inleave_clear():
    inleaveentry.delete(0,END)
    inleavetext.delete(1.0,END)


L1 = Label(root, text="Welcome To This Application ", font=f1, padx=200,bg='#7a7473',)
L1.pack(pady=20)
L2 = Label(root, text="Click The Options Below", font=f1, pady=30, padx=20,bg='#7a7473')
L2.pack(pady=20)
b1 =Button(root, text="Admin", font=f1, width=17, height=1, command=admin)
b1.pack(pady=20)

b2 = Button(root, text="Apply Leave", font=f1, padx=30, width=12, height=1, command=apply)
b2.pack(pady=20)

b3 = Button(root, text="Check status", font=f1, padx=40, width=10, height=1, command=check)
b3.pack(pady=20)

b4 = Button(root, text="Employee In Leave", font=f1, padx=40, width=10, height=1, command=leave)
b4.pack(pady=20)

root.mainloop()