#Chiluka Yashwanth
#id 190030311
#KL University

class BankAccount:
    def __init__(self,Accountnumber,IFSCcode, HolderName,Branch):
        self.accountbalance =0
        self.Accountnumber= Accountnumber
        self.IFSCcode = IFSCcode
        self.HolderName= HolderName
        self.Branch= Branch

    def addmoney(self, amount):
        self.accountbalance = self.accountbalance + amount
    def withdraw(self,amount):
        if self.accountbalance> amount:
            self.accountbalance -= amount
        else:
            print("Insufficient balance")
    def balance(self):
        return self.accountbalance


class MobileBankAccount(BankAccount):
    def __init__(self,Accountnumber,IFSCcode, HolderName,Branch,Phonenumber,Pin):
        super().__init__(Accountnumber,IFSCcode, HolderName,Branch)
        self.A_balance=0
        self.Phonenumber= Phonenumber
        self.Pin= Pin
    def transfer(self,amount1):
        if self.A_balance>= amount1:
         self.A_balance-=amount1
        else:
            print("Insufficient Fund")        
    def received(self,amount1):
          self.A_balance+= amount1
          
    def Totalbalance(self):
          return self.A_balance

        

class InternetBankAccount(MobileBankAccount):
    def __init__(self,Accountnumber,IFSCcode, HolderName,Branch,Phonenumber,Pin):
        self.A_balance2=0
        super().__init__(Accountnumber,IFSCcode, HolderName,Branch,Phonenumber,Pin)
    def onlinetransfer(self,amount2):
        if self.A_balance2>= amount2:
         self.A_balance2-=amount2
        else:
            print("Insufficient Fund")
    def onlinereceived(self,amount2):
       self.A_balance2+= amount2
    def onlinebalance(self):
        return self.A_balance2

if __name__=="__main__":
    account1 = BankAccount(10232394239,'SBINxxxxxx','CHILUKA YASHWANTH','Nellore')
    account2 = MobileBankAccount(10232394240,'SBIN000xxy','HARSHITH MEDURI','KHAMMAM',9848282343,4567)
    account3 = InternetBankAccount(10232394240,'SBIN000xxy','HARSHITH MEDURI','KHAMMAM',9848282343,4567)
    account1.addmoney(100)
    account1.withdraw(100)
    print(account1.balance())
    print(account1.Accountnumber)
    print(account1.IFSCcode)
    print(account1.HolderName)
    print(account1.Branch+ "\n"+'')

    account2.received(200)
    account2.transfer(100)
    print(account2.Totalbalance())
    print(account2.balance())
    print(account2.Accountnumber)
    print(account2.IFSCcode)
    print(account2.HolderName)
    print(account2.Pin)
    print(account2.Phonenumber)
    print(account2.Branch+ '\n' +'')

    account3.onlinereceived(300)
    account3.onlinetransfer(100)
    print(account3.onlinebalance())
    print(account3.Accountnumber)
    print(account3.IFSCcode)
    print(account3.HolderName)
    print(account3.Phonenumber)
    print(account3.Pin)
    print(account3.Branch )
    
#all the attributes for internet banking and mobile banking are same 

         
           
        
        
        
