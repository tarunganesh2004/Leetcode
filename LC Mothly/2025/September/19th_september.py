# Design SpreadSheet LC 3484

class SpreadSheet:

    def __init__(self,rows):
        self.sheet={}
    
    def setCell(self,cell,value):
        self.sheet[cell]=value

    def resetCell(self,cell):
        self.sheet[cell]=0
    
    def getValue(self,formula):
        x,y=formula[1:].split('+')
        try:
            x_val=int(x)
        except:  # noqa: E722
            x_val=self.sheet.get(x,0)
        try:
            y_val=int(y)
        except:  # noqa: E722
            y_val=self.sheet.get(y,0)
        return x_val+y_val
    