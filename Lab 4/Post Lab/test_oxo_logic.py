import unittest, os
from OXO import oxo_logic

class TestLogic(unittest.TestCase):
    def setUp(self):
        self.game = oxo_logic.newGame()
        
        home = os.environ['HOMEPATH'] or os.environ['HOME']
        self.gamepath = os.path.join(home, "oxogame.dat")
        
        if(os.path.exists(self.gamepath)):
            os.remove(self.gamepath)
        
    def tearDown(self):
        if(os.path.exists(self.gamepath)):
            os.remove(self.gamepath)
    
    def test_saveGame_checkIfGameHasBeenSaved(self):
        oxo_logic.saveGame(self.game)
        self.assertTrue(os.path.exists(self.gamepath))
    
    def test_restoreGame_returnEmptyGameIfSavedGameDoesNotExist(self):
        self.assertEqual(oxo_logic.restoreGame(), self.game)
        
    def test_restoreGame_returnNewGameIfSavedGameIsCorrupted(self):
        self.assertEqual(oxo_logic.restoreGame(), self.game)
    
    def test_restoreGame_returnSavedGame(self):
        oxo_logic.saveGame(self.game)
        saved_game = oxo_logic.restoreGame()
        self.assertEqual(len(saved_game), 9)
        self.assertIsInstance(saved_game, list)
    
    # User's Moves
    def test_userMove_insertXAtCellIfEmpty(self):
        oxo_logic.userMove(self.game, 0)
        self.assertEqual(self.game[0], 'X')
    
    def test_userMove_errorMsgIfCellIsNotEmpty(self):
        oxo_logic.userMove(self.game, 0)
        with self.assertRaises(ValueError) as ve:
            oxo_logic.userMove(self.game, 0)
        self.assertEqual(str(ve.exception), 'Invalid cell')
        
    def test_userMove_returnXIfWinningMove(self):
        oxo_logic.userMove(self.game, 0)
        oxo_logic.userMove(self.game, 1)
        actual = oxo_logic.userMove(self.game, 2)
        self.assertEqual(actual, 'X')
        
    def test_userMove_returnEmptryStringIfNotWinningMove(self):
        self.assertEqual(oxo_logic.userMove(self.game, 0), "")
    
    # Computer's Moves
    def test_computerMove_insertOAtCellIfEmpty(self):
        oxo_logic.computerMove(self.game)
        self.assertIn('O', self.game)
        
    def test_computerMove_returnDIfAllCellsAreTaken(self):
        self.game[:] = ['X'] * 10
        self.assertEqual(oxo_logic.computerMove(self.game), 'D')
        
    def test_computerMove_returnOIfWinningMove(self):
        self.game[0:8] = ['O'] * 8
        self.assertEqual(oxo_logic.computerMove(self.game), 'O')
        
    def test_computerMove_returnEmptryStringIfNotWinningMove(self):
        self.assertEqual(oxo_logic.computerMove(self.game), "")

if __name__ == '__main__':
    unittest.main()