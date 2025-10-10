# pyIPREQ input file for ADITYA-U

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
nr = 71    # number of grid points in R
nz = 111    # number of grid points in Z
r1 = np.linspace(0.4, 1.1, nr)    # R-grid, try not to have 0 in array
z1 = np.linspace(-0.55, 0.55, nz)    # Z-grid
Rmaj = 0.75    # Major Radius in meter
J0R, J0Z = Rmaj, 0.0    # center of guess current density profile at first iteration
alpha, beta, gamma = 1.2, 0.8, 1.2    # profile parameters for p' and FF'
pp_fx =  lambda s: beta * (1.0 - (1-s)**alpha)**gamma    # profile of p'
ffp_fx = lambda s: (1.0-beta) * (1.0 - (1-s)**alpha)**gamma    # profile of FF'
#alpha_p, beta, alpha_f = 1.5, 0.75, 1.2
#pp_fx =  lambda s: beta * (np.exp(-alpha_p * (1 - s)) - np.exp(-alpha_p)) / (np.exp(-alpha_p) - 1)
#ffp_fx = lambda s: (1.0-beta) * (np.exp(-alpha_f * (1 - s)) - np.exp(-alpha_f)) / (np.exp(-alpha_f) - 1)
Bphi0 = 1.2    # toroidal magnetic field at (Rmaj,0) in Tesla (only used in computation of other parameters like q, β, etc.)
Ip = 1.2e5    # plasma current in Ampere
drf, dzf = 0.01, 0.01    # filament sizes in which to divide coils (in m)
tol_in = 1.0e-5    # inner loop convergence tolerance
tol_out = 1.0e-5    # outer loop convergence tolerance

# Limiter contour
# last point and first point must be same
# points must be sequential, numpy array and in format [[r0,z0],[r1,z1],...,[r0,z0]]
Rmin = 0.25    # only used to define rzlims
thlims = np.linspace(0, 2.0*np.pi, 33)    # only used to define rzlims
rzlims = np.transpose(np.array([Rmaj + Rmin*np.cos(thlims), Rmin*np.sin(thlims)]))    # last point and first point must be same; points must be sequential, numpy array and in format [[r0,z0],[r1,z1],...,[r0,z0]]

#           R         Z        dR        dZ     turns name    (turns and name are unused in main code)
ccoils = [[0.22625,  0.00000, 0.10750,  1.04000, 174, 'TR-1'],      # 0 ###
          [0.39530,  0.84300, 0.23050,  0.16000,  56, 'TR-2-T'],    # 1
          [0.39530, -0.83952, 0.23050,  0.15700,  56, 'TR-2-B'],    # 2
          [1.22319,  0.72806, 0.03483,  0.06000,  -3, 'TR-3-T'],    # 3
          [1.22600, -0.72700, 0.03516,  0.05950,  -3, 'TR-3-B'],    # 4 OT-Coils
          [1.53400,  0.60209, 0.06446,  0.03820,   4, 'TR-4-T'],    # 5
          [1.53007, -0.60100, 0.06540,  0.03867,   4, 'TR-4-B'],    # 6
          [1.62700,  1.14800, 0.03400,  0.01550,  -1, 'TR-5-T'],    # 7
          [1.62700, -1.14750, 0.03500,  0.01600,  -1, 'TR-5-B'],    # 8 ###
          [0.37981,  1.05270, 0.16405,  0.12003, -60, 'BV-1-T'],    # 9 ###
          [0.38200, -1.05100, 0.16937,  0.11733, -60, 'BV-1-B'],    #10 BV-coils
          [1.64204,  1.18850, 0.18155,  0.03863, -22, 'BV-2-T'],    #11
          [1.64100, -1.18900, 0.17950,  0.03800, -22, 'BV-2-B'],    #12 ###
          [0.46250,  0.29700, 0.05500,  0.06500,  12, 'MDI-T'],     #13 ###
          [0.46200, -0.29700, 0.05500,  0.06500,  12, 'MDI-B'],     #14 Main Divertor Inner/Outer
          [1.06288,  0.33750, 0.02800,  0.01312,   1, 'MDO-T'],     #15
          [1.06288, -0.33750, 0.02814,  0.01326,   1, 'MDO-B'],     #16 ###
          [0.47000,  0.43000, 0.05500,  0.02166,   4, 'ADI-T'],     #17 ### Auxiliary Divertor Inner
          [0.47040, -0.43000, 0.05500,  0.02166,   4, 'ADI-B'],     #18 ###
          [0.47500,  0.39200, 0.02943,  0.01520,  -1, 'FFI-T'],     #19 ###
          [0.47000, -0.39200, 0.02923,  0.01496,   1, 'FFI-B'],     #20 Fast Feedback Inner/Outer
          [1.08750,  0.37700, 0.02814,  0.01291,   1, 'FFO-T'],     #21
          [1.08750, -0.37700, 0.02834,  0.01335,   1, 'FFO-B'],     #22 ###
          [1.52700,  0.52100, 0.09000,  0.05400, -18, 'BCC-T'],     #23 ### Black Correction
          [1.52700, -0.52100, 0.09000,  0.05400,  18, 'BCC-B'],     #24 ###
          [1.33000,  0.54000, 0.01500,  0.04000,   1, 'TF-1'],      #25 ### TF Coil Bus Bar
          [1.38000,  0.54000, 0.01500,  0.04000,  -1, 'TF-2']]      #26 ###
cnOT = (0, 1, 2, 3, 4, 5, 6, 7, 8)    # for Iot
cnVF = (9, 10, 11, 12)    # for Ivf
cnFF = (15, 16, 19, 20, 21, 22)    # for Iff
cnBC = (23, 24)    # for Ibc
cnDT = (13, 17)    # for IDt
cnDB = (14, 18)    # for IDb
cnTF = (25, 26)    # for Itf
ccurrs = np.empty(len(ccoils))
Iot = 0.0    # OT single-turn current in Ampere
Ivf = 5.0e3    # VF single-turn current in Ampere
Iff = 1.0e3    # FFB single-turn current in Ampere
Ibc = 0.0e3    # BCC single-turn current in Ampere
IDt = 0.0    # Top-Divertor Coils (MDI-T, ADI-T) single-turn current in Ampere
IDb = 0.0    # Bottom-Divertor Coils (MDI-B, ADI-B) single-turn current in Ampere
Itf = 0.0    # TF Bus Bar (TF-1, TF-2) single-turn current in Ampere
for i in cnOT:
    ccurrs[i] = ccoils[i][4] * Iot
for i in cnVF:
    ccurrs[i] = ccoils[i][4] * Ivf
for i in cnFF:
    ccurrs[i] = ccoils[i][4] * Iff
for i in cnBC:
    ccurrs[i] = ccoils[i][4] * Ibc
for i in cnDT:
    ccurrs[i] = ccoils[i][4] * IDt
for i in cnDB:
    ccurrs[i] = ccoils[i][4] * IDb
for i in cnTF:
    ccurrs[i] = ccoils[i][4] * Itf

# Vertical and Horizontal Instability Parameters (if unsure set them all to 0.0)
# Currents in feedback coils for respective instabilities are computed as:
# Ifbv = -C1Z * Ip * (Zax - fbZ)
# Ifbh = -C1R * Ip * (Rax - fbR)
C1Z = 0.0
fbZ = 0.0
C1R = 0.0
fbR = Rmaj
