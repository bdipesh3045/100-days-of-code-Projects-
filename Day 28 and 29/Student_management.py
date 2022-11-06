from prettytable import PrettyTable
import os
table=PrettyTable()
def add(data):
    a = input(f"Enter {data}")
    return a
class student:
    def __init__(self,fname,lname,roll):
        self.fname=fname
        self.lname=lname
        self.roll=roll
    # To add a student
    def addd(self,fname,lname,roll):
        ob =student(fname,lname,roll)
        ls.append(ob)
    # To print student
    def display(self,ob):
        table.clear()
        table.field_names=["fname","lname","roll"]
        li=[str(ob.fname),str(ob.lname),str(ob.roll)]
        table.add_row(li)
        print(table)
    # For searching:
    def search(self,rn):
        for i in range(ls.__len__()):
            if(ls[i].roll==rn):
                return i
    def display_all(self):
        
        table.clear()
        arr=["fname","lname","roll"]
        data=[]
        for z in range(3):
            item=arr[z]
            data=[]
            for i in range(ls.__len__()):
                if(z==0):
                    data.append((ls[i].fname))
                elif(z==1):
                    data.append((ls[i].lname))
                else:
                    data.append((ls[i].roll))
            table.add_column(item,data)
        print(table) 
    # For deleting
    def delete(self,rn):
        i = obj.search(rn)
        del ls[i]
    # for updating
    def update(self,rn):
        i = obj.search(rn)
        del(ls[i])
        ob =student(add("Fname"),add("Lname"),add("Lname"))
        ls.insert(i,ob)

ls=[]
obj= student("","",0)
print("Hello")
enter = True

while enter:
    print("""1 is for adding the data\n\n2 is for deleting particular data\n\n3 is for showing all data\n\n4 is for searching the data\n\n5 is for updating""")
    a = int(add("command:"))
    # os.system('clear')
    if (a==1):
        obj.addd(add("FName:"),add("Lname:"),int(add("Roll:")))
    elif (a==2):
        obj.delete(int(add("Roll:")))
    elif a==3:
        obj.display_all()
    elif a==4:
        p=int(input("Enter the roll number:"))
        l=int(obj.search(p))
        obj.display(ls[l])
    elif a==5:
        obj.update(add("Roll:"))
    
    else:
        obj.delete(add("Roll:"))


