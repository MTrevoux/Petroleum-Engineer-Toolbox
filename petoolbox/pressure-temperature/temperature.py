from numpy import array

class Temperature(object):
    """Class describing temperature as a value and a scale reference.
    
    Features:
        Value(float): measured value
        Reference(str): The scale reference must be included in the list ['c','f','r','k']
        c : celsius
        f : fahrenheit
        r : rankine
        k : kelvin
    """
    unit_list=['c', 'f', 'r', 'k']
    
    transfer_matrix_coeff = array([
                [ 1, 1.8, 1.8, 1 ],
                [ 1/1.8, 1, 1, 1/1.8 ],
                [ 1/1.8 ,1 ,1 ,1/1.8 ],
                [ 1,1.8,1.8,1]
    ])
    transfer_matrix_const = array([
                [ 0, 0, 0, 0],
                [-32 ,0 ,0 ,-32 ],
                [-459.67-32 ,0 ,0 ,-459.67-32 ],
                [0 ,-273.15 ,-273.15 ,0 ]
    ])
    transfer_matrix_const2 = array([
                [0,32, 459.67+32 ,273.15 ],
                [0, 0, 459.67 ,273.15 ],
                [0, -459.67, 0, 273.15],
                [-273.15, 32, 32+459.67, 0]
    ])
    
    def __init__(self, value, reference):
        if reference in Temperature.unit_list:
            self.reference = reference
            self.value = value
        else:
            print(f"wrong reference, it must be in {Temperature.unit_list}")
            return None

    def temptransfer(self, new_ref):
        if new_ref in Temperature.unit_list:
            i = Temperature.unit_list.index(self.reference)
            j = Temperature.unit_list.index(new_ref)
            Result = (self.value + Temperature.transfer_matrix_const[i]) * Temperature.transfer_matrix_coeff[i]
                    + Temperature.transfer_matrix_const2[i]
            return Result[j]
        else:
            return f"wrong reference, it must be in {Temperature.unit_list}"

    def c(self):
        return self.temptransfer('c')

    def f(self):
        return self.temptransfer('f')

    def r(self):
        return self.temptransfer('r')

    def k(self):
        return self.temptransfer('k')
    
    def add(self, value):
        """This attribute add the described temperature to the reference object.
        
        Input:
            value(float): temperature to be added.
        Return:
            The function return the new temperature using the reference scale.
        """
        NewValue = self.value + value
        return NewValue

        
    def show(self):
        return f"{self.value} °{self.reference}"
