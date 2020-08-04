
class ListOfPlayers:
    _instance = None

    next_player_id = 1
    players = dict()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def fetch(self):
        return self.players

    def add(self, player_name):
        self.players[self.next_player_id] = player_name
        self.next_player_id += 1
        return self.players


if __name__ == "__main__":
    players = ListOfPlayers()
    print(id(players))
    players.add("Gabriel")
    players.add("Sal")
    print(players.fetch())
    # Algum tempo depois...
    another_list = ListOfPlayers()  # cria outra instância
    print(id(another_list))
    print(another_list.fetch())  # vazia!
