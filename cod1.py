ot = input()
d = input()
s = ot.split(':')
b = d.split()
h = int(s[0]) + int(b[0])
m = int(s[1]) + int(b[1])
if m > 59:
    h = h + m // 59
    m = m % 59-1
if h > 23:
    h = h % 23-1
if m < 10:
    m = '0' + str(m)
if h < 10:
    h = '0' + str(h)
print(str(h) + ':' + str(m))
