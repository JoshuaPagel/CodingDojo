# Assignment:
# Paul is a fantasy basketball league manager, but also a programmer! He is trying
# to organize fantasy teams of players (that can be from any of the real teams) for his league website. 
# There is already a web service that collects the line-up data from friends in batches.

# So far, he has been able to get a single list of dictionaries at a time from the API, 
# and would like to put each team into a list of Player object instances, 
# so that he can use methods related to players.


kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets",
}

dame = {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    }

joel = {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    }


class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    def __repr__(self):
        display = f"Player: {self.name}, {self.age}, {self.position}, {self.team}"
        return display
    
    # Not to sure how this works
    # @classmethod
    # def get_all_players(cls):
    #     player_objects = []
    #     for dict in new_player:
    #         player_objects.append(cls(dict))
    #         return player_objects



# Player.get_all_players()

player_kyrie = Player(kyrie)
player_joel = Player(joel)
player_dame = Player(dame)

print(player_dame.name)
print(player_joel.position)
print(player_kyrie)


# attempts
    # @classmethod
    # def accept_dict(cls):
    #     for Player in cls.players:
    #         print(Player["name"])


# player_kevin = Player(kevin)
# player_Joel = Player(joel)
# player_dame = Player(dame)

