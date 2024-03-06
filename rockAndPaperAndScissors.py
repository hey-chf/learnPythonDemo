import random


class Game:
    def __init__(self):
        # 获得计算机的选择
        self.computer_pick = self.get_computer_pick()
        # 获得用户的选择
        self.user_pick = self.get_user_pick()
        # 获得游戏的结果
        self.result = self.get_result()

    def get_computer_pick(self):
        # 在1、2和3中获得随机数
        random_number = random.randint(1, 3)

        # 可能的选项
        options = {1: 'rock', 2: 'paper', 3: 'scissors'}

        # 返回存在于随机数的值
        return options[random_number]

    def get_user_pick(self):

        # 无限次循环
        while True:
            user_pick = input("input,rock/paper/scissors：")

            # 转换为小写字母
            user_pick = user_pick.lower()

            # 如果user_pick是石头或剪刀或布。
            # 终止循环
            if user_pick in ('rock', 'paper', 'scissors'):
                break
            else:
                print('错误的输入！')

        return user_pick

    def get_result(self):
        if self.computer_pick == self.user_pick:
            return '平'

        # 用户获胜的条件
        elif self.user_pick == 'paper' and self.computer_pick == 'rock':
            return "赢"
        elif self.user_pick == 'rock' and self.computer_pick == 'scissors':
            return '赢'
        elif self.user_pick == 'scissors' and self.computer_pick == ' pick':
            return '赢'
        # 在所有其他情况下，用户都会输
        else:
            return '输'

    def print_result(self):
        print(f"计算机的选择：{self.computer_pick}")
        print(f'你的选择：{self.user_pick}')
        print(f'你{self.result}了')


# 创建一个游戏类的对象
while True:
    game = Game()
    game.print_result()

    play_again = input('继续玩游戏？(y)')
    # 如果用户输入除y以外的任何其他字符，游戏结束
    if play_again != 'y':
        break
