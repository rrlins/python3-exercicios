s = 'TTAAC'
c = 0
r = ''

while c < len(s):
    if s[c] != r:
        print('{}: {}x'.format(s[c],s.count(s[c])))
    r = s[c]
    c += 1
