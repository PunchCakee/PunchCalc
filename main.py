print('''



███████████            ███                    ████   ██                                         
░░███░░░░░░█           ░░░                    ░░███  ███                                         
 ░███   █ ░   ██████   ████   █████   ██████   ░███ ░░░   █████                                  
 ░███████    ░░░░░███ ░░███  ███░░   ░░░░░███  ░███      ███░░                                   
 ░███░░░█     ███████  ░███ ░░█████   ███████  ░███     ░░█████                                  
 ░███  ░     ███░░███  ░███  ░░░░███ ███░░███  ░███      ░░░░███                                 
 █████      ░░████████ █████ ██████ ░░████████ █████     ██████                                  
░░░░░        ░░░░░░░░ ░░░░░ ░░░░░░   ░░░░░░░░ ░░░░░     ░░░░░░                                   
                                                                                                 
                                                                                                                                                   
                                                                                                 
                                                                                                 
   █████████            ████                      ████             █████                         
  ███░░░░░███          ░░███                     ░░███            ░░███                          
 ███     ░░░   ██████   ░███   ██████  █████ ████ ░███   ██████   ███████    ██████  ████████    
░███          ░░░░░███  ░███  ███░░███░░███ ░███  ░███  ░░░░░███ ░░░███░    ███░░███░░███░░███   
░███           ███████  ░███ ░███ ░░░  ░███ ░███  ░███   ███████   ░███    ░███ ░███ ░███ ░░░    
░░███     ███ ███░░███  ░███ ░███  ███ ░███ ░███  ░███  ███░░███   ░███ ███░███ ░███ ░███        
 ░░█████████ ░░████████ █████░░██████  ░░████████ █████░░████████  ░░█████ ░░██████  █████       
  ░░░░░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░    ░░░░░░░░ ░░░░░  ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░       

''')
usr_num = input(" Enter a number: ")
usr_num2 = input(" Enter a second number: ")
op_select = input(''' 
----------------------------------------------------------------
        |           1- multiplication                          |
        |                                                      |
        |          2- division                                 |
        |                                                      |
        |          3- subtraction                              |
        |                                                      |
        |          4- addition                                 |
-----------------------------------------------------------------
''')
num = float(usr_num)
num2 = float(usr_num2)
multi = num * num2
plus = num + num2
sub = num - num2
div = num / num2
if num == 0:
    print("Can't input 0 for now")
if num2 == 0:
    print("Can't input 0 for now")
if op_select == "1":
    print(multi)
if op_select == "2":
    print(div)
if op_select == "4":
    print(plus)
if op_select == "3":
    print(sub)