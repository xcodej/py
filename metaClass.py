class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
