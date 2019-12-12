a = [100]

def test01(num):
    num+=num
    print(num)
test01(a)
print(a)

print("="*50)
b = [100]
def test02(num):
    num = num + num
    print(num)
test02(b)
print(b)
