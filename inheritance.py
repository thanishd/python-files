class version1:
    def v1(self):
        print("label")
        print("input box")

class version2(version1):
    def v2(self):
        print("combo box")
        print("radio button")

class version3(version2):
    def v3(self):
        print("menu bar")
        print("submit button")

obj=version3()
obj.v3()
obj.v1()
obj.v2()
