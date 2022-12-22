import typing


class character(object):
    # idendity
    name = ""
    father_name = ""
    race = ""
    sub_race = ""
    job = ""

    # meta abilities
    intelligence = 0
    build_up = 0
    muscle = 0
    stamina = 0
    accuracy = 0
    insight = 0

    # side abilities
    poison = 10
    scouting = 10
    suffocation = 10
    construction = 10
    talkativeness = 10
    degeneration = 10
    money_making = 10
    stun = 10

    current_money = 0
    current_health = 0
    
    def __init__(self, name) -> None:
        self.name = name

    def to_dict(self):
        return {
            "name": self.name,
            "father_name": self.father_name,
            "race": self.race,
            "sub_race": self.sub_race,
            "job": self.job,

            "intelligence": self.intelligence,
            "build_up": self.build_up,
            "muscle": self.muscle,
            "stamina": self.stamina,
            "accuracy": self.accuracy,
            "insight": self.insight,

            "poison": self.poison,
            "scouting": self.scouting,
            "suffocation": self.suffocation,
            "construction": self.construction,
            "talkativeness": self.talkativeness,
            "degeneration": self.degeneration,
            "money_making": self.money_making,
            "stun": self.stun,

            "current_money": self.current_money,
            "current_health": self.current_health,
        }

    def to_string_all(self):
        result = ""
        print(self.__dict__)
        for k, v in self.to_dict().items():
            result += k + ": " + str(v) + "\n"
        return  result
        
    def to_string_defined(self):
        result = ""
        print(self.__dict__)
        for k, v in self.__dict__.items():
            result += k + ": " + str(v) + "\n"
        return  result

character_dict:typing.Dict[str, character] = {}


if __name__ == "__main__":
    import ruamel.yaml
    import sys

    ch = character("asd")
    ch1 = character("enes")
    ch1.intelligence = 22
    ch1.stun = 25
    print(ch1.__dict__)
    ch.intelligence = 10
    yaml = ruamel.yaml.YAML()
    yaml.register_class(character)
    # with open("/home/aenesbedir/RPGFather/character.yaml", "r") as stream:
    #     liste = yaml.load(stream)
    # print(liste[1].stun)

    print(yaml.load('/home/aenesbedir/RPGFather/character.yaml'))
    with open('/home/aenesbedir/RPGFather/character.yaml', 'w') as f:
        yaml.dump([ch, ch1], f)