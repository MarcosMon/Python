class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        
        if self.draft - self.crew *1.5 >20:
            return True
        else:
            return False

EmptyShip = Ship(0, 0)

assert EmptyShip.is_worth_it() == False

EmptyShip = Ship(200,40)

assert EmptyShip.is_worth_it() == True