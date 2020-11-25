import random
trail_times = 91
appear_time = []  # 储存刺激出现的时间
end_time = [] # 储存刺激结束的时间
stimu_delaytime = [0, 0, 0, 0, 0, 0, 0, 0, 0]
stimu_delaytime_list = []  # 储存每一次随机产生的刺激延迟时间

def time_random5():
    num = random.randint(60, 540)
    return num

for i in range(0, 10):
    stimu_delaytime_list.extend(stimu_delaytime)
random.shuffle(stimu_delaytime_list)
for i in range(0,trail_times-1):
    appear_time.append(i*600+time_random5())
for i in range(0,len(appear_time)):
    end_time.append(appear_time[i]+stimu_delaytime_list[i])
for  i in range(0,len(appear_time)):
    if appear_time[i]==end_time[i]:
        appear_time.pop(i)
        end_time.pop(i)