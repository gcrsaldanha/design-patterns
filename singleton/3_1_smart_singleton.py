# Pelo que entendi: new sempre vai chamar __init__ ao RETORNAR uma instância, logo não adianta só isso para o Singleton
class ListOfPlayers:
    __instance = None

    def __init__(self):
        print('calling init')
        self.next_player_id = 1
        self.players = dict()

    def __new__(cls):  # magic static method, calls init and returns the object
        print('entering new')
        if ListOfPlayers.__instance is None:
            print('is none')
            ListOfPlayers.__instance = super().__new__(cls)
            return ListOfPlayers.__instance
        print('returning')
        return ListOfPlayers.__instance

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
