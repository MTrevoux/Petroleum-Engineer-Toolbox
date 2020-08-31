class pressure(object):
    """
    Class describing pressure as a value and a scale reference.
    Features:
        Value(float): measured value
        First reference(str): The scale reference must be included in the list ['psi','bar','pa','atm','hPa','inchW','inchM']
        Second reference(str): 'g' for gage and 'a' for absolut
        
        inchW: temperature reference at 60°F
        inchM: temperature reference at 32°F
    """
    
    l=['psi','bar','pa','atm','hPa','inchW','inchM']
    convFactor=np.array([1,0.06894757,6894.757,0.06804596,68.94757,27.70759,2.036021])
    
    def __init__(self,value,unit,reference='g'):
        if unit in pressure.l and reference in ['g','a'] :
            self.reference=reference
            self.value=value
            self.unit=unit
        else:
            print("wrong unit, it must be in "+str(l))
            return None
        
    def ptransfer(self,newUnit,newRef='g'):
        '''
        Function used to transfer to another pressure unit.
        Base reference is gage pressure.
        INPUT:
            new unit desired
            new reference desired (base value 'g' for gage)
        OUTPUT:
            (float) pressure in the new unit.
        '''
        if newUnit in pressure.l and newRef in ['a','g']:
            i=pressure.l.index(self.unit)
            j=pressure.l.index(newUnit)
            result=self.value/pressure.convFactor[i]*pressure.convFactor[j]
            if newRef == self.reference:
                return result
            else:
                if newRef == 'g':
                    return result - 14.69595*pressure.convFactor[j]
                else:
                    return result + 14.69595*pressure.convFactor[j]
        else:
            return "wrong unit, it must be in " + str(pressure.l)
        
    def psia(self):
        return self.ptransfer('psi','a')

    def psig(self):
        return self.ptransfer('psi','g')

    def bara(self):
        return self.ptransfer('bar','a')

    def barg(self):
        return self.ptransfer('bar','g')
    
    def atma(self):
        return self.ptransfer('atm','a')

    def atmg(self):
        return self.ptransfer('atm','g')
    
    def paa(self):
        return self.ptransfer('pa','a')

    def pag(self):
        return self.ptransfer('pa','g')   
    
    def hpaa(self):
        return self.ptransfer('hpa','a')

    def hpag(self):
        return self.ptransfer('hpa','g')
    
    def inchWa(self):
        return self.ptransfer('inchW','a')

    def inchWg(self):
        return self.ptransfer('inchW','g')
    
    def inchMa(self):
        return self.ptransfer('inchM','a')

    def inchWg(self):
        return self.ptransfer('inchM','g')
    
    def add(self,value):
        """
        This attribute add the new described pressure to the reference object.
        Input:
            value(float): temperature to be added.
        Return:
            The function return the new temperature as a float.
        """
        newValue=self.value+value
        return newValue

        
    def show(self):
        return str(np.round(self.value,2))+' '+self.unit+self.reference
