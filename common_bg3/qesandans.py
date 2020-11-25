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
        return 'banana'

    def btnCallBack5(self):
        #print(15)
        return "dog"

    def btnCallBack6(self):
        #print(16)
        return "panda"

    def btnCallBack7(self):
        #print(17)
        return "uncertain"

    def btnCallBack9(self):
        return "apple"
    def btnCallBack10(self):
        return "cattle"
    def btnCallBack11(self):
        return "durian"
    def btnCallBack12(self):
        return "grape"
    def btnCallBack13(self):
        return "mug"
    def btnCallBack14(self):
        return "tiger"

    def run(self):
        window = self.window
        list_time_res = self.list_time_res
        surBtnNormal = pygame.image.load("../picture_resourse/btn_normal.png").convert_alpha()
        surBtnNormal = pygame.transform.scale(surBtnNormal, (120, 42))
        surBtnMove = pygame.image.load("../picture_resourse/btn_move.png").convert_alpha()
        surBtnMove = pygame.transform.scale(surBtnMove, (120, 42))
        surBtnDown = pygame.image.load("../picture_resourse/btn_down.png").convert_alpha()
        surBtnDown = pygame.transform.scale(surBtnDown, (120, 42))
        btnFont = pygame.font.SysFont("lisu", 40)
        time_start1 = self.toc(self.t1)

        #print("time_start1:{}".format(time_start1))

        state = True  # 点击下一个按钮，按钮弹起调用回调函数，会改变state为False，跳出循环。
        #print(state)
        btn8 = Button(375+self.weight/3, 340+self.height/3, "NEXT", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack, btnFont, (255, 0, 0))
        #print(state)
        btn1 = Button(0+self.weight/3, 0+self.height/3, "看到", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack1, btnFont, (255, 0, 0))
        btn2 = Button(200+self.weight/3, 0+self.height/3, "未看到", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack2, btnFont, (255, 0, 0))
        btn3 = Button(0+self.weight/3, 100+self.height/3, "蝴蝶", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack3, btnFont, (255, 0, 0))
        btn4 = Button(125+self.weight/3, 100+self.height/3, "香蕉", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack4, btnFont, (255, 0, 0))
        btn5 = Button(250+self.weight/3, 100+self.height/3, "狗", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack5, btnFont, (255, 0, 0))
        btn6 = Button(375+self.weight/3, 100+self.height/3, "熊猫", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack6, btnFont, (255, 0, 0))

        btn9 = Button(0 + self.weight / 3, 180 + self.height / 3, "苹果", surBtnNormal, surBtnMove, surBtnDown,
                      self.btnCallBack9, btnFont, (255, 0, 0))
        btn10 = Button(125 + self.weight / 3, 180 + self.height / 3, "牛", surBtnNormal, surBtnMove, surBtnDown,
                      self.btnCallBack10, btnFont, (255, 0, 0))
        btn11 = Button(250 + self.weight / 3, 180 + self.height / 3, "榴莲", surBtnNormal, surBtnMove, surBtnDown,
                      self.btnCallBack11, btnFont, (255, 0, 0))
        btn12 = Button(375 + self.weight / 3, 180 + self.height / 3, "葡萄", surBtnNormal, surBtnMove, surBtnDown,
                      self.btnCallBack12, btnFont, (255, 0, 0))
        btn13 = Button(0 + self.weight / 3, 260 + self.height / 3, "杯子", surBtnNormal, surBtnMove, surBtnDown,
                       self.btnCallBack13, btnFont, (255, 0, 0))
        btn14 = Button(125 + self.weight / 3, 260 + self.height / 3, "老虎", surBtnNormal, surBtnMove, surBtnDown,
                       self.btnCallBack14, btnFont, (255, 0, 0))


        btn7 = Button(250+self.weight/3, 260+self.height/3, "不确定", surBtnNormal, surBtnMove, surBtnDown, self.btnCallBack7, btnFont, (255, 0, 0))

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
                    btn3.getFocus(mx, my)
                    btn4.getFocus(mx, my)
                    btn5.getFocus(mx, my)
                    btn6.getFocus(mx, my)
                    btn7.getFocus(mx, my)
                    btn8.getFocus(mx, my)
                    btn9.getFocus(mx, my)
                    btn10.getFocus(mx, my)
                    btn11.getFocus(mx, my)
                    btn12.getFocus(mx, my)
                    btn13.getFocus(mx, my)
                    btn14.getFocus(mx, my)
                elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标按下
                    if pygame.mouse.get_pressed() == (1, 0, 0):  # 鼠标左键按下
                        btn1.mouseDown(mx, my)
                        btn2.mouseDown(mx, my)
                        btn3.mouseDown(mx, my)
                        btn4.mouseDown(mx, my)
                        btn5.mouseDown(mx, my)
                        btn6.mouseDown(mx, my)
                        btn7.mouseDown(mx, my)
                        btn8.mouseDown(mx, my)
                        btn9.mouseDown(mx, my)
                        btn10.mouseDown(mx, my)
                        btn11.mouseDown(mx, my)
                        btn12.mouseDown(mx, my)
                        btn13.mouseDown(mx, my)
                        btn14.mouseDown(mx, my)
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
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn3.mouseUp())
                    else:
                        btn3.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn4.mouseUp())
                    else:
                        btn4.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn5.mouseUp())
                    else:
                        btn5.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn6.mouseUp())
                    else:
                        btn6.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn7.mouseUp())
                    else:
                        btn7.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn9.mouseUp())
                    else:
                        btn9.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn10.mouseUp())
                    else:
                        btn10.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn11.mouseUp())
                    else:
                        btn11.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn12.mouseUp())
                    else:
                        btn12.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn13.mouseUp())
                    else:
                        btn13.mouseUp4()
                    if (tr1.get_thing() == None):
                        tr1.set_thing(btn14.mouseUp())
                    else:
                        btn14.mouseUp4()
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
            btn3.draw(window)
            btn4.draw(window)
            btn5.draw(window)
            btn6.draw(window)
            btn7.draw(window)
            btn8.draw(window)
            btn9.draw(window)
            btn10.draw(window)
            btn11.draw(window)
            btn12.draw(window)
            btn13.draw(window)
            btn14.draw(window)
            pygame.display.flip()



