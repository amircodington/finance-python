
class Pivot:
    def __init__(self, HIGHprev, LOWprev,CLOSEprev):
        self.HIGHprev = HIGHprev
        self.LOWprev = LOWprev
        self.CLOSEprev = CLOSEprev
        
    
    def traditional(self):
        PP = (self.HIGHprev + self.LOWprev + self.CLOSEprev) / 3
        R1 = PP * 2 - self.LOWprev
        S1 = PP * 2 - self.HIGHprev
        R2 = PP + (self.HIGHprev - self.LOWprev)
        S2 = PP - (self.HIGHprev - self.LOWprev)
        R3 = PP * 2 + (self.HIGHprev - 2 * self.LOWprev)
        S3 = PP * 2 - (2 * self.HIGHprev - self.LOWprev)
        R4 = PP * 3 + (self.HIGHprev - 3 * self.LOWprev)
        S4 = PP * 3 - (3 * self.HIGHprev - self.LOWprev)
        R5 = PP * 4 + (self.HIGHprev - 4 * self.LOWprev)
        S5 = PP * 4 - (4 * self.HIGHprev - self.LOWprev)
        RS = [(R1, S1), (R2, S2), (R3, S3), (R4, S4)]
        return RS
    
    def fibonacci(self):
        PP = (self.HIGHprev + self.LOWprev + self.CLOSEprev) / 3
        R1 = PP + 0.382 * (self.HIGHprev - self.LOWprev)
        S1 = PP - 0.382 * (self.HIGHprev - self.LOWprev)
        R2 = PP + 0.618 * (self.HIGHprev - self.LOWprev)
        S2 = PP - 0.618 * (self.HIGHprev - self.LOWprev)
        R3 = PP + (self.HIGHprev - self.LOWprev)
        S3 = PP - (self.HIGHprev - self.LOWprev)
        RS = [(R1, S1), (R2, S2), (R3, S3)]
        return RS
        
    def classic(self):
        PP = (self.HIGHprev + self.LOWprev + self.CLOSEprev) / 3
        R1 = 2 * PP - self.LOWprev
        S1 = 2 * PP - self.HIGHprev
        R2 = PP + (self.HIGHprev - self.LOWprev)
        S2 = PP - (self.HIGHprev - self.LOWprev)
        R3 = PP + 2 * (self.HIGHprev - self.LOWprev)
        S3 = PP - 2 * (self.HIGHprev - self.LOWprev)
        R4 = PP + 3 * (self.HIGHprev - self.LOWprev)
        S4 = PP - 3 * (self.HIGHprev - self.LOWprev)
        RS = [(R1, S1), (R2, S2), (R3, S3), (R4, S4)]
        return RS
    
    def camarilla(self):
        PP = (self.HIGHprev + self.LOWprev + self.CLOSEprev) / 3
        R1 = self.CLOSEprev + 1.1 * (self.HIGHprev - self.LOWprev) / 12
        S1 = self.CLOSEprev - 1.1 * (self.HIGHprev - self.LOWprev) / 12
        R2 = self.CLOSEprev + 1.1 * (self.HIGHprev - self.LOWprev) / 6
        S2 = self.CLOSEprev - 1.1 * (self.HIGHprev - self.LOWprev) / 6
        R3 = self.CLOSEprev + 1.1 * (self.HIGHprev - self.LOWprev) / 4
        S3 = self.CLOSEprev - 1.1 * (self.HIGHprev - self.LOWprev) / 4
        R4 = self.CLOSEprev + 1.1 * (self.HIGHprev - self.LOWprev) / 2
        S4 = self.CLOSEprev - 1.1 * (self.HIGHprev - self.LOWprev) / 2
        R5 = (self.HIGHprev / self.LOWprev) * self.CLOSEprev
        S5 = self.CLOSEprev - (R5 - self.CLOSEprev)
        RS = [(R1, S1), (R2, S2), (R3, S3), (R4, S4)]
        return RS
        
        