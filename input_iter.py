# pyIPREQ input file for ITER
# Data from: https://iopscience.iop.org/article/10.1088/0029-5515/44/2/007

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
'''nr = 121    # number of grid points in R
nz = 161    # number of grid points in Z
r1 = np.linspace(2.0, 12.0, nr)    # R-grid, try not to have 0 in array
z1 = np.linspace(-8.0, 8.0, nz)    # Z-grid'''
nr = 101    # number of grid points in R
nz = 201    # number of grid points in Z
r1 = np.linspace(3.5, 8.5, nr)    # R-grid, try not to have 0 in array
z1 = np.linspace(-5.0, 5.0, nz)    # Z-grid
'''nr = 121    # number of grid points in R
nz = 171    # number of grid points in Z
r1 = np.linspace(0.5, 12.5, nr)    # R-grid, try not to have 0 in array
z1 = np.linspace(-8.5, 8.5, nz)    # Z-grid'''
Rmaj = 6.2    # Major Radius in meter
J0R, J0Z = Rmaj, 0.5    # center of guess current density profile at first iteration
alpha, beta = 0.95, 0.63    # profile parameters for p' and FF'
pp_fx =  lambda s: beta * (s**alpha)    # profile of p'
ffp_fx = lambda s: (1.0-beta) * (s**alpha)    # profile of FF'/μ0
Bphi0 = 5.3    # toroidal magnetic field at (Rmaj,0) in Tesla (only used in computation of other parameters like q, β, etc.)
Ip = 15.0e6    # plasma current in Ampere
drf, dzf = 0.05, 0.05    # filament sizes in which to divide coils (in m)
tol_in = 1.0e-5    # IPREQ inner loop convergence tolerance
tol_out = 1.0e-5    # IPREQ outer loop convergence tolerance

# Limiter contour
# last point and first point must be same
# points must be sequential, numpy array and in format [[r0,z0],[r1,z1],...,[r0,z0]]
rzlims = np.array([[4.0455, -2.5063], [4.0455, -1.5], [4.0455, -0.4836], [4.0455, 0.5328], [4.0455, 1.5492], [4.0455, 2.5656], [4.0455, 3.582], [4.3109, 4.324], [4.9037, 4.7115], [5.7538, 4.5323], [6.587, 3.8934], [7.4672, 3.0833], [7.9338, 2.4024], [8.2703, 1.6814], [8.3944, 0.6329], [8.3063, -0.4215], [7.8987, -1.3417], [7.2829, -2.257], [6.2665, -3.0461], [6.171, -3.235], [5.9821, -3.2822], [5.815, -3.3823], [5.6842, -3.5265], [5.6008, -3.7024], [5.572, -3.895], [5.572, -3.896], [5.572, -3.9956], [5.572, -3.9961], [5.565, -4.0962], [5.565, -4.2494], [5.565, -4.4026], [5.565, -4.5559], [5.2727, -4.2636], [5.2628, -4.1244], [5.2529, -3.9852], [5.1496, -3.8382], [4.9982, -3.7414], [4.8215, -3.709], [4.6456, -3.746], [4.5687, -3.8276], [4.4918, -3.9092], [4.1799, -3.8847], [4.2457, -3.7497], [4.3115, -3.6148], [4.3773, -3.4799], [4.4062, -3.4048], [4.4064, -3.4043], [4.467, -3.2801], [4.5157, -3.1139], [4.5066, -2.941], [4.4408, -2.7808], [4.3257, -2.6514], [4.1742, -2.5674], [4.0455, -2.5063]])

#           R       Z     dR    dZ  name
ccoils = [[ 1.69,  5.00, 0.75, 2.00, 'CS3U'],      # 0 ###
          [ 1.69,  3.00, 0.75, 2.00, 'CS2U'],      # 1 ###
          [ 1.69,  1.00, 0.75, 2.00, 'CS1U'],      # 2 ###
          [ 1.69, -1.00, 0.75, 2.00, 'CS1L'],      # 3 ###
          [ 1.69, -3.00, 0.75, 2.00, 'CS2L'],      # 4 ###
          [ 1.69, -5.00, 0.75, 2.00, 'CS3L'],      # 5 ###
          [ 3.95,  7.56, 0.97, 0.98,  'PF1'],      # 6 ###
          [ 8.31,  6.53, 0.65, 0.60,  'PF2'],      # 7 ###
          [11.94,  3.27, 0.71, 1.13,  'PF3'],      # 8 ###
          [11.91, -2.24, 0.65, 1.13,  'PF4'],      # 9 ###
          [ 8.40, -6.73, 0.82, 0.95,  'PF5'],      #10 ###
          [ 4.29, -7.56, 1.63, 0.98,  'PF6']]      #11 ###
ccurrs = np.array([ -0.40,
                    -9.68,
                   -20.09,
                   -20.09,
                    -9.50,
                     3.22,
                     4.91,
                    -2.04,
                    -6.52,
                    -4.69,
                    -7.54,
                    17.20]) * 1.0e6
'''ccurrs = np.array([ -0.39,
                    -9.59,
                   -20.24,
                   -19.98,
                    -9.47,
                     2.88,
                     4.84,
                    -2.02,
                    -6.54,
                    -4.67,
                    -7.59,
                    17.36]) * 1.0e6'''
'''ccurrs = np.array([ -0.40,
                    -9.68,
                   -20.09,
                   -20.09,
                    -9.50,
                     3.22,
                     4.91,
                    -2.24,
                    -6.72,
                    -4.89,
                    -7.74,
                    17.20]) * 1.0e6'''

# Vertical and Horizontal Instability Parameters (if unsure set them all to 0.0)
# Currents in feedback coils for respective instabilities are computed as:
# Ifbv = -C1Z * Ip * (Zax - fbZ)
# Ifbh = -C1R * Ip * (Rax - fbR)
C1Z = 0.5
fbZ = 0.505
C1R = 0.1
fbR = Rmaj + 0.23
