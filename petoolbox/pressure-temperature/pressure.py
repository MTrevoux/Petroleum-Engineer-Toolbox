class Pressure(object):
    """Class describing pressure as a value and a scale reference.
    
    Features:
        Value(float): measured value
        First reference(str): The scale reference must be included in the list ['psi','bar','pa','atm','hPa','inchW','inchM']
        Second reference(str): 'g' for gage and 'a' for absolut
        
        inchW: temperature reference at 60°F
        inchM: temperature reference at 32°F
    """
    
    conv_factor_dict = {
        'psi': 1,
        'bar': 0.06894757,
        'pa': 6894.757,
        'atm': 0.06804596,
        'hPa': 68.94757,
        'inchW': 27.70759,
        'inchM': 2.036021
    }
    
    def __init__(self, value, unit, reference='g'):
        if unit in Pressure.conv_factor_dict.keys() and reference in ['g', 'a']:
            self.reference = reference
            self.value = value
            self.unit = unit
        else:
            print(f"wrong unit, it must be in {str(Pressure.conv_factor_dict.keys())} and reference must be in ['a', 'g']")
            return None
        
    def ptransfer(self, new_unit, new_ref='g'):
        '''Function used to transfer to another pressure unit.
        
        Base reference is gage pressure.
        INPUT:
            new unit desired
            new reference desired (base value 'g' for gage)
        OUTPUT:
            (float) pressure in the new unit.
        '''
        if new_unit in Pressure.conv_factor_dict.keys() and new_ref in ['a','g']:
            result = self.value / Pressure.conv_factor_dict[self.unit] * Pressure.conv_factor_dict[new_unit]
            if new_ref == self.reference:
                return result
            else:
                if new_ref == 'g':
                    return result - 14.69595 * Pressure.conv_factor_dict[new_unit]
                else:
                    return result + 14.69595 * Pressure.conv_factor_dict[new_unit]
        else:
            return f"wrong unit, it must be in {str(Pressure.conv_factor_dict.keys())} and reference must be in ['a', 'g']"
        
    def psia(self):
        return self.ptransfer('psi', 'a')

    def psig(self):
        return self.ptransfer('psi', 'g')

    def bara(self):
        return self.ptransfer('bar', 'a')

    def barg(self):
        return self.ptransfer('bar', 'g')
    
    def atma(self):
        return self.ptransfer('atm', 'a')

    def atmg(self):
        return self.ptransfer('atm', 'g')
    
    def paa(self):
        return self.ptransfer('pa', 'a')

    def pag(self):
        return self.ptransfer('pa', 'g')   
    
    def hpaa(self):
        return self.ptransfer('hpa', 'a')

    def hpag(self):
        return self.ptransfer('hpa', 'g')
    
    def inchWa(self):
        return self.ptransfer('inchW', 'a')

    def inchWg(self):
        return self.ptransfer('inchW', 'g')
    
    def inchMa(self):
        return self.ptransfer('inchM', 'a')

    def inchWg(self):
        return self.ptransfer('inchM', 'g')
    
    def add(self,value):
        """
        This attribute add the new described pressure to the reference object.
        Input:
            value(float): temperature to be added.
        Return:
            The function return the new temperature as a float.
        """
        NewValue = self.value + value
        return NewValue

        
    def show(self):
        return f"{str(self.value)} {self.unit}{self.reference}"
