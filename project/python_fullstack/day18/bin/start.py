import os,sys
re = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(re)
from core import ruiwen
if __name__ == '__main__':
    ruiwen.attack('sd')
