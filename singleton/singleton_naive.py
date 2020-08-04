class ListOfPlayers:
    __instance = None

    def __init__(self):
        self.next_player_id = 1
        self.players = dict()  # {1: 'Nome'}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def fetch(self):
        return self.players

    def add(self, player_name):
        self.players[self.next_player_id] = player_name
        self.next_player_id += 1
        return self.players


if __name__ == "__main__":
    players = ListOfPlayers()
    players.add("Gabriel")
    players.add("Sal")
    print(players.fetch())
    #....
    players2 = ListOfPlayers()
    print(players2.fetch())