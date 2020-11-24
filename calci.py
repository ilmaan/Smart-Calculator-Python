from tkinter import *

def add(a,b):
    return a+b


def sub(a,b):
    return a-b
    

def mul(a,b):
    return a*b


def div(a,b):
    return a/b
            

def mod(a,b):
    return a%b


def lcm(a,b):
    L = a if a>b else b 
    while L <- a*b==0 and L%b == 0:
        return L
    L+=1


def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H==0 and b%H==0:
            return H
        H-=1     
        
def textextractor(text):
    l =[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass    
    return l

def calci():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in oper.keys():
            try:
                l = textextractor(text)
                r = oper[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Please Enter some logic you FOOL!!')
            finally:
                break
        elif word.upper() not in oper.keys():
            list.delete(0,END)
            list.insert(END,'Please Enter some logic you FOOL!!')        



oper = {'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
        'SUB':sub,'DIFFRENCE':sub,'SUBTRACT':sub,'MINUS':sub,
        'MULTIPLY':mul,'INTO':mul,'MUL':mul,'PRODUCT':mul,
         'DIVIDE':div,'BY':div,'DIV':div,
         'MOD':mod,'REMAINDER':mod,'MODULUS':mod,'LCM':lcm,'HCF':hcf}        

win = Tk()
win.geometry('500x300')
win.title('Zoravars Artificial Intelligence Calculator')
win.configure(bg='darkred')

l1 = Label(win , text = 'Hey i am Zoravar A-I Calculator', width=40 , padx=2 , bg='black',foreground='white')
l1.place(relx=0.5,rely=0.08, anchor=CENTER)

l2 = Label(win , text = 'Designed By ILMAAN ZIA ', padx=2 , bg='black',foreground='white')
l2.place(relx=0.5,rely=0.18, anchor=CENTER)

l2 = Label(win , text = 'How Can i Assist You Sir', padx=2 , bg='black',foreground='white')
l2.place(relx=0.5,rely=0.38, anchor=CENTER)

textin = StringVar()
e1 =Entry(win, width=30 ,textvariable = textin)
e1.place(relx=0.5,rely=0.5, anchor=CENTER)

b1 = Button(win,text='Are You Done Sir' , command= calci )
b1.place(relx=0.5,rely=0.59, anchor=CENTER)

list = Listbox(win,width=20, height=3)
list.place(relx=0.5,rely=0.75, anchor=CENTER)

l3 = Label(win , text = 'check for the correct spellings for the operations ', width=40 , padx=1 , bg='black',foreground='white')
l3.place(relx=0.5,rely=0.95, anchor=CENTER)

win.mainloop()


