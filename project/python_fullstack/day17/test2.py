import re
if __name__ == '__main__':
    print("it is mysesif")
if __name__ =='test2':
    print("chousb")
s = re.search('(?P<w>\w+)\.(?P<fuck>\w+)\.(?P<com>\w+)', 'www.buleone.com')
print(s.group('fuck'))
