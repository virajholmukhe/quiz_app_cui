class Quiz:
    def __init__(self,qid=0,qst="",opta="",optb="",optc="",optd="",qans=""):
        self.qid = qid
        self.qst = qst
        self.opta = opta
        self.optb = optb
        self.optc = optc
        self.optd = optd        
        self.qans = qans        
    def __str__(self):
        data = str(self.qid)+","+self.qst
        data += ","+self.opta
        data += ","+self.optb
        data += ","+self.optc
        data += ","+self.optd
        data += ","+self.qans
        return data
