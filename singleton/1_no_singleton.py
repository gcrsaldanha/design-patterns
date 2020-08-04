class ListOfPlayers:
    def __init__(self, *args, **kwargs):
        self.next_player_id = 1
        self.players = dict()

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
    # Dez mil anos depois...
    players2 = ListOfPlayers()
    print(players2.fetch())
    assert id(players2) == id(players)
