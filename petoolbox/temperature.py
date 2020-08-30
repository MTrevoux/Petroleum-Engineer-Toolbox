import numpy as np

class temperature(object):
    """
    Class describing temperature as a value and a scale reference.
    Features:
        Value(float): measured value
        Reference(str): The scale reference must be included in the list ['c','f','r','k']
        c : celsius
        f : fahrenheit
        r : rankine
        k : kelvin
    """
    
    def __init__(self,value,reference):
        if reference in ['c','f','r','k']:
            self.reference=reference
            self.value=value
        else:
            print("wrong reference, it must be in ['c','f','r','k']")
            return None

    def temptransfer(self,newRef):
        l=['c','f','r','k']
        if newRef in l:
            transferMatrixCoeff=np.array([[1,1.8,1.8,1],[1/1.8,1,1,1/1.8],[1/1.8,1,1,1/1.8],[1,1.8,1.8,1]])
            transferMatrixConst=np.array([[0,0,0,0],[-32,0,0,-32],[-459.67-32,0,0,-459.67-32],[0,-273.15,-273.15,0]])
            transferMatrixConst2=np.array([[0,32,459.67+32,273.15],[0,0,459.67,273.15],[0,-459.67,0,273.15],[-273.15,32,32+459.67,0]])
            i=l.index(self.reference)
            j=l.index(newRef)
            result=(self.value+transferMatrixConst[i])*transferMatrixCoeff[i]+transferMatrixConst2[i]
            return result[j]
        else:
            return "wrong reference, it must be in ['c','f','r','k']"

    def c(self):
        return self.temptransfer('c')

    def f(self):
        return self.temptransfer('f')

    def r(self):
        return self.temptransfer('r')

    def k(self):
        return self.temptransfer('k')
    
    def add(self,value):
        """
        This attribute add the described temperature to the reference object.
        Input:
            value(float): temperature to be added.
        Return:
            The function return the new temperature using the reference scale.
        """
        newValue = self.value+value
        return newValue

        
    def show(self):
        return str(np.round(self.value,2))+' °'+self.reference
