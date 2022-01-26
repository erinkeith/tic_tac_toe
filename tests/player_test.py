import unittest
import player


class TestUpdatePlayer(unittest.TestCase):
    
    def test_update_row5_col5(self)
        player = Player()
        
        player.update(5, 5)
        
        self.assertEqual(player.__top_horizontal, 0)
        self.assertEqual(player.__right_vertical, 0)
        self.assertEqual(player.__upper_right_diagonal, 0)
    
    def test_update_row0_col2(self)
        player = Player()
        
        # should be scenario 2
        player.update(0, 2)
        
        self.assertEqual(player.__top_horizontal, 1)
        self.assertEqual(player.__right_vertical, 1)
        self.assertEqual(player.__upper_right_diagonal, 1)
    
    def test_update_row0_col2_row0_col1(self)
        player = Player()
        
        # should be scenario 2
        player.update(0, 2)
        
        # should be scenario 1
        player.update(0, 1)
        
        self.assertEqual(player.__top_horizontal, 2)
        self.assertEqual(player.__mid_vertical, 1)
        self.assertEqual(player.__right_vertical, 1)
        self.assertEqual(player.__upper_right_diagonal, 1)
    
    def test_update_row0_col2_row0_col1_row0_col0(self)
        player = Player()
        
        # should be scenario 2
        player.update(0, 2)
        
        # should be scenario 1
        player.update(0, 1)
        
        # should be scenario 0
        player.update(0, 0)
        
        self.assertEqual(player.__top_horizontal, 3)
        self.assertEqual(player.__left_vertical, 1)
        self.assertEqual(player.__mid_vertical, 1)
        self.assertEqual(player.__right_vertical, 1)
        self.assertEqual(player.__upper_left_diagonal, 1)
        self.assertEqual(player.__upper_right_diagonal, 1)
        
        
class TestIsWinner(unittest.TestCase):
    
    def test_win_top_horizontal(self)
        player = Player()
        
        # should be scenario 2
        player.update(0, 2)
        
        # should be scenario 1
        player.update(0, 1)
        
        # should be scenario 0
        player.update(0, 0)
        
        self.assertTrue(player.is_winner())
    
    def test_not_win_top_horizontal(self)
        player = Player()
        
        # should be scenario 2
        player.update(0, 2)
        
        # should be scenario 1
        player.update(0, 1)
        
        self.assertFalse(player.is_winner())
