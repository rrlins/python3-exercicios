s1 = 'AATTCGAA'
s2 = 'TG'
s3 = 'AC'
s4 = []
c  = 0

while c < len(s1):
    if s1[c] == s2[0]:
        s4.append(s3[0])
    elif s1[c] == s2[1]:
        s4.append(s3[1])
    else:
        s4.append(s1[c])
    c += 1

print(''.join(s4))
