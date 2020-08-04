class ListOfPlayers:
    __instance = None

    @staticmethod
    def get_instance(*args, **kwargs):
        if ListOfPlayers.__instance is None:
            ListOfPlayers(*args, **kwargs)
        return ListOfPlayers.__instance

    def __init__(self, *args, **kwargs):
        if ListOfPlayers.__instance is not None:
            raise Exception('This class is a singleton.')
        else:
            ListOfPlayers.__instance = self
            self.next_player_id = 1
            self.players = dict()

    def fetch(self):
        return self.players

    def add(self, player_name):
        self.players[self.next_player_id] = player_name
        self.next_player_id += 1
        return self.players


if __name__ == "__main__":
    players = ListOfPlayers.get_instance()
    players.add("Gabriel")
    players.add("Sal")
    print(players.fetch())
    # Dez mil anos depois...
    players2 = ListOfPlayers.get_instance()
    print(players2.fetch())
    assert id(players2) == id(players)
