# playing with strings Chapter 6 of Python for Everybody (Severance)
w1 = 'centripetal'
w2 = 'zooxanthellae'
print(w1,w2)
w1_syl_1 = w1[0:3]
w1_syl_2 = w1[3:6]
w1_syl_3 = w1[6:8]
w1_syl_4 = w1[8:11]
print(w1_syl_1,w1_syl_2,w1_syl_3,w1_syl_4)
print(w1[1:3])
w2_syl_1 = w2[0:3]
w2_syl_2 = w2[3:6]
w2_syl_3 = w2[6:9]
w2_syl_4 = w2[9:13]
print(w2_syl_1,w2_syl_2,w2_syl_3,w2_syl_4)
print(w1[:6])
print(w1[6:])
print(w1[6])
length_w1 = len(w1)
last_w1 = w1[length_w1-1]
print(last_w1)
print('Whadido?')
quit
str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)
x = '40'
y = int(x) + 2
print(y)
print(len('banana')*7)
text = "X-DSPAM-Confidence:     0.8475";
x = text.find("0")
#output_float = float(text[x:])
#print(output_float)
print([int(s) for s in text.split() if s.isdigit()])
l = []
for t in text.split():
    try:
        x = l.append(float(t))
    except ValueError:
        pass
#print(float[l])
print(x)
