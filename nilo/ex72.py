s1 = 'AAACTBF'
s2 = 'CBT'
s3 = []
c = 0
while c < len(s2):
    if s2[c] in s1:
        s3.append(s2[c])
    c+=1
print(''.join(s3))
