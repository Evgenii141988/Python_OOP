import sys


class Player:
    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


if __name__ == '__main__':
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    players = []
    for string in lst_in:
        name, old, score = [int(elm) if elm.isdigit() else elm for elm in string.split('; ')]
        players.append(Player(name, old, score))
    players_filtered = list(filter(bool, players))
    print(players_filtered)