import random


class TicTacToeAI:
    def __init__(self):
        self.players_type = {'user': self.user_play, 'easy': self.easy_play, 'medium': self.medium_play, 'hard': self.hard_play}
        self.tableau = [[' ' for _ in range(3)] for _ in range(3)]
        self.play()

    def affichage(self, tableau):
        print('-' * 9)
        print("| {} |".format(" ".join(tableau[0])))
        print("| {} |".format(" ".join(tableau[1])))
        print("| {} |".format(" ".join(tableau[2])))
        print('-' * 9)

    @staticmethod
    def check_empty(string, mark):
        if string.count(mark) == 2 and ' ' in string:
            return string.index(' ')
        else:
            return -1

    def winner(self, player):
        ch = ''.join([''.join(x) for x in self.tableau])
        if player * 3 in (ch[::4], ch[2:8:2], ch[::3], ch[1::3], ch[2::3], ch[:3], ch[3:6], ch[6:]):
            return True
        else:
            return False

    def end_game(self, tableau):
        tableau = ''.join([''.join(x) for x in tableau])
        test = True
        if (self.winner('X') and self.winner('O')) or abs(tableau.count('X') - tableau.count('O')) > 1:
            print("Impossible")
        elif not self.winner('X') and not self.winner('O') and (tableau.count('_') > 0 or tableau.count(' ') > 0):
            # print("Game not finished")
            test = False
        elif not self.winner('X') and not self.winner('O') and tableau.count('_') == 0 and tableau.count(' ') == 0:
            print("Draw")
        elif self.winner('X'):
            print("X wins")
        elif self.winner('O'):
            print("O wins")

        return test

    def easy_play(self, pion):
        print('Making move level "easy"')
        while True:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if self.tableau[x][y] in ('X', 'O'):
                pass
            else:
                self.tableau[x][y] = pion
                break

    def medium_play(self, pion):
        ch = ''.join([''.join(x) for x in self.tableau])
        print('Making move level "medium"')
        opponent_pion = 'X' if pion == 'O' else 'O'
        random_tour = True

        for mark in (pion, opponent_pion):
            # Lignes
            for i, line in enumerate(self.tableau):
                j = self.check_empty(''.join(line), mark)
                if j >= 0:
                    self.tableau[i][j] = pion
                    random_tour = False
                    break
            if not random_tour:
                break

            # Colonnes
            for i, line in enumerate(self.tableau):
                col = ''
                for j in range(len(line)):
                    col += self.tableau[j][i]
                k = self.check_empty(col, mark)
                if k >= 0:
                    self.tableau[k][i] = pion
                    random_tour = False
                    break
            if not random_tour:
                break

            # Diagonal principal
            if self.check_empty(ch[::4], mark) >= 0:
                i = self.check_empty(ch[::4], mark)
                self.tableau[i][i] = pion
                random_tour = False
                break

        while random_tour:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if self.tableau[x][y] in ('X', 'O'):
                pass
            else:
                self.tableau[x][y] = pion
                break
       
    def hard_play(self, pion):
        ch = ''.join([''.join(x) for x in self.tableau])
        print('Making move level "hard"')
        opponent_pion = 'X' if pion == 'O' else 'O'
        random_tour = True

        for mark in (pion, opponent_pion):

            # Lignes
            for i, line in enumerate(self.tableau):
                j = self.check_empty(''.join(line), mark)
                if j >= 0:
                    self.tableau[i][j] = pion
                    random_tour = False
                    break
            if not random_tour:
                break

            # Colonnes
            for i, line in enumerate(self.tableau):
                col = ''
                for j in range(len(line)):
                    col += self.tableau[j][i]
                k = self.check_empty(col, mark)
                if k >= 0:
                    self.tableau[k][i] = pion
                    random_tour = False
                    break
            if not random_tour:
                break

            # Diagonal principal
            if self.check_empty(ch[::4], mark) >= 0:
                i = self.check_empty(ch[::4], mark)
                self.tableau[i][i] = pion
                random_tour = False
                break

            # Diagonale secongaire
            if self.check_empty(ch[2:8:2], mark) == 0:
                self.tableau[0][2] = pion
                random_tour = False
                break
            elif self.check_empty(ch[2:8:2], mark) == 1:
                self.tableau[1][1] = pion
                random_tour = False
                break
            elif self.check_empty(ch[2:8:2], mark) == 2:
                self.tableau[2][0] = pion
                random_tour = False
                break

        while random_tour:
            x, y = random.randint(0, 2), random.randint(0, 2)
            if self.tableau[x][y] in ('X', 'O'):
                pass
            else:
                self.tableau[x][y] = pion
                break

    def user_play(self, carac):
        while True:
            coordonnates = input("Enter the coordinates: ").strip()
            if ' ' in coordonnates:
                x, y = coordonnates.split()[:2]
            else:
                x = y = coordonnates

            if not x.isdigit() or not y.isdigit():
                print("You should enter numbers!")
            else:
                if x not in '123' or y not in '123':
                    print("Coordinates should be from 1 to 3!")
                else:
                    x, y = int(x), int(y)
                    if self.tableau[x - 1][y - 1] in ('X', 'O'):
                        print("This cell is occupied! Choose another one!")
                    else:
                        self.tableau[x - 1][y - 1] = carac
                        break

    def play(self):

        while True:
            play_type = input("Input command: ").strip()
            self.tableau = [[' ' for _ in range(3)] for _ in range(3)]

            if play_type == 'exit':
                break
            else:
                play_type = play_type.split()
                if len(play_type) == 3 and play_type[0] == 'start' and play_type[1] in self.players_type and play_type[2] in self.players_type:
                    self.affichage(self.tableau)
                    while True:
                        self.players_type[play_type[1]]('X')
                        self.affichage(self.tableau)
                        if self.end_game(self.tableau):
                            break
                        else:
                            self.players_type[play_type[2]]('O')
                            self.affichage(self.tableau)
                            if self.end_game(self.tableau):
                                break
                    continue
                else:
                    print("Bad parameters!")


TicTacToeAI()
