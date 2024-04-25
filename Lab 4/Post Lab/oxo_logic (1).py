''' 
The oxo‐logic.py module is now converted to reflect OOP design by creating a Game class.
'''

import os, random
import oxo_data

class Game:
    def __init__(self):
        self.board = list(" " * 9)

    def saveGame(self):
        ' save game to disk '
        oxo_data.saveGame(self.board)
        
    def restoreGame(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.board = game
            else: 
                self.board = list(" " * 9)
        except IOError:
            self.board = list(" " * 9)
        
    def _generateMove(self):
        ''' generate a random cell from thiose available.
            If all cells are used return -1'''
        options = [i for i in range(len(self.board)) if  self.board[i] == " "]
        if options: return random.choice(options)
        else: return -1
        
    def _isWinningMove(self):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a,b,c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == player*3:
                return True
        return False

    def userMove(self,cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self._isWinningMove("X"):
            return 'X'
        else:
            return ""

    def computerMove(game):
        cell = self._generateMove()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._isWinningMove('O'):
            return 'O'
        else:
            return ""

    def test(self):
        result = ""
        while not result:
            print(self.board)
            try:
                result = self.userMove(self._generateMove())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computerMove()
                
            if not result: continue
            elif result == 'D':
                print("Its a draw")
            else:
                print("Winner is:", result)
            print(self.board)

if __name__ == "__main__":
    game = Game()
    game.play()

            
