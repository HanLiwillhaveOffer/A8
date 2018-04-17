from random import choice, randint
import random
def _3pointer_contest(_3PG):
    score=0
    for i in range(25):
        shoot = random.randint(1,sum(_3PG))
        if i<20:
            if shoot<=_3PG[0]:
                score+=1
            else:
                pass
        else:
            if shoot<=_3PG[0]:
                score+=2
            else:
                pass
    return score

def sort_dic(dic):
    return sorted(dic.items(),key = lambda item:item[1],reverse=True)

def get_game_result(candidate_number,player_list):
    threshold = 0
    score = 0
    result = {}
    next_round_candidate={}
    next_round_candidate_list = []
    for player in player_list:
        score = _3pointer_contest([player[1], player[2]])
        result[player[0]] = score
        print('{} got {} this round!'.format(player[0], score))
    threshold = sort_dic(result)[candidate_number-1][1]
    for key, value in result.items():
        if value >= threshold:
            next_round_candidate[key] = value
    for player in player_list:
        if player[0] in next_round_candidate.keys():
            next_round_candidate_list.append(player)
    return next_round_candidate_list

curry=['curry',70,30]
george=['george',65,35]
beal = ['beal',68,32]
thompson=['thompson',72,28]
gordan = ['gordan',69,31]
player_list = [curry,george,beal,thompson,gordan]
over_time_flag=True
highest_score=0
winner = ''
candidate_list = get_game_result(3,player_list)
print('The players in the final game are:')
for player in candidate_list:
    print(player[0])
candidate_list = get_game_result(1, candidate_list)
while over_time_flag:
    if len(candidate_list)==1:
        over_time_flag=False
    else:
        print('The players in the overtime game are:')
        for player in candidate_list:
            print(player[0])
        candidate_list=get_game_result(1,candidate_list)



print('The winner is {}!'.format(candidate_list[0][0]))







