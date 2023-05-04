def add_package():
  pname=input("Enter Package name:")
  destination=input("Enter package destination:")
  price=input("Enter package price")
  availability=input("Enter package availability")
  with open("packages.txt","a") as f:
    f.write(pname+"\n")
    f.write(destination+"\n")
    f.write(price+"\n")
    f.write(availability+"\n")
    print("Package added successfully")
    
def show_package():
    with open("packages.txt","r") as f:
        print("pname\t destination\t price\t availability\t")
        print(f.read())

def search():
    i=input("Enter the id to be searched")
    with open("packages.txt","r") as f:
        all=f.readlines()
        for data in all:
            d=data.split("\t",1)
            if(d[0]==i):
                print(data)
