# From Kittel: Introd. Solid State Physics, 7th ed. (1996)
Rydberg2eV = 13.6058
Bohr2Ang = 0.529177 
Ang2Bohr = 1/Bohr2Ang
amu2kg = 1.66053e-27
eV2Joule = 1.60219e-19
hbar2SI = 1.05459e-34

# From http://physics.nist.gov/constants
invm2eV =  1.239841875e-6
invcm2eV = 1.239841875e-4

# from http://physics.nist.gov/PhysRefData/Elements/
AtomicMass = {1:1.007947,    # H
              1001:2.016,    # Deuterium
              2:4.002602,    # He
              3:6.9412,      # Li
              4:9.012182,    # Be
              5:10.8117,     # B
              6:12.01078,    # C
              7:14.00672,    # N
              8:15.99943,    # O
              9:18.9984032,  # F
              11:22.989770,  # Na
              12:24.30506,   # Mg
              13:26.9815382, # Al
              14:28.0855,    # Si
              15:30.973761,  # P
              16:32.0655,    # S
              17:35.453,     # Cl
              19:39.0983,    # K
              20:40.0784,    # Ca
              22:47.867,     # Ti
              23:50.9415,    # V
              24:51.99616,   # Cr
              25:54.9380499, # Mn
              26:55.8452,    # Fe
              27:58.933200,  # Co
              28:58.69342,   # Ni
              29:63.5463,    # Cu
              30:65.4094,    # Zn
              31:69.7231,    # Ga
              33:74.92160,   # As
              45:102.90550,  # Rh
              46:106.42,     # Pd
              47:107.8682,   # Ag
              74:183.84,     # W
              77:192.217,    # Ir
              78:195.0782,   # Pt
              79:196.966552} # Au

# Map atomnumbers into elemental labels
PeriodicTable = {'H':1,1:'H','D':1001,1001:'D','He':2,2:'He','Li':3,3:'Li','Be':4,4:'Be','B':5,5:'B','C':6,6:'C','N':7,7:'N','O':8,8:'O','F':9,9:'F','Ne':10,10:'Ne','Na':11,11:'Na','Mg':12,12:'Mg','Al':13,13:'Al','Si':14,14:'Si','P':15,15:'P','S':16,16:'S','Cl':17,17:'Cl','Ar':18,18:'Ar','K':19,19:'K','Ca':20,20:'Ca','Sc':21,21:'Sc','Ti':22,22:'Ti','V':23,23:'V','Cr':24,24:'Cr','Mn':25,25:'Mn','Fe':26,26:'Fe','Co':27,27:'Co','Ni':28,28:'Ni','Cu':29,29:'Cu','Zn':30,30:'Zn','Ga':31,31:'Ga','Ge':32,32:'Ge','As':33,33:'As','Se':34,34:'Se','Br':35,35:'Br','Kr':36,36:'Kr','Rb':37,37:'Rb','Sr':38,38:'Sr','Y':39,39:'Y','Zr':40,40:'Zr','Nb':41,41:'Nb','Mo':42,42:'Mo','Tc':43,43:'Tc','Ru':44,44:'Ru','Rh':45,45:'Rh','Pd':46,46:'Pd','Ag':47,47:'Ag','Cd':48,48:'Cd','In':49,49:'In','Sn':50,50:'Sn','Sb':51,51:'Sb','Te':52,52:'Te','I':53,53:'I','Xe':54,54:'Xe','Cs':55,55:'Cs','Ba':56,56:'Ba','La':57,57:'La','Ce':58,58:'Ce','Pr':59,59:'Pr','Nd':60,60:'Nd','Pm':61,61:'Pm','Sm':62,62:'Sm','Eu':63,63:'Eu','Gd':64,64:'Gd','Tb':65,65:'Tb','Dy':66,66:'Dy','Ho':67,67:'Ho','Er':68,68:'Er','Tm':69,69:'Tm','Yb':70,70:'Yb','Lu':71,71:'Lu','Hf':72,72:'Hf','Ta':73,73:'Ta','W':74,74:'W','Re':75,75:'Re','Os':76,76:'Os','Ir':77,77:'Ir','Pt':78,78:'Pt','Au':79,79:'Au','Hg':80,80:'Hg','Tl':81,81:'Tl','Pb':82,82:'Pb','Bi':83,83:'Bi','Po':84,84:'Po','At':85,85:'At','Rn':86,86:'Rn','Fr':87,87:'Fr','Ra':88,88:'Ra','Ac':89,89:'Ac','Th':90,90:'Th','Pa':91,91:'Pa','U':92,92:'U','Np':93,93:'Np','Pu':94,94:'Pu','Am':95,95:'Am','Cm':96,96:'Cm','Bk':97,97:'Bk','Cf':98,98:'Cf','Es':99,99:'Es','Fm':100,100:'Fm','Md':101,101:'Md','No':102,102:'No'}
