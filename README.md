# Petroleum-Engineer-Toolbox
Useful tools that can be used to solve different kind of problems faced by the production or petroleum engineer.

# Inside the toolbox:
## temperature.py

This module define the class temperature. Easy engineer approach about how to deal with a temperature.
Instead of always converting the values, you just need to call the unit which is an attribute. Set available:
- 'c': Celsius
- 'f': Fahrenheit
- 'r': Rankine
- 'k': Kelvin

Example: 
```
t = temperature(15,'c')  # (str) 'c' standing for celsius
t.f                      # (float) return the value converted into Fahrenheit.
```

## pressure.py

Under construction

## gasProperties.py

Functions avaible:
- zfactorBeggsBrill / calculation of the z factor using Beggs and Brill correlation. Explicit approach.
- zfactorDAK / calculation of the z factor using DAK correlation. Implicit approach.
- SGgas / calculate the specific gravity of a gas at given P and T with air reference at 60°F and 1 atm
- rhoGas / calculate the density in lbs/tf of a gas at given P and T

## oilProperties.py

Under construction
