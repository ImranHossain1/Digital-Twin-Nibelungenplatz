import json
a = ("a", "b" "c")
b = ("1", "2" "3")
c = ("m", "k" "j")

for x,y,z in zip(a,b,c):
    print(x)
    print(y)
    print(z)

outputDict = dict()
for i in range(16):
    outputDict[i] = dict()
    outputDict[i]['x1'] = dict()
    temp = outputDict[i]['x1']
    temp['abc'] = 5
print(outputDict)