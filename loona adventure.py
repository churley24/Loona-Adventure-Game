#Camryn Hurley
#my layout:
#1- stay in eden
#	end game/play again
#2- leave eden
#	a- take everyone
#		end game/play again
#	b- leave olivia
#		i- suffer the consequences
#			end game
#		ii- go back to (2)

import time
import random
out = []
element = ""

import unicodedata


def prt_list(list):
    for j in list:
        print(j, flush=True)
        if len(j) < 70:
            time.sleep(2)
        else:
            time.sleep(3)


def prt_single(sentence, num):
    print(sentence, flush=True)
    time.sleep(num)

#intro story
def intro():
    story = [
        "There once lived four girls: Yves, Chuu, Gowon, and Olivia Hye,"
        "In a far away place called Eden -- above earth and the cosmos.",
        "They were happy and lived carefree.",
        "They had one rule - do not eat the forbidden fruit.",
        "Like all young girls, they were curious and wanted to know what would happen if you ate the forbidden fruit,",
        "And wanted to know what was beyound Eden.",
        "Yves was the most curious and wanted to leave Eden. \n"
    ]
    prt_list(story)

#first choice
def choose_1():
    act = [
        "They can listen to Yves or ignore her.",
        "Enter 1 to stay in Eden.",
        "Enter 2 to leave Eden.",
        "What would you do?"
        ]
    prt_list(act)
    response = str(input("(Please enter 1 or 2.)\n"))
    return response
    play_again()

#consequences of choose_1
def choose_11():
    act11 = [
        "They stay and live happily and ignorant together in Eden."
        ]
    prt_list(act11)
    play_again()

#consequences of choose_1
#second choice
def choose_12():
        act2 = [
            "Yves, Gowon, and Chuu create a plan to leave Eden,",
            "But do they take Olivia?",
            "Enter 1 to take Olivia.",
            "Enter 2 to leave Olivia.",
            ]
        prt_list(act2)
        response1 = str(input("(Please enter 1 or 2.)\n"))
        if response1 == "1":
            act3 = [
                "All four girls leave Eden and make it to earth.",
                "It is not what they imagined...",
                "After all, ignorance is bliss."
                ]
            prt_list(act3)
            play_again()
        else:
            act4 = [
                "They leave Eden without Olivia.",
                "This will have repercussions...", unicodedata.lookup("butterfly"),
                "They can go back in time to get Olivia or stay and suffer the consequences.",
                "Enter 1 to go back.",
                "Enter 2 to stay."
                ]
            prt_list(act4)
            choose_14()

#consequences of choose_12
def choose_14():
        response2 = str(input("(Please enter 1 or 2.)\n"))
        if response2 == "1":
            choose_12()
        else:
            act5 = [
                "Olivia burns the moon...",
                "There is no going back now."
                ]
            prt_list(act5)
            exit()




def game():
    response = choose_1()
    if response == "1":
        choose_11()
    elif response == "2":
        choose_12()
    else:
        game()
    game()



def Adventure():
    intro()
    game()
    play_again()


def play_again():
    global out
    prt_single("Would you like to play again?", 2)
    response2 = str(input("Please enter y for yes and n for no.\n").lower())
    if response2 == "y":
        out = []
        Adventure()
    elif response2 == "n":
        exit()
    else:
        play_again()


Adventure()
