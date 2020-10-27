"""
A simple card game a la poker.

10 players. 52 cards.

Each player is dealt with 3 cards drawn randomly one-by-one to players in turn.

Cards have weights from 2-14.

select_winner will decide who wins.
"""
import random

def main():
    """
    The main method
    """
    deck = init_deck()
    play = deal(deck,10)
    winner = select_winner(play)
    print('Winner is {:2d}'.format(winner))


def init_deck():
    """
    Initialize the deck.
    """
    deck = [('S',i) for i in range(2,15)]\
    + [('D',i) for i in range(2,15)]\
    + [('H',i) for i in range(2,15)]\
    + [('C',i) for i in range(2,15)]

    return deck

def deal(deck,num):
    """
    Deal the cards.
    """
    play = {}
    for i in range(1, 4) :
        for j in range(1, num+1):

            # play is a dict {playernum:[card1, card2, card3]}
            nextnum = random.randint(0, len(deck)-1)
            nextcard = deck[nextnum]
            del deck[nextnum]
            if j not in play:
                play[j] = [nextcard]
            else:
                play[j].append(nextcard)
    return play

def findmax(cards):
    """
    Find maximum of the card set.
    """
    tot = {}
    for key, val in cards.items():
        tot[key] = val[0][1] + val[1][1] + val[2][1]

    tot = {k: v for k, v in sorted(tot.items(), key=lambda item: item[1])}

    return list(tot)[-1]


def select_winner(play):
    """
    Select the winner.
    """
    totsum = {}
    color = {}
    sequence = {}
    triple = {}

    for k,val in play.items():
        val.sort(key = lambda x:x[1]) # sort cards so its easy to find sequence
        print('{:2d} {}'.format(k, val))

        # sum total for each player if needed to decide winner
        totsum[k] = val[0][1] + val[1][1] + val[2][1]

        if val[0][0] == val[1][0] == val[2][0]:
            color[k] = val

        if val[0][1] == val[1][1] == val[2][1]:
            triple[k] = val

        if val[0][1] == val[1][1]-1 and val[1][1] == val[2][1]-1:
            sequence[k] = val


    if triple:
        return findmax(triple)

    if sequence:
        return findmax(sequence)

    if color:
        return findmax(color)

    # Sort the totsum and return the last value (which is highest)
    totsum = {k: v for k, v in sorted(totsum.items(), key=lambda item: item[1])}
    return list(totsum)[-1]

if __name__ == '__main__':
    main()
