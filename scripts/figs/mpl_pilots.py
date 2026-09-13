import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from scipy.optimize import brentq
import os

OUT = '/Users/p0dyakov/Desktop/Projects/inno_notes/semester-4/Physics I/fig-pilots'
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'stix'})
BLUE, RED, GRAY = '#1f5fd0', '#d62728', '#8a8a8a'

# ---------- Pilot 1: pursuit triangle (exact geometry, nothing eyeballed) ----------
a = 4.0
A = np.array([0.0, 0.0]); B = np.array([a, 0.0]); C = np.array([a/2, a*np.sqrt(3)/2])
def unit(v): return v / np.linalg.norm(v)
L = 1.5
v1 = unit(B - A) * L; v2 = unit(C - B) * L; v3 = unit(A - C) * L
par = np.array([-1.0, 0.0]) * (L * 0.5)          # v2 parallel comp: along BA, magnitude v/2
perp = np.array([0.0, 1.0]) * (L * np.sqrt(3)/2) # v2 perpendicular comp
fig, ax = plt.subplots(figsize=(7, 5.2))
for P, Q in ((A, B), (B, C), (C, A)):
    ax.plot([P[0], Q[0]], [P[1], Q[1]], ls='--', color=GRAY, lw=1.2)
for P, V, col in ((A, v1, RED), (B, v2, RED), (C, v3, RED)):
    ax.annotate('', xy=tuple(P + V), xytext=tuple(P),
                arrowprops=dict(arrowstyle='-|>', color=col, lw=2, shrinkA=0, shrinkB=0))
ax.annotate('', xy=tuple(B + par), xytext=tuple(B),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.6))
ax.annotate('', xy=tuple(B + perp), xytext=tuple(B),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.6))
ax.add_patch(Arc(tuple(B), 1.0, 1.0, angle=0, theta1=120, theta2=180, color='k', lw=1))
for P, tag, off in ((A, '1', (-0.25, -0.35)), (B, '2', (0.12, -0.35)), (C, '3', (-0.05, 0.18))):
    ax.plot(*P, 'ko', ms=7)
    ax.text(P[0]+off[0], P[1]+off[1], tag, fontsize=13)
ax.text(*(A + v1/2 + [0, -0.35]), r'$\vec{v}_1$', color=RED, ha='center')
ax.text(*(B + v2/2 + [0.18, 0.05]), r'$\vec{v}_2$', color=RED)
ax.text(*(C + v3/2 + [-0.5, 0.1]), r'$\vec{v}_3$', color=RED, ha='center')
ax.text(*(B + par/2 + [0, -0.3]), r'$\vec{v}_{2,\parallel}$', color=BLUE, ha='center')
ax.text(*(B + perp + [0.12, 0.05]), r'$\vec{v}_{2,\perp}$', color=BLUE)
ax.text(B[0]-0.62, B[1]+0.32, r'$\pi/3$', fontsize=12)
ax.text(a/2, -0.55, r'$l(t)$', ha='center', fontsize=12)
ax.plot([A[0], B[0]], [0, 0], color='none')  # keep baseline in view
ax.set_aspect('equal'); ax.axis('off')
ax.set_xlim(-0.9, 5.3); ax.set_ylim(-1.0, 4.6)
fig.tight_layout(); fig.savefig(f'{OUT}/triangle_mpl.png', dpi=150); plt.close(fig)

# ---------- Pilot 2: S-curve with SOLVED (not drawn) tangency ----------
L2, k, t_infl = 2.0, 0.55, 11.0
S = lambda t: L2 / (1 + np.exp(-k*(t - t_infl)))
dS = lambda t: L2*k*np.exp(-k*(t-t_infl)) / (1 + np.exp(-k*(t-t_infl)))**2
t0 = brentq(lambda t: S(t) - t*dS(t), t_infl + 0.5, 21.5)  # tangent through origin
print(f't_infl={t_infl} t0={t0:.3f} S(t0)={S(t0):.3f} slope={dS(t0):.4f}')
t = np.linspace(0, 22, 600)
fig, ax = plt.subplots(figsize=(7, 4.6))
ax.plot(t, S(t), color=BLUE, lw=2)
ax.plot([0, t0], [0, S(t0)], color=RED, lw=2)
ax.plot(t_infl, S(t_infl), 'ko', ms=6)
ax.plot(t0, S(t0), 'o', color=RED, ms=6)
ax.plot([t_infl, t_infl], [0, S(t_infl)], ls='--', color=GRAY, lw=1)
ax.plot([t0, t0], [0, S(t0)], ls='--', color=RED, lw=1)
ax.text(t_infl, -0.14, r'$t_{\mathrm{infl}}$', ha='center')
ax.text(t0, -0.14, r'$t_0$', ha='center', color=RED)
ax.text(2.2, 1.55, r'$v_{\max}$ (inflection)', fontsize=12)
ax.text(t0 + 0.7, S(t0) - 0.35, r'$v(t_0)=\bar{v}(t_0)$', color=RED, fontsize=12)
ax.set_xlabel(r'$t$', fontsize=13); ax.set_ylabel(r'$S(t)$', fontsize=13, rotation=0, labelpad=15)
ax.set_xlim(0, 22); ax.set_ylim(-0.2, 2.3)
for spine in ('top', 'right'):
    ax.spines[spine].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/scurve_mpl.png', dpi=150); plt.close(fig)
print('saved')
