#!/usr/bin/python3.6
from random import randint
import os
def rule(user_char):
    if len(user_char)>1:
        print("You just Enter one character Please Enter To Continue")
        input()
        return True
    elif  str(user_char).isalnum:
        print("You just Enter character Not Number Please Enter To Continue")
        input()
        return True
    else:
        return False
def win(user_char,rand_char,final_score):
    if user_char==rand_char:
        final_score+=20
        os.system('clear')
        print(''.join(user_words))
        print("congratulations,You are Win :) :)")
        print("your Final Score is {}".format(final_score))
        return True
    else:
        return False
def score():
    if health == 10:
        score=3
    elif health == 5:
        score=5
    else:
         score=10
    return score
def game_level():
    answer=int(input("Enter Your Level For Game --> \n **** 1.EASY **** \n **** 2.Medium **** \n **** 3.HARD ****\n ---> "))
    if answer == 1:
        return 10
    elif answer == 2:
        return 5
    elif answer == 3:
        return 3
    else:
        print("Choose from '1' , '2' And '3' ")
        game_level()
words=('chelsea','manchester','tottenham','everton','arsenal','norwich','sunderland','newcastle','sunderland','wigan','southampton','liverpool')
rand_words=list(words[randint(0,11)])
guess_count=0
health=game_level()
user_words=[]
wrong_char=[]
score=int(score())
final_score=0
mines_score=0
for char in rand_words:
    user_words+='_'
while True:
    flag=1
    os.system('clear')
    print ("your health {} \n".format(health))
    print("\nYour score is  {} \n".format(final_score))
    print(' '.join(user_words))
    print('\nEnter below list pre (not use again) : \n')
    print(" , ".join(wrong_char))
    user_char=input("\nEnter Your guess --> ")
    if rule(user_char):
        continue
    for rand_number in range(0,len(rand_words)):
        if user_char == rand_words[rand_number]:
            if not user_char in user_words:
                final_score+=score
            user_words[rand_number]=user_char
            flag=0
    if flag:
        wrong_char.append(user_char)
        final_score-=5
        health-=1
    if not health:
        print("Game Over :( Im Sorry :( Try Again)")
        break
    elif win(''.join(user_words),''.join(rand_words),final_score):
        break
    print()
