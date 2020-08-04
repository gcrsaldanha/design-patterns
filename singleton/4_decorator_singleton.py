def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class ListOfPlayers:
    def __init__(self):
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
    # Algum tempo depois...
    another_list = ListOfPlayers()
    print(another_list.fetch())
    assert id(players) == id(another_list)
