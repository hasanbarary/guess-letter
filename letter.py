#!/usr/bin/python3.6
from random import randint
import os
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
words=('Chelsea','Manchester','Tottenham','Everton','Arsenal','Norwich','Sunderland','Newcastle','Sunderland','Wigan','Southampton','Liverpool')
rand_words=list(words[randint(0,11)])
guess_count=0
health=game_level()
user_words=[]
wrong_char=[]
for char in rand_words:
    user_words+='_'
while True:
    flag=1
    os.system('clear')
    print ("your health {} \n".format(health))
    print(' '.join(user_words))
    print('\nEnter below list pre (not use again) : \n')
    print(" , ".join(wrong_char))
    user_char=input("\nEnter Your guess --> ")
    if len(user_char)>1 or not "".isalpha:
        print("You just Enter one character Please Enter To Continue")
        input()
        continue
    for rand_number in range(0,len(rand_words)):
        if user_char == rand_words[rand_number]:
            user_words[rand_number]=user_char
            flag=0
    if flag:
        wrong_char.append(user_char)
        health-=1
    if not health:
        print("Game Over :( Im Sorry :( Try Again)")
        break
    elif ''.join(user_words) == ''.join(rand_words):
        print("congratulations,You are Win :)")
        break
