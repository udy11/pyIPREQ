# pyIPREQ input file for SST-1

# This file MUST declare the following variables (others are not used in pyIPREQ):
# mu0
# nr, nz, r1, z1
# Rmaj
# J0R, J0Z
# pp_fx, ffp_fx (along with any parameters used within them, like alpha, beta, gamma)
# Bphi0 (only used post-computation for quantities like q, beta, etc.)
# Ip
# drf, dzf
# tol_in, tol_out
# rzlims
# ccoils, ccurrs (coil names are unused in the code)
# C1Z, fbZ, C1R, fbR

import numpy as np

mu0 = 4.0e-7 * np.pi    # magnetic permeability
nr = 51    # number of grid points in R
nz = 86    # number of grid points in Z
r1 = np.linspace(0.6, 1.6, nr)    # R-grid, try not to have 0 in array
z1 = np.linspace(-0.85, 0.85, nz)    # Z-grid
Rmaj = 1.1    # Major Radius in meter
J0R, J0Z = Rmaj, 0.0    # center of guess current density profile at first iteration
alpha_p, beta_j, alpha_f = 0.7, 0.1, 1.7    # profile parameters for p' and FF'
pp_fx =  lambda s: (np.exp(-alpha_p * (1 - s)) - np.exp(-alpha_p)) / (np.exp(-alpha_p) - 1)    # profile of p'
ffp_fx = lambda s: (np.exp(-alpha_f * (1 - s)) - np.exp(-alpha_f)) / (np.exp(-alpha_f) - 1)    # profile of FF'
Bphi0 = 1.5    # toroidal magnetic field at (Rmaj,0) in Tesla (only used in computation of other parameters like q, β, etc.)
Ip = 1.0e5    # plasma current in Ampere
drf, dzf = 0.01, 0.01    # filament sizes in which to divide coils (in m)
tol_in = 1.0e-6    # inner loop convergence tolerance
tol_out = 1.0e-6    # outer loop convergence tolerance

# Limiter contour
# last point and first point must be same
# points must be sequential, numpy array and in format [[r0,z0],[r1,z1],...,[r0,z0]]
Rmin = 0.25    # only used to define rzlims
thlims = np.linspace(0, 2.0*np.pi, 33)    # only used to define rzlims
rzlims = np.transpose(np.array([Rmaj + Rmin*np.cos(thlims), Rmin*np.sin(thlims)]))    # last point and first point must be same; points must be sequential, numpy array and in format [[r0,z0],[r1,z1],...,[r0,z0]]

#           R       Z       dR     dZ   turns name    (turns and name are unused in main code)
ccoils = [[2.500,  1.3810, 0.117, 0.095, -24, 'VF_T'],    # 0    Ivf
          [2.500, -1.3810, 0.117, 0.095, -24, 'VF_B'],    # 1
          [0.252,  0.0000, 0.145, 2.580, 678, 'Tr1'],    # 2    Iot
          [0.591,  1.4800, 0.211, 0.102,  40, 'Tr2_T'],    # 3
          [0.591, -1.4800, 0.208, 0.102,  40, 'Tr2_B'],    # 4
          [2.451,  1.3040, 0.070, 0.030,   3, 'Tr3_T'],    # 5
          [2.451, -1.3040, 0.072, 0.030,   3, 'Tr3_B'],    # 6
          [2.472,  0.6000, 0.042, 0.046,   5, 'Tr4_T'],    # 7
          [2.472, -0.6000, 0.042, 0.046,   5, 'Tr4_B'],    # 8
          [0.450,  0.0875, 0.070, 0.160,  80, 'PF1_T'],    # 9    Ipfs[0]
          [0.450, -0.0875, 0.070, 0.160,  80, 'PF1_B'],    # 10
          [0.450,  0.4250, 0.070, 0.320,  40, 'PF2_T'],    # 11    Ipfs[1]
          [0.450, -0.4250, 0.070, 0.320,  40, 'PF2_B'],    # 12
          [0.500,  0.9300, 0.130, 0.350, 192, 'PF3_T'],    # 13    Ipfs[2]
          [0.500, -0.9300, 0.130, 0.350, 192, 'PF3_B'],    # 14
          [1.720,  1.0640, 0.160, 0.130,  40, 'PF4_T'],    # 15    Ipfs[3]
          [1.720, -1.0465, 0.160, 0.130,  40, 'PF4_B'],    # 16
          [2.070,  0.6500, 0.080, 0.130,  40, 'PF5_T'],    # 17    Ipfs[4]
          [2.070, -0.6500, 0.080, 0.130,  40, 'PF5_B'],    # 18
          [1.350,  0.3500, 0.025, 0.105,   8, 'PF6_T'],    # 19    Ipfs[5]
          [1.350, -0.3500, 0.025, 0.105,   8, 'PF6_B']]    # 20
ccurrs = np.empty(len(ccoils))
Iot = 0.0    # OT single-turn current in Ampere
Ivf = 3.25e3    # VF single-turn current in Ampere
Ipfs = [0.375e3,  # PF1, all values are per turn
        1.5e3,    # PF2
        0.0e3,    # PF3
        0.0e3,    # PF4
        0.0e3,    # PF5
        0.0e3]    # PF6
for i in range(2):
    ccurrs[i] = ccoils[i][4] * Ivf
for i in range(2, 9):
    ccurrs[i] = ccoils[i][4] * Iot
for j in range(9, 20, 2):
    for i in (j, j+1):
        ccurrs[i] = ccoils[i][4] * Ipfs[(j-9)//2]

# Vertical and Horizontal Instability Parameters (if unsure set them all to 0.0)
# Currents in feedback coils for respective instabilities are computed as:
# Ifbv = -C1Z * Ip * (Zax - fbZ)
# Ifbh = -C1R * Ip * (Rax - fbR)
C1Z = 0.0
fbZ = 0.0
C1R = 0.0
fbR = Rmaj
