s1 = 'CTA'
s2 = 'ABC'
s3 = []
c  = 0

while c < len(s1):
    if s2[c] not in s1:
        s3.append(s2[c])
    if s1[c] not in s2:
        s3.append(s1[c])
    c+=1

print(''.join(s3))
