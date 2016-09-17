i = '[{((()))}]'
a = [j for j in i]
s = []

for i in a:
    if i in ['{', '[', '(']:
        s.append(i)
    elif i in ['}', ']', ')']:
        if i == '}':
            if s[len(s)-1] == '{':
                del s[len(s)-1]
            else:
                break
        elif i == ']':
            if s[len(s)-1] == '[':
                del s[len(s)-1]
            else:
                break
        else:
            if s[len(s)-1] == '(':
                del s[len(s)-1]
            else:
                break

if len(s) == 0:
    print(True)
else:
    print(False)
            
