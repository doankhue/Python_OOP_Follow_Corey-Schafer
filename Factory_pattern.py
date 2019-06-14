


class VietNamLocalizer(object):
    def __init__(self):
        self.translations = {"dog":"con cho","cat":"con meo"}
    def localize(self, msg):
        return self.translations.get(msg,msg)

class EnglishLocalizer(object):
    def localize(self, msg):
        return msg

def get_localizer(language= "English"):
    localizers = {
        "English": EnglishLocalizer,
        "VietNam": VietNamLocalizer
    }
    return localizers[language]()

e, g = get_localizer(language="English"), get_localizer(language="VietNam")
for msg in "dog parrot cat bear".split():
    print(e.localize(msg), g.localize(msg))
