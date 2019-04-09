import hashlib
passwds=[
    'alex3714',
    'alex1313',
    'alex94139413',
    'alex123456',
    '123456alex',
    'a123lex',
    ]


def make_passwd_dic(passwds):
    dic={}
    for passwd in passwds:
        m=hashlib.md5()
        m.update(passwd.encode('utf-8'))
        dic[passwd]=m.hexdigest()
    return dic


def break_code(cryptograph,passwd_dic):
    for k,v in passwd_dic.items():
        if v == cryptograph:
            print('密码是===>\033[46m%s\033[0m' %k)


cryptograph='aee949757a2e698417463d47acac93df'
break_code(cryptograph,make_passwd_dic(passwds))
x = 'dsda'

