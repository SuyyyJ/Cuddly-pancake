import pygame
import random
import sys

class Settings:
    def __init__(self):
        self.picture_num = 4
        self.screen_width = 408
        self.screen_length = 809
        self.picture_length = 100
        self.screen_bgcol = (96, 127, 255)
        self.picture_speed = 5
        self.picture_bian = 1
        self.picture_distance = 102

class Picture:
    def __init__(self, num):
        self.picture_name = 'images/p{}.gif'.format(num)
        self.picture = pygame.image.load(self.picture_name)
        self.picture_rect = self.picture.get_rect()
    def display_picture(self, screen, x, y):
        self.picture_rect.x = x
        self.picture_rect.y = y
        screen.blit(self.picture, self.picture_rect)
'''def data_begin(data,p0):
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    ns = 16
    for i in range(4):
        for j in range(4):
            num = random.randint(0, ns-1)
            ns -= 1
            data[i][j] = n.pop(num)
            if data[i][j] == 16:
                p0[0] = i
                p0[1] = j'''
def data_begin(caozuoshu, p0, data):
    for i in caozuoshu:
        move(i, p0, data)

def move(i, p0, data):
    if i == 3 and p0[1] > 0:
        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0]][p0[1]-1]
        data[p0[0]][p0[1]-1] = t
        p0[1] -= 1
    elif i == 4 and p0[1] < 3:
        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0]][p0[1]+1]
        data[p0[0]][p0[1]+1] = t
        p0[1] += 1
    elif i == 1 and p0[0] > 0:
        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0]-1][p0[1]]
        data[p0[0]-1][p0[1]] = t
        p0[0] -= 1
    elif i == 2 and p0[0] < 3:
        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0]+1][p0[1]]
        data[p0[0]+1][p0[1]] = t
        p0[0] += 1

def create_caozuoshu():
    n = 30
    caozuo = [1, 2, 3, 4]
    caozuoshu = []
    for i in range(n):
        caozuoshu.append(random.choice(caozuo))
    return caozuoshu

def create_pictures(picture, data, set):
    for i in range(set.picture_num):
        for j in range(set.picture_num):
            p = Picture(data[i][j])
            picture[i][j] = p

def screen_updata(picture, screen, set, yuantu):
    screen.fill(set.screen_bgcol)
    x, y = 402, set.picture_bian
    for i in range(set.picture_num):
        for j in range(set.picture_num):
            picture[i][j].display_picture(screen, x, y)
            x += set.picture_distance
        x = 402
        y += set.picture_distance
    yuantu.display_picture(screen, 1, 4)
    pygame.display.flip()

def screen_create(set):
    pygame.init()
    screen = pygame.display.set_mode((set.screen_length, set.screen_width))
    pygame.display.set_caption("拼图")
    return screen

def game_over(data, set,bushu):
    datao = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
    for i in range(set.picture_num):
        for j in range(set.picture_num):
            if datao[i][j] != data[i][j]:
                return True
    print("牛逼！\n 游戏结束！\n 步数：{}".format(bushu[0]))
    return False

def updata(xinhao, picture, p0, data):
    if xinhao == 3:
        tmp = picture[p0[0]][p0[1]]
        picture[p0[0]][p0[1]] = picture[p0[0]][p0[1]-1]
        picture[p0[0]][p0[1]-1] = tmp

        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0]][p0[1]-1]
        data[p0[0]][p0[1]-1] = t
        p0[1] -= 1

    elif xinhao == 4:
        tmp = picture[p0[0]][p0[1]]
        picture[p0[0]][p0[1]] = picture[p0[0]][p0[1] + 1]
        picture[p0[0]][p0[1] + 1] = tmp

        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0]][p0[1]+1]
        data[p0[0]][p0[1]+1] = t
        p0[1] += 1
    elif xinhao == 1:
        tmp = picture[p0[0]][p0[1]]
        picture[p0[0]][p0[1]] = picture[p0[0] - 1][p0[1]]
        picture[p0[0] - 1][p0[1]] = tmp

        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0]-1][p0[1]]
        data[p0[0]-1][p0[1]] = t
        p0[0] -= 1
    elif xinhao == 2:
        tmp = picture[p0[0]][p0[1]]
        picture[p0[0]][p0[1]] = picture[p0[0] + 1][p0[1]]
        picture[p0[0] + 1][p0[1]] = tmp

        t = data[p0[0]][p0[1]]
        data[p0[0]][p0[1]] = data[p0[0] + 1][p0[1]]
        data[p0[0] +1][p0[1]] = t
        p0[0] += 1
    #print(data)

def check_events(picture, p0, data, bushu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and game_over(data, set, bushu):
            if event.key == pygame.K_DOWN and p0[0] > 0:
                xinhao = 1
                bushu[0] += 1
                updata(xinhao, picture, p0, data)
            elif event.key == pygame.K_UP and p0[0] < 3:
                xinhao = 2
                bushu[0] += 1
                updata(xinhao, picture, p0, data)
            elif event.key == pygame.K_RIGHT and p0[1] > 0:
                xinhao = 3
                bushu[0] += 1
                updata(xinhao, picture, p0, data)
            elif event.key == pygame.K_LEFT and p0[1] < 3:
                xinhao = 4
                bushu[0] += 1
                updata(xinhao, picture, p0, data)

if __name__ == '__main__':
    set = Settings()
    # 初始数据
    data = [[9, 1, 3, 4],
            [2, 16, 14, 8],
            [6, 10, 5, 12],
            [13, 7, 11, 15]]
    p0 = [1, 1]
    caozuoshu = create_caozuoshu()
    data_begin(caozuoshu, p0, data)
    bushu = [0]
    # 创建图片
    picture = [[None, None, None, None],
               [None, None, None, None],
               [None, None, None, None],
               [None, None, None, None]]
    yuantu = Picture(12)
    create_pictures(picture, data, set)
    # 创建窗口
    screen = screen_create(set)

    # 游戏主循环
    while True:
        check_events(picture, p0, data, bushu)
        screen_updata(picture, screen, set, yuantu)

