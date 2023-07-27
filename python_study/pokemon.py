from library import Pokemon

class Pikachu(Pokemon):
    no = 25
    type = '전기'
    
    def __init__(self,name,lv=5):
        # super -> 부모 클래스의 메소드를 호출하고자 할때 사용
        super().__init__()
        # 부모 클래스의 메소드를 직접 호출. self 인자로 넘겨야함
        # Pokemon.__init__(self)
        self.name = name
        self.lv = lv

        #최초의 피카츄가 태어났을때만 종 정보 기록
        # 내가 쓸거만 덮어써서 사용
        if Pikachu.first_child is None:
            Pikachu.first_child = self
            super().increase_species('피카츄')
        # super는 self라는 인자값을 넘겨주면서 함수를 호출하는 것이라 메소드를 가져올때 사용하는 것이다
        # 그게 아니라 클래스 변수에 접근하려면 부모 클래스의 이름을 명시적으로 입력해서 접근한다


class Metamon(Pokemon):
    no = 132
    type = '노말'
    
    def __init__(self,name,lv=5):
        super().__init__()
        self.name = name
        self.lv = lv

        if Metamon.first_child is None:
            Metamon.first_child = self
            super().increase_species('메타몽')
        
        self.skill_1 = '변신'
    
    def attack(self, target):
        self.type = target.type
        return f'{self.name}이 {target.name}으로 변신했다'

p1 = Pikachu('지우개')
m1 = Metamon('메타몽')
print(Pokemon.discovered_specices)
print(p1.attack(), m1.attack(p1))