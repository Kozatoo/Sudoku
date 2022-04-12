class Grid():
    def __init__(self) -> None:
        print("Grid Initialisation ...")

    state = True
    values = []

    def insertGrid(self):
        for row in range(9):
            vals= input().split(" ")
            # print("Read Line")
            # print(vals)
            self.values.append([])
            for col in range(9):
                # print(vals[col])
                self.values[row].append({"val":vals[col],"poss":[1,2,3,4,5,6,7,8,9]})
            # self.printGrid()
        for row in range(9):
            for col in range(9):
                self.fillPossibleValues(row,col)
        print("Insertion Complete")

    def fillPossibleValues(self,x,y):
        for i in range(9):
            if (self.values[i][y]["val"]!=0  and self.values[i][y]["val"] in self.values[x][y]["poss"] ):
                self.values[x][y]["poss"].remove(self.values[i][y]["val"])
            if (self.values[x][i]["val"]!=0  and self.values[x][i]["val"] in self.values[x][y]["poss"] ):
                self.values[x][y]["poss"].remove(self.values[x][i]["val"])
        for i in range(3):
            for j in range(3):
                if(self.values[3*(x//3)+i][3*(y//3)+j]["val"]!=0 and self.values[3*(x//3)+i][3*(y//3)+j]["val"] in self.values[x][y]["poss"]):
                    self.values[x][y]["poss"].remove(self.values[3*(x//3)+i][3*(y//3)+j])


    def verifRow(self):
        for row in range(9):
            actRow=self.values[row]
            actRow.sort()
            for col in range(8):
                if(actRow[col]["val"]==actRow[col+1]["val"] and actRow[col]["val"] != 0):
                    return False 
        return True
    
    def verifColumns(self):
        for col in range(9):
            actCol=[]
            for row in range(9):
                actCol.append(self.values[row][col]["val"])
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
                        blocValues.append=self.values[3*blocY+row][3*blocX+col]["val"]
                for i in range(len(blocValues)-1):
                    if(blocValues[i]==blocValues[i+1] and blocValues[i]!=0 ):
                        return False
        return True

    def insertValue(self,x,y,value):
        self.values[x][y]["val"]=value
        if(self.verifRow and self.verifColumns and self.verifBlocks):
            return True
        return False

    def deleteValue(self,x,y):
        self.values[x][y]["val"]=0
        if(self.verifRow and self.verifColumns and self.verifBlocks):
            return True
        return False
    def printGrid(self):
        poss=[]
        print(self.values)
        for row in range(len(self.values)):
            s=[]
            for col in range(len(self.values[row])):
                s.append(self.values[row][col]["val"])
                poss.append(self.values[row][col]["poss"])
            print(s)
        # print(poss)

