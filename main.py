"""24.10.17
    24.10.18飞机跑道"""
import random


class FlyChess:
    def __init__(self, color: str, x: int, y: int):
        self.color = color
        self.move_x = 1
        self.move_y = 1
        self.position = [int(x), int(y)]

    def move(self):
        self.position[0] += self.move_x
        self.position[1] += self.move_y

    def move_change(self):
        change = True
        if self.position == [5, 0]:
            self.move_y = 1
            self.move_x = 0
        elif self.position == [11, 0]:
            self.move_y = 0
            self.move_x = -1
        elif self.position == [5, 5]:
            self.move_y = 0
            self.move_x = -1
        elif self.position == [11, 5]:
            self.move_y = -1
            self.move_x = 0
        elif self.position == [0, 5]:
            self.move_y = 1
            self.move_x = 0
        elif self.position == [16, 5]:
            self.move_y = 0
            self.move_x = -1
        elif self.position == [0, 11]:
            self.move_y = 0
            self.move_x = 1
        elif self.position == [16, 11]:
            self.move_y = -1
            self.move_x = 0
        elif self.position == [5, 11]:
            self.move_y = 1
            self.move_x = 0
        elif self.position == [11, 11]:
            self.move_y = 0
            self.move_x = 1
        elif self.position == [5, 16]:
            self.move_y = 0
            self.move_x = 1
        elif self.position == [11, 16]:
            self.move_y = -1
            self.move_x = 0
        else:
            change = False
        if change:
            self.move()


class PlaYer:
    def __init__(self, color: str):
        self.chess_color = color
        self.chess_amount = 4
        self.chess: list[FlyChess] = []
        print(str(color) + "色选手已就位")


# 玩家入场
red_player = PlaYer("红")
yellow_player = PlaYer("黄")
blue_player = PlaYer("蓝")
green_player = PlaYer("绿")
for i in range(2):
    red_player.chess.append(FlyChess("红", 15, 15 + i))
    yellow_player.chess.append(FlyChess("黄", 0, 15 + i))
    blue_player.chess.append(FlyChess("蓝", 0, 0 + i))
    green_player.chess.append(FlyChess("绿", 15, 0 + i))
for i in range(2, 4):
    red_player.chess.append(FlyChess("红", 16, 13 + i))
    yellow_player.chess.append(FlyChess("黄", 1, 13 + i))
    blue_player.chess.append(FlyChess("蓝", 1, -2 + i))
    green_player.chess.append(FlyChess("绿", 16, -2 + i))

# 生成棋盘
ground = [["一" for i in range(17)] for j in range(17)]
start_chess = FlyChess("红黄蓝绿", 16, 11)
start_chess.move_change()
tail = 0
ground[8][1:6] = ["蓝" for i in range(6)]
ground[8][10:17] = ["红" for i in range(6)]
for i in range(7):
    ground[i][8] = "绿"
    ground[16 - i][8] = "黄"
for i in range(64):
    start_chess.move()
    start_chess.move_change()
    ground[start_chess.position[0]][start_chess.position[1]] = start_chess.color[tail]
    tail = (tail + 1) % 4
for i in ground:
    print(" ".join(map(str, i)))

show_ground = ground
for i in range(4):
    show_ground[red_player.chess[i].position[0]][red_player.chess[i].position[1]] = "红"
    show_ground[yellow_player.chess[i].position[0]][yellow_player.chess[i].position[1]] = "黄"
    show_ground[blue_player.chess[i].position[0]][blue_player.chess[i].position[1]] = "蓝"
    show_ground[green_player.chess[i].position[0]][green_player.chess[i].position[1]] = "绿"
for i in show_ground:
    print(" ".join(map(str, i)))

head = 0
while True:
    x = int(input("请输入点数"))
    if x == 6:
        choice = input("前进，出发")
        if choice == "1":
            yellow_player.chess[head].position = [6,1]
            head += 1
        elif choice == "2":
            chess_choice = int(input("前进"))
            yellow_player.chess[chess_choice-1].move()
