
score_map = {
    # ROCK 
    "X":
    {
        # ROCK
        "A" : 3 + 1,
        # PAPER
        "B" : 0 + 1,
        # SCISSOR
        "C" : 6 + 1,
    },

    # PAPER
    "Y" :
    {
        "A" : 6 + 2,
        "B" : 3 + 2,
        "C" : 0 + 2,
    },

    # SCISSOR
    "Z":
    {
        "A" : 0 + 3,
        "B" : 6 + 3,
        "C" : 3 + 3,
    }
}

win_lose_map = {
    # ROCK 
    "A":
    {
        # PAPER
        "Z" : 6 + 2,
        # ROCK
        "Y" : 3 + 1,
        # SCISSOR
        "X" : 0 + 3,
    },

    # PAPER
    "B" :
    {
        "Z" : 6 + 3,
        "Y" : 3 + 2,
        "X" : 0 + 1,
    },

    # SCISSOR
    "C":
    {
        "Z" : 6 + 1,
        "Y" : 3 + 3,
        "X" : 0 + 2,
    }
}

# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win

total_1 = 0
total_2 = 0
game_scores_1 = []
game_scores_2 = []
with open("input.txt") as file:
    for l in file:
        if l != "\n":
            a = l.strip("\n").split(" ")
            
            # game 1
            game_score_1 = score_map[a[1]][a[0]]
            game_scores_1.append(game_score_1)
            total_1 = total_1 + game_score_1

            # game 2
            game_score_2 = win_lose_map[a[0]][a[1]]
            game_scores_2.append(game_score_2)
            total_2 = total_2 + game_score_2


print(total_1)

print(total_2)
