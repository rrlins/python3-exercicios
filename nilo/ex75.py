s1 = 'AATTGGAA'
s2 = 'TG'
s3 = []
c  = 0

while c < len(s1):
    if s1[c] not in s2:
        s3.append(s1[c])
    c+=1
print(''.join(s3))
