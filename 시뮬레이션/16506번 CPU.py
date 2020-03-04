# 16506번 CPU

opcode = {'ADD': '00000', 'ADDC': '00001', 'SUB':'00010', 'SUBC': '00011',
       'MOV': '00100', 'MOVC': '00101', 'AND': '00110', 'ANDC': '00111',
       'OR': '01000', 'ORC': '01001', 'NOT': '01010', 'MULT': '01100', 'MULTC': '01101',
       'LSFTL': '01110', 'LSFTLC': '01111', 'LSFTR': '10000', 'LSFTRC': '10001',
       'ASFTR': '10010', 'ASFTRC': '10011', 'RL': '10100', 'RLC': '10101', 'RR': '10110', 'RRC': '10111'
       }
res = []
for i in range(int(input())):
    order = list(input().split())
    ans = ""
    ans += opcode[order[0]]
    ans += "0"
    tmp = format(int("{}".format(order[1])), 'b')
    if len(tmp) == 1:
        ans += '00' + tmp
    elif len(tmp) == 2:
        ans += '0' + tmp
    elif len(tmp) == 3:
        ans += tmp

    if order[0] == "MOV" or order[0] == "MOVC" or order[0] == "NOT":
        ans += '000'
    else:
        tmp = format(int("{}".format(order[2])), 'b')
        if len(tmp) == 1:
            ans += '00' + tmp
        elif len(tmp) == 2:
            ans += '0' + tmp
        elif len(tmp) == 3:
            ans += tmp

    if ans[4] == '0':
        tmp = format(int("{}".format(order[3])), 'b')
        if len(tmp) == 1:
            ans += '00' + tmp
        elif len(tmp) == 2:
            ans += '0' + tmp
        elif len(tmp) == 3:
            ans += tmp
        ans += '0'
    elif ans[4] == "1":
        tmp = format(int("{}".format(order[3])), 'b')
        if len(tmp) == 1:
            ans += '000' + tmp
        elif len(tmp) == 2:
            ans += '00' + tmp
        elif len(tmp) == 3:
            ans += '0' + tmp
        elif len(tmp) == 4:
            ans += tmp

    ans = ('').join(ans)
    res.append(ans)

for i in res:
    print(i)
