from team import Team


class Player(Team):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def get_player_info(self):
        playerInfoDic = {
            'team': self.teamName,
            'name': self.name,
            'age': self.age
        }

        return playerInfoDic


p = Player('justin', 29)
print(p.teamName)
info = p.get_player_info()
print(info)
