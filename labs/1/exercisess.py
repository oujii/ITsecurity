"""
x = [1,2,3,4]
out = []

for item in x:
    out.append(item**2)

print(out)

"""

def end_other(a,b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or a == b [-(len(a)):]