class Grid():
    def __init__(self) -> None:
        print("Grid Initialisation!")

    state = True
    coherence = True
    values = []

    #TODO Add tracker to redondent values and track them in incoherentCases table
    incoherentCases=[]

    def insertGrid(self):
        for row in range(9):
            vals= input().split(" ")
            self.values.append([])
            for col in range(9):
                self.values[row].append({"val":vals[col],"poss":["1","2","3","4","5","6","7","8","9"]})
        for row in range(9):
            for col in range(9):
                self.fillPossibleValues(row,col)
        self.verifyCoherence()
        print("Grid Insertion Completed ...")

    def fillPossibleValues(self,x,y):
        for i in range(9):
            if (self.values[i][y]["val"]!=0  and self.values[i][y]["val"] in self.values[x][y]["poss"] ):
                self.values[x][y]["poss"].remove(self.values[i][y]["val"])
            if (self.values[x][i]["val"]!=0  and self.values[x][i]["val"] in self.values[x][y]["poss"] ):
                self.values[x][y]["poss"].remove(self.values[x][i]["val"])
        for i in range(3):
            for j in range(3):
                if(self.values[3*(x//3)+i][3*(y//3)+j]["val"]!=0 and self.values[3*(x//3)+i][3*(y//3)+j]["val"] in self.values[x][y]["poss"]):
                    self.values[x][y]["poss"].remove(self.values[3*(x//3)+i][3*(y//3)+j]["val"])

    def verifRow(self):
        for row in range(9):
            actRow=[]
            for col in range(9):
                actRow.append(self.values[row][col]["val"])
            actRow.sort()
            for col in range(8):
                if(actRow[col]==actRow[col+1] and actRow[col]!= "0"):
                    print("row",actRow,actRow[col],actRow[col+1])
                    return False 
        return True
    
    def verifColumns(self):
        for col in range(9):
            actCol=[]
            for row in range(9):
                actCol.append(self.values[row][col]["val"])
            actCol.sort()
            for row in range(8):
                if(actCol[row]==actCol[row+1] and actCol[row]!="0"):
                    return False
        return True
    
    def verifBlocks(self):
        for blocX in range(3):
            for blocY in range(3):
                blocValues=[]
                for col in range(3):
                    for row in range(3):
                        blocValues.append(self.values[3*blocY+row][3*blocX+col]["val"])
                for i in range(len(blocValues)-1):
                    if(blocValues[i]==blocValues[i+1] and blocValues[i]!="0" ):
                        return False
        return True
    def verifyCoherence(self):
        if(self.verifRow() and self.verifColumns() and self.verifBlocks()):
            print("Coherent Grid!")
            self.coherence=True
            return True
        else:
            print("Incoherent Grid")
            self.coherence=False
            return False

    def insertValue(self,x,y,value):
        self.values[x][y]["val"]=str(value)
        return self.verifyCoherence()
        
    def deleteValue(self,x,y):
        self.values[x][y]["val"]=str(0)
        return self.verifyCoherence()

    def printGrid(self):
        poss=[]
        for row in range(len(self.values)):
            s=[]
            for col in range(len(self.values[row])):
                s.append(self.values[row][col]["val"])
                poss.append(self.values[row][col]["poss"])
            print(s)

