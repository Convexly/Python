username = "test"
password = "test"

print("""            ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
            ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
            ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
            ██║     ██║   ██║██║   ██║██║██║╚██╗██║
            ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
            ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                       """)
print("""            |                                     |
            |                                     |
            |  username = test | password = test  |
            |                                     |
            |                                     |""")

usernametry = input("\nUsername: ")
passwordtry = input("\nPassword: ")

if usernametry == username:
    print(" ")

if passwordtry != password:
    print("Wrong login.")

if usernametry != username and passwordtry == password:
    print("\nWrong login.")

if usernametry == username and passwordtry == password:
    print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
                                                              
    
    
              Successfuly logged in as TEST
              Press Run to start over.



    
        
    
    





    
    
    
    
    
    
    
    
    
    
    
    """)
