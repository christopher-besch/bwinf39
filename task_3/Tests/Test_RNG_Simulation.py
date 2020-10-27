import unittest
from RNG_Simulation import play_RNG

class Test_play_RNG(unittest.TestCase):
    def test_2(self):
        players=[0,1]
        skill_levels=[2,6]
        n=1000
        average_player1=skill_levels[0]/(skill_levels[0]+skill_levels[1])
        average_player2=skill_levels[1]/(skill_levels[0]+skill_levels[1])
        count_wins_player1=0
        count_wins_player2=0
        for _ in range(n):
            winning_player=play_RNG(players[0],players[1],skill_levels)
            if(winning_player==0):
                count_wins_player1+=1
            else:
                count_wins_player2+=1
        self.assertAlmostEqual(count_wins_player1/n,average_player1,1)
        self.assertAlmostEqual(count_wins_player2/n,average_player2,1)



