"""24.10.17
    24.10.18飞机跑道"""
import random
import time


class FlyChess:
    def __init__(self, color: str, x: int, y: int, h: list, jump: list, turn: list):
        self.color = color
        self.move_x = 1
        self.move_y = 1
        self.position = [int(x), int(y)]
        self.resurrection = h
        self.taking_off = True
        self.jump = jump
        self.turn = turn
        self.turn_judge = False

    def move(self):
        self.position[0] += self.move_x
        self.position[1] += self.move_y

    def move_change(self):
        change = True
        if self.position == [5, 0] or self.position == [0, 5] or self.position == [5, 11]:
            self.move_y = 1
            self.move_x = 0
        elif self.position == [11, 0] or self.position == [5, 5] or self.position == [16, 5]:
            self.move_y = 0
            self.move_x = -1
        elif self.position == [11, 5] or self.position == [16, 11] or self.position == [11, 16]:
            self.move_y = -1
            self.move_x = 0
        elif self.position == [0, 11] or self.position == [5, 16] or self.position == [11, 11]:
            self.move_y = 0
            self.move_x = 1
        else:
            change = False
        if change and self.position != self.resurrection:
            self.move()

    def final_move(self, pace: int):  # pace 是 前进距离
        global player_head
        def_rush = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        self.move_x = def_rush[player_head][0]
        self.move_y = def_rush[player_head][1]
        for i in range(pace):
            if abs(self.position[0] - self.turn[0]) == 6:
                self.move_x = -self.move_x
            if abs(self.position[1] - self.turn[1]) == 6:
                self.move_y = -self.move_y
            self.move()
        if abs(self.position[0] - self.turn[0]) == 6 or abs(self.position[1] - self.turn[1]) == 6:
            print("目的抵达")
            self.position = [8, 8]


class PlaYer:
    def __init__(self, color: str):
        self.chess_color = color
        self.chess_amount = 4
        self.chess: list[FlyChess] = []
        print(str(color) + "色选手已就位")


def generate_ground():
    # 生成棋盘
    basic_ground = [["一" for i in range(17)] for j in range(17)]
    start_chess = FlyChess("红黄蓝绿", 16, 11, [0, 0], [0, 0], [0, 0])
    start_chess.move_change()
    tail = 0
    basic_ground[8][1:6] = ["蓝" for i in range(6)]
    basic_ground[8][10:17] = ["红" for i in range(6)]
    for i in range(7):
        basic_ground[i][8] = "绿"
        basic_ground[16 - i][8] = "黄"
    for i in range(64):
        start_chess.move()
        start_chess.move_change()
        basic_ground[start_chess.position[0]][start_chess.position[1]] = start_chess.color[tail]
        tail = (tail + 1) % 4
    return basic_ground


def generate_show_ground():
    showground = generate_ground()
    showground[11][4] = "宏"
    showground[4][5] = "凰"
    showground[5][12] = "岚"
    showground[12][11] = "律"
    return showground


# 玩家入场
red_player = PlaYer("红")
yellow_player = PlaYer("黄")
blue_player = PlaYer("蓝")
green_player = PlaYer("绿")
player_list = [red_player, yellow_player, blue_player, green_player]
for i in range(2):
    red_player.chess.append(FlyChess("红", 15, 15 + i, [11, 16], [11, 4], [8, 16]))
    yellow_player.chess.append(FlyChess("黄", 15, 0 + i, [16, 5], [4, 5], [16, 8]))
    blue_player.chess.append(FlyChess("蓝", 0, 0 + i, [5, 0], [5, 12], [8, 0]))
    green_player.chess.append(FlyChess("绿", 0, 15 + i, [0, 11], [12, 11], [0, 8]))
for i in range(2, 4):
    red_player.chess.append(FlyChess("红", 16, 13 + i, [11, 16], [11, 4], [8, 16]))
    yellow_player.chess.append(FlyChess("黄", 16, -2 + i, [16, 5], [4, 5], [16, 8]))
    blue_player.chess.append(FlyChess("蓝", 1, -2 + i, [5, 0], [5, 12], [8, 0]))
    green_player.chess.append(FlyChess("绿", 1, 13 + i, [0, 11], [12, 11], [0, 8]))
ground = generate_ground()
show_ground = generate_show_ground()

# 飞机降落飞机场
for i in range(4):
    ground[red_player.chess[i].position[0]][red_player.chess[i].position[1]] = "红"
    ground[yellow_player.chess[i].position[0]][yellow_player.chess[i].position[1]] = "黄"
    ground[blue_player.chess[i].position[0]][blue_player.chess[i].position[1]] = "蓝"
    ground[green_player.chess[i].position[0]][green_player.chess[i].position[1]] = "绿"
head = 0
player_head = 1
remain_mount = 0
# 主程序
while True:
    move_player = yellow_player
    print("现在是" + str(move_player.chess_color) + "方的回合")
    take_off = False
    # 移动前
    for j in show_ground:
        print(" ".join(map(str, j)))
    # player_head += 1
    dice_mount = random.randint(1, 6)
    print("骰子点数是" + str(dice_mount))
    if dice_mount == 6:
        take_off = input("出发，前进")
        # player_head -= 1
    if take_off == "1":
        if head <= 3:
            move_player.chess[head].position = [16, 5]
            move_player.chess[head].taking_off = False
            print("第" + str(head) + "起飞")
            if move_player.chess[head].color == "黄":
                move_player.chess[head].move_x = -1
                move_player.chess[head].move_y = 0
            head += 1
        else:
            print("还有飞机？")
            time.sleep(5)
    # 移动
    else:
        chess_choice = int(input("选择棋子序号1-4"))
        if move_player.chess[chess_choice - 1].position == [8, 8]:
            print("再起？")
            continue
        if not move_player.chess[chess_choice - 1].taking_off:
            if move_player.chess[chess_choice - 1].turn_judge:
                move_player.chess[chess_choice - 1].final_move(int(dice_mount))
            for i in range(dice_mount):
                # 移动
                if not move_player.chess[chess_choice - 1].turn_judge:
                    move_player.chess[chess_choice - 1].move()
                    move_player.chess[chess_choice - 1].move_change()
                # 最后冲刺判定
                if move_player.chess[chess_choice - 1].position == move_player.chess[chess_choice - 1].turn or \
                        move_player.chess[chess_choice - 1].turn_judge:
                    move_player.chess[chess_choice - 1].turn_judge = True
                    remain_mount = dice_mount - i - 1
                    break
            if move_player.chess[chess_choice - 1].turn_judge:
                move_player.chess[chess_choice - 1].final_move(int(remain_mount))
            chess_position = move_player.chess[chess_choice - 1].position

            # 飞12
            if chess_position == move_player.chess[chess_choice - 1].jump:
                for j in range(12):
                    move_player.chess[chess_choice - 1].move()
                    move_player.chess[chess_choice - 1].move_change()
                print("飞12格")
            # 飞4格
            if str(ground[chess_position[0]][chess_position[1]]) == move_player.chess[chess_choice - 1].color:
                if not move_player.chess[chess_choice - 1].turn_judge:
                    for j in range(4):
                        move_player.chess[chess_choice - 1].move()
                        move_player.chess[chess_choice - 1].move_change()
                print("飞4格")
        else:
            print("你的飞机是跑车吗")
            time.sleep(50)
    show_ground = generate_show_ground()
    show_ground[move_player.chess[0].position[0]][move_player.chess[0].position[1]] = "壹"
    show_ground[move_player.chess[1].position[0]][move_player.chess[1].position[1]] = "二"
    show_ground[move_player.chess[2].position[0]][move_player.chess[2].position[1]] = "三"
    show_ground[move_player.chess[3].position[0]][move_player.chess[3].position[1]] = "四"

    # 棋子移动后的棋盘
    print("移动后")
    for i in show_ground:
        print(" ".join(map(str, i)))
    # player_head = player_head % 4
