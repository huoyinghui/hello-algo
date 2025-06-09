# 假设我们有一个基类
class BaseModel:
    def save(self):
        print(f"Saving {self.__class__.__name__} to DB")


# 假设我们要动态构造一个 ORM 模型类
def create_model_class(name, fields):
    attrs = {}
    for field_name, field_type in fields.items():
        attrs[field_name] = field_type
    return type(name, (BaseModel,), attrs)


def main():
    # 定义字段
    fields = {
        'id': int,
        'name': str
    }

    User = create_model_class("User", fields)
    u = User()
    u.name = "Alice"
    u.save()  # 输出: Saving User to DB


if __name__ == '__main__':
    main()


"""
/usr/local/bin/python3.11 /Users/huoyinghui/github/hello-algo/codes/python/basic/demo_type_orm.py 
Saving User to DB
"""