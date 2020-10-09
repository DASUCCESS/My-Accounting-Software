import tkinter
from tkinter import *
import time
import datetime
import random
import tkinter.messagebox
from tkinter import Frame, Label, Tk

root =Tk()
root.geometry("1350x700+0+0")
root.title("DASUCCESS SYSTEM SOFTWARE")
root.configure(background='white')

################### The widget here ######################
Scrollbar = Scrollbar(root)
Scrollbar.pack(side=RIGHT, fill=Y,)

Tops = Frame(root,bg='white',bd=10,pady=5,relief=RIDGE)
Tops.pack(side=TOP)
MenuFrame = Frame(root,bg='green',bd=5, relief=RIDGE)
MenuFrame.pack(side=TOP)
NameFrame=Frame(MenuFrame,bg='green',bd=4)
NameFrame.pack(side=TOP)
DrinksFrame=Frame(MenuFrame,bg='green',bd=4, relief=RIDGE)
DrinksFrame.pack(side=LEFT)
FoodFrame=Frame(MenuFrame,bg='green',bd=4,relief=RIDGE)
FoodFrame.pack(side=LEFT)
AFrame=Frame(MenuFrame,bg='green',bd=4,relief=RIDGE)
AFrame.pack(side=LEFT)
BFrame=Frame(MenuFrame,bg='green',bd=4,relief=RIDGE)
BFrame.pack(side=LEFT)
Buttons=Frame(root,bg='green',bd=4)
Buttons.pack(side=LEFT)
ButtonsFrame=Frame(Buttons,bg='green',bd=4)
ButtonsFrame.pack(side=TOP)
ButtonsFrame2=Frame(Buttons,bg='green',bd=4)
ButtonsFrame2.pack(side=TOP)
Receipt = Frame(root,bg='green',bd=10, height=200,relief=SUNKEN)
Receipt.pack(side=TOP)
ReceiptFrame=Frame(Receipt,bg='green',bd=4,relief=RIDGE)
ReceiptFrame.pack(side=TOP)


################################ Variable for Checkbox ########################################
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)

### Name Variable
Firtsnamestring = StringVar()
Middlenamestring = StringVar()
Surnamenamestring = StringVar()
costdrinkstring = StringVar()
costfoodstring = StringVar()
### Drinks Variable
PepsiString = StringVar()
CocaColaString = StringVar()
MojitoString = StringVar()
E_CappuccinoString = StringVar()
FantaString = StringVar()
VijumilkString = StringVar()
ChilledCoffeeString = StringVar()
VijuMilkString =  StringVar()

### Food Variable
SpagghetiString = StringVar()
RiceString = StringVar()
BeansString = StringVar()
ChickenString = StringVar()
FishString = StringVar()
MeatString = StringVar()
SemoVitaString = StringVar()

######### Final cost of drinks and foods
finalcostofdrinks = StringVar()
finalcostoffoods = StringVar()
finaloverallcost= StringVar()
overallcost = StringVar()

finalcostofdrinks.set('')
finalcostoffoods.set('')
finaloverallcost.set('')
overallcost.set('')

##############  set the var to zero's ##################
PepsiString.set(0)
CocaColaString.set(0)
MojitoString.set(0)
E_CappuccinoString.set(0)
FantaString.set(0)
VijumilkString.set(0)
ChilledCoffeeString.set(0)
SpagghetiString.set(0)
RiceString.set(0)
BeansString.set(0)
ChickenString.set(0)
FishString.set(0)
MeatString.set(0)
SemoVitaString.set(0)
############################################## FUNCTIONS################################################
def Exit():
    Exit=tkinter.messagebox.askyesno("Exit DASUCCESS System","Confirm if you want to exit")
    if Exit > 0:
        root.destroy()
    return
def cmdpepsi():
    if(var2.get() == 1):
        txtPepsi.configure(state = NORMAL)
        txtPepsi.focus()
        txtPepsi.delete('0',END)
        PepsiString.set("")
    elif(var1.get() == 0):
        txtPepsi.configure(state = DISABLED)
        PepsiString.set("0")
def cmdcocacola():
    if(var3.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var3.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        CocaColaString.set("0")
def cmdmojito():
    if(var4.get() == 1):
        txtMojito.configure(state = NORMAL)
        txtMojito.delete('0',END)
        txtMojito.focus()
    elif(var4.get() == 0):
        txtMojito.configure(state = DISABLED)
        MojitoString.set("0")
def cmdcappuccino():
    if(var5.get() == 1):
        txtCappuccino.configure(state = NORMAL)
        txtCappuccino.delete('0',END)
        txtCappuccino.focus()
    elif(var5.get() == 0):
        txtCappuccino.configure(state = DISABLED)
        E_CappuccinoString.set("0")
def cmdfanta():
    if(var6.get() == 1):
        txtFanta.configure(state = NORMAL)
        txtFanta.delete('0',END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state = DISABLED)
        FantaString.set("0")
def cmdCoffee():
    if(var7.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        txtColdCoffee.delete('0',END)
        txtColdCoffee.focus()
    elif(var7.get() == 0):
        txtColdCoffee.configure(state = DISABLED)
        ChilledCoffeeString.set("0")
# def cmdvijumilk():
#     if(var8.get() == 1):
#         txtVijuMilk.configure(state = NORMAL)
#         txtVijuMilk.delete('0',END)
#         txtVijuMilk.focus()
#     elif(var8.get() == 0):
#         txtVijuMilk.configure(state = DISABLED)
#         VijuMilkString.set("0")

############################## FUNCTION FOR FOODS ############################################
def cmdspagghetti():
    if(var9.get() == 1):
        txtSpagghetti.configure(state = NORMAL)
        txtSpagghetti.delete('0',END)
        txtSpagghetti.focus()
    elif(var9.get() == 0):
        txtSpagghetti.configure(state = DISABLED)
        SpagghetiString.set("0")
def cmdrice():
    if(var10.get() == 1):
        txtRice.configure(state = NORMAL)
        txtRice.delete('0',END)
        txtRice.focus()
    elif(var10.get() == 0):
        txtRice.configure(state = DISABLED)
        RiceString.set("0")
def cmdbeans():
    if(var11.get() == 1):
        txtBeans.configure(state = NORMAL)
        txtBeans.delete('0',END)
        txtBeans.focus()
    elif(var11.get() == 0):
        txtBeans.configure(state = DISABLED)
        BeansString.set("0")
def cmdchicken():
    if(var12.get() == 1):
        txtChicken.configure(state = NORMAL)
        txtChicken.delete('0',END)
        txtChicken.focus()
    elif(var12.get() == 0):
        txtChicken.configure(state = DISABLED)
        ChickenString.set("0")
def cmdfish():
    if(var13.get() == 1):
        txtFish.configure(state = NORMAL)
        txtFish.delete('0',END)
        txtFish.focus()
    elif(var13.get() == 0):
        txtFish.configure(state = DISABLED)
        FishString.set("0")
def cmdmeat():
    if(var14.get() == 1):
        txtMeat.configure(state = NORMAL)
        txtMeat.delete('0',END)
        txtMeat.focus()
    elif(var14.get() == 0):
        txtMeat.configure(state = DISABLED)
        MeatString.set("0")
def cmdSemoVita():
    if(var14.get() == 1):
        txtSemoVita.configure(state = NORMAL)
        txtSemoVita.delete('0',END)
        txtSemoVita.focus()
    elif(var14.get() == 0):
        txtSemoVita.configure(state = DISABLED)
        SemoVitaString.set("0")
     
def timer():
    mydate = time.strftime('%d/%m/%y');
    return mydate
######################## RESET BUTTON ################
def reset():
    # SubTotal.set("")
    # TotalCost.set("")
    finalcostofdrinks.set("")
    finaloverallcost.set('')
    finalcostoffoods.set("")
    # txtReceipt.delete("1.0",END)

    Firtsnamestring.set('')
    Middlenamestring.set('')
    Surnamenamestring.set('')
    PepsiString.set("0")
    CocaColaString.set("0")
    MojitoString.set("0")
    E_CappuccinoString.set("0")
    FantaString.set("0")
    ChilledCoffeeString.set("0")

    SpagghetiString.set("0")
    RiceString.set("0")
    BeansString.set("0")
    ChickenString.set("0")
    FishString.set("0")
    MeatString.set("0")
    SemoVitaString.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtPepsi.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtMojito.configure(state=DISABLED)
    txtCappuccino.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtSpagghetti.configure(state=DISABLED)
    txtRice.configure(state=DISABLED)
    txtBeans.configure(state=DISABLED)
    txtChicken.configure(state=DISABLED)
    txtFish.configure(state=DISABLED)
    txtMeat.configure(state=DISABLED)
    txtSemoVita.configure(state=DISABLED)
    

############################## FUNCTION FOR COST ############################################
def allcost():
    Fname = Firtsnamestring.get()
    Mname = Middlenamestring.get()
    Lname = Surnamenamestring.get()
    ### Drinks Variable
    product1 = float(PepsiString.get()) 
    product2 = float(CocaColaString.get()) 
    product3 = float(MojitoString.get()) 
    product4 = float(E_CappuccinoString.get()) 
    product5 = float(FantaString.get()) 
    product6 = float(VijumilkString.get()) 
    product7 = float(ChilledCoffeeString.get())
    # product8 = float(VijuMilkString.get()) 
    ### Food Variable
    product9 = float(SpagghetiString.get()) 
    product10 = float(RiceString.get()) 
    product11 = float(BeansString.get())
    product12 = float(ChickenString.get()) 
    product13 = float(FishString.get())
    product14 = float(MeatString.get()) 
    product15 = float(SemoVitaString.get())
    ############ cost for drinks ###########
    mydrinks = (product1 * 100) + (product2 * 100) + (product3 * 100) + (product4 * 100) + (product5 * 100) + (product6 * 100) + (product7 * 100)
    myfoods =  (product9 * 300) + (product10 * 500) + (product11 * 300) + (product12 * 1000) + (product13 * 400) + (product13 * 500) + (product14 * 400) + (product15 * 400)
    totalcostdrinks= 'Ngn', str('%.2f'%(mydrinks))
    totalcostfoods = 'Ngn', str('%.2f'%(myfoods))
    overallcost = 'Ngn', str('%.2f'%(mydrinks + myfoods))
    
    finalcostofdrinks.set(totalcostdrinks)
    finalcostoffoods.set(totalcostfoods)
    finaloverallcost.set(overallcost)

################### The widget Label ################################
lblTitle=Label(Tops,font=('arial black',20,'bold'), width=70, text='ACCOUNTING SYSTEM SOFTWARE\t\t\t\t Date:'+timer(),bd=15,bg='green',
                fg='cornsilk',justify=LEFT)
lblTitle.grid(row=0)

############################################## Information of customer################################################
###################### & Drinks ####################################################################
Fullname=Label(NameFrame,font=('arial',14,'bold'),text='Full Name:',padx='4', pady='4', bg='green',bd=7,
                fg='black',)
Fullname.grid(row=0,sticky=W)
Middlename=Label(NameFrame,font=('arial',14,'bold'),text='Middle Name:',bg='green',bd=7,
                fg='black',)
Middlename.grid(row=1,column=0,sticky=W)
Surname=Label(NameFrame,font=('arial',14,'bold'),text='Surname:',bg='green',bd=7,
                fg='black',)
Surname.grid(row=2,column=0,sticky=W)
############################################## Name Entry###############################################################

FNEntry=Entry(NameFrame,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,textvariable=Firtsnamestring)
FNEntry.grid(row=0,column=1)

MNEntry=Entry(NameFrame,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2, textvariable=Middlenamestring)
MNEntry.grid(row=1,column=1)

SNEntry=Entry(NameFrame,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2, textvariable=Surnamenamestring)
SNEntry.grid(row=2,column=1)
#######################################  COST OF ALL PRODUCT  ########################################################
CostDrinks=Label(NameFrame,font=('arial',14,'bold'),text='TOTAL COST(DRINKS):',bg='green',bd=7,
                fg='white', padx=20,)
CostDrinks.grid(row=0,column=3,sticky=W)
CostDrinkEntry=Entry(NameFrame,bg='white',bd=7,font=('arial',14,'bold'),width=15, 
                     textvariable=finalcostofdrinks)
CostDrinkEntry.grid(row=0,column=4)
CostFood=Label(NameFrame,font=('arial',14,'bold'),text='TOTAL COST(FOODS):',bg='green',bd=7,
                fg='white',padx=20)
CostFood.grid(row=1,column=3,sticky=W)
CostFoodEntry=Entry(NameFrame,bg='white',bd=7,font=('arial',14,'bold'),
                        width=15, textvariable=finalcostoffoods)
CostFoodEntry.grid(row=1,column=4)
overalllabel=Label(NameFrame,font=('arial',14,'bold'),text='TOTAL COST(OVERALL):',bg='green',bd=7,
                fg='white',padx=20)
overalllabel.grid(row=2,column=3,sticky=W)
OverallEntry=Entry(NameFrame,bg='white',bd=7,font=('arial',14,'bold'),
                        width=15, textvariable=finaloverallcost)
OverallEntry.grid(row=2, column=4)


######## customer drinks #########
headerDrinks=Label(DrinksFrame,font=('arial black',10,'bold'), width=35, text='CHOOSE DRINKS OF YOUR CHOICE HERE',bd=10,bg='white',
                fg='green', justify=LEFT)
headerDrinks.grid(row=0)
Pepsi=Checkbutton(DrinksFrame,text='Pepsi',variable=var2,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdpepsi).grid(row=3,sticky=W)
Cocacola=Checkbutton(DrinksFrame,text='Cocacola',variable=var3,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdcocacola).grid(row=4,sticky=W)
Mojito=Checkbutton(DrinksFrame,text='Mojito',variable=var4,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green',command=cmdmojito).grid(row=5,sticky=W)
Cappuccino=Checkbutton(DrinksFrame,text='Capucino',variable=var5,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdcappuccino).grid(row=6,sticky=W)
Fanta=Checkbutton(DrinksFrame,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdfanta).grid(row=7,sticky=W)
ChilledCoffee=Checkbutton(DrinksFrame,text='Coffee',variable=var7,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green',command=cmdCoffee).grid(row=8,sticky=W)
# Vijumilk=Checkbutton(DrinksFrame,text='VijuMilk',variable=var8,onvalue=1,offvalue=0,font=('arial',15,'bold'),
#                     fg='white',bg='green',command=cmdvijumilk).grid(row=9,sticky=W)

############################################## Name Entry For Drinks ###############################################################

txtPepsi = Entry(DrinksFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=PepsiString)
txtPepsi.grid(row=3,column=0)

txtCocaCola = Entry(DrinksFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=CocaColaString)
txtCocaCola.grid(row=4,column=0)

txtMojito= Entry(DrinksFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=MojitoString)
txtMojito.grid(row=5,column=0)

txtCappuccino = Entry(DrinksFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=E_CappuccinoString)
txtCappuccino.grid(row=6,column=0)

txtFanta = Entry(DrinksFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=FantaString)
txtFanta.grid(row=7,column=0)

txtColdCoffee = Entry(DrinksFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=ChilledCoffeeString,)
txtColdCoffee.grid(row=8,column=0)

# txtVijuMilk = Entry(DrinksFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
#                         ,textvariable=VijuMilkString,)
# txtVijuMilk.grid(row=9,column=0)

################################## Customer food ####################################

headerFood=Label(FoodFrame,font=('arial black',10,'bold'), width=35, text='CHOOSE FOOOD OF YOUR CHOICE HERE',bd=10,bg='white',
                fg='green', justify=LEFT)
headerFood.grid(row=0)
Spagghetti=Checkbutton(FoodFrame,text='Spagghetti',variable=var9,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green',command=cmdspagghetti).grid(row=1,sticky=W)
Rice=Checkbutton(FoodFrame,text='Rice',variable=var10,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdrice).grid(row=2,sticky=W)
Beans=Checkbutton(FoodFrame,text='Beans',variable=var11,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdbeans).grid(row=3,sticky=W)
Chicken=Checkbutton(FoodFrame,text='Chicken',variable=var12,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdchicken).grid(row=4,sticky=W)
Fish=Checkbutton(FoodFrame,text='Fish',variable=var13,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command = cmdfish).grid(row=5,sticky=W)
Meat=Checkbutton(FoodFrame,text='Meat',variable=var14,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command= cmdmeat).grid(row=6,sticky=W)
SemoVita=Checkbutton(FoodFrame,text='SemoVita',variable=var15,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green', command=cmdSemoVita).grid(row=7,sticky=W)

############################################## Name Entry For Foods ###############################################################

txtSpagghetti = Entry(FoodFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=SpagghetiString)
txtSpagghetti.grid(row=1,column=0)

txtRice= Entry(FoodFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=RiceString)
txtRice.grid(row=2,column=0)

txtBeans= Entry(FoodFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=BeansString)
txtBeans.grid(row=3,column=0)

txtChicken = Entry(FoodFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=ChickenString)
txtChicken.grid(row=4,column=0)

txtFish = Entry(FoodFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=FishString)
txtFish.grid(row=5,column=0)

txtMeat = Entry(FoodFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=MeatString)
txtMeat.grid(row=6,column=0)

txtSemoVita = Entry(FoodFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=SemoVitaString)
txtSemoVita.grid(row=7,column=0)

################################## AFRAME Customer food ####################################

headerFood=Label(AFrame,font=('arial black',10,'bold'), width=35, text='CHOOSE FOOOD OF YOUR CHOICE HERE',bd=10,bg='white',
                fg='green', justify=LEFT)
headerFood.grid(row=0)
Spagghetti=Checkbutton(AFrame,text='Spagghetti',variable=var8,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=1,sticky=W)
Rice=Checkbutton(AFrame,text='Rice',variable=var9,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=2,sticky=W)
Beans=Checkbutton(AFrame,text='Beans',variable=var10,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=3,sticky=W)
Chicken=Checkbutton(AFrame,text='Chicken',variable=var11,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=4,sticky=W)
Fish=Checkbutton(AFrame,text='Fish',variable=var12,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=5,sticky=W)
Meat=Checkbutton(AFrame,text='Meat',variable=var13,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=6,sticky=W)
SemoVita=Checkbutton(AFrame,text='SemoVita',variable=var14,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=7,sticky=W)

############################################## Name Entry For Foods ###############################################################

txtSpagghetti = Entry(AFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=SpagghetiString)
txtSpagghetti.grid(row=1,column=0)

txtRice= Entry(AFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=RiceString)
txtRice.grid(row=2,column=0)

txtBeans= Entry(AFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=BeansString)
txtBeans.grid(row=3,column=0)

txtChicken = Entry(AFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=ChickenString)
txtChicken.grid(row=4,column=0)

txtFish = Entry(AFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=FishString)
txtFish.grid(row=5,column=0)

txtMeat = Entry(AFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=MeatString)
txtMeat.grid(row=6,column=0)

txtSemoVita = Entry(AFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=SemoVitaString)
txtSemoVita.grid(row=7,column=0)

################################## BFRAME Customer food ####################################

headerFood=Label(BFrame,font=('arial black',10,'bold'), width=35, text='CHOOSE MORE HERE',bd=10,bg='white',
                fg='green', justify=RIGHT)
headerFood.grid(row=0)
Spagghetti=Checkbutton(BFrame,text='Spagghetti',variable=var8,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=1,sticky=W)
Rice=Checkbutton(BFrame,text='Rice',variable=var9,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=2,sticky=W)
Beans=Checkbutton(BFrame,text='Beans',variable=var10,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=3,sticky=W)
Chicken=Checkbutton(BFrame,text='Chicken',variable=var11,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=4,sticky=W)
Fish=Checkbutton(BFrame,text='Fish',variable=var12,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=5,sticky=W)
Meat=Checkbutton(BFrame,text='Meat',variable=var13,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=6,sticky=W)
SemoVita=Checkbutton(BFrame,text='SemoVita',variable=var14,onvalue=1,offvalue=0,font=('arial',15,'bold'),
                    fg='white',bg='green').grid(row=7,sticky=W)

############################################## Name Entry For Foods ###############################################################

txtSpagghetti = Entry(BFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=SpagghetiString)
txtSpagghetti.grid(row=1,column=0)

txtRice= Entry(BFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=RiceString)
txtRice.grid(row=2,column=0)

txtBeans= Entry(BFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=BeansString)
txtBeans.grid(row=3,column=0)

txtChicken = Entry(BFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=ChickenString)
txtChicken.grid(row=4,column=0)

txtFish = Entry(BFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=FishString)
txtFish.grid(row=5,column=0)

txtMeat = Entry(BFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=MeatString)
txtMeat.grid(row=6,column=0)

txtSemoVita = Entry(BFrame,font=('arial',16,'bold'),bd=4,width=4,justify=LEFT,state=DISABLED
                        ,textvariable=SemoVitaString)
txtSemoVita.grid(row=7,column=0)

########################################### BUTTONS ################################################################################
btnTotal=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=4,text='Total',
                        bg='green', command= allcost).grid(row=0,column=0)
btnReceipt=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='green').grid(row=0,column=1)
btnReset=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='green', command=reset).grid(row=0,column=2)
btnSearch=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=4,text='Search',
                        bg='green').grid(row=0,column=3)
btnUpdate=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=14,text='Display Info',
                        bg='green').grid(row=0,column=4)
btnDelete=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=4,text='Delete',
                        bg='green').grid(row=1,column=1)
btnDisplayInfo=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=4,text='Add Info',
                        bg='green').grid(row=1,column=2)
btnExit=Button(ButtonsFrame,padx=16,pady=1,bd=7,fg='white',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='green', command=Exit).grid(row=1,column=3)

############################  call of action for the buttons ########################################################
databaseTitle=Label(ButtonsFrame2,font=('arial black',10,'bold'), width=70, text='YOU CAN UPDATE INFORMATION OF CUSTOMERS, \n SAVE, FIND TOTAL COST, RECEIPT AND QUIT THE SYSTEM \nFROM THIS SECTION, ',bd=10,bg='green',
                fg='cornsilk')
databaseTitle.grid(row=0)
databaseTitle=Text(ReceiptFrame,font=('arial black',10,'bold'), width=70,bd=10,bg='white',
                fg='cornsilk')
databaseTitle.grid(row=0)

















root.mainloop()