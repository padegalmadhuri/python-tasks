def password_check(passwd): 
      
    sym =['!','^','*','$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 5 or len(passwd)>15:
        print('length should be in 5-15 range') 
        val = False
          
    if not any(i.isdigit() for i in passwd): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(i.isupper() for i in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(i.islower() for i in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if not any(i in sym for i in passwd): 
        print('Password should have at least one of the symbols') 
        val = False
    if val: 
        return val 
def check_usrname(usr):
    symb1='@'
    symb2='.'
    for i in usr:
        if symb1 not in usr and symb2 not in usr:
            return False
        else:
            for i in usr:
                if i=='@':
                    x=usr.index(i)
                if i=='.':
                    y=usr.index(i)
            if x>y:
                return False
            else:
                return True
    
def main(): 
    username=input()
    passwd = input()
    if (check_usrname(username)):
        print("valid user name")
    else:
        print("invalid user name")
    if (password_check(passwd)): 
        print("Password is valid") 
    else: 
        print("Invalid Password !!") 
          
      
if __name__ == '__main__': 
    main() 


    
