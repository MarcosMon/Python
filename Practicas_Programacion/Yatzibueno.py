class Yatzy:

    @staticmethod
    def chance(*args):
        puntuacionTotal = 0
        for dado in args:
            puntuacionTotal += dado
        return puntuacionTotal

    @staticmethod
    def yatzy(*dice):
        assert type(dice) == tuple
        assert type(dice[0]) == int
        for num in dice:
            if dice.count(num) == 5:
                return 50
            return 0


    @staticmethod
    def ones(*args):
        acumulador = 0
        assert type(args) == tuple
        for dado in args:
            if dado == 1:
                acumulador += dado
        assert type(acumulador) == int
        return acumulador

    @staticmethod
    def twos(*args):
        acumulador = 0
        assert type(args) == tuple
        for dado in args:
            if dado == 2:
                acumulador += dado
        assert type(acumulador) == int
        return acumulador
    
    @staticmethod
    def threes(* args):
        acumulador = 0
        assert type(args) == tuple
        for dado in args:
            if dado == 3:
                acumulador += dado
        assert type(acumulador) == int
        return acumulador
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
    def fours(*args):
        acumulador = 0
        assert type(args) == tuple
        for dado in args:
            if dado == 4:
                acumulador += dado
        assert type(acumulador) == int
        return acumulador
    

    def fives(*args):
        acumulador = 0
        assert type(args) == tuple
        for dado in args:
            if dado == 5:
                acumulador += dado
        assert type(acumulador) == int
        return acumulador
    

    def sixes(* args):
        acumulador = 0
        assert type(args) == tuple
        for dado in args:
            if dado == 6:
                acumulador += dado
        assert type(acumulador) == int
        return acumulador
    
    @staticmethod
    def score_pair(*args):
        listaDados=[]
        for dado in args:
            if args.count(dado) == 2:
                listaDados.append(dado)
        return (max(listaDados)*2)

    @staticmethod
    def two_pair(*args):
        new=sorted(args)
        new1=new[0:2] + new[3:5]
        total=0
        for num in new1:
            if new1.count(num) == 2:
                total+=num
            else:
                return 0
        return total


    @staticmethod
    def three_of_a_kind(*args):
        
        for dado in range(6):
            if args.count(dado) >=3:
                return dado*3


    @staticmethod
    def four_of_a_kind(*args):
        for dado in range(6):
            if args.count(dado) >=4:
                return dado*4
        return 0
    

    @staticmethod
    def smallStraight(*args):

        return (sum(args)) if len(set(args)) == 5 else 0


    

    @staticmethod
    def largeStraight(*args):
        
        return (sum(args)) if len(set(sorted(args))) == 5 else 0
    

    @staticmethod
    def fullHouse(*args):
        total=0
        for dado in args:

            if args.count(dado) >=2:
                total+=dado
            else:
                return 0
        return total

if __name__ == '__main__':


    #caras del dado

    d1 = 1
    d2 = 2
    d3 = 3
    d4 = 4
    d5 = 5
    d6 = 6
    
    #casos test de ones 

    assert Yatzy.ones(d1, d5, d2) == 1
    assert Yatzy.ones(d2, d1, d3, d3, d2) == 1
    assert Yatzy.ones(d2, d4, d4, d2) == 0
    assert Yatzy.ones(d1, d1, d1, d1) == 4
    #casos test de chance

#def test_chance_scores_sum_of_all_dice():
    expected = 15
    actual = Yatzy.chance(d2,d3,d4,d5,d1)
    assert expected == actual
    assert 16 == Yatzy.chance(d3,d3,d4,d5,d1)


#def test_ones():
    assert Yatzy.ones(d1,d2,d3,d4,d5) == 1
    assert 2 == Yatzy.ones(d1,d2,d1,d4,d5)
    assert 0 == Yatzy.ones(d6,d2,d2,d4,d5)
    assert 4 == Yatzy.ones(d1,d2,d1,d1,d1)
      

#def test_twos():
    assert 4 == Yatzy.twos(d1,d2,d3,d2,d6)
    assert 10 == Yatzy.twos(d2,d2,d2,d2,d2)
      

#def test_threes():
    assert 6 == Yatzy.threes(d1,d2,d3,d2,d3)
    assert 12 == Yatzy.threes(d2,d3,d3,d3,d3)
      

#def test_fours_test():

#estaban de esta manera y no funcionaba    assert 12 == Yatzy(4,4,4,5,5).fours()
    assert 12 == Yatzy.fours(d4,d4,d4,d5,d5)
    assert 8 == Yatzy.fours(d4,d4,d5,d5,d5)
    assert 4 == Yatzy.fours(d4,d5,d5,d5,d5)
      

#def test_fives():

#estaban de esta manera y no funcionaba       assert 10 == Yatzy(4,4,4,5,5).fives()

    assert 10 == Yatzy.fives(d4,d4,d4,d5,d5)
    assert 15 == Yatzy.fives(d4,d4,d5,d5,d5)
    assert 20 == Yatzy.fives(d4,d5,d5,d5,d5)
      
#estaban de esta manera y no funcionaba       assert 0 == Yatzy(4,4,4,5,5).sixes()

#def test_sixes_test():
    assert 0 == Yatzy.sixes(d4,d4,d4,d5,d5)
    assert 6 == Yatzy.sixes(d4,d4,d6,d5,d5)
    assert 18 == Yatzy.sixes(d6,d5,d6,d6,d3)

#def test_Yatzy():

    expected = 50
    actual = Yatzy.yatzy(d4,d4,d4,d4,d4)
    assert expected == actual
    assert 50 == Yatzy.yatzy(d6,d6,d6,d6,d6)
    assert 0 == Yatzy.yatzy(d6,d6,d6,d6,d3)

#def test_one_pair():
    assert 6 == Yatzy.score_pair(d3,d4,d3,d5,d6)
    assert 10 == Yatzy.score_pair(d5,d3,d3,d3,d5)
    assert 12 == Yatzy.score_pair(d5,d3,d6,d6,d5)

#def test_two_Pair():
    assert 16 == Yatzy.two_pair(d3,d3,d5,d4,d5)
    assert 18 == Yatzy.two_pair(d3,d3,d6,d6,d6)
    assert 0 == Yatzy.two_pair(d3,d3,d6,d5,d3)


#def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(d3,d3,d3,d4,d5)
    assert 15 == Yatzy.three_of_a_kind(d5,d3,d5,d4,d5)
    assert 9 == Yatzy.three_of_a_kind(d3,d3,d3,d3,d5)

#def test_four_of_a_knd():
    assert 12 == Yatzy.four_of_a_kind(d3,d3,d3,d3,d5)
    assert 20 == Yatzy.four_of_a_kind(d5,d5,d5,d4,d5)
    assert 12 == Yatzy.four_of_a_kind(d3,d3,d3,d3,d3)
    assert 0  == Yatzy.four_of_a_kind(d3,d3,d3,d2,d1)

#def test_smallStraight():
    assert 15 == Yatzy.smallStraight(d1,d2,d3,d4,d5)
    assert 15 == Yatzy.smallStraight(d2,d3,d4,d5,d1)
    assert 0 == Yatzy.smallStraight(d1,d2,d2,d4,d5)


#def test_largeStraight():
    assert 20 == Yatzy.largeStraight(d6,d2,d3,d4,d5)
    assert 20 == Yatzy.largeStraight(d2,d3,d4,d5,d6)
    assert 0 == Yatzy.largeStraight(d1,d2,d2,d4,d5)

#def test_fullHouse():
    assert 18 == Yatzy.fullHouse(d6,d2,d2,d2,d6)
    assert 0 == Yatzy.fullHouse(d2,d3,d4,d5,d6)


