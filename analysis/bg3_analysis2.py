import matplotlib.pyplot as plt

def bg1_time(str):
    """
    :param str: 存储结果的一行字符串，string类型
    :return: 刺激出现的时间，int类型，单位为1/60s
    """
    time = ""
    for char in str:
        if char != "\t":
            time = time+char
        elif char == "\t":
            break
    return int(time)

def bg1_res(str):
    """
    :param str: str: 存储结果的一行字符串，string类型
    :return: 判断的结果是否出现，string类型
    """
    res = ""
    length = len(str)
    flag = False
    for i in range(0,length):
        if str[i] != ":":
            continue
        elif str[i] == ":" and flag==False:
            flag = True
            continue
        elif str[i] == ":" and flag ==True:
            while(str[i+1]!=" "and i<length-1):
                i = i+1
                res = res+str[i]
            break
    return res

def bg1_thing(str):
    res = ""
    length = len(str)
    flag = 0
    for i in range(0, length):
        if str[i] != ":":
            continue
        elif str[i] == ":" and flag < 2:
            flag = flag+1
            continue
        elif str[i] == ":" and flag == 2:
            while (i<length-2):
                i = i + 1
                res = res + str[i]
            break
    return res



stimu_delaytime = [0, 2, 4, 6, 8, 10, 12, 14, 16]
fp = open('../result/dt_bg3_100_1.txt','r', encoding='utf-8')
lines = fp.readlines()
ciji_times = [0,0,0,0,0,0,0,0,0]
result = [0,0,0,0,0,0,0,0,0]
acc = [0,0,0,0,0,0,0,0,0]
for i in range(0,len(lines)-1):
    if len(lines[i])<10:
        continue
    else:
        time = bg1_time(lines[i])
        res = bg1_res(lines[i])
        thing = bg1_thing(lines[i])
        print(time)
        print(res)
        print(thing)
        if time == stimu_delaytime[0]:
            ciji_times[0] = ciji_times[0] + 1
            if res == "未看到不同的白噪声":
                result[0] = result[0] + 1
        for j in range(1, 9):
            if time == stimu_delaytime[j]:
                ciji_times[j] = ciji_times[j] + 1
                if res == "看到不同的白噪声" and thing == "None" :
                    result[j] = result[j] + 1
                elif thing == "不确定":
                    result[j] = result[j] + 1

for i in range(0,len(ciji_times)):
    acc[i] = result[i]/ciji_times[i]
    print(result[i])
plt.plot(stimu_delaytime,acc)
plt.show()