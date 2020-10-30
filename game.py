"""
A simple card game a la poker.

10 players. 52 cards.

Each player is dealt with 3 cards drawn randomly one-by-one to players in turn.

Cards have weights from 2-14.

select_winner will decide who wins.
"""
import secrets


def main():
    """
    The main method
    """
    deck = init_deck()
    play = deal(deck,10)
    print_play(play)
    winner, reason = select_winner(play)
    print('Player {:<d} wins: {:s}.'.format(winner,reason))


def init_deck():
    """
    Initialize the deck.
    """
    deck = [(i,'♠️ ') for i in range(2,15)]\
    + [(i, '♦️ ') for i in range(2,15)]\
    + [(i,'♥️ ') for i in range(2,15)]\
    + [(i,'♣️ ') for i in range(2,15)]

    return deck

def deal(deck,num):
    """
    Deal the cards.
    """
    secretsgen = secrets.SystemRandom()
    play = {}
    for i in range(1, 4) :
        for j in range(1, num+1):

            # play is a dict {playernum:[card1, card2, card3]}
            nextnum = secretsgen.randint(0, len(deck)-1)
            nextcard = deck[nextnum]
            del deck[nextnum]
            if j not in play:
                play[j] = [nextcard]
            else:
                play[j].append(nextcard)
    return play

def tiebreak(cards, reason):
    """
    Find maximum of the card set.
    """
    #if reason=='double' and len(cards)>1:
            
    tot = {}
    for key, val in cards.items():
        tot[val[0][0] + val[1][0] + val[2][0]] = key

    #return sorted(tot.items(), key=lambda x: x[0])[-1][1]
    return sorted(tot.items())[-1][1], reason


def select_winner(play):
    """
    Select the winner.
    """
    totsum = {}
    color = {}
    sequence = {}
    coloredsequence = {}
    double = {}
    triple = {}

    for k,val in play.items():
        val.sort(key = lambda x:x[0]) # sort cards so its easy to find sequence
        #print('{:2d} {}'.format(k, val))

        # sum total for each player if needed to decide winner
        totsum[k] = val[0][0] + val[1][0] + val[2][0]

        if val[0][1] == val[1][1] == val[2][1]:
            color[k] = val

        if val[0][0] == val[1][0] == val[2][0]:
            triple[k] = val

        if val[0][0] == val[1][0] or val[1][0] == val[2][0] or val[0][0] == val[2][0]:
            double[k] = val

        if (val[0][0] == val[1][0]-1 and val[1][0] == val[2][0]-1)\
             or sorted([val[0][0],val[1][0],val[2][0]])==[2,3,14]:
            sequence[k] = val

        if (val[0][0] == val[1][0]-1 and val[1][0] == val[2][0]-1)\
            and val[0][1] == val[1][1] == val[2][1]:
            coloredsequence[k] = val


    if triple:
        return tiebreak(triple,"triple")

    if coloredsequence:
        return tiebreak(coloredsequence, "colored sequence")

    if sequence:
        return tiebreak(sequence, "sequence")

    if color:
        return tiebreak(color, "colour")

    if double:
        return tiebreak(double, "double")

    # Sort the totsum and return the last value (which is highest)
    totsum = {k: v for k, v in sorted(totsum.items(), key=lambda item: item[1])}
    return list(totsum)[-1], "Sum"

def print_play(play):
    display = {
        11: 'J',
        12: 'Q',
        13: 'K',
        14: 'A',
    }

    for k,v in play.items():
        print('{:2d}. {:>2s}{} {:>2s}{} {:>2s}{}'.\
        format(k, display.get(v[0][0], str(v[0][0])), v[0][1],\
               display.get(v[1][0], str(v[1][0])), v[1][1],\
               display.get(v[2][0], str(v[2][0])),v[2][1]),end="\n\n")


def test():

    # Normal case sum wins 7
    p1={1:[(2,'H'),(3,'H'),(5,'S')],\
        2:[(2,'D'),(3,'D'),(5,'C')],\
        3:[(2,'S'),(3,'C'),(5,'D')],\
        4:[(2,'C'),(3,'S'),(5,'H')],\
        5:[(4,'H'),(6,'H'),(7,'S')],\
        6:[(4,'D'),(6,'D'),(7,'C')],\
        7:[(14,'H'),(13,'H'),(11,'D')],\
        8:[(4,'S'),(6,'C'),(7,'D')],\
        9:[(4,'C'),(6,'S'),(7,'H')],\
        10:[(8,'H'),(9,'D'),(11,'S')]}

    # Normal case sequence wins 6
    p2={1:[(2,'D'),(3,'H'),(5,'D')],\
        2:[(2,'C'),(3,'C'),(5,'H')],\
        3:[(6,'H'),(7,'D'),(9,'C')],\
        4:[(6,'D'),(7,'H'),(9,'S')],\
        5:[(6,'C'),(7,'C'),(9,'H')],\
        6:[(2,'H'),(3,'D'),(4,'S')],\
        7:[(8,'H'),(10,'D'),(11,'D')],\
        8:[(8,'D'),(10,'H'),(11,'H')],\
        9:[(8,'C'),(10,'S'),(11,'S')],\
        10:[(8,'S'),(10,'C'),(11,'C')]}

#    # color wins 4
#    p3={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # coloredsequence wins 9
#    p4={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # double wins 7
#    p5={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # triple wins 8
#    p6={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # triple but 2 people
#    p7={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # 2 winners with same sequence
#    p8={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # 3 winners with same sequence
#    p9={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # A-2-3 sequence
#    p10={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # A-K-Q and A-2-3 sequence
#    p11={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # ridiculous coincidences
#    p12={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    # ridiculous coincidences
#    p13={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p14={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p15={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p16={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p17={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p18={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p19={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p20={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#
#    p21={1:[(),(),()],\
#        2:[(),(),()],\
#        3:[(),(),()],\
#        4:[(),(),()],\
#        5:[(),(),()],\
#        6:[(),(),()],\
#        7:[(),(),()],\
#        8:[(),(),()],\
#        9:[(),(),()],\
#        10:[(),(),()]}
#

if __name__ == '__main__':
    main()
