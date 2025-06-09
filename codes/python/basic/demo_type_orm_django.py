class CharField:
    def __init__(self, max_length):
        self.max_length = max_length


Field = CharField


class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        """
        在创建中：处理attrs中特定的orm filed字段
        """
        fields = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                fields[k] = v
        attrs['_meta_fields'] = fields
        print(f"cls {cls} name: {name} bases: {bases} attrs {attrs}")
        return super().__new__(cls, name, bases, attrs)


class Model(metaclass=ModelBase):
    """
    Model 用 ModelBase 来创建类 Model不是默认的 type，我要自己控制类的创建过程

    Model = ModelBase('Model', base=(), attrs: {'save': ...})
    cls <class '__main__.ModelBase'>
    name: Model
    bases: ()
    attrs {'__module__': '__main__', '__qualname__': 'Model',  'save': <function Model.save at 0x100732fc0>, '_meta_fields': {}}
    """
    def save(self):
        print(f"Saving {self.__class__.__name__} with fields {self._meta_fields}")


# 用户层的接口
class User(Model):
    """
    User = type("User", (Model,), {...})

    cls <class '__main__.ModelBase'>
    name: User
    bases: (<class '__main__.Model'>,)
    attrs {'__module__': '__main__', '__qualname__': 'User', 'name': <__main__.CharField object at 0x100889290>, '_meta_fields': {'name': <__main__.CharField object at 0x100889290>}}
    """
    name = CharField(max_length=100)


def main():
    # 使用
    u = User()
    u.save()  # 输出: Saving User with fields {'name': <__main__.CharField object at ...>}


if __name__ == '__main__':
    main()

"""
Saving User with fields {'name': <__main__.CharField object at 0x1013a4f50>}
"""