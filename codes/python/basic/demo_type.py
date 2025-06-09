# 普通 class 写法
class MyClass(object):
    x = 10

    def hello(self):
        print(f"Hello from MyClass, x = {self.x}")


# 等价的 type 写法
def hello(self):
    print(f"Hello from DynamicClass, x = {self.x}")


def main():
    DynamicClass = type('DynamicClass', (object,), {
        'x': 10,
        'hello': hello,
    })
    # 使用实例
    obj = DynamicClass()
    obj.hello()  # 输出: Hello from DynamicClass, x = 10

    instance = MyClass()
    instance.hello()


if __name__ == '__main__':
    main()

"""
/usr/local/bin/python3.11 /Users/huoyinghui/github/hello-algo/codes/python/basic/demo_type.py 
Hello from DynamicClass, x = 10
Hello from MyClass, x = 10
"""