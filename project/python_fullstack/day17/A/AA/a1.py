import os,sys
re = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(re)
print(sys.path)
sys.path.append(re)
print(sys.path)

def kill():
    print('kill')

import test3
test3.mmp()