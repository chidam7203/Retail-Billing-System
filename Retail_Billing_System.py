from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib


def clear():
    bathsoapEntry.delete(0,END)
    bathsoapEntry.insert(0,0)
    facecreamEntry.delete(0,END)
    facecreamEntry.insert(0,0)
    facewashEntry.delete(0,END)
    facewashEntry.insert(0,0)
    hairsprayEntry.delete(0,END)
    hairsprayEntry.insert(0,0)
    hairgelEntry.delete(0,END)
    hairgelEntry.insert(0,0)
    bodylotionEntry.delete(0,END)
    bodylotionEntry.insert(0,0)

    riceEntry.delete(0,END)
    riceEntry.insert(0,0)
    oilEntry.delete(0,END)
    oilEntry.insert(0,0)
    wheatEntry.delete(0,END)
    wheatEntry.insert(0,0)
    dallEntry.delete(0,END)
    dallEntry.insert(0,0)
    sugarEntry.delete(0,END)
    sugarEntry.insert(0,0)
    teaEntry.delete(0,END)
    teaEntry.insert(0,0)

    maazaEntry.delete(0,END)
    maazaEntry.insert(0,0)
    pepsiEntry.delete(0,END)
    pepsiEntry.insert(0,0)
    spriteEntry.delete(0,END)
    spriteEntry.insert(0,0)
    frootiEntry.delete(0,END)
    frootiEntry.insert(0,0)
    cococolaEntry.delete(0,END)
    cococolaEntry.insert(0,0)
    redbullEntry.delete(0,END)
    redbullEntry.insert(0,0)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    colddrinkstaxEntry.delete(0,END)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    colddrinkspriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)


def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
        except:
            messagebox.showerror('Error','Somthing went wrong,please try again',parent=root1)
        
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        gmailIdLabel=Label(senderFrame,text="sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        gmailIdLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)


        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)

        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,columnspan=2,padx=10,pady=8)

        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,width=42,height=11,relief=SUNKEN)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=14,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)


        


        
        root1.mainloop()





def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')





def search_bill():
    for i in os.listdir('bills/'):
        #if i.split('.')[0] == billnumberEntry.get():
        if ("969.txt")== billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')



#functionality part
    


def save_bill():
    global billnumber
    result=messagebox.askyesno('confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        messagebox.showinfo('success',f'bill number {billnumber} save successfully')
        billnumber=random.randint(500,1000)



billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and colddrinkspriceEntry.get()=='':
        messagebox.showerror('Error','No Product are selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and colddrinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error','No Product are selected')

    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        #textarea.insert(END,'Bill Number'+str(billnumber))
        textarea.insert(END,f'\nBill Number: {billnumber}')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END,f'\nCustomer phone Number: {phoneEntry.get()}')
        textarea.insert(END,'\n==================================================')
        textarea.insert(END,'\nProduct\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n==================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap:\t\t{bathsoapEntry.get()}\t\t\t{soapprice}Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream:\t\t{facecreamEntry.get()}\t\t\t{facecreamprice}Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Wash:\t\t{facewashEntry.get()}\t\t\t{facewashprice}Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nhair Spray:\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice}Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nhair Gel:\t\t{hairgelEntry.get()}\t\t\t{hairgelprice}Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion:\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice}Rs')

        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice:\t\t{riceEntry.get()}\t\t\t{riceprice}Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil:\t\t{oilEntry.get()}\t\t\t{oilprice}Rs')
        if dallEntry.get()!='0':
            textarea.insert(END,f'\nDall:\t\t{dallEntry.get()}\t\t\t{dallprice}Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar:\t\t{sugarEntry.get()}\t\t\t{sugarprice}Rs')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea:\t\t{teaEntry.get()}\t\t\t{teaprice}Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat:\t\t{wheatEntry.get()}\t\t\t{wheatprice}Rs')


        if maazaEntry.get()!='0':
            textarea.insert(END,f'\nMaaza:\t\t{maazaEntry.get()}\t\t\t{maazaprice}Rs')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi:\t\t{pepsiEntry.get()}\t\t\t{pepsiprice}Rs')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite:\t\t{spriteEntry.get()}\t\t\t{spriteprice}Rs')
        if redbullEntry.get()!='0':
            textarea.insert(END,f'\nRed Bull:\t\t{redbullEntry.get()}\t\t\t{redbullprice}Rs')
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti:\t\t{frootiEntry.get()}\t\t\t{frootiprice}Rs')
        if cococolaEntry.get()!='0':
            textarea.insert(END,f'\nCococola:\t\t{cococolaEntry.get()}\t\t\t{cococolaprice}Rs')
        textarea.insert(END,'\n--------------------------------------------------')

        if cosmetictaxEntry!='0.0Rs':
            textarea.insert(END,f'\n Cosmetic Tax:\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry!='0.0Rs':
            textarea.insert(END,f'\n Grocery Tax:\t\t\t\t{grocerytaxEntry.get()}')
        if colddrinkstaxEntry!='0.0Rs':
            textarea.insert(END,f'\n Cold Drinks Tax:\t\t\t\t{colddrinkstaxEntry.get()}')

        textarea.insert(END,f'\n\nTotal bill: \t\t\t{totalbill} Rs')
        textarea.insert(END,'\n--------------------------------------------------')
    
        save_bill()
        


    
    


    
def total():
    #cosmeticprice
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,dallprice,sugarprice,teaprice,wheatprice
    global maazaprice,pepsiprice,spriteprice,redbullprice,frootiprice,cococolaprice
    global totalbill
    
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,str(totalcosmeticprice)+' Rs')
    #cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmetictax)+' Rs')


    #grocery price
    riceprice=int(riceEntry.get())*30
    oilprice=int(oilEntry.get())*120
    dallprice=int(dallEntry.get())*100
    sugarprice=int(sugarEntry.get())*50
    teaprice=int(teaEntry.get())*140
    wheatprice=int(wheatEntry.get())*80

    totalgroceryprice=riceprice+oilprice+dallprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+' Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+' Rs')



    #cold drinks price
    maazaprice=int(maazaEntry.get())*50
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spriteEntry.get())*30
    redbullprice=int(redbullEntry.get())*20
    frootiprice=int(frootiEntry.get())*45
    cococolaprice=int(cococolaEntry.get())*90

    totalcolddrinksprice=maazaprice+pepsiprice+spriteprice+redbullprice+frootiprice+cococolaprice
    colddrinkspriceEntry.delete(0,END)
    colddrinkspriceEntry.insert(0,str(totalcolddrinksprice)+' Rs')
    colddrinkstax=totalcolddrinksprice*0.05
    colddrinkstaxEntry.delete(0,END)
    colddrinkstaxEntry.insert(0,str(colddrinkstax)+' Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totalcolddrinksprice+cosmetictax+grocerytax+colddrinkstax



    
    

    




    

    
    
    

















#GUI part
root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('E:/py_tkinter_project/Retail_Billing_System/icon.ico')



headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),
                   bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)




customer_details_frame=LabelFrame(root,text='customer details',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)


nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',
                fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
nameEntry.grid(row=0,column=1,padx=8)


phoneLabel=Label(customer_details_frame,text='phone Number',font=('times new roman',15,'bold'),bg='gray20',
                fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
phoneEntry.grid(row=0,column=3,padx=8)


billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',
                fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=8,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)




#productFrame


productFrame=Frame(root)
productFrame.pack()




cosmeticsFrame=LabelFrame(productFrame,text='cusmetics',font=('times new roman',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticsFrame,font=('times new romen',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=('times new romen',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticsFrame,font=('times new romen',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticsFrame,font=('times new romen',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticsFrame,font=('times new romen',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new romen',15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodylotionEntry=Entry(cosmeticsFrame,font=('times new romen',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)



#groceryFrame


groceryFrame=LabelFrame(productFrame,text='Grocery',font=('times new roman',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceryFrame,font=('times new romen',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryFrame,font=('times new romen',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

dallLabel=Label(groceryFrame,text='Dall',font=('times new romen',15,'bold'),bg='gray20',fg='white')
dallLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
dallEntry=Entry(groceryFrame,font=('times new romen',15,'bold'),width=10,bd=5)
dallEntry.grid(row=2,column=1,pady=9,padx=10)
dallEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new romen',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(groceryFrame,font=('times new romen',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new romen',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(groceryFrame,font=('times new romen',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new romen',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry=Entry(groceryFrame,font=('times new romen',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)



#drinksFrame


drinksFrame=LabelFrame(productFrame,text='Cold Drinks',font=('times new romen',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)

maazaLabel=Label(drinksFrame,text='Maaza',font=('times new romen',15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry=Entry(drinksFrame,font=('times new romen',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new romen',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(drinksFrame,font=('times new romen',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new romen',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(drinksFrame,font=('times new romen',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

redbullLabel=Label(drinksFrame,text='Red Bull',font=('times new romen',15,'bold'),bg='gray20',fg='white')
redbullLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
redbullEntry=Entry(drinksFrame,font=('times new romen',15,'bold'),width=10,bd=5)
redbullEntry.grid(row=3,column=1,pady=9,padx=10)
redbullEntry.insert(0,0)

frootiLabel=Label(drinksFrame,text='Frooti',font=('times new romen',15,'bold'),bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry=Entry(drinksFrame,font=('times new romen',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLabel=Label(drinksFrame,text='Coco Cola',font=('times new romen',15,'bold'),bg='gray20',fg='white')
cococolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
cococolaEntry=Entry(drinksFrame,font=('times new romen',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)



#billFrame


billFrame=Frame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=10)
#Label
billareaLabel=Label(billFrame,text='Bill Area',font=('times new romen',15,'bold'),bd=8,relief=GROOVE)
billareaLabel.pack(fill=X)

#scrollbar
scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

#textarea
textarea=Text(billFrame,height=18,width=50,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)



#billmenuFrame


billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new romen',15,'bold'),
                          fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

#price

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new romen',15,'bold'),bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=('times new romen',13,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new romen',15,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('times new romen',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

colddrinkspriceLabel=Label(billmenuFrame,text='Cold Drinks Price',font=('times new romen',15,'bold'),bg='gray20',fg='white')
colddrinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
colddrinkspriceEntry=Entry(billmenuFrame,font=('times new romen',13,'bold'),width=10,bd=5)
colddrinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)



#tax


cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new romen',15,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=('times new romen',13,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)


grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new romen',15,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('times new romen',13,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

colddrinkstaxLabel=Label(billmenuFrame,text='Cold Drinks Tax',font=('times new romen',15,'bold'),bg='gray20',fg='white')
colddrinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
colddrinkstaxEntry=Entry(billmenuFrame,font=('times new romen',13,'bold'),width=10,bd=5)
colddrinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)



#Buttons

ButtonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
ButtonFrame.grid(row=0,column=4,rowspan=3)

#total

totalButton=Button(ButtonFrame,text='Total',font=('arial',16,'bold'),bg='red',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

#bill

billButton=Button(ButtonFrame,text='Bill',font=('arial',16,'bold'),bg='red',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

#email

emailButton=Button(ButtonFrame,text='Email',font=('arial',16,'bold'),bg='red',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

#print

printButton=Button(ButtonFrame,text='Print',font=('arial',16,'bold'),bg='red',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

#clear

clearButton=Button(ButtonFrame,text='Clear',font=('arial',16,'bold'),bg='red',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

























root.mainloop()
