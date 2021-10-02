import random
import art
from replit import clear

def blackjack():

    wanna_play = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    while True:
        if wanna_play.lower() == "y" or wanna_play.lower() == "n":
            break
        else:
            wanna_play = input("Please type correctly! ")

    if wanna_play == "n":
        return
    else:
        clear()
        print(art.logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        yourCards = []
        computerCards = []
        for i in range(1, 3):
            yourCards += [random.choice(cards)]
            computerCards += [random.choice(cards)]
        yourScore = sum(yourCards)
        computerScore = sum(computerCards)


        def computerGetNew(computerScore, computerCards):

            while computerScore < 17:
              newCard = random.choice(cards)
              if newCard == 11 and newCard + computerScore > 21:
                  computerScore += 1
                  computerCards += [1]
              else:
                  computerScore += newCard
                  computerCards += [newCard]

            return [computerScore,computerCards]

        def showResult(yourScore, computerScore, computerCards):
            newComputer = computerGetNew(computerScore, computerCards)
            computerScore = newComputer[0]
            computerCards = newComputer[1]
            if yourScore > 21:
                print(f"Your cards: {yourCards}, current score: {yourScore}")
                print(f"Computer's first card: {computerCards[0]}\n")
                print(
                    f"Your final hand: {yourCards}, final score: {yourScore}")
                print(
                    f"Computer's final hand: {computerCards}, final score: {computerScore}"
                )
                print("You went over, you lose!\n")
            elif computerScore > 21:
                print(f"Your cards: {yourCards}, current score: {yourScore}")
                print(f"Computer's first card: {computerCards[0]}\n")
                print(
                    f"Your final hand: {yourCards}, final score: {yourScore}")
                print(
                    f"Computer's final hand: {computerCards}, final score: {computerScore}"
                )
                print("You won!\n")
            elif yourScore == computerScore:
                print(f"Your cards: {yourCards}, current score: {yourScore}")
                print(f"Computer's first card: {computerCards[0]}\n")
                print(
                    f"Your final hand: {yourCards}, final score: {yourScore}")
                print(
                    f"Computer's final hand: {computerCards}, final score: {computerScore}"
                )
                print("It is a draw ;)\n")
            elif yourScore > computerScore:
                print(f"Your cards: {yourCards}, current score: {yourScore}")
                print(f"Computer's first card: {computerCards[0]}\n")
                print(
                    f"Your final hand: {yourCards}, final score: {yourScore}\n")
                print(
                    f"Computer's final hand: {computerCards}, final score: {computerScore}"
                )
                print("You are closer, you won!")
            else:
                print(f"Your cards: {yourCards}, current score: {yourScore}")
                print(f"Computer's first card: {computerCards[0]}\n")
                print(
                    f"Your final hand: {yourCards}, final score: {yourScore}")
                print(
                    f"Computer's final hand: {computerCards}, final score: {computerScore}"
                )
                print("Computer is closer, you lost!\n")

        while True:
            print(f"Your cards: {yourCards}, current score: {yourScore}")
            print(f"Computer's first card: {computerCards[0]}")
            keepGoing = input("Type 'y' to get another type 'n' to pass: ")

            while True:
                if keepGoing.lower() == "y" or keepGoing.lower() == "n":
                    break
                else:
                    keepGoing = input("Please type correctly!")

            if keepGoing == "n":
                showResult(yourScore, computerScore, computerCards)
                break
            else:
                aNewCard = random.choice(cards)
                if aNewCard == 11 and yourScore + aNewCard > 21:
                    yourCards += [1]
                    yourScore = sum(yourCards)
                    continue
                elif yourScore + aNewCard > 21:
                    yourCards += [aNewCard]
                    yourScore = sum(yourCards)
                    showResult(yourScore, computerScore, computerCards)
                    break
                else:
                    yourCards += [aNewCard]
                    yourScore = sum(yourCards)
                    continue
    blackjack()

blackjack()
