"""Matplotlib replacements for Differential Equations tikz figures.

dirfield_mpl: construction schematic of one direction-field element.
falling_mpl:  falling body v(t)=49+(v0-49)e^{-t/5} for v0 in {40,49,60}-ish,
              converging to the 49 m/s equilibrium line.
logistic_mpl: logistic N(t)=Np/(1+A e^{-at}) with Np=100 (equilibrium),
              N0=20 (S-curve from below) + over-capacity decay from N0=180.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   '..', '..', 'semester-4', 'Differential Equations', 'fig-mpl')
OUT = os.path.normpath(OUT)
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'stix'})
BLUE, RED, GRAY = '#1f5fd0', '#d62728', '#8a8a8a'

# ---- 1. direction-field element schematic (grid + one slope segment) ----
fig, ax = plt.subplots(figsize=(5.6, 4.4))
ax.set_xlim(-0.5, 5.2); ax.set_ylim(-0.5, 3.8)
ax.annotate('', xy=(5.2, 0), xytext=(-0.5, 0), arrowprops=dict(arrowstyle='->', lw=1))
ax.annotate('', xy=(0, 3.8), xytext=(0, -0.5), arrowprops=dict(arrowstyle='->', lw=1))
ax.text(5.35, -0.1, '$t$'); ax.text(0.1, 3.85, '$x$')
for gx in (2, 3.5):
    ax.plot([gx, gx], [0, 2], ls='--', color=GRAY, lw=1)
ax.plot([0, 2], [3.2, 3.2], ls='--', color=GRAY, lw=1)
ax.plot([0, 2], [2, 2], ls='--', color=GRAY, lw=1)
ax.text(2, -0.18, '$t_i$', ha='center'); ax.text(3.5, -0.18, '$t_{i+1}$', ha='center')
ax.text(-0.25, 2, '$x_j$', ha='right', va='center'); ax.text(-0.25, 3.2, '$x_{j+1}$', ha='right', va='center')
ax.annotate('', xy=(3.5, 0.5), xytext=(2, 0.5),
            arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1))
ax.text(2.75, 0.32, r'$\Delta t$', ha='center', color=GRAY, bbox=dict(fc='white', ec='none', pad=1))
ax.annotate('', xy=(0.5, 3.2), xytext=(0.5, 2),
            arrowprops=dict(arrowstyle='<->', color=GRAY, lw=1))
ax.text(0.5, 2.6, r'$\Delta x$', ha='center', color=GRAY, bbox=dict(fc='white', ec='none', pad=1))
L, k = 0.5, 1.0
dx, dy = L/2/np.hypot(1, k), k*L/2/np.hypot(1, k)
ax.plot([2-dx, 2+dx], [2-dy, 2+dy], color=BLUE, lw=2)
ax.plot(2, 2, 'o', color='black', ms=4)
ax.text(2.05, 1.8, '$(t_i, x_j)$', fontsize=9)
d = np.array([1.0, 1.0]) / np.sqrt(2); n = np.array([-1.0, 1.0]) / np.sqrt(2)
P1 = tuple(np.array([2.0, 2.0]) - d*0.38 - n*0.28)
P2 = tuple(np.array([2.0, 2.0]) + d*0.38 - n*0.28)
ax.annotate('', xy=P2, xytext=P1, arrowprops=dict(arrowstyle='<->', color=BLUE, lw=1))
ax.text(2.42, 1.68, '$L$', color=BLUE, ha='center', bbox=dict(fc='white', ec='none', pad=1))
ax.text(2.85, 2.15, r'$x - x_j = k_{ij}(t - t_i)$', color=BLUE, fontsize=9)
ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/dirfield_mpl.png', dpi=150); plt.close(fig)

# ---- 2. falling body: dv/dt = 9.8 - v/5, v_eq = 49 ----
m, g, kk = 10.0, 9.8, 2.0
v_eq = m*g/kk  # 49
tau = m/kk     # 5
fig, ax = plt.subplots(figsize=(6.0, 4.6))
t = np.linspace(0, 25, 600)
for v0, style in ((40.0, {}), (60.0, {})):
    ax.plot(t, v_eq + (v0 - v_eq)*np.exp(-t/tau), color=BLUE, lw=2, **style)
ax.axhline(v_eq, ls='--', color=RED, lw=1.8)
ax.text(4.5, v_eq + 8.5, r'$v = 49\,\mathrm{m/s}$ (equilibrium)', color=RED, ha='left',
        bbox=dict(fc='white', ec='none', pad=2))
for tt in (4.0, 10.0, 16.0, 22.0):
    for vv in (v_eq + 9*np.exp(-tt/tau), v_eq, v_eq - 9*np.exp(-tt/tau)):
        slope = (g - kk*vv/m) / 5.0  # scaled for display aspect
        seg = 1.6
        ax.plot([tt-seg, tt+seg], [vv-slope*seg, vv+slope*seg], color=GRAY, lw=1.6)
ax.set_xlabel('$t$', fontsize=13)
ax.set_ylabel('$v$', fontsize=13, rotation=0, labelpad=12)
ax.set_xlim(0, 25); ax.set_ylim(35, 65)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/falling_mpl.png', dpi=150); plt.close(fig)

# ---- 3. logistic: Np=100, a from tikz data (S-curve N0=20, decay N0=180) ----
Np, a = 100.0, 0.5
def N(t, N0):
    A = (Np - N0)/N0
    return Np/(1 + A*np.exp(-a*t))
fig, ax = plt.subplots(figsize=(6.4, 4.6))
t = np.linspace(0, 26, 600)
ax.plot(t, N(t, 20.0), color=BLUE, lw=2)
ax.plot(t, N(t, 180.0), color=RED, lw=2)
ax.axhline(Np, ls='--', color=GRAY, lw=1.4)
ax.text(25.2, 108, r'Equilibrium ($N_0 = N_p$)', va='bottom', ha='right', fontsize=10)
ax.axhline(Np/2, ls=':', color=GRAY, lw=1.2)
ax.text(26.2, Np/2, r'$N_p/2$', va='center', fontsize=10)
ax.plot(0, 20, 'ko', ms=5)
ax.text(-0.5, 20, '$N_0$', ha='right', va='center')
ax.text(21, 66, 'S-shaped curve', color=BLUE, ha='center', fontsize=10)
ax.text(6, 30, 'concave up', color=BLUE, ha='center', fontsize=10)
ax.text(22, 84, 'concave down', color=BLUE, ha='center', fontsize=10)
ax.text(4, 128, 'Over-capacity decay ($N_0 > N_p$)', color=RED, ha='left', va='center', fontsize=10)
t_infl = np.log((Np-20.0)/20.0)/a
ax.plot(t_infl, N(t_infl, 20.0), 'ko', ms=6)
ax.text(14, 36, 'inflection: max growth', ha='center', fontsize=10)
ax.set_xlabel('$t$', fontsize=13)
ax.set_ylabel('$N(t)$', fontsize=13, rotation=0, labelpad=15)
ax.set_xlim(-0.5, 30); ax.set_ylim(0, 200)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/logistic_mpl.png', dpi=150); plt.close(fig)
print('de saved')
