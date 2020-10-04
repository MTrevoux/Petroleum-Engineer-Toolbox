from numpy import log10,exp
from scipy.optimize import root

def zfactorBeggsBrill(P,T,SG):
	"""
	Calculation of z factor using explicit method
	INPUT:
	P in psia
	T in Rankine
	SG is the gas specific gravity
	Sutton correlation is used to calcultate pseudocritical properties. Validity SG in [0.57,1.68].
	No CO2 nor H2S corrections
	OUTPUT:
	z factor
	"""

	Ppc = 756.8 - 131.07 * SG - 3.6 * SG**2
	Tpc = 169.2 + 349.5 * SG - 74 * SG**2
	Tr = T / Tpc #rankine
	Pr = P / Ppc #psia

	A = 1.39 * (Tr - 0.92)**0.5 - 0.36 * Tr - 0.1
	E = 9 * (Tr - 1)
	F = 0.3106 - 0.49 * Tr + 0.1824 * Tr**2
	B = (0.62 - 0.23 * Tr) * Pr + (0.066 / (Tr - 0.86) - 0.037) * Pr**2 + 0.32 * Pr**2 / 10**E
	C = 0.132 - 0.32 * log10(Tr)
	D = 10**F

	z = A + (1 - A) / exp(B) + C * Pr**D

	return z


def zfactorDAK(P,T,SG):
	"""
	Calculation of z factor using implicit method
	INPUT:
	P in psia
	T in Rankine
	Sutton correlation is used to calcultate pseudocritical properties. Validity SG in [0.57,1.68].
	SG is the gas specific gravity
	No CO2 nor H2S corrections
	OUTPUT
	[z factor, Boolean]
	"""
	Ppc = 756.8 - 131.07 * SG - 3.6 * SG**2
	Tpc= 169.2 + 349.5 * SG - 74 * SG**2
	Tr = T / Tpc #rankine
	Pr = P / Ppc #psia
	#Dranchuk / Abou Kassem
	def katzfunc(z):
		rhor = 0.27 * Pr / ( Tr * z)
		C = [0, 0.3265, -1.07, -0.5339, 0.01569, -0.05165, 0.5475, -0.7361, 0.1844, 0.1056, 0.6134, 0.7210]
		RESULT = -z + 1
		+ (C[1] + C[2] / Tr + C[3] / Tr**3 + C[4] / Tr**4 + C[5] / Tr**5) * rhor + (C[6] + C[7] / Tr + C[8] / Tr**2) * rhor**2 - C[9] * (C[7] / Tr + C[8] / Tr**2 ) * rhor**5 + C[10] * (1 + C[11] * rhor**2) * (rhor**2 / Tr**3* exp(-C[11] * rhor**2))
		return RESULT

	X = root(katzfunc,1)
	results = [X.x[0], X.success]

	return results


def gasSG(z,P,T,SG):
	"""
	INPUT
	P = psia / T = f°
	z factor
	SG: gas specific gravity
	OUTPUT
	Gas specific gravity at P and T
	"""
	return 28.967 * SG * P / (z * (T + 459.67) * 10.732) / (28.967 * 14.7 / ((459.67 + 60) * 10.732))

def rhoGas(z,P,T,SG):
	"""
	INPUT
	P = psia / T = f°
	z factor
	SG: gas specific gravity
	OUTPUT
	Gas gravity in lbs/ft3 at P and T
	"""
	return 28.967 * SG * P / (z * (T + 459.67) * 10.732)

def standardVolume(V,z,P,T):
	"""
	Function to calculate a volume into standard conditions.
	INPUT
	V = volume or flow rate in whatever unit
	P = psia
	T = F
	zfactor
	OUTPUT
	volume in the same unit as V in standard condition 1 atm / 60°F.
	"""
	return V * P / (z * (T + 459.67)) * 1/(14.7 / (459.67 + 60))

def fluidPressure(rho,h):
	"""
	INPUT
	rho = lbs per ft3 and h = feet
	OUTPUT
	Pressure at the bottom of fluid column
	"""
	return rho * h / 144

