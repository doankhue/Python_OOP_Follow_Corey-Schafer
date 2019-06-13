

class TextTag(object):
    def __init__(self, text):
        self.text = text
    def render(self):
        return self.text

class BoldWrapper(TextTag):
    def __init__(self, Obj):
        self.content = Obj
    def render(self):
        return "<b>{}</b>".format(self.content.render())
class ItalicWrapper(TextTag):
    def __init__(self, Obj):
        self.content = Obj
    def render(self):
        return "<i>{}</i>".format(self.content.render())

simple_hello = TextTag('hello world')
special_hello = ItalicWrapper(BoldWrapper(TextTag('hello world')))
print('Before Decorator:',simple_hello.render())
print('After use Decorator:',special_hello.render())