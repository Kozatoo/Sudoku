from this import d


class grid():
    state = True
    values = [[0]*9]*9

    def insertGrid(self):
        for row in range(9):
            vals= input().split("")
            for col in range[9]:
                self.values[col][row]= int(vals[col])

    def verifRow(self):
        for row in range(9):
            actRow=self.values[row]
            actRow.sort()
            for col in range(8):
                if(actRow[col]==actRow[col+1] and actRow[col] != 0):
                    return False 
        return True
    
    def verifColumns(self):
        for col in range(9):
            actCol=[]
            for row in range(9):
                actCol.append(self.values[col][row])
            actCol.sort()
            for row in range(8):
                if(actCol[row]==actCol[row+1] and actCol[row]!=0):
                    return False
        return True
    
    def verifBlocks(self):
        for blocX in range(3):
            for blocY in range(3):
                blocValues=[]
                for col in range(3):
                    for row in range(3):
                        blocValues.append=self.values[blocY+row][blocX+col]
                for i in range(len(blocValues)-1):
                    if(blocValues[i]==blocValues[i+1] and blocValues[i]!=0 ):
                        return False
        return True

    def insertValue(self,x,y,value):
        self.values[x][y]=value
        if(self.verifRow and self.verifColumns and self.verifBlocks):
            return True
        return False

    def deleteValue(self,x,y):
        self.values[x][y]=0
        if(self.verifRow and self.verifColumns and self.verifBlocks):
            return True
        return False

