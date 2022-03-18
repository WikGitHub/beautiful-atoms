"""
Todo: add ionic_radii

"""
from ase.data.colors import jmol_colors, cpk_colors
from ase.data import covalent_radii, vdw_radii
vdw_radii.flags.writeable = True

covalent_radii[0] = 1.0
vdw_radii[0] = 1.0
ionic_radii = {}


jmol_colors[0] = [0.8, 0.8, 0.0]
cpk_colors[0] = [0.8, 0.8, 0.0]


vesta_color = {
    'X': [0.8, 0.0, 0.8],
    'H': [1.0, 0.8, 0.8],
    'D': [0.8, 0.8, 1.0],
    'He': [0.98907, 0.91312, 0.81091],
    'Li': [0.52731, 0.87953, 0.4567],
    'Be': [0.37147, 0.8459, 0.48292],
    'B': [0.1249, 0.63612, 0.05948],
    'C': [0.5043, 0.28659, 0.16236],
    'N': [0.69139, 0.72934, 0.9028],
    'O': [0.99997, 0.01328, 0.0],
    'F': [0.69139, 0.72934, 0.9028],
    'Ne': [0.99954, 0.21788, 0.71035],
    'Na': [0.97955, 0.86618, 0.23787],
    'Mg': [0.98773, 0.48452, 0.0847],
    'Al': [0.50718, 0.70056, 0.84062],
    'Si': [0.10596, 0.23226, 0.98096],
    'P': [0.75557, 0.61256, 0.76425],
    'S': [1.0, 0.98071, 0.0],
    'Cl': [0.19583, 0.98828, 0.01167],
    'Ar': [0.81349, 0.99731, 0.77075],
    'K': [0.63255, 0.13281, 0.96858],
    'Ca': [0.35642, 0.58863, 0.74498],
    'Sc': [0.71209, 0.3893, 0.67279],
    'Ti': [0.47237, 0.79393, 1.0],
    'V': [0.9, 0.1, 0.0],
    'Cr': [0.0, 0.0, 0.62],
    'Mn': [0.66148, 0.03412, 0.62036],
    'Fe': [0.71051, 0.44662, 0.00136],
    'Co': [0.0, 0.0, 0.68666],
    'Ni': [0.72032, 0.73631, 0.74339],
    'Cu': [0.1339, 0.28022, 0.86606],
    'Zn': [0.56123, 0.56445, 0.50799],
    'Ga': [0.62292, 0.89293, 0.45486],
    'Ge': [0.49557, 0.43499, 0.65193],
    'As': [0.45814, 0.81694, 0.34249],
    'Se': [0.6042, 0.93874, 0.06122],
    'Br': [0.49645, 0.19333, 0.01076],
    'Kr': [0.98102, 0.75805, 0.95413],
    'Rb': [1.0, 0.0, 0.6],
    'Sr': [0.0, 1.0, 0.15259],
    'Y': [0.40259, 0.59739, 0.55813],
    'Zr': [0.0, 1.0, 0.0],
    'Nb': [0.29992, 0.70007, 0.46459],
    'Mo': [0.70584, 0.52602, 0.68925],
    'Tc': [0.80574, 0.68699, 0.79478],
    'Ru': [0.81184, 0.72113, 0.68089],
    'Rh': [0.80748, 0.82205, 0.67068],
    'Pd': [0.75978, 0.76818, 0.72454],
    'Ag': [0.72032, 0.73631, 0.74339],
    'Cd': [0.95145, 0.12102, 0.86354],
    'In': [0.84378, 0.50401, 0.73483],
    'Sn': [0.60764, 0.56052, 0.72926],
    'Sb': [0.84627, 0.51498, 0.31315],
    'Te': [0.67958, 0.63586, 0.32038],
    'I': [0.55914, 0.122, 0.54453],
    'Xe': [0.60662, 0.63218, 0.97305],
    'Cs': [0.05872, 0.99922, 0.72578],
    'Ba': [0.11835, 0.93959, 0.17565],
    'La': [0.3534, 0.77057, 0.28737],
    'Ce': [0.82055, 0.99071, 0.02374],
    'Pr': [0.9913, 0.88559, 0.02315],
    'Nd': [0.98701, 0.5556, 0.02744],
    'Pm': [0.0, 0.0, 0.96],
    'Sm': [0.99042, 0.02403, 0.49195],
    'Eu': [0.98367, 0.03078, 0.83615],
    'Gd': [0.75325, 0.01445, 1.0],
    'Tb': [0.44315, 0.01663, 0.99782],
    'Dy': [0.1939, 0.02374, 0.99071],
    'Ho': [0.02837, 0.25876, 0.98608],
    'Er': [0.28688, 0.45071, 0.23043],
    'Tm': [0.0, 0.0, 0.88],
    'Yb': [0.15323, 0.99165, 0.95836],
    'Lu': [0.15097, 0.99391, 0.71032],
    'Hf': [0.70704, 0.70552, 0.3509],
    'Ta': [0.71952, 0.60694, 0.33841],
    'W': [0.55616, 0.54257, 0.50178],
    'Re': [0.70294, 0.69401, 0.55789],
    'Os': [0.78703, 0.69512, 0.47379],
    'Ir': [0.78975, 0.81033, 0.45049],
    'Pt': [0.79997, 0.77511, 0.75068],
    'Au': [0.99628, 0.70149, 0.22106],
    'Hg': [0.8294, 0.72125, 0.79823],
    'Tl': [0.58798, 0.53854, 0.42649],
    'Pb': [0.32386, 0.32592, 0.35729],
    'Bi': [0.82428, 0.18732, 0.97211],
    'Po': [0.0, 0.0, 1.0],
    'At': [0.0, 0.0, 1.0],
    'Rn': [1.0, 1.0, 0.0],
    'Fr': [0.0, 0.0, 0.0],
    'Ra': [0.42959, 0.66659, 0.34786],
    'Ac': [0.39344, 0.62101, 0.45034],
    'Th': [0.14893, 0.99596, 0.47106],
    'Pa': [0.16101, 0.98387, 0.20855],
    'U': [0.47774, 0.63362, 0.66714],
    'Np': [0.3, 0.3, 0.3],
    'Pu': [0.3, 0.3, 0.3],
    'Am': [0.3, 0.3, 0.3],
    'XX': [0.3, 0.3, 0.3],
}

# Default bondsetting suggestion from VESTA
# bond pair    search mode   polyhedra
default_bonds = {
    ('Ac', 'O'):  [1,  1, 0],
    ('Ac', 'F'):  [1,  1, 0],
    ('Ac', 'Cl'):  [1,  1, 0],
    ('Ac', 'Br'):  [1,  1, 0],
    ('Ag', 'O'):  [1,  1, 0],
    ('Ag', 'S'):  [1,  1, 0],
    ('Ag', 'F'):  [1,  1, 0],
    ('Ag', 'Cl'):  [1,  1, 0],
    ('Ag', 'Br'):  [1,  1, 0],
    ('Ag', 'I'):  [1,  1, 0],
    ('Ag', 'Se'):  [1,  1, 0],
    ('Ag', 'Te'):  [1,  1, 0],
    ('Ag', 'N'):  [1,  1, 0],
    ('Ag', 'P'):  [1,  1, 0],
    ('Ag', 'As'):  [1,  1, 0],
    ('Ag', 'H'):  [1,  1, 0],
    ('Al', 'O'):  [1,  1, 0],
    ('Al', 'S'):  [1,  1, 0],
    ('Al', 'Se'):  [1,  1, 0],
    ('Al', 'Te'):  [1,  1, 0],
    ('Al', 'F'):  [1,  1, 0],
    ('Al', 'Cl'):  [1,  1, 0],
    ('Al', 'Br'):  [1,  1, 0],
    ('Al', 'I'):  [1,  1, 0],
    ('Al', 'N'):  [1,  1, 0],
    ('Al', 'P'):  [1,  1, 0],
    ('Al', 'As'):  [1,  1, 0],
    ('Al', 'H'):  [1,  1, 0],
    ('Am', 'O'):  [1,  1, 0],
    ('Am', 'F'):  [1,  1, 0],
    ('Am', 'Cl'):  [1,  1, 0],
    ('Am', 'Br'):  [1,  1, 0],
    ('As', 'S'):  [1,  1, 0],
    ('As', 'Se'):  [1,  1, 0],
    ('As', 'O'):  [1,  1, 0],
    ('As', 'Te'):  [1,  1, 0],
    ('As', 'F'):  [1,  1, 0],
    ('As', 'Cl'):  [1,  1, 0],
    ('As', 'Br'):  [1,  1, 0],
    ('As', 'I'):  [1,  1, 0],
    ('As', 'C'):  [1,  1, 0],
    ('Au', 'Cl'):  [1,  1, 0],
    ('Au', 'I'):  [1,  1, 0],
    ('Au', 'O'):  [1,  1, 0],
    ('Au', 'S'):  [1,  1, 0],
    ('Au', 'F'):  [1,  1, 0],
    ('Au', 'Br'):  [1,  1, 0],
    ('Au', 'N'):  [1,  1, 0],
    ('Au', 'Se'):  [1,  1, 0],
    ('Au', 'Te'):  [1,  1, 0],
    ('Au', 'P'):  [1,  1, 0],
    ('Au', 'As'):  [1,  1, 0],
    ('Au', 'H'):  [1,  1, 0],
    ('B', 'O'):  [1,  1, 0],
    ('B', 'S'):  [1,  1, 0],
    ('B', 'Se'):  [1,  1, 0],
    ('B', 'Te'):  [1,  1, 0],
    ('B', 'F'):  [1,  1, 0],
    ('B', 'Cl'):  [1,  1, 0],
    ('B', 'Br'):  [1,  1, 0],
    ('B', 'I'):  [1,  1, 0],
    ('B', 'N'):  [1,  1, 0],
    ('B', 'P'):  [1,  1, 0],
    ('B', 'As'):  [1,  1, 0],
    ('B', 'H'):  [1,  1, 0],
    ('B', 'B'):  [1,  1, 0],
    ('Ba', 'O'):  [1,  1, 0],
    ('Ba', 'S'):  [1,  1, 0],
    ('Ba', 'Se'):  [1,  1, 0],
    ('Ba', 'Te'):  [1,  1, 0],
    ('Ba', 'F'):  [1,  1, 0],
    ('Ba', 'Cl'):  [1,  1, 0],
    ('Ba', 'Br'):  [1,  1, 0],
    ('Ba', 'I'):  [1,  1, 0],
    ('Ba', 'N'):  [1,  1, 0],
    ('Ba', 'P'):  [1,  1, 0],
    ('Ba', 'As'):  [1,  1, 0],
    ('Ba', 'H'):  [1,  1, 0],
    ('Be', 'O'):  [1,  1, 0],
    ('Be', 'S'):  [1,  1, 0],
    ('Be', 'Se'):  [1,  1, 0],
    ('Be', 'Te'):  [1,  1, 0],
    ('Be', 'F'):  [1,  1, 0],
    ('Be', 'Cl'):  [1,  1, 0],
    ('Be', 'Br'):  [1,  1, 0],
    ('Be', 'I'):  [1,  1, 0],
    ('Be', 'N'):  [1,  1, 0],
    ('Be', 'P'):  [1,  1, 0],
    ('Be', 'As'):  [1,  1, 0],
    ('Be', 'H'):  [1,  1, 0],
    ('Bi', 'O'):  [1,  1, 0],
    ('Bi', 'S'):  [1,  1, 0],
    ('Bi', 'Se'):  [1,  1, 0],
    ('Bi', 'F'):  [1,  1, 0],
    ('Bi', 'Cl'):  [1,  1, 0],
    ('Bi', 'Br'):  [1,  1, 0],
    ('Bi', 'I'):  [1,  1, 0],
    ('Bi', 'N'):  [1,  1, 0],
    ('Bi', 'Te'):  [1,  1, 0],
    ('Bi', 'P'):  [1,  1, 0],
    ('Bi', 'As'):  [1,  1, 0],
    ('Bi', 'H'):  [1,  1, 0],
    ('Bk', 'O'):  [1,  1, 0],
    ('Bk', 'F'):  [1,  1, 0],
    ('Bk', 'Cl'):  [1,  1, 0],
    ('Bk', 'Br'):  [1,  1, 0],
    ('Br', 'O'):  [1,  1, 0],
    ('Br', 'F'):  [1,  1, 0],
    ('Br', 'Cl'):  [1,  1, 0],
    ('C', 'Au'):  [1,  1, 0],
    ('C', 'O'):  [2,  1, 0],
    ('C', 'Cl'):  [2,  1, 0],
    ('C', 'C'):  [2,  0, 0],
    ('C', 'S'):  [2,  0, 0],
    ('C', 'F'):  [2,  1, 0],
    ('C', 'Br'):  [2,  1, 0],
    ('C', 'N'):  [2,  1, 0],
    ('C', 'Se'):  [2,  1, 0],
    ('C', 'I'):  [2,  1, 0],
    ('C', 'Te'):  [1,  1, 0],
    ('C', 'P'):  [2,  1, 0],
    ('C', 'Pt'):  [1,  1, 0],
    ('C', 'H'):  [1,  0, 0],
    ('Ca', 'O'):  [1,  1, 0],
    ('Ca', 'S'):  [1,  1, 0],
    ('Ca', 'Se'):  [1,  1, 0],
    ('Ca', 'Te'):  [1,  1, 0],
    ('Ca', 'F'):  [1,  1, 0],
    ('Ca', 'Cl'):  [1,  1, 0],
    ('Ca', 'Br'):  [1,  1, 0],
    ('Ca', 'I'):  [1,  1, 0],
    ('Ca', 'N'):  [1,  1, 0],
    ('Ca', 'P'):  [1,  1, 0],
    ('Ca', 'As'):  [1,  1, 0],
    ('Ca', 'H'):  [1,  1, 0],
    ('Cd', 'O'):  [1,  1, 0],
    ('Cd', 'S'):  [1,  1, 0],
    ('Cd', 'Se'):  [1,  1, 0],
    ('Cd', 'Te'):  [1,  1, 0],
    ('Cd', 'F'):  [1,  1, 0],
    ('Cd', 'Cl'):  [1,  1, 0],
    ('Cd', 'Br'):  [1,  1, 0],
    ('Cd', 'I'):  [1,  1, 0],
    ('Cd', 'N'):  [1,  1, 0],
    ('Cd', 'P'):  [1,  1, 0],
    ('Cd', 'As'):  [1,  1, 0],
    ('Cd', 'H'):  [1,  1, 0],
    ('Ce', 'O'):  [1,  1, 0],
    ('Ce', 'S'):  [1,  1, 0],
    ('Ce', 'F'):  [1,  1, 0],
    ('Ce', 'Cl'):  [1,  1, 0],
    ('Ce', 'Br'):  [1,  1, 0],
    ('Ce', 'I'):  [1,  1, 0],
    ('Ce', 'N'):  [1,  1, 0],
    ('Ce', 'Se'):  [1,  1, 0],
    ('Ce', 'Te'):  [1,  1, 0],
    ('Ce', 'P'):  [1,  1, 0],
    ('Ce', 'As'):  [1,  1, 0],
    ('Ce', 'H'):  [1,  1, 0],
    ('Cf', 'O'):  [1,  1, 0],
    ('Cf', 'F'):  [1,  1, 0],
    ('Cf', 'Cl'):  [1,  1, 0],
    ('Cf', 'Br'):  [1,  1, 0],
    ('Cl', 'H'):  [1,  0, 0],
    ('Cl', 'O'):  [1,  1, 0],
    ('Cl', 'F'):  [1,  1, 0],
    ('Cl', 'Cl'):  [1,  1, 0],
    ('Cm', 'O'):  [1,  1, 0],
    ('Cm', 'F'):  [1,  1, 0],
    ('Cm', 'Cl'):  [1,  1, 0],
    ('Co', 'H'):  [1,  1, 0],
    ('Co', 'O'):  [1,  1, 0],
    ('Co', 'S'):  [1,  1, 0],
    ('Co', 'F'):  [1,  1, 0],
    ('Co', 'Cl'):  [1,  1, 0],
    ('Co', 'N'):  [1,  1, 0],
    ('Co', 'C'):  [1,  1, 0],
    ('Co', 'Br'):  [1,  1, 0],
    ('Co', 'I'):  [1,  1, 0],
    ('Co', 'Se'):  [1,  1, 0],
    ('Co', 'Te'):  [1,  1, 0],
    ('Co', 'P'):  [1,  1, 0],
    ('Co', 'As'):  [1,  1, 0],
    ('Cr', 'O'):  [1,  1, 0],
    ('Cr', 'F'):  [1,  1, 0],
    ('Cr', 'Cl'):  [1,  1, 0],
    ('Cr', 'Br'):  [1,  1, 0],
    ('Cr', 'I'):  [1,  1, 0],
    ('Cr', 'N'):  [1,  1, 0],
    ('Cr', 'S'):  [1,  1, 0],
    ('Cr', 'Se'):  [1,  1, 0],
    ('Cr', 'Te'):  [1,  1, 0],
    ('Cr', 'P'):  [1,  1, 0],
    ('Cr', 'As'):  [1,  1, 0],
    ('Cr', 'H'):  [1,  1, 0],
    ('Cs', 'O'):  [1,  1, 0],
    ('Cs', 'S'):  [1,  1, 0],
    ('Cs', 'Se'):  [1,  1, 0],
    ('Cs', 'Te'):  [1,  1, 0],
    ('Cs', 'F'):  [1,  1, 0],
    ('Cs', 'Cl'):  [1,  1, 0],
    ('Cs', 'Br'):  [1,  1, 0],
    ('Cs', 'I'):  [1,  1, 0],
    ('Cs', 'N'):  [1,  1, 0],
    ('Cs', 'P'):  [1,  1, 0],
    ('Cs', 'As'):  [1,  1, 0],
    ('Cs', 'H'):  [1,  1, 0],
    ('Cu', 'O'):  [1,  1, 0],
    ('Cu', 'S'):  [1,  1, 0],
    ('Cu', 'Se'):  [1,  1, 0],
    ('Cu', 'F'):  [1,  1, 0],
    ('Cu', 'Cl'):  [1,  1, 0],
    ('Cu', 'Br'):  [1,  1, 0],
    ('Cu', 'I'):  [1,  1, 0],
    ('Cu', 'N'):  [1,  1, 0],
    ('Cu', 'P'):  [1,  1, 0],
    ('Cu', 'As'):  [1,  1, 0],
    ('Cu', 'C'):  [1,  1, 0],
    ('Cu', 'Te'):  [1,  1, 0],
    ('Cu', 'H'):  [1,  1, 0],
    ('Dy', 'O'):  [1,  1, 0],
    ('Dy', 'F'):  [1,  1, 0],
    ('Dy', 'Cl'):  [1,  1, 0],
    ('Dy', 'Br'):  [1,  1, 0],
    ('Dy', 'I'):  [1,  1, 0],
    ('Dy', 'S'):  [1,  1, 0],
    ('Dy', 'Se'):  [1,  1, 0],
    ('Dy', 'Te'):  [1,  1, 0],
    ('Dy', 'N'):  [1,  1, 0],
    ('Dy', 'P'):  [1,  1, 0],
    ('Dy', 'As'):  [1,  1, 0],
    ('Dy', 'H'):  [1,  1, 0],
    ('Er', 'O'):  [1,  1, 0],
    ('Er', 'S'):  [1,  1, 0],
    ('Er', 'Se'):  [1,  1, 0],
    ('Er', 'F'):  [1,  1, 0],
    ('Er', 'Cl'):  [1,  1, 0],
    ('Er', 'Br'):  [1,  1, 0],
    ('Er', 'I'):  [1,  1, 0],
    ('Er', 'Te'):  [1,  1, 0],
    ('Er', 'N'):  [1,  1, 0],
    ('Er', 'P'):  [1,  1, 0],
    ('Er', 'As'):  [1,  1, 0],
    ('Er', 'H'):  [1,  1, 0],
    ('Es', 'O'):  [1,  1, 0],
    ('Eu', 'O'):  [1,  1, 0],
    ('Eu', 'S'):  [1,  1, 0],
    ('Eu', 'F'):  [1,  1, 0],
    ('Eu', 'Cl'):  [1,  1, 0],
    ('Eu', 'Br'):  [1,  1, 0],
    ('Eu', 'I'):  [1,  1, 0],
    ('Eu', 'N'):  [1,  1, 0],
    ('Eu', 'Se'):  [1,  1, 0],
    ('Eu', 'Te'):  [1,  1, 0],
    ('Eu', 'P'):  [1,  1, 0],
    ('Eu', 'As'):  [1,  1, 0],
    ('Eu', 'H'):  [1,  1, 0],
    ('F', 'H'):  [1,  0, 0],
    ('Fe', 'O'):  [1,  1, 0],
    ('Fe', 'S'):  [1,  1, 0],
    ('Fe', 'F'):  [1,  1, 0],
    ('Fe', 'Cl'):  [1,  1, 0],
    ('Fe', 'Br'):  [1,  1, 0],
    ('Fe', 'I'):  [1,  1, 0],
    ('Fe', 'N'):  [1,  1, 0],
    ('Fe', 'C'):  [1,  1, 0],
    ('Fe', 'Se'):  [1,  1, 0],
    ('Fe', 'Te'):  [1,  1, 0],
    ('Fe', 'P'):  [1,  1, 0],
    ('Fe', 'As'):  [1,  1, 0],
    ('Fe', 'H'):  [1,  1, 0],
    ('Ga', 'Se'):  [1,  1, 0],
    ('Ga', 'O'):  [1,  1, 0],
    ('Ga', 'S'):  [1,  1, 0],
    ('Ga', 'F'):  [1,  1, 0],
    ('Ga', 'Cl'):  [1,  1, 0],
    ('Ga', 'Br'):  [1,  1, 0],
    ('Ga', 'I'):  [1,  1, 0],
    ('Ga', 'Te'):  [1,  1, 0],
    ('Ga', 'N'):  [1,  1, 0],
    ('Ga', 'P'):  [1,  1, 0],
    ('Ga', 'As'):  [1,  1, 0],
    ('Ga', 'H'):  [1,  1, 0],
    ('Gd', 'O'):  [1,  1, 0],
    ('Gd', 'F'):  [1,  1, 0],
    ('Gd', 'S'):  [1,  1, 0],
    ('Gd', 'Cl'):  [1,  1, 0],
    ('Gd', 'Br'):  [1,  1, 0],
    ('Gd', 'I'):  [1,  1, 0],
    ('Gd', 'Se'):  [1,  1, 0],
    ('Gd', 'Te'):  [1,  1, 0],
    ('Gd', 'N'):  [1,  1, 0],
    ('Gd', 'P'):  [1,  1, 0],
    ('Gd', 'As'):  [1,  1, 0],
    ('Gd', 'H'):  [1,  1, 0],
    ('Ge', 'O'):  [1,  1, 0],
    ('Ge', 'S'):  [1,  1, 0],
    ('Ge', 'Se'):  [1,  1, 0],
    ('Ge', 'F'):  [1,  1, 0],
    ('Ge', 'Cl'):  [1,  1, 0],
    ('Ge', 'Br'):  [1,  1, 0],
    ('Ge', 'I'):  [1,  1, 0],
    ('Ge', 'Te'):  [1,  1, 0],
    ('Ge', 'N'):  [1,  1, 0],
    ('Ge', 'P'):  [1,  1, 0],
    ('Ge', 'As'):  [1,  1, 0],
    ('Ge', 'H'):  [1,  1, 0],
    ('Ge', 'Ge'):  [1,  1, 0],
    ('O', 'H'):  [1,  0, 0],
    ('H', 'O'):  [0,  0, 1],
    ('H', 'N'):  [0,  0, 1],
    ('O', 'D'):  [1,  0, 0],
    ('D', 'O'):  [0,  0, 0],
    ('D', 'F'):  [1,  0, 0],
    ('D', 'Cl'):  [1,  0, 0],
    ('D', 'N'):  [1,  0, 0],
    ('Hf', 'F'):  [1,  1, 0],
    ('Hf', 'O'):  [1,  1, 0],
    ('Hf', 'Cl'):  [1,  1, 0],
    ('Hf', 'Br'):  [1,  1, 0],
    ('Hf', 'S'):  [1,  1, 0],
    ('Hf', 'Se'):  [1,  1, 0],
    ('Hf', 'Te'):  [1,  1, 0],
    ('Hf', 'I'):  [1,  1, 0],
    ('Hf', 'N'):  [1,  1, 0],
    ('Hf', 'P'):  [1,  1, 0],
    ('Hf', 'As'):  [1,  1, 0],
    ('Hf', 'H'):  [1,  1, 0],
    ('Hg', 'O'):  [1,  1, 0],
    ('Hg', 'F'):  [1,  1, 0],
    ('Hg', 'Cl'):  [1,  1, 0],
    ('Hg', 'S'):  [1,  1, 0],
    ('Hg', 'Br'):  [1,  1, 0],
    ('Hg', 'I'):  [1,  1, 0],
    ('Hg', 'Se'):  [1,  1, 0],
    ('Hg', 'Te'):  [1,  1, 0],
    ('Hg', 'N'):  [1,  1, 0],
    ('Hg', 'P'):  [1,  1, 0],
    ('Hg', 'As'):  [1,  1, 0],
    ('Hg', 'H'):  [1,  1, 0],
    ('Hg', 'Hg'):  [1,  1, 0],
    ('Ho', 'O'):  [1,  1, 0],
    ('Ho', 'S'):  [1,  1, 0],
    ('Ho', 'F'):  [1,  1, 0],
    ('Ho', 'Cl'):  [1,  1, 0],
    ('Ho', 'Br'):  [1,  1, 0],
    ('Ho', 'I'):  [1,  1, 0],
    ('Ho', 'Se'):  [1,  1, 0],
    ('Ho', 'Te'):  [1,  1, 0],
    ('Ho', 'N'):  [1,  1, 0],
    ('Ho', 'P'):  [1,  1, 0],
    ('Ho', 'As'):  [1,  1, 0],
    ('Ho', 'H'):  [1,  1, 0],
    ('I', 'I'):  [1,  1, 0],
    ('I', 'F'):  [1,  1, 0],
    ('I', 'Cl'):  [1,  1, 0],
    ('I', 'O'):  [1,  1, 0],
    ('In', 'Cl'):  [1,  1, 0],
    ('In', 'O'):  [1,  1, 0],
    ('In', 'S'):  [1,  1, 0],
    ('In', 'F'):  [1,  1, 0],
    ('In', 'Br'):  [1,  1, 0],
    ('In', 'I'):  [1,  1, 0],
    ('In', 'Co'):  [1,  1, 0],
    ('In', 'Mn'):  [1,  1, 0],
    ('In', 'Se'):  [1,  1, 0],
    ('In', 'Te'):  [1,  1, 0],
    ('In', 'N'):  [1,  1, 0],
    ('In', 'P'):  [1,  1, 0],
    ('In', 'As'):  [1,  1, 0],
    ('In', 'H'):  [1,  1, 0],
    ('Ir', 'O'):  [1,  1, 0],
    ('Ir', 'F'):  [1,  1, 0],
    ('Ir', 'Cl'):  [1,  1, 0],
    ('Ir', 'S'):  [1,  1, 0],
    ('Ir', 'Se'):  [1,  1, 0],
    ('Ir', 'Te'):  [1,  1, 0],
    ('Ir', 'Br'):  [1,  1, 0],
    ('Ir', 'I'):  [1,  1, 0],
    ('Ir', 'N'):  [1,  1, 0],
    ('Ir', 'P'):  [1,  1, 0],
    ('Ir', 'As'):  [1,  1, 0],
    ('Ir', 'H'):  [1,  1, 0],
    ('K', 'O'):  [1,  1, 0],
    ('K', 'S'):  [1,  1, 0],
    ('K', 'Se'):  [1,  1, 0],
    ('K', 'Te'):  [1,  1, 0],
    ('K', 'F'):  [1,  1, 0],
    ('K', 'Cl'):  [1,  1, 0],
    ('K', 'Br'):  [1,  1, 0],
    ('K', 'I'):  [1,  1, 0],
    ('K', 'N'):  [1,  1, 0],
    ('K', 'P'):  [1,  1, 0],
    ('K', 'As'):  [1,  1, 0],
    ('K', 'H'):  [1,  1, 0],
    ('Kr', 'F'):  [1,  1, 0],
    ('La', 'O'):  [1,  1, 0],
    ('La', 'S'):  [1,  1, 0],
    ('La', 'Se'):  [1,  1, 0],
    ('La', 'Te'):  [1,  1, 0],
    ('La', 'F'):  [1,  1, 0],
    ('La', 'Cl'):  [1,  1, 0],
    ('La', 'Br'):  [1,  1, 0],
    ('La', 'I'):  [1,  1, 0],
    ('La', 'N'):  [1,  1, 0],
    ('La', 'P'):  [1,  1, 0],
    ('La', 'As'):  [1,  1, 0],
    ('La', 'H'):  [1,  1, 0],
    ('Li', 'O'):  [1,  1, 0],
    ('Li', 'S'):  [1,  1, 0],
    ('Li', 'Se'):  [1,  1, 0],
    ('Li', 'Te'):  [1,  1, 0],
    ('Li', 'F'):  [1,  1, 0],
    ('Li', 'Cl'):  [1,  1, 0],
    ('Li', 'Br'):  [1,  1, 0],
    ('Li', 'I'):  [1,  1, 0],
    ('Li', 'N'):  [1,  1, 0],
    ('Lu', 'O'):  [1,  1, 0],
    ('Lu', 'S'):  [1,  1, 0],
    ('Lu', 'Se'):  [1,  1, 0],
    ('Lu', 'Te'):  [1,  1, 0],
    ('Lu', 'F'):  [1,  1, 0],
    ('Lu', 'Cl'):  [1,  1, 0],
    ('Lu', 'Br'):  [1,  1, 0],
    ('Lu', 'I'):  [1,  1, 0],
    ('Lu', 'N'):  [1,  1, 0],
    ('Lu', 'P'):  [1,  1, 0],
    ('Lu', 'As'):  [1,  1, 0],
    ('Lu', 'H'):  [1,  1, 0],
    ('Mg', 'O'):  [1,  1, 0],
    ('Mg', 'S'):  [1,  1, 0],
    ('Mg', 'Se'):  [1,  1, 0],
    ('Mg', 'Te'):  [1,  1, 0],
    ('Mg', 'F'):  [1,  1, 0],
    ('Mg', 'Cl'):  [1,  1, 0],
    ('Mg', 'Br'):  [1,  1, 0],
    ('Mg', 'I'):  [1,  1, 0],
    ('Mg', 'N'):  [1,  1, 0],
    ('Mg', 'P'):  [1,  1, 0],
    ('Mg', 'As'):  [1,  1, 0],
    ('Mg', 'H'):  [1,  1, 0],
    ('Mn', 'O'):  [1,  1, 0],
    ('Mn', 'S'):  [1,  1, 0],
    ('Mn', 'F'):  [1,  1, 0],
    ('Mn', 'Cl'):  [1,  1, 0],
    ('Mn', 'Br'):  [1,  1, 0],
    ('Mn', 'I'):  [1,  1, 0],
    ('Mn', 'N'):  [1,  1, 0],
    ('Mn', 'Se'):  [1,  1, 0],
    ('Mn', 'Te'):  [1,  1, 0],
    ('Mn', 'P'):  [1,  1, 0],
    ('Mn', 'As'):  [1,  1, 0],
    ('Mn', 'H'):  [1,  1, 0],
    ('Mo', 'S'):  [1,  1, 0],
    ('Mo', 'Cl'):  [1,  1, 0],
    ('Mo', 'O'):  [1,  1, 0],
    ('Mo', 'F'):  [1,  1, 0],
    ('Mo', 'Br'):  [1,  1, 0],
    ('Mo', 'N'):  [1,  1, 0],
    ('Mo', 'I'):  [1,  1, 0],
    ('Mo', 'Se'):  [1,  1, 0],
    ('Mo', 'Te'):  [1,  1, 0],
    ('Mo', 'P'):  [1,  1, 0],
    ('Mo', 'As'):  [1,  1, 0],
    ('Mo', 'H'):  [1,  1, 0],
    ('N', 'H'):  [1,  0, 0],
    ('N', 'O'):  [1,  1, 0],
    ('N', 'F'):  [1,  1, 0],
    ('N', 'Cl'):  [1,  1, 0],
    ('N', 'N'):  [1,  1, 0],
    ('Na', 'O'):  [1,  1, 0],
    ('Na', 'S'):  [1,  1, 0],
    ('Na', 'Se'):  [1,  1, 0],
    ('Na', 'Te'):  [1,  1, 0],
    ('Na', 'F'):  [1,  1, 0],
    ('Na', 'Cl'):  [1,  1, 0],
    ('Na', 'Br'):  [1,  1, 0],
    ('Na', 'I'):  [1,  1, 0],
    ('Na', 'N'):  [1,  1, 0],
    ('Na', 'P'):  [1,  1, 0],
    ('Na', 'As'):  [1,  1, 0],
    ('Na', 'H'):  [1,  1, 0],
    ('Nb', 'O'):  [1,  1, 0],
    ('Nb', 'F'):  [1,  1, 0],
    ('Nb', 'Cl'):  [1,  1, 0],
    ('Nb', 'Br'):  [1,  1, 0],
    ('Nb', 'N'):  [1,  1, 0],
    ('Nb', 'I'):  [1,  1, 0],
    ('Nb', 'S'):  [1,  1, 0],
    ('Nb', 'Se'):  [1,  1, 0],
    ('Nb', 'Te'):  [1,  1, 0],
    ('Nb', 'P'):  [1,  1, 0],
    ('Nb', 'As'):  [1,  1, 0],
    ('Nb', 'H'):  [1,  1, 0],
    ('Nd', 'O'):  [1,  1, 0],
    ('Nd', 'S'):  [1,  1, 0],
    ('Nd', 'Se'):  [1,  1, 0],
    ('Nd', 'Te'):  [1,  1, 0],
    ('Nd', 'F'):  [1,  1, 0],
    ('Nd', 'Cl'):  [1,  1, 0],
    ('Nd', 'Br'):  [1,  1, 0],
    ('Nd', 'I'):  [1,  1, 0],
    ('Nd', 'N'):  [1,  1, 0],
    ('NH', 'O'):  [1,  1, 0],
    ('NH', 'F'):  [1,  1, 0],
    ('NH', 'Cl'):  [1,  1, 0],
    ('Ni', 'O'):  [1,  1, 0],
    ('Ni', 'S'):  [1,  1, 0],
    ('Ni', 'F'):  [1,  1, 0],
    ('Ni', 'Cl'):  [1,  1, 0],
    ('Ni', 'Br'):  [1,  1, 0],
    ('Ni', 'I'):  [1,  1, 0],
    ('Ni', 'N'):  [1,  1, 0],
    ('Ni', 'Se'):  [1,  1, 0],
    ('Ni', 'Te'):  [1,  1, 0],
    ('Ni', 'P'):  [1,  1, 0],
    ('Ni', 'As'):  [1,  1, 0],
    ('Ni', 'H'):  [1,  1, 0],
    ('Np', 'F'):  [1,  1, 0],
    ('Np', 'Cl'):  [1,  1, 0],
    ('Np', 'S'):  [1,  1, 0],
    ('Np', 'Br'):  [1,  1, 0],
    ('Np', 'I'):  [1,  1, 0],
    ('Np', 'O'):  [1,  1, 0],
    ('O', 'O'):  [1,  0, 0],
    ('Os', 'O'):  [1,  1, 0],
    ('Os', 'S'):  [1,  1, 0],
    ('Os', 'F'):  [1,  1, 0],
    ('Os', 'Cl'):  [1,  1, 0],
    ('Os', 'Br'):  [1,  1, 0],
    ('P', 'O'):  [1,  1, 0],
    ('P', 'S'):  [1,  1, 0],
    ('P', 'Se'):  [1,  1, 0],
    ('P', 'F'):  [1,  1, 0],
    ('P', 'Cl'):  [1,  1, 0],
    ('P', 'Br'):  [1,  1, 0],
    ('P', 'N'):  [1,  1, 0],
    ('P', 'I'):  [1,  1, 0],
    ('P', 'P'):  [1,  1, 0],
    ('P', 'As'):  [1,  1, 0],
    ('P', 'H'):  [1,  1, 0],
    ('Pa', 'O'):  [1,  1, 0],
    ('Pa', 'F'):  [1,  1, 0],
    ('Pa', 'Cl'):  [1,  1, 0],
    ('Pa', 'Br'):  [1,  1, 0],
    ('Pb', 'O'):  [1,  1, 0],
    ('Pb', 'S'):  [1,  1, 0],
    ('Pb', 'Se'):  [1,  1, 0],
    ('Pb', 'F'):  [1,  1, 0],
    ('Pb', 'Cl'):  [1,  1, 0],
    ('Pb', 'Br'):  [1,  1, 0],
    ('Pb', 'I'):  [1,  1, 0],
    ('Pb', 'N'):  [1,  1, 0],
    ('Pb', 'Te'):  [1,  1, 0],
    ('Pb', 'P'):  [1,  1, 0],
    ('Pb', 'As'):  [1,  1, 0],
    ('Pb', 'H'):  [1,  1, 0],
    ('Pd', 'O'):  [1,  1, 0],
    ('Pd', 'S'):  [1,  1, 0],
    ('Pd', 'F'):  [1,  1, 0],
    ('Pd', 'Cl'):  [1,  1, 0],
    ('Pd', 'Br'):  [1,  1, 0],
    ('Pd', 'I'):  [1,  1, 0],
    ('Pd', 'N'):  [1,  1, 0],
    ('Pd', 'C'):  [1,  1, 0],
    ('Pd', 'Se'):  [1,  1, 0],
    ('Pd', 'Te'):  [1,  1, 0],
    ('Pd', 'P'):  [1,  1, 0],
    ('Pd', 'As'):  [1,  1, 0],
    ('Pd', 'H'):  [1,  1, 0],
    ('Pm', 'F'):  [1,  1, 0],
    ('Pm', 'Cl'):  [1,  1, 0],
    ('Pm', 'Br'):  [1,  1, 0],
    ('Po', 'O'):  [1,  1, 0],
    ('Po', 'F'):  [1,  1, 0],
    ('Pr', 'O'):  [1,  1, 0],
    ('Pr', 'S'):  [1,  1, 0],
    ('Pr', 'Se'):  [1,  1, 0],
    ('Pr', 'Te'):  [1,  1, 0],
    ('Pr', 'F'):  [1,  1, 0],
    ('Pr', 'Cl'):  [1,  1, 0],
    ('Pr', 'Br'):  [1,  1, 0],
    ('Pr', 'I'):  [1,  1, 0],
    ('Pr', 'N'):  [1,  1, 0],
    ('Pr', 'P'):  [1,  1, 0],
    ('Pr', 'As'):  [1,  1, 0],
    ('Pr', 'H'):  [1,  1, 0],
    ('Pt', 'O'):  [1,  1, 0],
    ('Pt', 'S'):  [1,  1, 0],
    ('Pt', 'F'):  [1,  1, 0],
    ('Pt', 'Cl'):  [1,  1, 0],
    ('Pt', 'Br'):  [1,  1, 0],
    ('Pt', 'C'):  [1,  1, 0],
    ('Pt', 'N'):  [1,  1, 0],
    ('Pt', 'I'):  [1,  1, 0],
    ('Pt', 'Se'):  [1,  1, 0],
    ('Pt', 'Te'):  [1,  1, 0],
    ('Pt', 'P'):  [1,  1, 0],
    ('Pt', 'As'):  [1,  1, 0],
    ('Pt', 'H'):  [1,  1, 0],
    ('Pu', 'O'):  [1,  1, 0],
    ('Pu', 'F'):  [1,  1, 0],
    ('Pu', 'Cl'):  [1,  1, 0],
    ('Pu', 'S'):  [1,  1, 0],
    ('Pu', 'Br'):  [1,  1, 0],
    ('Pu', 'I'):  [1,  1, 0],
    ('Rb', 'O'):  [1,  1, 0],
    ('Rb', 'S'):  [1,  1, 0],
    ('Rb', 'Se'):  [1,  1, 0],
    ('Rb', 'Te'):  [1,  1, 0],
    ('Rb', 'F'):  [1,  1, 0],
    ('Rb', 'Cl'):  [1,  1, 0],
    ('Rb', 'Br'):  [1,  1, 0],
    ('Rb', 'I'):  [1,  1, 0],
    ('Rb', 'N'):  [1,  1, 0],
    ('Rb', 'P'):  [1,  1, 0],
    ('Rb', 'As'):  [1,  1, 0],
    ('Rb', 'H'):  [1,  1, 0],
    ('Re', 'Cl'):  [1,  1, 0],
    ('Re', 'O'):  [1,  1, 0],
    ('Re', 'F'):  [1,  1, 0],
    ('Re', 'Br'):  [1,  1, 0],
    ('Re', 'I'):  [1,  1, 0],
    ('Re', 'S'):  [1,  1, 0],
    ('Re', 'Se'):  [1,  1, 0],
    ('Re', 'Te'):  [1,  1, 0],
    ('Re', 'N'):  [1,  1, 0],
    ('Re', 'P'):  [1,  1, 0],
    ('Re', 'As'):  [1,  1, 0],
    ('Re', 'H'):  [1,  1, 0],
    ('Rh', 'O'):  [1,  1, 0],
    ('Rh', 'F'):  [1,  1, 0],
    ('Rh', 'Cl'):  [1,  1, 0],
    ('Rh', 'Br'):  [1,  1, 0],
    ('Rh', 'N'):  [1,  1, 0],
    ('Rh', 'I'):  [1,  1, 0],
    ('Rh', 'S'):  [1,  1, 0],
    ('Rh', 'Se'):  [1,  1, 0],
    ('Rh', 'Te'):  [1,  1, 0],
    ('Rh', 'P'):  [1,  1, 0],
    ('Rh', 'As'):  [1,  1, 0],
    ('Rh', 'H'):  [1,  1, 0],
    ('Ru', 'Se'):  [1,  1, 0],
    ('Ru', 'F'):  [1,  1, 0],
    ('Ru', 'O'):  [1,  1, 0],
    ('Ru', 'S'):  [1,  1, 0],
    ('Ru', 'Cl'):  [1,  1, 0],
    ('Ru', 'N'):  [1,  1, 0],
    ('Ru', 'Br'):  [1,  1, 0],
    ('Ru', 'I'):  [1,  1, 0],
    ('Ru', 'Te'):  [1,  1, 0],
    ('Ru', 'P'):  [1,  1, 0],
    ('Ru', 'As'):  [1,  1, 0],
    ('Ru', 'H'):  [1,  1, 0],
    ('S', 'O'):  [1,  1, 0],
    ('S', 'S'):  [1,  1, 0],
    ('S', 'N'):  [1,  1, 0],
    ('S', 'F'):  [1,  1, 0],
    ('S', 'Cl'):  [1,  1, 0],
    ('S', 'Br'):  [1,  1, 0],
    ('S', 'I'):  [1,  1, 0],
    ('S', 'H'):  [1,  1, 0],
    ('Sb', 'O'):  [1,  1, 0],
    ('Sb', 'S'):  [1,  1, 0],
    ('Sb', 'Se'):  [1,  1, 0],
    ('Sb', 'F'):  [1,  1, 0],
    ('Sb', 'Cl'):  [1,  1, 0],
    ('Sb', 'Br'):  [1,  1, 0],
    ('Sb', 'I'):  [1,  1, 0],
    ('Sb', 'N'):  [1,  1, 0],
    ('Sb', 'Te'):  [1,  1, 0],
    ('Sb', 'P'):  [1,  1, 0],
    ('Sb', 'As'):  [1,  1, 0],
    ('Sb', 'H'):  [1,  1, 0],
    ('Sc', 'O'):  [1,  1, 0],
    ('Sc', 'S'):  [1,  1, 0],
    ('Sc', 'Se'):  [1,  1, 0],
    ('Sc', 'Te'):  [1,  1, 0],
    ('Sc', 'F'):  [1,  1, 0],
    ('Sc', 'Cl'):  [1,  1, 0],
    ('Sc', 'Br'):  [1,  1, 0],
    ('Sc', 'I'):  [1,  1, 0],
    ('Sc', 'N'):  [1,  1, 0],
    ('Sc', 'P'):  [1,  1, 0],
    ('Sc', 'As'):  [1,  1, 0],
    ('Sc', 'H'):  [1,  1, 0],
    ('Se', 'S'):  [1,  1, 0],
    ('Se', 'Se'):  [1,  1, 0],
    ('Se', 'O'):  [1,  1, 0],
    ('Se', 'F'):  [1,  1, 0],
    ('Se', 'Cl'):  [1,  1, 0],
    ('Se', 'Br'):  [1,  1, 0],
    ('Se', 'N'):  [1,  1, 0],
    ('Se', 'I'):  [1,  1, 0],
    ('Se', 'H'):  [1,  1, 0],
    ('Si', 'O'):  [1,  1, 0],
    ('Si', 'S'):  [1,  1, 0],
    ('Si', 'Se'):  [1,  1, 0],
    ('Si', 'Te'):  [1,  1, 0],
    ('Si', 'F'):  [1,  1, 0],
    ('Si', 'Cl'):  [1,  1, 0],
    ('Si', 'Br'):  [1,  1, 0],
    ('Si', 'I'):  [1,  1, 0],
    ('Si', 'C'):  [1,  1, 0],
    ('Si', 'N'):  [1,  1, 0],
    ('Si', 'P'):  [1,  1, 0],
    ('Si', 'As'):  [1,  1, 0],
    ('Si', 'H'):  [1,  1, 0],
    ('Si', 'Si'):  [1,  1, 0],
    ('Sm', 'O'):  [1,  1, 0],
    ('Sm', 'N'):  [1,  1, 0],
    ('Sm', 'S'):  [1,  1, 0],
    ('Sm', 'Se'):  [1,  1, 0],
    ('Sm', 'Te'):  [1,  1, 0],
    ('Sm', 'F'):  [1,  1, 0],
    ('Sm', 'Cl'):  [1,  1, 0],
    ('Sm', 'Br'):  [1,  1, 0],
    ('Sm', 'I'):  [1,  1, 0],
    ('Sm', 'P'):  [1,  1, 0],
    ('Sm', 'As'):  [1,  1, 0],
    ('Sm', 'H'):  [1,  1, 0],
    ('Sn', 'O'):  [1,  1, 0],
    ('Sn', 'S'):  [1,  1, 0],
    ('Sn', 'F'):  [1,  1, 0],
    ('Sn', 'Cl'):  [1,  1, 0],
    ('Sn', 'Br'):  [1,  1, 0],
    ('Sn', 'I'):  [1,  1, 0],
    ('Sn', 'N'):  [1,  1, 0],
    ('Sn', 'Se'):  [1,  1, 0],
    ('Sn', 'Te'):  [1,  1, 0],
    ('Sn', 'P'):  [1,  1, 0],
    ('Sn', 'As'):  [1,  1, 0],
    ('Sn', 'H'):  [1,  1, 0],
    ('Sr', 'O'):  [1,  1, 0],
    ('Sr', 'S'):  [1,  1, 0],
    ('Sr', 'Se'):  [1,  1, 0],
    ('Sr', 'Te'):  [1,  1, 0],
    ('Sr', 'F'):  [1,  1, 0],
    ('Sr', 'Cl'):  [1,  1, 0],
    ('Sr', 'Br'):  [1,  1, 0],
    ('Sr', 'I'):  [1,  1, 0],
    ('Sr', 'N'):  [1,  1, 0],
    ('Sr', 'P'):  [1,  1, 0],
    ('Sr', 'As'):  [1,  1, 0],
    ('Sr', 'H'):  [1,  1, 0],
    ('Ta', 'O'):  [1,  1, 0],
    ('Ta', 'S'):  [1,  1, 0],
    ('Ta', 'F'):  [1,  1, 0],
    ('Ta', 'Cl'):  [1,  1, 0],
    ('Ta', 'Br'):  [1,  1, 0],
    ('Ta', 'I'):  [1,  1, 0],
    ('Ta', 'Se'):  [1,  1, 0],
    ('Ta', 'Te'):  [1,  1, 0],
    ('Ta', 'N'):  [1,  1, 0],
    ('Ta', 'P'):  [1,  1, 0],
    ('Ta', 'As'):  [1,  1, 0],
    ('Ta', 'H'):  [1,  1, 0],
    ('Tb', 'O'):  [1,  1, 0],
    ('Tb', 'S'):  [1,  1, 0],
    ('Tb', 'Se'):  [1,  1, 0],
    ('Tb', 'Te'):  [1,  1, 0],
    ('Tb', 'F'):  [1,  1, 0],
    ('Tb', 'Cl'):  [1,  1, 0],
    ('Tb', 'Br'):  [1,  1, 0],
    ('Tb', 'I'):  [1,  1, 0],
    ('Tb', 'N'):  [1,  1, 0],
    ('Tb', 'P'):  [1,  1, 0],
    ('Tb', 'As'):  [1,  1, 0],
    ('Tb', 'H'):  [1,  1, 0],
    ('Tc', 'O'):  [1,  1, 0],
    ('Tc', 'F'):  [1,  1, 0],
    ('Tc', 'Cl'):  [1,  1, 0],
    ('Te', 'O'):  [1,  1, 0],
    ('Te', 'S'):  [1,  1, 0],
    ('Te', 'F'):  [1,  1, 0],
    ('Te', 'Cl'):  [1,  1, 0],
    ('Te', 'Br'):  [1,  1, 0],
    ('Te', 'I'):  [1,  1, 0],
    ('Te', 'Se'):  [1,  1, 0],
    ('Te', 'Te'):  [1,  1, 0],
    ('Te', 'N'):  [1,  1, 0],
    ('Te', 'P'):  [1,  1, 0],
    ('Te', 'H'):  [1,  1, 0],
    ('Th', 'O'):  [1,  1, 0],
    ('Th', 'S'):  [1,  1, 0],
    ('Th', 'Se'):  [1,  1, 0],
    ('Th', 'Te'):  [1,  1, 0],
    ('Th', 'F'):  [1,  1, 0],
    ('Th', 'Cl'):  [1,  1, 0],
    ('Th', 'Br'):  [1,  1, 0],
    ('Th', 'I'):  [1,  1, 0],
    ('Th', 'N'):  [1,  1, 0],
    ('Th', 'P'):  [1,  1, 0],
    ('Th', 'As'):  [1,  1, 0],
    ('Th', 'H'):  [1,  1, 0],
    ('Ti', 'F'):  [1,  1, 0],
    ('Ti', 'Cl'):  [1,  1, 0],
    ('Ti', 'Br'):  [1,  1, 0],
    ('Ti', 'O'):  [1,  1, 0],
    ('Ti', 'S'):  [1,  1, 0],
    ('Ti', 'I'):  [1,  1, 0],
    ('Ti', 'Se'):  [1,  1, 0],
    ('Ti', 'Te'):  [1,  1, 0],
    ('Ti', 'N'):  [1,  1, 0],
    ('Ti', 'P'):  [1,  1, 0],
    ('Ti', 'As'):  [1,  1, 0],
    ('Ti', 'H'):  [1,  1, 0],
    ('Tl', 'O'):  [1,  1, 0],
    ('Tl', 'S'):  [1,  1, 0],
    ('Tl', 'F'):  [1,  1, 0],
    ('Tl', 'Cl'):  [1,  1, 0],
    ('Tl', 'Br'):  [1,  1, 0],
    ('Tl', 'I'):  [1,  1, 0],
    ('Tl', 'Se'):  [1,  1, 0],
    ('Tl', 'Te'):  [1,  1, 0],
    ('Tl', 'N'):  [1,  1, 0],
    ('Tl', 'P'):  [1,  1, 0],
    ('Tl', 'As'):  [1,  1, 0],
    ('Tl', 'H'):  [1,  1, 0],
    ('Tm', 'O'):  [1,  1, 0],
    ('Tm', 'S'):  [1,  1, 0],
    ('Tm', 'Se'):  [1,  1, 0],
    ('Tm', 'Te'):  [1,  1, 0],
    ('Tm', 'F'):  [1,  1, 0],
    ('Tm', 'Cl'):  [1,  1, 0],
    ('Tm', 'Br'):  [1,  1, 0],
    ('Tm', 'I'):  [1,  1, 0],
    ('Tm', 'N'):  [1,  1, 0],
    ('Tm', 'P'):  [1,  1, 0],
    ('Tm', 'As'):  [1,  1, 0],
    ('Tm', 'H'):  [1,  1, 0],
    ('U', 'O'):  [1,  1, 0],
    ('U', 'S'):  [1,  1, 0],
    ('U', 'F'):  [1,  1, 0],
    ('U', 'Cl'):  [1,  1, 0],
    ('U', 'Br'):  [1,  1, 0],
    ('U', 'I'):  [1,  1, 0],
    ('U', 'N'):  [1,  1, 0],
    ('U', 'Se'):  [1,  1, 0],
    ('U', 'Te'):  [1,  1, 0],
    ('U', 'P'):  [1,  1, 0],
    ('U', 'As'):  [1,  1, 0],
    ('U', 'H'):  [1,  1, 0],
    ('V', 'O'):  [1,  1, 0],
    ('V', 'Cl'):  [1,  1, 0],
    ('V', 'S'):  [1,  1, 0],
    ('V', 'F'):  [1,  1, 0],
    ('V', 'Br'):  [1,  1, 0],
    ('V', 'N'):  [1,  1, 0],
    ('V', 'I'):  [1,  1, 0],
    ('V', 'Se'):  [1,  1, 0],
    ('V', 'Te'):  [1,  1, 0],
    ('V', 'P'):  [1,  1, 0],
    ('V', 'As'):  [1,  1, 0],
    ('V', 'H'):  [1,  1, 0],
    ('W', 'O'):  [1,  1, 0],
    ('W', 'F'):  [1,  1, 0],
    ('W', 'Cl'):  [1,  1, 0],
    ('W', 'Br'):  [1,  1, 0],
    ('W', 'I'):  [1,  1, 0],
    ('W', 'S'):  [1,  1, 0],
    ('W', 'Se'):  [1,  1, 0],
    ('W', 'Te'):  [1,  1, 0],
    ('W', 'N'):  [1,  1, 0],
    ('W', 'P'):  [1,  1, 0],
    ('W', 'As'):  [1,  1, 0],
    ('W', 'H'):  [1,  1, 0],
    ('Xe', 'O'):  [1,  1, 0],
    ('Xe', 'F'):  [1,  1, 0],
    ('Y', 'O'):  [1,  1, 0],
    ('Y', 'S'):  [1,  1, 0],
    ('Y', 'Se'):  [1,  1, 0],
    ('Y', 'Te'):  [1,  1, 0],
    ('Y', 'F'):  [1,  1, 0],
    ('Y', 'Cl'):  [1,  1, 0],
    ('Y', 'Br'):  [1,  1, 0],
    ('Y', 'I'):  [1,  1, 0],
    ('Y', 'N'):  [1,  1, 0],
    ('Y', 'P'):  [1,  1, 0],
    ('Y', 'As'):  [1,  1, 0],
    ('Y', 'H'):  [1,  1, 0],
    ('Yb', 'O'):  [1,  1, 0],
    ('Yb', 'N'):  [1,  1, 0],
    ('Yb', 'S'):  [1,  1, 0],
    ('Yb', 'Se'):  [1,  1, 0],
    ('Yb', 'Te'):  [1,  1, 0],
    ('Yb', 'F'):  [1,  1, 0],
    ('Yb', 'Cl'):  [1,  1, 0],
    ('Yb', 'Br'):  [1,  1, 0],
    ('Yb', 'I'):  [1,  1, 0],
    ('Yb', 'P'):  [1,  1, 0],
    ('Yb', 'As'):  [1,  1, 0],
    ('Yb', 'H'):  [1,  1, 0],
    ('Zn', 'O'):  [1,  1, 0],
    ('Zn', 'S'):  [1,  1, 0],
    ('Zn', 'Se'):  [1,  1, 0],
    ('Zn', 'Te'):  [1,  1, 0],
    ('Zn', 'F'):  [1,  1, 0],
    ('Zn', 'Cl'):  [1,  1, 0],
    ('Zn', 'Br'):  [1,  1, 0],
    ('Zn', 'I'):  [1,  1, 0],
    ('Zn', 'N'):  [1,  1, 0],
    ('Zn', 'P'):  [1,  1, 0],
    ('Zn', 'As'):  [1,  1, 0],
    ('Zn', 'H'):  [1,  1, 0],
    ('Zr', 'O'):  [1,  1, 0],
    ('Zr', 'F'):  [1,  1, 0],
    ('Zr', 'Cl'):  [1,  1, 0],
    ('Zr', 'S'):  [1,  1, 0],
    ('Zr', 'Se'):  [1,  1, 0],
    ('Zr', 'Te'):  [1,  1, 0],
    ('Zr', 'Br'):  [1,  1, 0],
    ('Zr', 'I'):  [1,  1, 0],
    ('Zr', 'N'):  [1,  1, 0],
    ('Zr', 'P'):  [1,  1, 0],
    ('Zr', 'As'):  [1,  1, 0],
    ('Zr', 'H'):  [1,  1, 0],
}

default_polyhedras = {
    'Ac', 'Zr', 'Pr', 'Mo', 'Li', 'Ba', 'Cd', 'C',
    'Es', 'Al', 'Os', 'V', 'Sm', 'Dy', 'Ti', 'Pb', 'Ni', 'Sr', 'Na',
    'Lu', 'Y', 'Tb', 'Au', 'Be', 'Sn', 'Xe', 'As', 'Cr',
    'Ru', 'Re', 'Yb', 'I', 'Ag', 'H', 'Se', 'Th', 'In', 'Pu', 'Te',
    'W', 'Ca', 'Co', 'Pd', 'Tl', 'B', 'Br', 'Rh', 'Pa', 'Tc', 'Zn',
    'Eu', 'Ta', 'Cm', 'Nb', 'Hf', 'La', 'Ce', 'Cf', 'D', 'U', 'Mn',
    'Si', 'Hg', 'Cu', 'Rb', 'K', 'Er', 'NH', 'Fe', 'Ge', 'Am', 'P',
    'Tm', 'Gd', 'Ga', 'Pm', 'Bi', 'Mg', 'Sc', 'Kr', 'Sb', 'Ir', 'Po',
    'Bk', 'F', 'Ho', 'Nd', 'Cs', 'Np', 'Pt',
}
