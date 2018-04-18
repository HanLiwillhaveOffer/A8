from random import choice, randint
import random
import math

class player():
    name=''
    _3PG = 0
    stamina = 0
    on_fire_prob = 0
    growing = 1
    def __init__(self,name,_3PG, stamina,on_fire_prob,growing,bonus=5,strategy=1):
        self.name = name
        self._3PG=_3PG
        self.stamina= stamina
        self.on_fire_prob = on_fire_prob
        self.growing=growing
        self.bonus = bonus
        self.strategy = strategy

    def _3pointer_contest(self):
        """
        simulate the score based on the shooting percetage of the player
        :param _3PG: shooting percentage of a player
        :return: the simulated score of the player
        """
        score=0
        offset = 0
        state=1
        lefttime = 60.0
        for i in range(25):
            shoot = random.randint(1,100)
            runtime = self.runtime(i)
            shootingtime = self.shootingtime(i, lefttime)
            if i in range(self.bonus*5-4 ,self.bonus*5+1):
                if shoot<=self._3PG*(1-self.stamina/100*(i))*state*math.log2(0.5*shootingtime+1):
                    score+=2
                    offset+=2
                else:
                    offset-=3
            else:
                if shoot<=self._3PG*(1-self.stamina/100*(i))*state*math.log2(0.5*shootingtime+1):
                    score+=1
                    offset+=2
                else:
                    offset-=3
            state = self.get_on_fire_state(offset)
            lefttime -= shootingtime + runtime
        return score


    def get_on_fire_state(self,offset):
        prob = random.randint(1,100)
        if prob<(self.on_fire_prob+offset):
            state = self.growing
            #print(self.name+ " is onfire")
        else:
            state= 1
        return state

    def runtime(self, i):
        if (i + 1) % 5 == 0 and i < 24:
            runtime = random.uniform(2, 4)
        else:
            runtime = 0
        return runtime

    def shootingtime(self, i, lefttime):
        if self.strategy == 1:
            shootingtime = random.uniform(1, lefttime/(25-i))
        elif self.strategy == 2:
            if i in range(self.bonus * 5 - 4, self.bonus * 5 + 1):
                shootingtime = random.uniform(1, lefttime / (25 - i)) * 2
            else:
                shootingtime = random.uniform(1, lefttime/(25-i))
        elif self.strategy == 3:
            if i in range(10):
                shootingtime = random.uniform(1, lefttime / (25 - i)) * 1.5
            else:
                shootingtime = random.uniform(1, lefttime / (25 - i))
        elif self.strategy == 4:
            if i in range(10):
                shootingtime = random.uniform(1 / 0.8, lefttime / (25 - i)) * 0.8
            else:
                shootingtime = random.uniform(1, lefttime / (25 - i))
        return shootingtime


def sort_dic(dic):
    """
    get the sorted game result based on the socres
    :param dic: the game result
    :return: the sorted game result
    """
    return sorted(dic.items(),key = lambda item:item[1],reverse=True)

def get_game_result(candidate_number,player_list):
    """
    To get the player list of next round based on the number of required candidate and the player list of current round.
    :param candidate_number: the number of required candidate
    :param player_list: the player list of current round
    :return: the player list of next round
    """
    threshold = 0
    score = 0
    result = {}
    next_round_candidate={}
    next_round_candidate_list = []
    for player in player_list:
        score = player._3pointer_contest()
        result[player.name] = score
        print('{} got {} this round!'.format(player.name, score))
    threshold = sort_dic(result)[candidate_number-1][1]
    for key, value in result.items():
        if value >= threshold:
            next_round_candidate[key] = value
    for player in player_list:
        if player.name in next_round_candidate.keys():
            next_round_candidate_list.append(player)
    return next_round_candidate_list

def one_simulation():
    """
    Simulate one game
    :return: the winner of the game
    """
    curry = player('curry', 70,1,15,1.28,1,4)
    george =player('george', 65,1,25,1.38)
    beal = player('beal',68,1,22,1.32)
    thompson = player('thompson',72,0.5,10,1.25)
    gorden = player('gorden',69,1.5,13,1.3)
    booker = player('booker',74,1.5,18,1.21)

    player_list = [curry,george,beal,thompson,gorden,booker]
    over_time_flag=True
    candidate_list = get_game_result(3,player_list)
    #print('The players in the final game are:')
    candidate_list = get_game_result(1, candidate_list)
    while over_time_flag:
        if len(candidate_list)==1:
            over_time_flag=False
        else:
            #print('The players in the overtime game are:')
            #for player in candidate_list:
                #print(player[0])
            candidate_list=get_game_result(1,candidate_list)


    winner = candidate_list[0].name
    #print('The winner is {}!'.format(candidate_list[0][0]))
    return winner


def main():
    winner_list = []
    for i in range(10000):
        winner_list.append(one_simulation())
    print('The winning rate of curry is {}.'.format(winner_list.count('curry')/len(winner_list)))
    print('The winning rate of george is {}.'.format(winner_list.count('george') / len(winner_list)))
    print('The winning rate of beal is {}.'.format(winner_list.count('beal') / len(winner_list)))
    print('The winning rate of thompson is {}.'.format(winner_list.count('thompson') / len(winner_list)))
    print('The winning rate of gorden is {}.'.format(winner_list.count('gorden') / len(winner_list)))
    print('The winning rate of booker is {}.'.format(winner_list.count('booker') / len(winner_list)))
if __name__ == '__main__':
    main()



