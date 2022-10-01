from tkinter import *
from tkinter import ttk
#pyinstaller --onefile -w filename

class Prepare_list:
    """universal class for list"""
    def __init__(self, prsn_name, pr_list=[],holiday_days=5, gen=False):
        """Constructor"""
        self.name = prsn_name
        self.list = pr_list
        self.days=holiday_days
        self.generic = gen

dina_list = Prepare_list("Dina", ['dresses','Shirts','Jeans','tights','underpants','bra','petticoats','Medicines','Socks','Makeup','careshoes','to','change','scarf','clothes','hat'])
abigail_list = Prepare_list("Abigail", ['Shirts','Jeans','tights','dresses','underpants','Socks','thermal socks','Ointment for tusks','Writing Tools','sweatshirt','determines','shoes to change','clothes'])
general_list = Prepare_list("General", ['Loads','Money','Passports','Camera','paracetamol','Opthalgin','toothpaste','Toothbrushes','typecast','Mobile Charger','Sugar, tea, coffee','Headphones -2','hair brush','Get travel insurance','A large bag for the supermarket','Folding bag'])
vova_winter_list = Prepare_list("Vova winter", ['Sweater','Shirts - 5','Underwear-5','Socks-4','Thermal socks-1','Jerseys-3','Gloves','Scarf','Hat','Shoes to change','Sunglasses','Slippers','Swim clothes'])
vova_summer_list = Prepare_list("Vova summer", ['Shirts - 5','Underwear-5','Socks-4','Jerseys-3','Shoes to change','Sunglasses','Swim clothes'])


#tkinter part
window = Tk()
window.configure(padx=20,pady=20)
window.title('Prepare list')

ttk.Style().configure("TCombobox",font=('Arial 15'),foreground="red" ,fieldbackground="black",selectbackground="gold",lightcolor="lime")

Label(window,font=("Arial", 15),text = 'Prepare list:').pack()

item_list = Listbox(window,font=("Arial", 15))



def list_build(obj):
    item_list.delete(0,'end')
    for i in obj.list:
        item_list.insert('end', i.capitalize())

def choiceFunc(event):
    if person_list.get() == vova_winter_list.name:
        list_build(vova_winter_list)
    elif person_list.get() == vova_summer_list.name:
        list_build(vova_summer_list)
    elif person_list.get() == dina_list.name:
        list_build(dina_list)
    elif person_list.get() == abigail_list.name:
        list_build(abigail_list)
    elif person_list.get() == general_list.name:
        list_build(general_list)

def itemChoice(event):
    if '\u0336' in item_list.selection_get():
        ready=''.join(item_list.selection_get().replace('\u0336',''))
    else: 
        ready='\u0336'.join(item_list.selection_get()) + '\u0336'
    
    item_list.delete(item_list.curselection())
    item_list.insert('end',ready)
    
    
        
person_list = ttk.Combobox(window,values=[vova_winter_list.name,vova_summer_list.name, dina_list.name,abigail_list.name,general_list.name],state="readonly")
person_list.bind("<<ComboboxSelected>>", choiceFunc)
item_list.bind('<<ListboxSelect>>', itemChoice)
person_list.pack()
item_list.pack()
mainloop()



