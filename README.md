# score_predictor
Problem Statement:- To build a system that predicts win percentage of a team before the start of the match and during a match. Phase 1 would be to deal with calculating the win percentage of both teams just before the start of the match. 

The win percentage could be calculated by first calculating the predicted scores of both the teams on the basis of several parameters, The difference in both teams score could be used to calculate the percentage of win. Higher the diff. in predicted scores -> More are the chances for a team to win,

Parameters for Score Prediction:

1. Average Batting Ability of players 
2. Average Bowling Ability of opposite team
3. Home or Away
4. Toss
5. Average runs at venue batting first/second
...To be added (Factors to be kept limited at first)

The difference in predicted scores can be used to assign a percentage according to:- 
If X score is more
Win percent of Team X = 50 + Func(Diff in scores,Mean of scores) %
Win percent of Team Y = 50 - Func(Diff in score,Mean of scores) %

Func can be a linear function with adjusted constants.


Consideration for Models for score prediction:- 
The number of Odis played after 2000 are about 2200 -> 4400 innings.
If we exclude the rain affected matches we would have around 3500 innings of proper 50 over data.
