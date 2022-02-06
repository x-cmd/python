
def hi(obj="world"):
    print("Hi " + obj)

def ensure(pkg):
    pkg = __import__(pkg)

if __name__ == "main":
    hi()
