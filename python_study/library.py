
class Pokemon:
    num_of_pokemon = 0
    discovered_specices = []
    first_child = None

    def __init__(self):
        self.skill_1 = '몸통박치기'
        Pokemon.increase_number()

    # 모든 포켓몬은 공격 가능
    # 포켓몬이라는 클래스가 공격을 하는게 아니라 클래스로 만들어진 인스턴스가 공격하는것
    def attack(self):
        return self.skill_1

    @classmethod
    def increase_species(cls, species):
        # 아직 추가 된 적이 없던 종이라면 추가
        if species not in cls.discovered_specices:
            cls.discovered_specices.append(species)

    @classmethod
    def increase_number(cls):
        cls.num_of_pokemon += 1 