import random


class GuessNumber:
    number = None
    randomize_number = None
    life = None
    victory = False
    level = {'easy': 9, 'normal': 6, 'hard': 3}


    def radomize_number(self):
        """
        Generate random number
        :return:
        """
        self.randomize_number = random.randrange(1, 16)


    def player_input_number(self):
        """
        Player input number
        :return:
        """
        self.number = int(input('Input number from 1 to 15: '))


    def number_of_lives(self):
        """
        Case  for level choose
        :return: self.life
        """
        while True:
            number = int(input('Choose your level (1 - easy / 2 - normal / 3 - hard): '))
            if number == 1:
                self.life = self.level['easy']
                print(f'Chosen level - easy, you have {self.level["easy"]} life\'s')
                return self.life
            elif number == 2:
                self.life = self.level['normal']
                print(f'Chosen level - normal, you have {self.level["normal"]} life\'s')
                return self.life
            elif number == 3:
                self.life = self.level['hard']
                print(f'Chosen level - hard, you have {self.level["hard"]} life\'s')
                return self.life
            else:
                print('You input wrong number! Please repeat input!')


    def game_logic(self, life):
        """
        Game logic, definition of number.
        :param life:
        :return:
        """
        count = 1
        self.radomize_number()
        print(f'You have {life} try\'s')
        while count <= life:
            print(f'Try number {count}')
            self.player_input_number()
            if self.number > self.randomize_number:
                print('The number is higher than hidden number!')
                count += 1
                continue
            elif self.number < self.randomize_number:
                print('The number is lower than hidden number!')
                count += 1
                continue
            else:
                print(f'You guessed the hidden number: {self.randomize_number}')
                self.victory = True
                break
        if self.victory:
            print(f'Congratulation!!! You win!!!')
        else:
            print(f'You lose, try another time!!!')


gn = GuessNumber()
life = gn.number_of_lives()
gn.game_logic(life)