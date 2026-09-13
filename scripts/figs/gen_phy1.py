"""Matplotlib replacements for Physics I/1 tikz figures (computed geometry only).

Covers: fig-1d-coordinate-axis, fig-secant-slope (replaces tikz secant),
fig-rod (1.7 sliding rod), fig-mach (1.9, exact tangency), fig-curve (1.10
osculating arc), pursuit (4.4 police chase x(t), exact crossing).
Also writes scurve_mpl (solved S-curve tangency) and triangle_mpl
(cyclic pursuit triangle) into the same fig-mpl directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc as MArc
import numpy as np
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   '..', '..', 'semester-4', 'Physics I', 'fig-mpl')
OUT = os.path.normpath(OUT)
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'mathtext.fontset': 'stix'})
BLUE, RED, GRAY = '#1f5fd0', '#d62728', '#8a8a8a'

# ---- 1. 1D axis with displacement + direction polarity ----
fig, ax = plt.subplots(figsize=(7.2, 2.6))
ax.plot([-4.5, 4.5], [0, 0], color='k', lw=1.6)
ax.annotate('', xy=(4.5, 0), xytext=(4.3, 0), arrowprops=dict(arrowstyle='-|>', color='k', lw=1.6))
for n in range(-4, 5):
    ax.plot([n, n], [-0.1, 0.1], color='k', lw=1)
    ax.text(n, -0.22, f'${n}$', ha='center', va='top')
ax.plot(0, 0, '|', color='k', ms=14, mew=2.4)
ax.text(0, -0.62, 'Origin', ha='center', va='top')
ax.text(4.75, 0.02, r'$x$ (m)', va='center')
ax.annotate('', xy=(3, 0.55), xytext=(-2, 0.55),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=4, shrinkB=4))
ax.plot(-2, 0.55, 'o', color=BLUE, ms=6)
ax.plot(3, 0.55, 'o', color=BLUE, ms=6)
ax.text(-2, 0.42, '$x_1$', color=BLUE, ha='right', va='top')
ax.text(3, 0.42, '$x_2$', color=BLUE, ha='left', va='top')
ax.text(0.5, 0.66, r'$\Delta x = +5\,\mathrm{m}$', color=BLUE, ha='center', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.annotate('', xy=(-3, 1.25), xytext=(-1, 1.25),
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.4))
ax.text(-2, 1.42, 'Negative direction', color=RED, ha='center', va='bottom')
ax.annotate('', xy=(3, 1.25), xytext=(1, 1.25),
            arrowprops=dict(arrowstyle='->', color=RED, lw=1.4))
ax.text(2, 1.42, 'Positive direction', color=RED, ha='center', va='bottom')
ax.set_xlim(-4.8, 5.4); ax.set_ylim(-1.0, 2.0); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/axis_mpl.png', dpi=150); plt.close(fig)

# ---- 2. secant slope (same parabola 0.3t^2-0.2t-0.6, points (1,-0.5),(4,3.4)) ----
fig, ax = plt.subplots(figsize=(6.0, 5.0))
t = np.linspace(1.0, 4.0, 400)
x = 0.3*t*t - 0.2*t - 0.6
ax.plot(t, x, color=BLUE, lw=2)
t1, x1, t2, x2 = 1.0, -0.5, 4.0, 3.4
ax.plot([t1, t2], [x1, x2], color=RED, lw=2)
ax.plot([t1], [x1], 'ko', ms=7); ax.plot([t2], [x2], 'ko', ms=7)
ax.text(t1 - 0.12, x1 - 0.12, '$(t_1, x_1)$', ha='right', va='top',
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(t2 + 0.08, x2 + 0.05, '$(t_2, x_2)$', ha='left', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
y0 = x1 - 0.45
ax.plot([t1, t2], [y0, y0], ls='--', color=GRAY, lw=1)
ax.plot([t1, t1], [x1, y0], ls='--', color=GRAY, lw=1)
ax.plot([t2, t2], [y0, x2], ls='--', color=GRAY, lw=1)
ax.text((t1+t2)/2, x1 - 0.6, r'$\Delta t$', ha='center', va='top', color=GRAY)
ax.text(t2 + 0.15, (x1+x2)/2, r'$\Delta x$', ha='left', va='center', color=GRAY,
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(1.85, 2.05, r'slope $= v_{\mathrm{avg}}$', color=RED, ha='center',
        bbox=dict(fc='white', ec='none', pad=2))
ax.set_xlabel('$t$', fontsize=13); ax.set_ylabel('$x$', fontsize=13, rotation=0, labelpad=12)
ax.set_xlim(-0.4, 4.6); ax.set_ylim(-1.6, 3.9)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_position(('data', 0)); ax.spines['bottom'].set_position(('data', 0))
fig.tight_layout(); fig.savefig(f'{OUT}/secant_mpl.png', dpi=150); plt.close(fig)

# ---- 3. sliding rod: A=(3.2,0) B=(0,3), l label, v right, vB down (clear of rod) ----
fig, ax = plt.subplots(figsize=(5.6, 4.6))
A = np.array([3.2, 0.0]); B = np.array([0.0, 3.0])
ax.annotate('', xy=(4.5, 0), xytext=(-0.5, 0), arrowprops=dict(arrowstyle='->', lw=1))
ax.annotate('', xy=(0, 4.0), xytext=(0, -0.5), arrowprops=dict(arrowstyle='->', lw=1))
ax.text(4.6, 0.05, '$x$'); ax.text(0.08, 4.05, '$y$')
ax.text(-0.18, -0.18, '$O$')
ax.plot([A[0], B[0]], [A[1], B[1]], color='#1d4ed8', lw=3)
mid = (A + B) / 2
ax.text(mid[0] + 0.15, mid[1] + 0.1, '$l$', color='#1d4ed8', ha='left', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot(*A, 'o', color='#b91c1c', ms=8); ax.plot(*B, 'o', color='#b91c1c', ms=8)
ax.text(A[0], -0.3, '$A(X_A, 0)$', color='#b91c1c', ha='center', va='top')
ax.text(-0.12, B[1], '$B(0, Y_B)$', color='#b91c1c', ha='right', va='center')
ax.annotate('', xy=(A[0] + 0.9, 0), xytext=tuple(A),
            arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=2, shrinkA=3, shrinkB=0))
ax.text(A[0] + 0.45, 0.15, '$v$', color='#b91c1c', ha='center', va='bottom')
vB_tail = (B[0], B[1] - 0.28)          # just below dot B, on the wall line x=0
vB_len = B[1] / 4                        # proportional to current rod height
ax.annotate('', xy=(vB_tail[0], vB_tail[1] - vB_len), xytext=vB_tail,
            arrowprops=dict(arrowstyle='-|>', color='#b91c1c', lw=2, shrinkA=0, shrinkB=0))
ax.text(vB_tail[0] + 0.14, vB_tail[1] - vB_len/2, '$v_B$', color='#b91c1c', ha='left', va='center')
ax.set_xlim(-0.6, 4.8); ax.set_ylim(-0.7, 4.2); ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/rod_mpl.png', dpi=150); plt.close(fig)

# ---- 4. Mach cone: right triangle OBC (OB=H vertical, BC=ut horizontal),
# cone generator CO, exact tangent circle from A to CO ----
fig, ax = plt.subplots(figsize=(7.0, 4.6))
O = np.array([1.0, 0.0]); Bpt = np.array([1.0, 3.0]); C = np.array([5.5, 3.0]); A = np.array([2.8, 3.0])
d = O - C
d = d / np.linalg.norm(d)            # unit vector along cone generator CO
n = np.array([-d[1], d[0]])          # unit normal to CO
r = abs(float((A - C) @ n))          # distance from A to line CO
foot = A - float((A - C) @ n) * n    # projection of A onto line CO
T = foot                             # exact tangency point, T=(3.631,1.754)
ax.plot([-0.5, 6.5], [0, 0], color='k', lw=1.6)
ax.text(6.6, 0.02, 'Ground', va='center')
ax.plot([-0.5, 6.5], [3, 3], ls='--', color=GRAY, lw=1)
ax.text(6.6, 3.02, 'Flight path', va='center')
ax.plot([Bpt[0], O[0]], [Bpt[1], O[1]], color='k', lw=1.6)
ax.text(0.82, 1.5, '$H$', ha='right', va='center')
ax.plot([1.0, 1.3, 1.3], [2.7, 2.7, 3.0], color='k', lw=1)  # right-angle mark
ax.annotate('', xy=(5.5, 3.5), xytext=(1.15, 3.5),
            arrowprops=dict(arrowstyle='<->', lw=1))
ax.text(3.3, 3.62, '$ut$', ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=1))
ax.plot([C[0], O[0]], [C[1], O[1]], color=RED, lw=2)
th = np.linspace(0, 2*np.pi, 300)
ax.plot(A[0] + r*np.cos(th), A[1] + r*np.sin(th), ls='--', color=BLUE, lw=1.2)
ax.annotate('', xy=tuple(T), xytext=tuple(A),
            arrowprops=dict(arrowstyle='->', color=BLUE, lw=1.4, shrinkA=0, shrinkB=1))
ax.text((A[0]+T[0])/2 - 0.15, (A[1]+T[1])/2 + 0.12, "$ct'$", color=BLUE, ha='right', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot(*T, 'ko', ms=5)
ax.add_patch(MArc(tuple(C), 1.1, 1.1, angle=0, theta1=180, theta2=214, color='k', lw=1))
ax.text(4.72, 2.52, r'$\alpha$', ha='center', va='center', bbox=dict(fc='white', ec='none', pad=1))
ax.text(1.0, 3.95, '$B$ ($t=0$)', ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=1))
ax.text(5.5, 3.95, '$C$ ($t$)', ha='center', va='bottom', bbox=dict(fc='white', ec='none', pad=1))
ax.text(O[0], -0.25, '$O$ (Observer)', ha='center', va='top')
ax.text(A[0] + 0.12, A[1] + 0.12, '$A$', ha='left', va='bottom', bbox=dict(fc='white', ec='none', pad=1))
ax.set_xlim(-0.6, 7.3); ax.set_ylim(-0.6, 4.3); ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/mach_mpl.png', dpi=150); plt.close(fig)
print(f'mach: foot={foot.round(3)} r={r:.3f}')
# ---- 5. osculating circle: compact arc 52..128 deg, r=2, C=(2,-0.2), A=(2,1.8) ----
fig, ax = plt.subplots(figsize=(6.2, 4.0))
Cc = np.array([2.0, -0.2]); Ap = np.array([2.0, 1.8])
phi = np.linspace(np.deg2rad(52), np.deg2rad(128), 200)
ax.plot(Cc[0] + 2*np.cos(phi), Cc[1] + 2*np.sin(phi), ls='--', color=GRAY, lw=1.2)
tt = np.linspace(0.3, 3.7, 300)
ax.plot(tt, 1.8 - 0.55*(tt - 2.0)**2 + 0.06*(tt - 2.0)**3, color='k', lw=2)
ax.text(-0.85, 1.1, 'trajectory $l$', ha='left', va='center')
ax.plot(*Cc, 'ko', ms=6); ax.text(2.0, -0.42, '$C$', ha='center', va='top')
ax.plot(*Ap, 'ko', ms=6)
ax.text(2.0, 1.95, '$A$', ha='right', va='bottom', bbox=dict(fc='white', ec='none', pad=1))
ax.plot([Cc[0], Ap[0]], [Cc[1], 0.6], color='k', ls=':', lw=1.6)
ax.text(2.18, 0.7, r'$\rho$', ha='left', va='center')
ax.annotate('', xy=(3.2, 1.8), xytext=(2.0, 1.8),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=2, shrinkB=0))
ax.text(2.6, 1.95, r'$\vec{\tau}$', color=BLUE, ha='center', va='bottom')
ax.annotate('', xy=(2.0, 0.6), xytext=(2.0, 1.8),
            arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, shrinkA=2, shrinkB=0))
ax.text(1.85, 1.2, r'$\vec{n}$', color=RED, ha='right', va='center')
ax.set_xlim(-1.3, 4.2); ax.set_ylim(-0.7, 2.4); ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/curve_mpl.png', dpi=150); plt.close(fig)

# ---- 6. police pursuit x(t): SI units, exact crossing (21.94 s, 680.1 m) ----
vc, am, dly = 31.0, 3.6, 2.5
t_star = (40 + np.sqrt(1519)) / 3.6
x_star = vc * t_star
t = np.linspace(0, 25, 600)
xc = vc * t
xm = np.where(t < dly, 0.0, 0.5 * am * (t - dly) ** 2)
fig, ax = plt.subplots(figsize=(6.0, 4.6))
ax.plot(t, xc, color=BLUE, lw=2)
ax.plot(t, xm, color=RED, lw=2)
ax.plot([dly, dly], [0, 0.5*am*0.09], ls='--', color=GRAY, lw=1)
ax.plot([t_star, t_star], [0, x_star], ls='--', color=GRAY, lw=1)
ax.plot([0, t_star], [x_star, x_star], ls='--', color=GRAY, lw=1)
ax.plot(t_star, x_star, 'ko', ms=6)
ax.text(dly, -28, r'$\Delta t_d$', ha='center', va='top')
ax.text(t_star, -28, "$t^*$", ha='center', va='top')
ax.text(-0.9, x_star, "$x^*$", ha='right', va='center')
ax.text(t_star - 0.4, x_star + 30, 'Overtake', ha='right', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(13.5, vc*13.5 + 60, '$x_c(t)$', color=BLUE, ha='center', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(19.5, 0.5*am*(19.5-dly)**2 - 45, '$x_m(t)$', color=RED, ha='center', va='top',
        bbox=dict(fc='white', ec='none', pad=1))
ax.set_xlabel('$t$ (s)', fontsize=13); ax.set_ylabel('$x$ (m)', fontsize=13)
ax.set_xlim(-0.6, 25.5); ax.set_ylim(-40, 800)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/pursuit_mpl.png', dpi=150); plt.close(fig)
print('phy1 saved:', t_star, x_star)
