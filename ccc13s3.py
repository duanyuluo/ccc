"""CCC '13 S3 - Chances of Winning
Canadian Computing Competition: 2013 Stage 1, Junior #5, Senior #3

You want to determine the chances that your favourite team will be the champion of a small tournament.
There are exactly four teams. At the end of the tournament, a total of six games will have been played with each team playing every other team exactly once. For each game, either one team wins (and the other loses), or the game ends in a tie. If the game does not end in a tie, the winning team is awarded three points and the losing team is awarded zero points. If the game ends in a tie, each team is awarded one point.
Your favourite team will only be the champion if it ends the tournament with strictly more total points than every other team (i.e., a tie for first place is not good enough for your favourite team).
The tournament is not over yet but you know the scores of every game that has already been played. You want to consider all possible ways points could be awarded in the remaining games that have not yet been played and determine in how many of these cases your favourite team will be the tournament champion.
"""

import ccc

in_params = ccc.load_std_input_file("ccc13s3_2.log", ccc.tc_int)

fav_team_id = in_params[0][0]
finish_game_cnt = in_params[1][0]

score_board = [[] for i in range(4)]

def calc_score(team_me, team_other):
    if (team_me == team_other):
        return 1
    else:
        return team_me > team_other and 3 or 0

for i in range(2, finish_game_cnt+2):
    team_l, team_r = in_params[i][0], in_params[i][1]
    result_l, result_r = in_params[i][2], in_params[i][3]
    score_board[team_l-1].append(calc_score(result_l, result_r))
    score_board[team_r-1].append(calc_score(result_r, result_l))

cur_score_sum = [sum(n) for n in score_board]
cur_best_score = max(cur_score_sum)
cur_best_team = cur_score_sum.index(cur_best_score) + 1
cur_fav_score = cur_score_sum[fav_team_id-1]

fav_team_todo_games = 3 - len(score_board[fav_team_id-1])
fav_max_todo_score = fav_team_todo_games * 3

fav_max_total_score = cur_fav_score + fav_max_todo_score

if cur_best_team != fav_team_id and fav_max_total_score < cur_best_score:
    print(0)
else:
    print(fav_max_total_score)