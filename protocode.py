from operator import attrgetter
from random import randint

from models.round import Round
from models.match import Match
from models.player import Player
from models.tournament import Tournament
from datetime import datetime


# Sort method by score, then rank, then birthday
def sortPlayersByScoreThenRank(playersList):
    return sorted(playersList, key=attrgetter('score', 'rank', 'birthday'), reverse=True)


def generateFirstTourMatchesPairs(sortedList):
    matches = []
    for i in range(0, int(len(sortedList) / 2), 1):
        matches.append(Match(sortedList[i], sortedList[i + int(len(sortedList) / 2)]))
    return matches


def generateFollowingTourMatchesPairs(sortedList):
    matches = []
    while len(sortedList) >= 2:
        print("in the while")
        for j in range(1, len(sortedList), 1):
            print(j)
            print(sortedList[j].opponent_list.name)
            if sortedList[0] not in sortedList[j].opponent_list:
                matches.append(Match(sortedList[0], sortedList[j]))
                sortedList.pop(j)
                sortedList.pop(0)
                break
            else:
                print("else")

    return matches


# méthode de tri des joueurs
def generateMatchesPairsWithSwissSystem(playersList, isFirstTour):
    sortedList = sortPlayersByScoreThenRank(playersList)
    if isFirstTour:
        return generateFirstTourMatchesPairs(sortedList)
    else:
        return generateFollowingTourMatchesPairs(sortedList)


firstRound = True
tournament = Tournament("Le Tournoi de la mort", "Marolles en Brie", "18 février 2023", 4,
                        "Le Grand Tournoi d'échecs de Marolles en Brie réunit plus de 2000 passionnés d'échecs",
                        "blitz")

joueur1 = Player("Moncorger", "Thierry", "1983-02-18", 0, 4)
joueur2 = Player("Degtyarova", "Tetyana", "1984-04-06", 1, 4)
joueur3 = Player("Moncorger", "Alexandre", "2014-04-30", 0, 3)
joueur4 = Player("Moncorger", "Antoine", "2016-01-25", 0, 3)
joueur5 = Player("Moncorger", "Valentina", "2022-05-16", 1, 2)
joueur6 = Player("Moncorger", "Julie", "1980-09-19", 1, 2)
joueur7 = Player("Som", "François", "1984-04-04", 0, 1)
joueur8 = Player("Combette", "Tristan", "1990-09-15", 0, 1)

tournament.attendees.append(joueur1)
tournament.attendees.append(joueur2)
tournament.attendees.append(joueur3)
tournament.attendees.append(joueur4)
tournament.attendees.append(joueur5)
tournament.attendees.append(joueur6)
tournament.attendees.append(joueur7)
tournament.attendees.append(joueur8)

for i in range(tournament.nb_of_rounds):
    if firstRound is True:
        firstRoundMatches = generateMatchesPairsWithSwissSystem(tournament.attendees, True)

        tournament.rounds.append(Round("Round " + str(i + 1), datetime.now(), firstRoundMatches))

        print(tournament.rounds[i].name)
        for match in tournament.rounds[i].matches:
            # Tirage au sort d'un gagnant
            draw = randint(0, 2)

            result = ()
            if draw == 0:
                result = match.updateScore(match.whitePlayer)
            elif draw == 1:
                result = match.updateScore(match.blackPlayer)
            else:
                result = match.updateScore(None)

            # match.updateScore()
            print(
                result[0][0].firstname +
                " " + str(result[0][0].score) +
                " (+" + str(result[0][1]) + ")"
                + " - " +
                result[1][0].firstname +
                " " + str(result[1][0].score) +
                " (+" + str(result[1][1]) + ")"
            )

        firstRound = False
    else:
        followingRoundMatches = generateMatchesPairsWithSwissSystem(tournament.attendees, False)

        tournament.rounds.append(Round("Round " + str(i + 1), datetime.now(), followingRoundMatches))

        print(tournament.rounds[i].name)
        for match in tournament.rounds[i].matches:
            # Tirage au sort d'un gagnant
            draw = randint(0, 2)

            result = ()
            if draw == 0:
                result = match.updateScore(match.whitePlayer)
            elif draw == 1:
                result = match.updateScore(match.blackPlayer)
            else:
                result = match.updateScore(None)

            # match.updateScore()
            print(
                result[0][0].firstname +
                " " + str(result[0][0].score) +
                " (+" + str(result[0][1]) + ")"
                + " - " +
                result[1][0].firstname +
                " " + str(result[1][0].score) +
                " (+" + str(result[1][1]) + ")"
            )


position = 0
final_list = sortPlayersByScoreThenRank(tournament.attendees)
for player in final_list:
    position += 1
    print(str(position)+") " + player.firstname + " " + player.lastname + " ("+ str(player.score) +" points)")