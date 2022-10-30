from models.match import Match
from models.player import Player
from views.homeview import HomeView
from operator import attrgetter
from random import randint
from datetime import datetime


class TournamentRunnerController:

    def __init__(self, view, tournament, database):
        # views
        self.view = view
        self.db = database
        self.tournament = tournament

    def run(self):
        self.view.show_welcome()
        self.initial_check_tournament(self.tournament)

    def back_home(self):
        self.view = HomeView()
        self.run()

    def initial_check_tournament(self, tournament):
        if tournament.attendees is None or len(tournament.attendees) == 0:
            self.add_attendees(self.db, tournament)

    def add_attendees(self, db, tournament):
        def load_players_list_from_database():
            players_list = []
            serialized_players_list_from_db = self.db.get_players_from_database()

            if serialized_players_list_from_db is not None:
                for serialized_player in serialized_players_list_from_db:
                    player = Player(serialized_player['lastname'],
                                    serialized_player['firstname'],
                                    serialized_player['birthday'],
                                    serialized_player['gender'],
                                    serialized_player['rank'])
                    players_list.append(player)
            return players_list

        all_players_list = load_players_list_from_database()
        i = 0
        for player in all_players_list:
            i += 1
            self.view.display_player(i, player)

    # méthode de tri des joueurs
    def generate_match_pairs_with_swiss_system(self, playersList, isFirstTour):
        def sort_players_by_score_then_rank(playersList):
            return sorted(playersList, key=attrgetter('score', 'rank', 'birthday'), reverse=True)

        def generate_first_tour_matches_pairs(sortedList):
            matches = []
            for i in range(0, int(len(sortedList) / 2), 1):
                matches.append(Match(sortedList[i], sortedList[i + int(len(sortedList) / 2)]))
            return matches

        def generate_following_tour_matches_pairs(sortedList):
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

        sorted_list = sort_players_by_score_then_rank(playersList)
        if isFirstTour:
            return generate_first_tour_matches_pairs(sorted_list)
        else:
            return generate_following_tour_matches_pairs(sorted_list)
