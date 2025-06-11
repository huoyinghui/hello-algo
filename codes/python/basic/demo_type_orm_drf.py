import copy
from collections import OrderedDict
from functools import cached_property


# todo 换为drf的filed
class CharField:
    def __init__(self, max_length):
        self.max_length = max_length


Field = CharField


class SerializerMetaclass(type):
    """
    This metaclass sets a dictionary named `_declared_fields` on the class.

    Any instances of `Field` included as attributes on either the class
    or on any of its superclasses will be include in the
    `_declared_fields` dictionary.
    """

    @classmethod
    def _get_declared_fields(cls, bases, attrs):
        fields = [
            (field_name, attrs.pop(field_name))
            for field_name, obj in list(attrs.items())
            if isinstance(obj, Field)
        ]
        fields.sort(key=lambda x: x[1]._creation_counter)

        # If this class is subclassing another Serializer, add that Serializer's
        # fields.  Note that we loop over the bases in *reverse*. This is necessary
        # in order to maintain the correct order of fields.
        for base in reversed(bases):
            if hasattr(base, '_declared_fields'):
                fields = [
                             (field_name, obj) for field_name, obj
                             in base._declared_fields.items()
                             if field_name not in attrs
                         ] + fields

        return OrderedDict(fields)

    def __new__(cls, name, bases, attrs):
        attrs['_declared_fields'] = cls._get_declared_fields(bases, attrs)
        return super().__new__(cls, name, bases, attrs)


class Serializer(object, metaclass=SerializerMetaclass):
    id = Field(
        default=1,
        help_text="id",
    )

    def __init__(self):
        pass

    def __str__(self):
        return f"{self._declared_fields}"

    def __getattr__(self, item):
        return self._declared_fields.get(item)

    def get_fields(self):
        """
        Returns a dictionary of {field_name: field_instance}.
        """
        # Every new serializer is created with a clone of the field instances.
        # This allows users to dynamically modify the fields on a serializer
        # instance without affecting every other serializer instance.
        return copy.deepcopy(self._declared_fields)

    @cached_property
    def fields(self):
        """
        A dictionary of {field_name: field_instance}.
        """
        # `fields` is evaluated lazily. We do this to ensure that we don't
        # have issues importing modules that use ModelSerializers as fields,
        # even if Django's app-loading stage has not yet run.
        fields = BindingDict(self)
        for key, value in self.get_fields().items():
            fields[key] = value
        return fields


def main():
    s = Serializer()
    print(s.id)
    # Field(default=1, help_text='id')
    print(s.fields)
    # {'id': Field(default=1, help_text='id')}
    pass


if __name__ == '__main__':
    main()