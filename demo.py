from random import choice, randint
import random

class player():
    name=''
    _3PG = 0
    def __init__(self,name,_3PG):
        self.name = name
        self._3PG=_3PG

    def _3pointer_contest(self):
        """
        simulate the score based on the shooting percetage of the player
        :param _3PG: shooting percentage of a player
        :return: the simulated score of the player
        """
        score=0
        for i in range(25):
            shoot = random.randint(1,100)
            if i<20:
                if shoot<=self._3PG:
                    score+=1
                else:
                    pass
            else:
                if shoot<=self._3PG:
                    score+=2
                else:
                    pass
        return score

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
        #print('{} got {} this round!'.format(player[0], score))
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
    curry = player('curry', 70)
    george =player('george', 65)
    beal = player('beal',68)
    thompson = player('thompson',72)
    gorden = player('gorden',69)
    booker = player('booker',74)
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



