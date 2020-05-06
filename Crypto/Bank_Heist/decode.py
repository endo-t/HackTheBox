MAP = [[""],\
    [""],\
    ["A","B","C"],\
    ["D","E","F"],\
    ["G","H","I"],\
    ["J","K","L"],\
    ["M","N","O"],\
    ["P","Q","R","S"],\
    ["T","U","V"],\
    ["W","X","Y","Z"]\
]
TEXT = "444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777."

S = list(map(str,TEXT.split()))
ans = []
for s in S:
    tmp = s[0]
    num = 0
    for i in range(1,len(s)):
        if tmp == s[i]:
            num += 1
        else:
            ans.append(MAP[int(tmp)][num])
            tmp = s[i] if i < len(s) else ""
            num = 0
    else:
        if tmp.isdecimal():
            ans.append(MAP[int(tmp)][num])
        else:
            ans.append(tmp)
    ans.append(" ")
print(''.join(ans))
