import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import saxspy
import matplotlib.pyplot as plt
import numpy as np
# Instantiate the synthetic model: 'P', 'G', or 'D'
import argparse

parser = argparse.ArgumentParser(description='Phase for generation')

parser.add_argument('-phase', help='phase_to_visualize')
parser.add_argument('--cubic_mesophase', '--mph', help='cubic_mesophase')

args = parser.parse_args()

phase = args.phase
cubic_mesophase = args.cubic_mesophase

if cubic_mesophase is not None:
    assert cubic_mesophase == 'Im3m' or cubic_mesophase == 'la3d' or cubic_mesophase == 'Pn3m'

print(f"running cubic {cubic_mesophase} model...")
cm = saxspy.CubicModel(cubic_mesophase)

#----------------------- generate synthetic data -----------------------#
# ranges of: lattice parameter, length of lipid, lipid head sigma

# params = np.array([[28, 40], [0.2, 0.5], [0.5, 1]])  #good but lattice parameter
# params = np.array([[10, 40], [0.07, 0.1], [0.1, 0.4]]) #good for Im3m

params = np.array([[10, 40], [0.07, 0.1], [0.1, 0.4]])


store_it = cm.generateSynthCubic(params, 4, 2, 2)

np.save(f'Synthetic_raw/{cubic_mesophase}_cubic.npy', store_it)