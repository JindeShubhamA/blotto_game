###### Rock papaer scissor ###########
import random
import math
from . import TOM
from . import game

def rps_run(total_no_of_runs,p1order,p2order):
    """ variable decleration """
    turn=0
    p1=0
    p2=0
    rps={1:"rock",2:"paper",3:"scissor"}
    count=1 # run/round count
    p1_order=p1order # order of player one here it is zero order
    p2_order=p2order # order of plater two here it is first order
    p1_ch=[] # player 1 choice
    p2_ch=[] # player 2 choice
    tom=TOM.tom() # calling the TOM function
    a=game.rps_game()
    res_limit=5 # limit for the order of agents trails
    t_runs=total_no_of_runs # total number of runs
    file_to_save_result="result.txt" # storage file for the output of each game result
    print("########--------------------------------------------------------########")
    print("This is an rock paper scissor game ---------- the choice are \
         \n 1:Rock \n 2.scissor \n 3.paper \n \
        each player need to choose one of the above options  ")
    print("------------------------------------------------------------------------")
    print("For the rest of the game \n 1=Rock \n 2=paper \n 3=scissor")
    with open(file_to_save_result,'a') as result:
        result.write("In the game \n 1=Rock \n 2=paper \n 3=scissor \n")
        result.write("\n")
    print("------------------------------------------------------------------------")

    while (count <= t_runs):
        print("Round :",count)
        while turn < 2:
            if turn == 0:
                print("player one turn -------->")
                if count > res_limit:
                    p1=tom.agents_functionality("p1",p1_order,p1_ch,p2_ch)
                    print("player one ("+str(p1_order)+" order) choice at round "+str(count)+":",rps[p1])
                    p1_ch.append(p1)
                else:
                    p1=random.randint(1,3)
                    print("player one choice at round "+ str(count) +":",rps[p1])
                    p1_ch.append(p1)
            if turn == 1:
                print("player two turn -------->")
                if count > res_limit:
                    p2=tom.agents_functionality("p2",p2_order,p1_ch,p2_ch)
                    print(p2)
                    print("player two ("+str(p2_order)+" order) choice at round "+str(count)+":",rps[p2])
                    p2_ch.append(p2)
                else:
                    p2=random.randint(1,3)
                    print("player two choice at round "+str(count)+":",rps[p2])
                    p2_ch.append(p2)
            turn+=1

         # game running part
        a.game(p1,p2)
        #print("The winner is : ",a.compute_res())
        count+=1
        turn=0


    game_summary,score_p1,score_p2=a.compute_res()

    with open(file_to_save_result,'a') as result:
        result.write("The choices of player 1 :")
        result.write(str(p1_ch))
        result.write("\n")
        result.write("The choices of player 2 :")
        result.write(str(p2_ch))
        result.write("\n")
        result.write("The result of the game :")
        result.write(str(game_summary))
        result.write("\n")

    print("The choices of player 1 :",p1_ch)
    print("The choices of player 2 :",p2_ch)
    print(score_p1)
    print(score_p2)
    print("The result of the game :",game_summary)

    return score_p1,score_p2

#run(20,0,1)