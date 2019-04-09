class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('出现with语句,对象的__enter__被触发,有返回值则赋值给as声明的变量')
        # return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('game over')
        print(exc_type)
        print(exc_val)
        print(exc_tb)


with Open('a.txt') as f:
    print('=====>执行代码块')

print("caonima")