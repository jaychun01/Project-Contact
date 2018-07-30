import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
class Contact:
    def __init__(self, name, pnum, email, addr):
        self.name=name
        self.pnum=pnum
        self.email=email
        self.addr=addr
    def print_info(self):
        print("Name: ",self.name)
        print("Phone num: ",self.pnum)
        print("Email: ",self.email)
        print("Address: ",self.addr)

def set_contact(plist):
    name=input("Name: ")
    pnum=input("Phone number: ")
    email=input("Email: ")
    addr=input("Address: ")
    person= Contact(name, pnum, email, addr)
    return person

def print_contact(plist, fname):
    for p in plist:
        if p.name == fname:
            p.print_info()
            return
    print("We do not have", fname,"in our database")

def delete_contact(plist, dname):
    for i, person in enumerate(plist):
        if person.name == dname:
            del plist[i]
            return
    print("We do not have", dname,"in our database")

def save_contact(plist):
    f= open("contact_db.txt", "wt")
    for person in plist:
        f.write(person.name +"\t")
        f.write(person.pnum +"\t")
        f.write(person.email +"\t")
        f.write(person.addr+"\t\n")
    f.close()

def load_contact(plist):
    try:
        f=open("contact_db.txt","rt")
    except FileNotFoundError as e:
        print("No data")
        return
    else:
        lines = f.readlines()
    num=len(lines)
    for i in range(num):
        p=lines[i].split('\t')
        name=p[0]
        pnum=p[1]
        email=p[2]
        addr=p[3].rstrip()
        person = Contact(name, pnum, email, addr)
        plist.append(person)
    f.close()

def print_menu():
    print("------MENU------")
    print("1. Type")
    print("2. Find")
    print("3. Delete")
    print("4. Quit")
    print("------MENU------")
    menu=input("Select menu: ")
    print("------INFO------")
    return int(menu)

def run():
    plist=[]
    load_contact(plist)
    while 1:
        menu=print_menu()
        if menu==1:
            person=set_contact(plist)
            same=False
            for p in plist:
                if p.name == person.name:
                    same=True
                    p.name=person.name
                    p.pnum=person.pnum
                    p.email=person.email
                    p.addr=person.addr
                    break
            if same==True:
                continue
            plist.append(person)
        elif menu==2:
            fname=input("Find: ")
            print_contact(plist, fname)
        elif menu==3:
            dname=input("Delete: ")
            delete_contact(plist, dname)
        elif menu==4:
            save_contact(plist)
            break

if __name__=="__main__":
    sys.stdout.flush()
    run()
