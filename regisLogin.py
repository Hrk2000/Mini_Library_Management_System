from tkinter import *
import re
import os
import time
import tkinter.messagebox as tmsg


def rtrn():
    pass 

def gtbk():
    screen11 = Toplevel(screen)
    ip = inp.get().upper()
    output = []
    f = open("booklist.txt","r")
    g = open(f"{user1}books", "a+")
    for line in f:
         if not ip in line:
             output.append(line)
         else:
             Label()
    g.write(f"{ip}\n")
    g.close()
    f = open("booklist.txt", "w")
    f.writelines(output)
    f.close()


def gb():
    screen10 = Toplevel(screen)
    screen10.title("Lent Books")
    screen10.configure(background="gray15")
    screen10.geometry("850x750")
    Label(screen10,text="GET BOOKS",bg="gray20",fg="gray75",font="serif 12 bold").pack(fill=X)
    Label(screen10,text="\n",bg="gray15").pack()
    Label(screen10,text="Book Name",bg="gray20",fg="gray75",font="serif 9 bold").pack()
    Label(screen10,text="\n",bg="gray15").pack()
    global inp
    inp = StringVar()
    Entry(screen10,text=inp,bg="gray15",fg="gray75",font="serif 8 bold").pack()
    Label(screen10,text="\n",bg="gray15").pack()
    Button(screen10,text="Get",bg="gray20",fg="gray75",font="serif 7 bold", command=gtbk).pack()
    
    Button(screen10, text="×",bg="gray15",fg="red", font="Roboto 10 bold",border=3, highlightbackground="red",command=screen10.destroy).pack(anchor="ne")
    


def newbook():
    nb = bken.get()
    f = open("booklist.txt","a+")
    adb = f.write("{"+nb.upper()+"}"+"\n")
    Label(screen9,text=f"\"{nb.upper()}\"\n, added successfully",font="serif 8 bold",bg="gray15",fg="yellow").pack()
    bken.set("")


def bklist():
    screen8 = Toplevel(screen)
    screen8.configure(background="gray15")
    screen8.title("List")
    screen8.geometry("850x750")
    Label(screen8,text="LIBRARY's BOOK",font="serif 12 bold",fg="gray75",bg="gray15").pack()
    Label(screen8,text="",bg="gray15").pack()
    bk = open("booklist.txt", "r")
    verf = bk.read()
    Label(screen8,text=verf,bg="gray18",fg="wheat2",font="Roboto 8 bold").pack(fill=X, padx=6)
    bk.close()
    Label(screen8,text="\n\n\n",bg="gray15").pack()
    Button(screen8, text="×",bg="gray15",fg="red", font="Roboto 10 bold",border=3, highlightbackground="red",command=screen8.destroy).pack(anchor="ne")
    

def addBook():
    global screen9
    screen9 = Toplevel(screen)
    screen9.geometry("850x750")
    screen9.title("Add Book")
    screen9.configure(background="gray15")
    global bken
    bken = StringVar()
    adbk = open("booklist.txt","a+")
    Label(screen9,text="ADD BOOK",font="serif 20 bold",bg="gray20",fg="gray75").pack()
    Label(screen9,text="\n",bg="gray15").pack()
    Label(screen9,text="Enter book name",bg="gray20",fg="gray75", font="serif 13 bold").pack()
    Label(screen9,text="",bg="gray15").pack()
    bkentry= Entry(screen9,text=bken, width=25).pack(padx=7)
    Label(screen9,text="",bg="gray15").pack()
    Button(screen9,text="Submit", font="serif 8 bold",bg="gray15",fg="gray75",command=newbook).pack()
    
    
    Button(screen9, text="Close",bg="gray15",fg="red", font="Roboto 7 bold",border=3, highlightbackground="red",command=screen9.destroy).pack(anchor="ne")


def upd_done():
    # screen7 = Toplevel(screen)
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_-+={}[]:;\'\"|\\?/>.<,12345678901234567891234567890"
    key = 5
    encrypt = ''
    for i in u_info:
        position = alp.find(i)
        newposition = position+5
        encrypt += alp[newposition]
    f3 = open(f"{user2}"+".txt", "w")
    f3.write(f"{encrypt}")
    tmsg.showinfo("Updated", "Your password is successfully updated. You can now log in with this password.")
    screen6.destroy()
    # Label(screen7, text="Updated").pack()
    f3.close()


def check2():
    global u_info
    statusvar = StringVar()
    statusvar.set("Ready")
    sbar = Label(screen6, textvariable = statusvar, relief = SUNKEN,anchor = "center")
    sbar.pack(side = BOTTOM, fill = X)
    u_info = userupname.get()
    x = True
    while x:  
        if (len(u_info)==0):
            put = "Fill the box(s) first."
            statusvar.set(f'{put}\nScreen update after 6 seconds')
            sbar.update()
            # time.sleep(3)
            statusvar.set("Ready Now")
            sbar.update()
            break
        elif (len(u_info)<=8 or len(u_info)>12):
            
            # time.sleep(1)
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            # time.sleep(3)
            statusvar.set("Ready Now")
            sbar.update()
            break
        elif not re.search("[a-z]",u_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            # time.sleep(3)
            statusvar.set("Ready Now")
            sbar.update()
            break
        elif not re.search("[0-9]",u_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            # time.sleep(3)
            statusvar.set("Ready Now")
            sbar.update()
            break
        elif not re.search("[A-Z]",u_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            # time.sleep(3)
            statusvar.set("Ready Now")
            sbar.update()
            break
        elif not re.search("[$#@]",u_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            # time.sleep(3)
            statusvar.set("Ready Now")
            sbar.update()
            break
        elif re.search("\s",u_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            # time.sleep(3)
            statusvar.set("Ready Now")
            sbar.update()
            break
        else:
            statusvar.set("Updated")
            sbar.update()
            upd_done()
            break






def search1(event=''):
    screen5.destroy()
    global screen6
    screen6 =Toplevel(screen)
    screen6.geometry("850x750")
    screen6.title("User")
    global user2
    user2 = user_verify1.get()
    list_of = os.listdir()
    if user2 in list_of:
        f2 = open(f"{user2}", "r")
        check = f2.read().splitlines()
        Label(screen6,text="User Found").pack()
        global userupname
        userupname = StringVar()
        finalUpEntry=Entry(screen6, textvariable=userupname)
        finalUpEntry.pack()
        b = Button(screen6,text="Update", command=check2)
        b.pack()
   
    else:
        d = tmsg.showerror("Error !", "Issue while searching User.\n• Check username\n• Spelling Mistake\n• Not Exists\nIf following info are wrong,\nthen type a mail to\nhritikkarn@gmail.com")
    user_verify1.set("")
    

def delete2():
    screen4.destroy()
    f = tmsg.askquestion("Rating us","Is your experience good\nwith this library")
    if f == "yes":
        g = tmsg.showinfo("Rated","Thanks For rating us\nPlease Review to our\n HRK-Lib-app.")
    else:
        h = tmsg.showinfo("Rated","Thanks For rating us\nWe'll try to make it better.")

#-------------------------------------------------------------
def forget(event=''):
    global screen5
    screen2.destroy()
    screen5 = Toplevel(screen)
    screen5.geometry("850x750")
    screen5.title("Forget Password")
    screen5.configure(background="gray15")
    Label(screen5, text="PASSWORD UPDATION", bg="gray20",fg="gray75",width="30", height="2",font="Roboto 20 bold").pack(fill=BOTH)
    Label(screen5, text="",bg="gray15").pack()
    Label(screen5, text="User-ID",bg="gray15",fg="gray75",font="Roboto 15 bold").pack()
    global user_entry2
    global user_verify1
    user_verify1 = StringVar()
    us_entry2 = Entry(screen5,text=user_verify1, width=40,border=3,font="arial 15 bold").pack()
    Label(screen5, text="\n",bg="gray15").pack()
    sm = Button(screen5,text="Search",bg="gray15",fg="gray75",font="Arial 12 bold",border=6, command=search1)
    sm.pack()
    sm.bind("<Return>", search1)
    Label(screen5, text="\n\n",bg="gray15").pack()



def login_success():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Login Success")
    screen4.geometry("850x750")
    screen4.configure(background="gray15")
    Label(screen4, text="HRK-LIBRARY", bg="gray20",fg="gray75",width="25", height="2",font="Roboto 10 bold").pack()
    Label(screen4,text="\n",bg="gray15").pack()
    Button(screen4,text="Add Book",bg="gray15", font="Roboto 10 bold",fg="gray60", borderwidth=4,command=addBook).pack()
    Label(screen4,text="\n",bg="gray15").pack()
    Button(screen4,text="Get Book",bg="gray15", font="Roboto 10 bold",fg="gray60", borderwidth=4,command=gb).pack()
    Label(screen4,text="\n",bg="gray15").pack()
    
    Button(screen4,text="Book List",bg="gray15", font="Roboto 10 bold",fg="gray60", borderwidth=4, command=bklist).pack()
    Label(screen4,text="\n",bg="gray15").pack()
    Button(screen4,text="Return Book",bg="gray15", font="Roboto 10 bold",fg="gray60", borderwidth=4,command=rtrn).pack()
    Label(screen4,text="\n\n",bg="gray15").pack()
    Button(screen4, text="close",bg="gray15",font="Roboto 8 bold",fg="red", command=delete2).pack(anchor="se")
    
    
def pass_not_reco():
    b = tmsg.showinfo("Password Error",f"You had entered\nwrong password !\n\nClick on \'Forgot Password\'\nif you not remember.")
        
def user_not_found():
    c=tmsg.showinfo("User Error","User Identity is not found,\nPlease Check User-Id.\n\tOR\nCreate a new one.\nTHANKS !!")
            
    

def login_verify():
    global user1
    global pass1
    user1 = user_verify.get()
    pass1 = pass_verify.get()

    key = 5
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_-+={}[]:;\'\"|\\?/>.<,12345678901234567891234567890"
    decrypt = ''
    for i in pass1:
        position = alp.find(i)
        newposition = position+5
        decrypt += alp[newposition]
        # print(decrypt)


    
    lof = os.listdir()
    if user1 in lof:
        f1 = open(f"{user1}"+".txt", "r")
        verify =f1.read().splitlines()
        if decrypt in verify:
            login_success()
        else:
            pass_not_reco()
    else:
            user_not_found()
            
    screen2.destroy()
            
def shpass(args):
    p = pass_verify.get()
    if args == 1:
        sp.config(text = f'{p}')
    else:
        sp.config(text = 'Show Password ?')

def login(event=''):
    global sp, sp1
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("850x750")
    screen2.configure(background="gray15")
    Label(screen2, text="LOGIN", bg="gray20",fg="gray75",width="25", height="2",font="Roboto 20 bold").pack(fill=X)
    Label(screen2,text="",bg="gray15").pack()
    Label(screen2,text="Username", bg="gray15", fg="gray60",font='serif 15 italic').pack()
    #Label(screen2,text="",bg="gray15").pack()
    global user_entry1
    global pass_entry1
    global user_verify
    global pass_verify
    user_verify =StringVar()
    pass_verify =StringVar ()
    
    user_entry1=Entry(screen2, text=user_verify, width=25,highlightcolor="yellow",highlightthickness=2,font="arial 15 bold"). pack ()
    Label(screen2,text="",bg="gray15").pack()
    Label(screen2,text="Password", bg="gray15", fg="gray60",font='serif 15 italic').pack()
   # Label(screen2,text="",bg="gray15").pack()
    pass_entry1=Entry(screen2, textvariable=pass_verify, width=25,highlightcolor="yellow",highlightthickness=2,font="arial 15 bold",show="•")
    pass_entry1.pack ()
   
    sp = Button(screen2,text="Show Password ?",fg="gray60",bg="gray15",font="serif 10 italic", width=15, height=1,relief=FLAT, command=lambda:shpass(1))
    sp1 = Button(screen2,text="Hide Password ?",fg="gray60",bg="gray15",font="serif 10 italic", width=15, height=1, command=lambda:shpass(2))
    sp.pack(anchor="n",pady=5)
    sp1.pack(anchor="n",pady=5)
    
    
    fb = Button(screen2,text="Forgot Password ?",fg="orange",bg="gray15",font="serif 12 italic", width=15, height=1, command=forget)
    fb.pack(anchor="n",pady=20)
    fb.bind("<Return>", forget)
    
    Label(screen2,text="\n",bg="gray15").pack()
    
    Button(screen2,text="Login",bg="gray15",fg="gray60",width=15,font="serif 15 bold", command=login_verify).pack()
  #  Label(screen2,text="\n",bg="gray15").pack()
    
    Label(screen2,text="\n",bg="gray15").pack()
    Button(screen2, text="Close",bg="gray15",fg="red", font="Roboto 15 bold",border=2, highlightbackground="red",command=screen2.destroy).pack(anchor="ne",pady=10)

def check(event=''):
    cont_info = cont_val.get()
    password_info = password.get()
    c = chb_val.get()

    x = True
    while x:  
        if (len(password_info)==0):
            put = "Fill the box(s) first."
            statusvar.set(f'{put}\nScreen update after 6 seconds')
            sbar.update()
            time.sleep(3)
            statusvar.set("Ready Now")
            break
        elif (len(password_info)<=8 or len(password_info)>12):
            
            # time.sleep(1)
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            time.sleep(3)
            statusvar.set("Ready Now")
            break
        elif not re.search("[a-z]",password_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            time.sleep(3)
            statusvar.set("Ready Now")
            break
        elif not re.search("[0-9]",password_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            time.sleep(3)
            statusvar.set("Ready Now")
            break
        elif not re.search("[A-Z]",password_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            time.sleep(3)
            statusvar.set("Ready Now")
            break
        elif not re.search("[$#@]",password_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            time.sleep(3)
            statusvar.set("Ready Now")
            break
        elif re.search("\s",password_info):
            put = "Password is not matching with its criteria."
            statusvar.set(f'{put}\nScreen update after 3 seconds')
            sbar.update()
            time.sleep(3)
            statusvar.set("Ready Now")
            break
        
        else:
            # print("Valid Password")
            # Label(screen1, text="Valid Password", font="lucida 15 bold").pack()
            x=False
            # submit()
            if c == 'Yes':
                submit()
            else:
                statusvar.set("Please check the box")
                sbar.update()
                # print("Its not selected")
            break
    
    try:
        int(cont_info)
        y = True
        while y:  
            if (len(cont_info)>10):
                put = 'Number is not greater than 10'
                statusvar.set(f'{put}')
                sbar.update()
                time.sleep(3)
                statusvar.set("Ready Now")
                break
            elif (len(cont_info)==10):
                statusvar.set('Done')
                sbar.update()
                time.sleep(3)
                statusvar.set("Ready Now")
                break
            else:
                statusvar.set('Number not less than 10')
                sbar.update()
                time.sleep(3)
                statusvar.set("Ready Now")
                break
            
    except ValueError:
        statusvar.set('Should be 10-digit numbers only in Contact.\nScreen will update in 6 seconds')
        sbar.update()
        time.sleep(3)
        statusvar.set("Ready Now")

def rshp(args):
    pg = password.get()
    if args == 1:
        rsp.config(text = f'{pg}')
    else:
        rsp.config(text = 'Show Password ?')


def submit ():
    username_info = username.get()
    password_info = password.get()
    cont_info = cont_val.get()
    name_info = name_val.get()
    

    global key
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_-+={}[]:;\'\"|\\?/>.<,12345678901234567891234567890"
    key = 5
    encrypt = ''
    for i in password_info:
        position = alp.find(i)
        newposition = position+5
        encrypt += alp[newposition]
        # print(encrypt)

    f = open(f"{username_info}","w")
    psaver = open(f"{username_info}"+".txt", "w")
    f.write(f"{name_info}\n{cont_info}\n{username_info}")
    psaver.write(f"{encrypt}")
    a = tmsg.showinfo("Success",f"Name: {name_info}\nContact: {cont_info}\nUser-ID: {username_info}\nPassword: {password_info}\n")
    f.close()
    psaver.close()
    
    os.system(f"attrib +h /s /d {username_info}.txt")
    os.system(f"attrib +h /s /d {username_info}")

    name_val.set("")
    cont_val.set("")
    username.set("")
    password.set("")
    screen1.update()
    time.sleep(1)
    screen1.destroy()


def exit_command_of_scr1(event=''):
    screen1.destroy()

def register (event=''):
    global username
    global password
    global name_val
    global cont_val
    global screen1
    global lbl
    global chb_val
    global rsp,rsp1
    chb_val = StringVar()
    name_val = StringVar()
    cont_val = StringVar()
    username = StringVar()
    password = StringVar()
    screen1 = Toplevel(screen)
    screen1.title("Registration")
    screen1.geometry("870x800")
    screen1.minsize(870,800)
    screen1.configure(background="gray15")
    Label(screen1, text="REGISTER", bg="gray20",fg="gray75",width="25", height="2",font="Roboto 20 bold").pack(fill=X)
    Label (screen1,text="",bg="gray15").pack ()
    Label(screen1,text="Name*",bg="gray15",fg='gray60', font="serif 15 italic", underline=0).pack()
    name_entry=Entry(screen1, textvariable=name_val,bg="gray50",border=2,highlightcolor="yellow",fg="gray0",width=40,font="arial 12 bold",justify=CENTER)
    name_entry.pack(padx=5,pady=5)
    Label (screen1, text="",bg="gray15").pack()
    Label(screen1,text="Contact*",bg="gray15",fg='gray60', font="serif 15 italic", underline=3).pack()
    contact_entry=Entry(screen1, textvariable=cont_val,bg="gray50",border=2,highlightcolor="yellow",fg="gray0",width=40,font="arial 12 bold",justify=CENTER)
    contact_entry.pack(padx=10,pady=10)
    lbl = Label (screen1, text="",bg="gray15")
    lbl.pack()
    Label(screen1,text="Username*",bg="gray15",fg='gray60',font="serif 15 italic", underline=3).pack()
    user_entry=Entry(screen1, textvariable=username,bg="gray50",border=2,highlightcolor="yellow",fg="gray0",width=40,font="arial 12 bold",justify=CENTER).pack(padx=10,pady=10)
    Label (screen1, text="",bg="gray15").pack()
    Label(screen1,text="Password*",bg="gray15",fg='gray60',font="serif 15 italic", underline=4).pack()
    password_entry=Entry(screen1, textvariable=password,bg="gray50",border=2,highlightcolor="yellow",fg="gray0",show="•",width=40,font="arial 12 bold",justify=CENTER)
    password_entry.pack(padx=10,pady=10)
    password_entry.bind("<Return>", check)
    rsp = Button(screen1,text="Show Password ?",fg="gray60",bg="gray15",font="serif 10 italic", width=15, height=1,relief=FLAT, command=lambda:rshp(1))
    rsp1 = Button(screen1,text="Hide Password ?",fg="gray60",bg="gray15",font="serif 10 italic", width=15, height=1, command=lambda:rshp(2))
    rsp.pack(anchor="n",pady=5)
    rsp1.pack(anchor="n",pady=5)
    
    Label(screen1,text="Password must contain 8 character's (12+ recommended):\n• Atleast 1-Uppercase\n• Atleast 1-Lowercase\n• Atleast 1-Special Character\nAtleast 1-number\nTo best security.",bg="gray15",fg="gray75", highlightbackground="gray15",highlightthickness=3,font="serif 10 bold").pack()

    chb = Checkbutton(screen1,text="All the above boxes are filled correctly !",variable=chb_val,bg="gray15",fg="black", highlightbackground="gray15",highlightthickness=3,font="serif 15 bold",onvalue='Yes', offvalue='No')
    chb.pack()
    global statusvar, sbar
    statusvar = StringVar()
    statusvar.set("Ready")
    sbar = Label(screen1, textvariable = statusvar, relief = SUNKEN,anchor = "center")
    sbar.pack(side = BOTTOM, fill = X)
    Label(screen1,text="",bg="gray15").pack()
    sbm = Button(screen1,text="Submit",bg="gray15",fg="gray60",font="arial 10 bold",width=15, command=check)
    sbm.pack()
    sbm.bind("<Return>", check)
    
    Label (screen1, text="\n",bg="gray15").pack()
    clb = Button(screen1, text="Close",bg="yellow",fg="red", font="Roboto 10 bold",border=3, highlightbackground="red",command=screen1.destroy)
    clb.pack(anchor="ne")
    clb.bind("<Return>", exit_command_of_scr1)


def main_screen():
    global screen
    global name_val
    screen = Tk()
    screen.configure(bg="black")
    screen.title("HRK LIBRARY MANAGEMENT SYSTEM")
    screen.geometry("850x750")
    head = Label(screen, text="LIBRARY MANAGEMENT", bg="gray20",fg="gray75",width="300", height="2",font="Roboto 20 bold")
    head.pack()
    Label(screen,text="",bg="black").pack()
    rgb=Button(screen, text="Register",bg="black", borderwidth=4,font="serif 15 italic",width="15",height="1",fg="white",command=register)
    rgb.pack(padx=10,pady=10)
    rgb.bind("<Return>", register)
    Label(screen,text="\n",bg="black").pack()
    lgb=Button(screen, text="Login",bg="black", borderwidth=4,font="serif 15 italic",width="15",height="1",highlightbackground="yellow",fg="white", command=login)
    lgb.pack(padx=10,pady=10)
    lgb.bind("<Return>", login)
    
    Label(screen,text="",bg="black").pack()
    
    Label(screen,text="",bg="black").pack()
    ext = Button(screen, text="Exit", bg="black", borderwidth=4,font="serif 15 italic",width=15,height=1,highlightbackground="yellow",fg="white", command=quit)
    ext.pack()
    ext.bind("<Return>", quit)
    Label(screen,text="\n\n\n",bg="black").pack()
    Label(screen,text="NOTE :",bg="black",fg="red", font="ms 15 bold").pack()
    Label(screen,text="This is a library management system. \nIn which students have choice to read books.\n\nIn a new window, click on\n[x] or [close/exit] to close particular window.",bg="black",fg="red", font="ms 15 bold").pack()
    
    screen.mainloop()
    
main_screen()

