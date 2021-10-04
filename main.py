def start() :
    # this is the welcome screen
    print('''
     ███████████                                   █████████            ████          
    ░░███░░░░░███                                 ███░░░░░███          ░░███          
     ░███    ░███ █████ ████ ████████    ██████  ███     ░░░   ██████   ░███   ██████ 
     ░██████████ ░░███ ░███ ░░███░░███  ███░░███░███          ░░░░░███  ░███  ███░░███
     ░███░░░░░░   ░███ ░███  ░███ ░███ ░███ ░░░ ░███           ███████  ░███ ░███ ░░░ 
     ░███         ░███ ░███  ░███ ░███ ░███  ███░░███     ███ ███░░███  ░███ ░███  ███
     █████        ░░████████ ████ █████░░██████  ░░█████████ ░░████████ █████░░██████ 
    ░░░░░          ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░    ░░░░░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░  

    ''')
    # cofigring user inputs and the selection screen
    usr_num = input(" Enter a number: ")
    usr_num2 = input(" Enter a second number: ")
    op_select = input(''' 
    ----------------------------------------------------------------
            |          1- multiplication                           |
            |                                                      |
            |          2- division                                 |
            |                                                      |
            |          3- subtraction                              |
            |                                                      |
            |          4- addition                                 |
    -----------------------------------------------------------------
    ''')
    # here are the operators
    num = float(usr_num)
    num2 = float(usr_num2)
    multi = num * num2
    plus = num + num2
    sub = num - num2
    div = num / num2
    # and these ofcourse are the if statments
    if num == 0:
        print("Can't input 0 for now")
    if num2 == 0:
        print("Can't input 0 for now")
    if op_select == "1":
        print(multi)
    if op_select == "2":
        print(div)
    if op_select == "3":
        print(sub)
    if op_select == "4":
        print(plus)
print(start())
end_screen = input("would you like to restart? if you would press 1, if you would like to quit press 0:")
while end_screen == "1":
    start()
