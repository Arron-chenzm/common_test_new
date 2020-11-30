from Button import Button
import pygame
from test_res import test_res
import time
class qesandans():
    def __init__(self,window=None,t1=None,time_start=None,delay_time = None,list_time_res = None,list_num = None,weight=None,height=None):
        self.window = window
        self.t1 = t1
        self.list_time_res = list_time_res
        self.list_num = list_num
        self.time_start = time_start
        self.delay_time = delay_time
        self.state = True
        self.weight = weight
        self.height = height
        #print("shilihua")
    def btnCallBack(self):  # 开始下一个trail的按钮



        self.state = False
        time_end1 = self.toc(self.t1)
        self.delay_time = self.delay_time + time_end1 - self.time_start
        #print("start:{}end:{}delay:{}".format(time_start1, time_end1, delay_time))
        #print("btnCallBack被按下了")
    def get_delaytime(self):
        return self.delay_time
    def toc(self,t1):
        t = time.time()
        return (t - t1) * 1000
    def btnCallBack1(self):
        #print(11)
        pass

    def btnCallBack2(self):
        #print(12)
        return 'n'

    def btnCallBack3(self):
        #print(13)
        return 'butterfly'

    def btnCallBack4(self):
        #print(14)
        return 'dog'

    def btnCallBack5(self):
        #print(15)
        return "apple"

    def btnCallBack6(self):
        #print(16)
        return "monkey"

    def btnCallBack7(self):
        #print(17)
        return "uncertain"
    def run(self):
        window = self.window
        list_time_res = self.list_time_res
        surBtnNormal = pygame.image.load("../picture_resourse/btn_normal.png").convert_alpha()
        surBtnNorma2 = pygame.transform.scale(surBtnNormal, (380, 40))
        surBtnNorma3 = pygame.transform.scale(surBtnNormal, (120, 42))
        surBtnMove = pygame.image.load("../picture_resourse/btn_move.png").convert_alpha()
        surBtnMove2 = pygame.transform.scale(surBtnMove, (380, 40))
        surBtnMove3 = pygame.transform.scale(surBtnMove, (120, 42))
        surBtnDown = pygame.image.load("../picture_resourse/btn_down.png").convert_alpha()
        surBtnDown2 = pygame.transform.scale(surBtnDown, (380, 40))
        surBtnDown3 = pygame.transform.scale(surBtnDown, (120, 42))
        btnFont = pygame.font.SysFont("fangsong", 36)
        time_start1 = self.toc(self.t1)

        #print("time_start1:{}".format(time_start1))

        state = True  # 点击下一个按钮，按钮弹起调用回调函数，会改变state为False，跳出循环。
        #print(state)
        btn8 = Button(600+self.weight/3, 275+self.height/3, "NEXT", surBtnNorma3, surBtnMove3, surBtnDown3, self.btnCallBack, btnFont, (255, 0, 0))
        #print(state)
        btn1 = Button(self.weight/3-50, 0+self.height/3, "看到不同栅距光栅", surBtnNorma2, surBtnMove2, surBtnDown2, self.btnCallBack1, btnFont, (255, 0, 0))
        btn2 = Button(350+self.weight/3, 0+self.height/3, "未看到不同栅距光栅", surBtnNorma2, surBtnMove2, surBtnDown2, self.btnCallBack2, btnFont, (255, 0, 0))
        #btn3 = Button(0+self.weight/3, 100+self.height/3, "蝴蝶", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack3, btnFont, (255, 0, 0))
        #btn4 = Button(125+self.weight/3, 100+self.height/3, "青蛙", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack4, btnFont, (255, 0, 0))
        #btn5 = Button(250+self.weight/3, 100+self.height/3, "苹果", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack5, btnFont, (255, 0, 0))
        #btn6 = Button(375+self.weight/3, 100+self.height/3, "猴子", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack6, btnFont, (255, 0, 0))
        btn7 = Button(200+self.weight/3, 150+self.height/3, "不确定", surBtnNorma3, surBtnMove3, surBtnDown3, self.btnCallBack7, btnFont, (255, 0, 0))

        #print("2333333333")
        #print(state)
        tr1 = test_res()
        tr1.set_times(self.list_num)
        while self.state:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.MOUSEMOTION:  # 鼠标移动事件
                    # 判断鼠标是否移动到按钮范围内
                    btn1.getFocus(mx, my)
                    btn2.getFocus(mx, my)
                    #btn3.getFocus(mx, my)
                    #btn4.getFocus(mx, my)
                    #btn5.getFocus(mx, my)
                    #btn6.getFocus(mx, my)
                    btn7.getFocus(mx, my)
                    btn8.getFocus(mx, my)
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
                    if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键按下
                        btn1.mouseDown(mx, my)
                        btn2.mouseDown(mx, my)
                        #btn3.mouseDown(mx, my)
                        #btn4.mouseDown(mx, my)
                        #btn5.mouseDown(mx, my)
                        #btn6.mouseDown(mx, my)
                        btn7.mouseDown(mx, my)
                        btn8.mouseDown(mx, my)
                        # print("鼠标按下")
                elif event.type == pygame.MOUSEBUTTONUP:  # 鼠标弹起
                    if (tr1.get_see() == None):
                        tr1.set_see(btn1.mouseUp())
                    else:
                        btn1.mouseUp4()
                    if (tr1.get_see() == None):
                        tr1.set_see(btn2.mouseUp())
                    else:
                        btn2.mouseUp4()
                    #if (tr1.get_thing() == None):
                        #tr1.set_thing(btn3.mouseUp())
                    #if (tr1.get_thing() == None):
                        #tr1.set_thing(btn4.mouseUp())
                    #if (tr1.get_thing() == None):
                       # tr1.set_thing(btn5.mouseUp())
                    #if (tr1.get_thing() == None):
                        #tr1.set_thing(btn6.mouseUp())
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn7.mouseUp())
                    else:
                        btn7.mouseUp4()
                    btn8.mouseUp3()
                    tr1.printres()
                    list_time_res[self.list_num] = tr1.res2str()
                    #print(list_time_res[self.list_num])
                    #print("鼠标弹起")

            # pygame.time.delay(16)
            window.fill((0, 0, 0))
            # 绘制按钮
            btn1.draw(window)
            btn2.draw(window)
            #btn3.draw(window)
            #btn4.draw(window)
            #btn5.draw(window)
            #btn6.draw(window)
            btn7.draw(window)
            btn8.draw(window)
            pygame.display.flip()



