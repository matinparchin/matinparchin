import builtwith
wq='\t*******************************************************\n\n\n \t         telegram chanell : @persian_cyber_org \n\n\n\t*******************************************************'
print(wq)
id=input("\n\nid ? ? ?")
message=input("message ? ? ?")
m=message.replace(" ","+")
pass1='9323'
q=4
w=0
n=input("what is password? ? ?")
if n == pass1:
    
    site = "http://persian-cyber.xyz/send-message/AR-MAN.php?message="+m+"&id="+id+"&pass=@Persian_Cyer_Org"
    mmd=builtwith.parse(site)
    print("OK ! !  done successfully")
else :
    print("error password")
    
input("\n\n\tT H E   E N D  .  .  .")
