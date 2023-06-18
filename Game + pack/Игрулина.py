import pygame,sys
import math
import random

pygame.init()
win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Fire Car")
fon = pygame.image.load('pole.jpeg')

#Загрузка изображений
Go_Car = [pygame.image.load('Car(1).png'),pygame.image.load('Car(2).png')]
Stop_Car = pygame.image.load ('Car(0).png')
Pushka = pygame.image.load ('Pushka_(3).png')
Voda = pygame.image.load('Voda(1).png')
Home=pygame.image.load('House.png')
Vzriv=pygame.image.load('Vzriv.png')
Fair=[pygame.image.load('Ogon(0)).png'),pygame.image.load('Ogon(1)).png')]
HP=pygame.image.load('HP.png')
HPtic=pygame.image.load('HPtic.png')
Instr=pygame.image.load('Instr.jpg')

#Определение центра картинки
orig_rect = Pushka.get_rect()
orig_rect_vod=Voda.get_rect()



clock= pygame.time.Clock()
#pygame.mixer.music.load('Go.mp3')

pygame.mixer.music.load('FonTr.mp3')

pygame.mixer.music.set_volume(0.2)
sound2 = pygame.mixer.Sound('Vibor.ogg')
sound1 = pygame.mixer.Sound('VZRIV.ogg')
sound = pygame.mixer.Sound('ZvukMigal.ogg')
sound.set_volume(0.4)

#Константы
Go_Car_New=[]
MOTOR_OFF=0
CAR_X = 100
CAR_Y = 600
CarCount=0
PUSH_X=5
PUSH_Y=5
DIRECTION="up"
Px = CAR_X-300
Py = CAR_Y-200
rot = 0
rad_alfa = float ()
bullets= []
Go=True
GoHom=True
House_X=20
House_Y=70
Fair_Count=0
Fx = House_X+40
Fy = House_Y+10
MaxLen=20
Coint=201
Hos=True
MAXHOME=random.randint(0,8)
House_SIZE=270
Anti_Home=[]
k=0
proces=0
t=0
speed=5
X_KU=random.randint(3,8)
Homi=[0,1,2,3,4,5,6,7,8]
i=random.randint(0,8)



#Last()
#Sc=0
#Дома
def Update():
    global Coint,MOTOR_OFF,CAR_X,CAR_Y,Anti_Home,proces,k,Homi
    Coint=201
    MOTOR_OFF=0
    CAR_X=100
    CAR_Y=600
    Anti_Home.clear()
    k=0
    Homi = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for house in Houses:
        house.Hp=100
        house.image=Home
    proces=0


class House:
    def __init__(self,HouseX,HouseY):
        self.HouseX = HouseX
        self.HouseY = HouseY
        self.image=Home
        self.Hp=100
        self.img_vriv=Vzriv
        #self.Nubmer=Number

    def draw(self,win):
        win.blit(self.image,(self.HouseX,self.HouseY))

    def render_Bar(self,win):
        win.blit(HP,(self.HouseX+20,self.HouseY-10))
        m=1
        z=self.Hp//2
        while m<z:
            win.blit(HPtic,(self.HouseX+19+m*2,self.HouseY-9))
            m+=1
    def ghost(self,CAR_X,CAR_Y):
        if (self.HouseX > CAR_X-110) and (self.HouseX < CAR_X + 40) and (self.HouseY > CAR_Y - 130) and (self.HouseY < CAR_Y+60):
            return 1
        else:
            return 0










Houses=[House(House_X,House_Y),House(House_X+House_SIZE,House_Y),House(House_X+(2*House_SIZE),House_Y),
        House(House_X+(3*House_SIZE),House_Y),House(House_X,House_Y+House_SIZE),
        House(House_X+House_SIZE,House_Y+House_SIZE),House(House_X+(2*House_SIZE),House_Y+House_SIZE),
        House(House_X+House_SIZE,House_Y+(2*House_SIZE)),House(House_X+(2*House_SIZE),House_Y+(2*House_SIZE))]

class Menu:
    def __init__(self,punkts=[128,140,u'Punkt',(250,250,30),(250,30,250),0]):
        self.punkts=punkts
    def render(self,poverhnost,font,num_punkt):
        for o in self.punkts:
            if num_punkt == o[5]:
                poverhnost.blit(font.render(o[2], 1, o[4]), (o[0], o[1]))
            else:
                poverhnost.blit(font.render(o[2], 1, o[3]), (o[0], o[1]))
    def menu(self):
        done=True
        font_menu=pygame.font.SysFont('Times New Roman', 60)
        punkt=-1

        mapa=True
        while done:
            if mapa==True:
                win.blit(fon,(0,0))
            mp = pygame.mouse.get_pos()
            if mapa==True:
                for o in self.punkts:
                    if mp[0]>o[0] and mp[0]<o[0]+155 and mp[1] > o[1] and mp[1]<o[1]+50:
                        punkt=o[5]
                self.render(win,font_menu,punkt)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    sound2.play()
                    if event.key== pygame.K_ESCAPE:
                        sys.exit()
                    if event.key==pygame.K_UP:
                        if punkt>0:
                            punkt-=1
                    if event.key==pygame.K_DOWN:
                        if punkt < len(self.punkts) -1:
                            punkt+=1
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) or \
                        event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                    sound2.play()
                    if punkt == 1:
                        done = False
                    elif punkt==0:
                        mapa=False
                        win.blit(Instr,(0,0))

                    elif punkt == 2:
                        sys.exit()
                    if mapa==False:
                        punkt=1

            pygame.display.update()

    def menuGO(self):
        over = True
        font_menu = pygame.font.SysFont('Times New Roman', 50)
        punkt =-1
        while over:
            pygame.display.update()
            mp = pygame.mouse.get_pos()
            for o in self.punkts:
                if mp[0] > o[0] and mp[0] < o[0] + 155 and mp[1] > o[1] and mp[1] < o[1] + 50:
                    punkt = o[5]
            self.render(win, font_menu, punkt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if punkt==4:
                        sys.exit()
                    if punkt==3:
                        Update()
                        over = False
        pygame.display.update()



class Kust:
    def __init__(self,X_Kust,Y_Kust):
        self.image=pygame.image.load('Kusti(1).png')
        self.X_Kust=X_Kust
        self.Y_Kust=Y_Kust
    def render(self):
        win.blit(self.image,(self.X_Kust,self.Y_Kust))
    def ghost(self,CAR_X,CAR_Y):
        if (self.X_Kust > CAR_X-50) and (self.X_Kust < CAR_X + 50) and (self.Y_Kust > CAR_Y - 30) and (self.Y_Kust < CAR_Y+30):
            return 1
        else:
            return 0


Kusts=[Kust(20,220),Kust(80,220),Kust(140,220),Kust(200,220),Kust(260,220),Kust(320,220),Kust(380,220),
       Kust(440,220),Kust(500,220),Kust(560,220),Kust(620,220),Kust(680,220),Kust(740,220),Kust(800,220),
       Kust(860,220),Kust(920,220)]




def Kust_random(X_KU):
    Kusts_random = [Kust(X_KU * 100, 210), Kust(X_KU * 100, 260), Kust(X_KU * 100, 310)]
    for kust in Kusts_random:
        kust.render()

def Score():
    f2 = pygame.font.SysFont('serif', 48)
    text2 = f2.render("Очки: " + str(k), 0, (0, 0, 0))
    win.blit(text2, (10, 700))

def HP_Min(n):
    global MAX_Home,Anti_Home,proces
    Houses[n].Hp-=5
    if Houses[n].Hp <= 0:
        Houses[n].image=Vzriv
        sound1.play()
        Anti_Home.append(n)
        #proces+=1
        return 1

def DelHome(n):
    global Coint
    p=0
    if HP_Min(n):
        Coint=201
        p+=1
        if p==1:
            Homi.remove(n)
        #pygame.time.set_timer(25, 2500)

def Last():
    global i,Homi
    i = random.choice(Homi)
    Q=i
    Homi.remove(Q)


def HomeDELE():
    global proces
    proces=0
    for home in Houses:
        if home.Hp<=0:
            proces+=1


def Proces(proces):
    if proces >= 9:
        return 0
    else:
        return 1




def TrafficPush ():
    # Получение кординат мышки
    #pos = pygame.mouse.get_pos()
    global rot,Push,orig_rect,rad_alfa
    rot_rect = orig_rect.copy()
    #Px = pos[0] - CAR_X
    #Py = pos[1] - CAR_Y
    #rot = math.atan2(Py,Px) * -180/math.pi
    if rot >=360:
        rot=0

    #Поворот пушки
    Push=pygame.transform.rotate(Pushka,rot)
    rot_rect.center = Push.get_rect().center
    Push = Push.subsurface(rot_rect).copy()

    rad_alfa = rot * (math.pi / 180)

def TraficVod (diriction):
    global  orig_rect_vod,Vod
    if diriction == "up":
        Vod = pygame.transform.rotate(Voda, rot)
    elif diriction == "left":
        Vod = pygame.transform.rotate(Voda, rot + 270)
    elif diriction == "right":
        Vod = pygame.transform.rotate(Voda, rot + 270)
    else:
        Vod = pygame.transform.rotate(Voda, rot)

    rot_rect = orig_rect_vod.copy()
    # Px = pos[0] - CAR_X
    # Py = pos[1] - CAR_Y
    # rot = math.atan2(Py,Px) * -180/math.pi

    # Поворот спарйта воды
    #Vod = pygame.transform.rotate(Voda, rot)
    rot_rect.center = Vod.get_rect().center
    Vod = Vod.subsurface(rot_rect).copy()



class snaryad():
    def __init__(self,Px,Py):
        self.Px = Px
        self.Py= Py
    def draw(self,win):
        win.blit(Vod,(self.Px,self.Py))

#Функция правильного направления воды от угла поворота машины и определение начальных точек
def Prov(diriction):
    global Coint,Px,Py,MaxLen,k,t
    if diriction == "up":
        bullet.Px -= (20 * math.sin(rad_alfa))
        bullet.Py -= (20 * math.cos(rad_alfa))
        Px = CAR_X -20
        Py = CAR_Y-19
    elif diriction== "left":
        bullet.Px -= (20 * math.cos(rad_alfa))
        bullet.Py += (20 * math.sin(rad_alfa))
        Px = CAR_X -20
        Py = CAR_Y -20
    elif diriction == "right":
        bullet.Px += (20 * math.cos(rad_alfa))
        bullet.Py -= (20 * math.sin(rad_alfa))
        Px = CAR_X+20
        Py = CAR_Y -17
    else:
        bullet.Px += (20 * math.sin(rad_alfa))
        bullet.Py += (20 * math.cos(rad_alfa))
        Px = CAR_X-20
        Py = CAR_Y+18
    if Coint <=200:
        if Stolnovenie(bullet.Px, bullet.Py, Fx, Fy,50):
            MaxLen=15
            Coint+=1
            if Coint==200:
                k+=173+t
        #if Kust_VODA_STOP(bullet.Px, bullet.Py, X_KU):
            #MaxLen = 15

    else:
        MaxLen=20




def Koord_Fair(n):
    global Fx,Fy
    Fx=Houses[n].HouseX
    Fy= Houses[n].HouseY






def Rotate(direction): # Функция поворта спрайта головой вперед
    global Go_Car_New
    if direction == "right":
        Go_Car_New = [pygame.transform.rotate(Go_Car[0],270),pygame.transform.rotate(Go_Car[1],270)]
    elif direction == "left":
        Go_Car_New = [pygame.transform.rotate(Go_Car[0],-270),pygame.transform.rotate(Go_Car[1],-270)]
    elif direction == "up":
        Go_Car_New = [pygame.transform.rotate(Go_Car[0],0),pygame.transform.rotate(Go_Car[1],0)]
    elif direction == "down":
        Go_Car_New = [pygame.transform.rotate(Go_Car[0],180),pygame.transform.rotate(Go_Car[1],180)]


def Stolnovenie(Px,Py,Fx,Fy,A):
    if (Fy>Py-A) and (Fy<Py+A) and (Fx>Px-A) and (Fx<Px+A):
        return 1
    else:
        return 0




def Kust_STOP(CARX,CARY):
    global CAR_X,CAR_Y
    for kust in Kusts:
        if kust.ghost(CARX,CARY):
            CAR_X=kust.X_Kust
            CAR_Y=kust.Y_Kust+40

def Kust_VODA_STOP(VodaX,VodaY,X_KU):
    Kusts_random = [Kust(X_KU * 100, 210), Kust(X_KU * 100, 260), Kust(X_KU * 100, 310)]
    for kust in Kusts_random:
        if (kust.X_Kust > VodaX - 50) and (kust.X_Kust < VodaX + 50) and (kust.Y_Kust > VodaY - 50) and (kust.Y_Kust < VodaY + 50):
            return 1
        else:
            return 0
#Функция рисования
def DrowWindow():
    global CarCount,Sc,Stop_Car,Fx,Fy,Fair_Count,House_X,Hos,Home,i,k,X_KU
    win.blit(fon,(0,0))
    Score()

    for house in Houses:
        house.draw(win)
        house.render_Bar(win)
        #if house.Hp <= 0:
            #house.vzriv(win)


    if Hos==True:
        #if GoHom==True:
        i = random.choice(Homi)
        X_KU = random.randint(2, 7)
    if Coint<200:
        #Kust_random(X_KU)
        Hos=False
        if Fair_Count + 1 >= 10:
            Fair_Count = 0
        win.blit(Fair[Fair_Count // 5], (Fx, Fy))
        Fair_Count += 1

    else:
        Hos=True
        sound.stop()

    for bullet in bullets:
        bullet.draw(win)
    if CarCount + 1 >=10:
        CarCount =0
    if MOTOR_OFF==0:
        win.blit(Stop_Car,(CAR_X,CAR_Y))
        #обновление картинки

        Stop_Car.fill(0)
        Stop_Car = pygame.image.load('Car(0).png')
        Stop_Car.blit(Push, (PUSH_X, PUSH_Y))


        #Sc = 0
        #pygame.mixer.music.pause()

    else:
        global Go_Car
        Rotate(DIRECTION)
        win.blit(Go_Car_New[CarCount//5], (CAR_X, CAR_Y))
        Go_Car[CarCount//5].blit(Push, (PUSH_X, PUSH_Y))
        Go_Car[0].fill(0)
        Go_Car[1].fill(0)
        Go_Car = [pygame.image.load('Car(1).png'), pygame.image.load('Car(2).png')]
        Go_Car[CarCount // 5].blit(Push, (PUSH_X, PUSH_Y))
        CarCount+=1
    for kust in Kusts:
        kust.render()



    pygame.display.update()

'''Создание меню'''
punkts=[(400,140,u'Инструктаж',(255,0,0),(25,2,250),0),
         (400,240,u'Старт',(255,255,0),(25,2,250),1),
        (400,340,u'Выход',(255,255,0),(25,2,250),2)]
game=Menu(punkts)
game.menu()
'''После конца игры'''
punkts_GAMEOVER=[(630,600,u'Играть снова',(255,255,00),(25,2,250),3),
        (20,600,u'Выход',(255,0,00),(255,255,200),4)]



pygame.mixer.music.play(-1)
RUN=True
pygame.time.set_timer(27, 100)
pygame.time.set_timer(25, 10000)
pygame.time.set_timer(26,900)
#Игровой процесс
while RUN:
    clock.tick(30)
    if Proces(proces):
        Koord_Fair(i)
        TraficVod(DIRECTION)
        TrafficPush()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN=False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    MOTOR_OFF += 1
                    DIRECTION="up"

                    if MOTOR_OFF > 1:
                        MOTOR_OFF = 0
            if event.type==27:
                HomeDELE()

            elif event.type == 25:
                sound.play()
                Coint = 0

            elif event.type==26:
                if Coint <= 200:
                    DelHome(i)




            if event.type==pygame.KEYUP:
                if event.key==pygame.K_r:
                    Go=False

        DrowWindow()
        keys = pygame.key.get_pressed()

        if MOTOR_OFF == 1:
            Kust_STOP(CAR_X,CAR_Y)
            for house in Houses:
                if keys[pygame.K_a]:
                    if CAR_X>=15:
                        if house.ghost(CAR_X,CAR_Y):
                            CAR_X=house.HouseX+120
                        else:
                            CAR_X-=2
                        DIRECTION="left"
                elif keys[pygame.K_d]:
                    if CAR_X <=900:
                        if house.ghost(CAR_X, CAR_Y):
                            CAR_X = house.HouseX-50
                        else:
                            CAR_X+=2
                        DIRECTION="right"
                elif keys[pygame.K_w]:
                    if CAR_Y>=15:
                        if house.ghost(CAR_X, CAR_Y):
                            CAR_Y = house.HouseY+140
                        else:
                            CAR_Y-=2
                        DIRECTION="up"
                elif keys[pygame.K_s]:
                    if CAR_Y<=700:
                        if house.ghost(CAR_X, CAR_Y):
                            CAR_Y=house.HouseY-70
                        else:
                            CAR_Y+=2
                        DIRECTION="down"

        if keys[pygame.K_LEFT]:
            rot += 5
        elif keys[pygame.K_RIGHT]:
            rot -= 5

        for bullet in bullets:
            Prov(DIRECTION)
            if  bullet.Px > 1100 or bullet.Py > 901 or bullet.Px<-300 or bullet.Py<-300:
                MaxLen=5
            if len(bullets)> MaxLen or Go==False:
                bullets.remove(bullet)

        if keys[pygame.K_r]:
            Go=True
            MaxLen=20
            bullets.append(snaryad (Px,Py))
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        f3 = pygame.font.SysFont('serif', 300)
        text3 = f3.render('GAME', 0, (0, 0, 0))
        text4 = f3.render('OVER', 0, (0, 0, 0))
        win.blit(text3, (50, 60))
        win.blit(text4, (50, 310))
        gameOV = Menu(punkts_GAMEOVER)
        gameOV.menuGO()









pygame.quit()