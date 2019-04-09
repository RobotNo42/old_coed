import getpass
name = input("input your name:")
password = getpass.getpass("input your passwod:")
if name == "jack" and password == "123456":
    print("welcome")
else:
    print("gun")