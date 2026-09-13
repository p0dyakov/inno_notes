"""Matplotlib replacements for Physics I/2 tikz figures (computed geometry only).

vectors_mpl:    r1/r2/Delta-r/v on smooth path (literal tikz coordinates).
projectile_mpl: y(x)=tan*t-g x^2/(2(v0 cos)^2); v0,g solved from the two tikz
                curves so they share one R=5.2 (30/60 deg pair).
circular_mpl:   uniform circular motion, r=2, p at 45 deg; v tangent, a inward.
natural_mpl:    arc element rho=4.5, angles 45/75 deg, tau1/tau2/n + dtau inset.
decomp_mpl:     parabola y=0.12t^2+0.3 at P(2.2,~0.88); v tangent, a_tau/a_n/a
                from exact derivatives (not eyeballed offsets).
triangle2_mpl:  cyclic pursuit triangle side 4.5, v2 projection v/2 exact.
pursuit90_mpl:  orthogonal pursuit: trajectory integrated numerically
                (u=1, v=2, l=10, T=20/3); geometry exact, not hand points.
vgraph_mpl:     piecewise v(t) polyline through the literal tikz nodes.
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
ORANGE, PURPLE, TEAL = '#c2410c', '#7e22ce', '#0d9488'

# ---- 0. kinematic vectors ----
fig, ax = plt.subplots(figsize=(6.6, 4.6))
tp = np.array([[0.8, 1.2], [2, 2.8], [3.5, 3.6], [5.2, 2.8]])
tc = np.linspace(0, 1, 200)
path = sum(np.outer((1-tc)**(3-i)*tc**i, p) * c
           for i, (p, c) in enumerate(zip(tp, [1, 3, 3, 1])))
ax.plot(path[:, 0], path[:, 1], color=GRAY, lw=2)
P1 = np.array([2.0, 2.8]); P2 = np.array([4.5, 3.3])
ax.annotate('', xy=tuple(P1), xytext=(0, 0),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=0, shrinkB=2))
ax.annotate('', xy=tuple(P2), xytext=(0, 0),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=0, shrinkB=2))
ax.text(0.35, 1.15, r'$\vec{r}_1$', color=BLUE, ha='right', va='center',
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(2.6, 1.05, r'$\vec{r}_2$', color=BLUE, ha='left', va='center',
        bbox=dict(fc='white', ec='none', pad=1))
ax.annotate('', xy=tuple(P2), xytext=tuple(P1),
            arrowprops=dict(arrowstyle='-|>', color=ORANGE, lw=2, shrinkA=2, shrinkB=2))
ax.text(3.1, 2.9, r'$\Delta\vec{r}$', color=ORANGE, ha='center', va='top',
        bbox=dict(fc='white', ec='none', pad=1))
ax.annotate('', xy=tuple(P1 + [0.95, 0.5]), xytext=tuple(P1),
            arrowprops=dict(arrowstyle='-|>', color=PURPLE, lw=2.4, shrinkA=2, shrinkB=0))
ax.text(3.35, 3.6, r'$\vec{v}$', color=PURPLE, ha='left', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot(*P1, 'ko', ms=6); ax.plot(*P2, 'ko', ms=6)
ax.text(1.82, 2.72, '$P_1$', ha='right', va='bottom')
ax.text(4.62, 3.3, '$P_2$', ha='left', va='center')
ax.text(5.5, 2.35, 'Path', color=GRAY, ha='center', va='center')
ax.set_xlabel('$x$', fontsize=13); ax.set_ylabel('$y$', fontsize=13, rotation=0, labelpad=12)
ax.set_xlim(-0.5, 6.8); ax.set_ylim(-0.4, 4.6)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/vectors_mpl.png', dpi=150); plt.close(fig)

# ---- 1. projectile pair: shared v0,g from tikz curves, R=5.2 common ----
# tikz: y1=0.577x-0.111x^2 (30deg), y2=1.732x-0.333x^2 (60deg)
g = 9.8
v0 = np.sqrt(5.2*g/np.sin(np.deg2rad(60)))
th1, th2 = np.deg2rad(30), np.deg2rad(60)
fig, ax = plt.subplots(figsize=(6.2, 4.2))
x = np.linspace(0, 5.2, 400)
for th, col in ((th1, BLUE), (th2, RED)):
    y = np.tan(th)*x - g*x**2/(2*(v0*np.cos(th))**2)
    ax.plot(x, y, color=col, lw=2)
ax.text(3.6, 0.9, r'$\theta_1 = 30^\circ$', color=BLUE, ha='center', va='center',
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(1.6, 2.5, r'$\theta_2 = 60^\circ$', color=RED, ha='center', va='center',
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot(5.2, 0, 'ko', ms=6)
ax.text(5.2, -0.22, '$R$', ha='center', va='top')
ax.set_xlabel('$x$', fontsize=13); ax.set_ylabel('$y$', fontsize=13, rotation=0, labelpad=12)
ax.set_xlim(-0.2, 6.0); ax.set_ylim(-0.4, 3.2)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/projectile_mpl.png', dpi=150); plt.close(fig)

# ---- 2. uniform circular motion, r=2, p at 45 deg ----
r = 2.0
th = np.deg2rad(45)
p = np.array([r*np.cos(th), r*np.sin(th)])
fig, ax = plt.subplots(figsize=(5.2, 5.2))
phi = np.linspace(0, 2*np.pi, 400)
ax.plot(r*np.cos(phi), r*np.sin(phi), ls='--', color=GRAY, lw=1.2)
ax.plot(*p, 'ko', ms=6)
ax.text(p[0]+0.12, p[1]+0.12, '$p(x_p, y_p)$', ha='left', va='bottom')
ax.annotate('', xy=tuple(p), xytext=(0, 0),
            arrowprops=dict(arrowstyle='-|>', color='k', lw=2, shrinkA=0, shrinkB=2))
ax.text(p[0]/2 - 0.1, p[1]/2 - 0.25, '$r$', ha='right', va='top')
tangent = np.array([-np.sin(th), np.cos(th)])
ax.annotate('', xy=tuple(p + 0.85*tangent), xytext=tuple(p),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=2, shrinkB=0))
ax.text(*(p + 0.95*tangent + [-0.15, 0.1]), r'$\vec{v}$', color=BLUE, ha='left', va='bottom')
ax.annotate('', xy=tuple(p*0.5), xytext=tuple(p),
            arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, shrinkA=0, shrinkB=0))
ax.text(p[0]*0.72 - 0.28, p[1]*0.72, r'$\vec{a}$', color=RED, ha='right', va='center')
ax.set_xlabel('$x$', fontsize=13); ax.set_ylabel('$y$', fontsize=13, rotation=0, labelpad=12)
ax.set_xlim(-2.6, 3.1); ax.set_ylim(-2.6, 2.9); ax.set_aspect('equal')
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
ax.spines['left'].set_position(('data', 0)); ax.spines['bottom'].set_position(('data', 0))
fig.tight_layout(); fig.savefig(f'{OUT}/circular_mpl.png', dpi=150); plt.close(fig)

# ---- 3. natural coordinates: arc rho=4.5 between 45 and 75 deg + dtau inset ----
rho = 4.5
a1, a2 = np.deg2rad(45), np.deg2rad(75)
P_1 = rho*np.array([np.cos(a1), np.sin(a1)])
P_2 = rho*np.array([np.cos(a2), np.sin(a2)])
fig, ax = plt.subplots(figsize=(7.4, 5.2))
phi = np.linspace(a1 - 0.35, a2 + 0.35, 300)
ax.plot(rho*np.cos(phi), rho*np.sin(phi), color='k', lw=2)
ax.plot([0, P_1[0]], [0, P_1[1]], ls='--', color=GRAY, lw=1.2)
ax.plot([0, P_2[0]], [0, P_2[1]], ls='--', color=GRAY, lw=1.2)
ax.text(P_1[0]/2 - 0.1, P_1[1]/2 - 0.25, r'$\rho$', ha='right', va='top')
ax.text(P_2[0]/2 - 0.45, P_2[1]/2 + 0.1, r'$\rho$', ha='right', va='bottom')
ax.plot(0, 0, 'ko', ms=6); ax.text(0, -0.25, '$O$', ha='center', va='top')
ax.plot(*P_1, 'ko', ms=6); ax.text(P_1[0]+0.12, P_1[1]-0.05, '$1$', ha='left', va='center')
ax.plot(*P_2, 'ko', ms=6); ax.text(P_2[0]+0.05, P_2[1]+0.15, '$2$', ha='left', va='bottom')
t1 = np.array([-np.sin(a1), np.cos(a1)]); t2 = np.array([-np.sin(a2), np.cos(a2)])
ax.annotate('', xy=tuple(P_1 + 1.2*t1), xytext=tuple(P_1),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=2, shrinkB=0))
ax.text(*(P_1 + 1.35*t1 + [0.15, 0.05]), r'$\boldsymbol{\tau}_1$', color=BLUE, ha='left', va='bottom')
ax.annotate('', xy=tuple(P_2 + 1.2*t2), xytext=tuple(P_2),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=2, shrinkB=0))
ax.text(*(P_2 + 1.35*t2 + [-0.1, 0.1]), r'$\boldsymbol{\tau}_2$', color=BLUE, ha='right', va='bottom')
mid = (a1+a2)/2
nmid = -np.array([np.cos(mid), np.sin(mid)])
ax.annotate('', xy=tuple(rho*np.array([np.cos(mid), np.sin(mid)]) + nmid*1.2),
            xytext=tuple(rho*np.array([np.cos(mid), np.sin(mid)])),
            arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, shrinkA=2, shrinkB=0))
ax.text(*(rho*np.array([np.cos(mid), np.sin(mid)]) + nmid*1.35 + [0.3, 0]),
        r'$\boldsymbol{n}$', color=RED, ha='left', va='center')
ax.add_patch(MArc((0, 0), 2.6, 2.6, angle=0, theta1=45, theta2=75, color='k', lw=1))
ax.text(1.55, 1.35, r'$d\alpha$', ha='left', va='bottom')
# inset: dtau triangle
ix, iy = 4.35, 0.55
ax.annotate('', xy=(ix+1.5, iy), xytext=(ix, iy),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=0, shrinkB=0))
ax.text(ix+0.75, iy-0.18, r'$\boldsymbol{\tau}_1$', color=BLUE, ha='center', va='top')
ax.annotate('', xy=(ix+1.5*np.cos(np.deg2rad(30)), iy+1.5*np.sin(np.deg2rad(30))), xytext=(ix, iy),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=0, shrinkB=0))
ax.text(ix+1.15, iy+0.95, r'$\boldsymbol{\tau}_2$', color=BLUE, ha='left', va='bottom')
ax.annotate('', xy=(ix+1.5*np.cos(np.deg2rad(30)), iy+1.5*np.sin(np.deg2rad(30))), xytext=(ix+1.5, iy),
            arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, shrinkA=0, shrinkB=0))
ax.text(ix+1.62, iy+0.4, r'$d\boldsymbol{\tau}$', color=RED, ha='left', va='center')
ax.add_patch(MArc((ix, iy), 1.2, 1.2, angle=0, theta1=0, theta2=30, color='k', lw=1))
ax.text(ix+0.75, iy+0.22, r'$d\alpha$', ha='left', va='bottom')
ax.set_xlim(-0.7, 6.6); ax.set_ylim(-0.7, 5.4); ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/natural_mpl.png', dpi=150); plt.close(fig)

# ---- 4. acceleration decomposition on y=0.12t^2+0.3 at P(2.2, ~0.88) ----
f = lambda t: 0.12*t*t + 0.3
P = np.array([2.2, f(2.2)])
fp = 0.24*2.2                      # dy/dt
tau = np.array([1.0, fp]); tau /= np.linalg.norm(tau)
nrm = np.array([-fp, 1.0]); nrm /= np.linalg.norm(nrm)
v = tau*1.7
a_tau = tau*1.17
a_n = nrm*1.17
a = a_tau + a_n
fig, ax = plt.subplots(figsize=(6.0, 4.6))
t = np.linspace(0.8, 4.2, 300)
ax.plot(t, f(t), color='k', lw=2)
ax.plot(*P, 'ko', ms=7)
ax.text(P[0]+0.08, P[1]-0.12, '$P$', ha='left', va='top')
ax.annotate('', xy=tuple(P+v), xytext=tuple(P),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2.4, shrinkA=2, shrinkB=0))
ax.text(*(P+v+[0.08, 0.05]), r'$\vec{v}$', color=BLUE, ha='left', va='bottom')
ax.annotate('', xy=tuple(P+a_tau), xytext=tuple(P),
            arrowprops=dict(arrowstyle='-|>', color=TEAL, lw=2, shrinkA=2, shrinkB=0))
ax.text(*(P+a_tau+[0.08, -0.12]), r'$\vec{a}_\tau$', color=TEAL, ha='left', va='top')
ax.annotate('', xy=tuple(P+a_n), xytext=tuple(P),
            arrowprops=dict(arrowstyle='-|>', color=ORANGE, lw=2, shrinkA=2, shrinkB=0))
ax.text(*(P+a_n+[-0.35, 0.05]), r'$\vec{a}_n$', color=ORANGE, ha='right', va='bottom')
ax.annotate('', xy=tuple(P+a), xytext=tuple(P),
            arrowprops=dict(arrowstyle='-|>', color=RED, lw=2.4, shrinkA=2, shrinkB=0))
ax.text(*(P+a+[0.05, 0.08]), r'$\vec{a}$', color=RED, ha='left', va='bottom')
ax.plot([P[0]+a_tau[0], P[0]+a[0]], [P[1]+a_tau[1], P[1]+a[1]], ls='--', color=GRAY, lw=1.2)
ax.plot([P[0]+a_n[0], P[0]+a[0]], [P[1]+a_n[1], P[1]+a[1]], ls='--', color=GRAY, lw=1.2)
ax.set_xlabel('$x$', fontsize=13); ax.set_ylabel('$y$', fontsize=13, rotation=0, labelpad=12)
ax.set_xlim(-0.5, 5.2); ax.set_ylim(-0.4, 3.7)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/decomp_mpl.png', dpi=150); plt.close(fig)

# ---- 5. cyclic pursuit triangle, side 4.5 ----
s_side = 4.5
A = np.array([0.0, 0.0]); B = np.array([s_side, 0.0]); C = np.array([s_side/2, s_side*np.sqrt(3)/2])
def unit(v): return v/np.linalg.norm(v)
L = 1.6
v1 = unit(B-A)*L; v2 = unit(C-B)*L; v3 = unit(A-C)*L
fig, ax = plt.subplots(figsize=(6.6, 5.4))
for P_, Q_ in ((A, B), (B, C), (C, A)):
    ax.plot([P_[0], Q_[0]], [P_[1], Q_[1]], ls='--', color=GRAY, lw=1.4)
ax.text(2.25, -0.32, '$l$', ha='center', va='top', fontsize=12)
for P_, V_ in ((A, v1), (B, v2), (C, v3)):
    ax.annotate('', xy=tuple(P_+V_), xytext=tuple(P_),
                arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, shrinkA=2, shrinkB=0))
ax.text(*(A + v1/2 + [0, 0.25]), r'$\vec{v}_1$', color=RED, ha='center', va='bottom')
ax.text(*(B + v2/2 + [0.45, 0.3]), r'$\vec{v}_2$', color=RED, ha='left', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(*(C + v3/2 + [-0.45, 0.05]), r'$\vec{v}_3$', color=RED, ha='right', va='center')
par = np.array([-0.8, 0.0])
ax.annotate('', xy=tuple(B+par), xytext=tuple(B),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=2, shrinkB=0, ls='dashed'))
ax.text(B[0]-0.4, -0.32, r'$\vec{v}_{2,G}$', color=BLUE, ha='center', va='top',
        bbox=dict(fc='white', ec='none', pad=1))
ax.annotate('', xy=(3.7, 1.386), xytext=(3.7, 0),
            arrowprops=dict(arrowstyle='-|>', color=GRAY, lw=1.6, ls='dashed', shrinkA=0, shrinkB=0))
ax.text(3.3, 0.75, r'$\vec{v}_{2,V}$', color=GRAY, ha='right', va='center',
        bbox=dict(fc='white', ec='none', pad=1))
ax.add_patch(MArc(tuple(B), 1.2, 1.2, angle=0, theta1=120, theta2=180, color='k', lw=1))
ax.text(3.5, 0.5, r'$\pi/3$', ha='center', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot(*A, 'ko', ms=7); ax.plot(*B, 'ko', ms=7); ax.plot(*C, 'ko', ms=7)
ax.text(-0.22, -0.12, '$1$', ha='right', va='top', fontsize=13)
ax.text(4.62, -0.12, '$2$', ha='left', va='top', fontsize=13)
ax.text(2.25, 4.02, '$3$', ha='center', va='bottom', fontsize=13)
ax.set_xlim(-0.8, 5.5); ax.set_ylim(-0.8, 4.6); ax.set_aspect('equal'); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/triangle2_mpl.png', dpi=150); plt.close(fig)

# ---- 6. orthogonal pursuit: integrate trajectory (u=1, v=2, l=10) ----
u, v, l = 1.0, 2.0, 10.0
dt = 0.002
XA, YA, XB, traj = [0.0], [-l], [0.0], [(0.0, -l)]
t = 0.0
while True:
    dx, dy = XB[-1]-XA[-1], 0.0-YA[-1]
    d = np.hypot(dx, dy)
    XA.append(XA[-1] + v*dx/d*dt); YA.append(YA[-1] + v*dy/d*dt); XB.append(XB[-1] + u*dt)
    t += dt
    traj.append((XA[-1], YA[-1]))
    if d < 0.02 or t > 30:
        break
T_num = t
T_exact = v*l/(v*v-u*u)
print(f'pursuit90: T_num={T_num:.3f} T_exact={T_exact:.3f}')
traj = np.array(traj)
fig, ax = plt.subplots(figsize=(6.6, 4.6))
ax.plot(traj[:, 0], traj[:, 1], color=BLUE, lw=2)
ax.plot(0, -l, 'o', color=BLUE, ms=7)
ax.text(0.18, -l, '$A(0, -l)$', ha='left', va='center', color=BLUE,
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot([0, 0], [0, -l], ls='--', color=GRAY, lw=1.2)
ax.text(-0.12, -l/2, '$l$', ha='right', va='center', color=GRAY)
Ax_, Ay_ = 2.2, float(np.interp(2.2, traj[:, 0], traj[:, 1]))
Bx_ = 4.2
ax.plot(Ax_, Ay_, 'o', color=BLUE, ms=6)
ax.text(Ax_-0.15, Ay_-0.1, '$A(X_A, Y_A)$', ha='right', va='bottom', color=BLUE, fontsize=10)
ax.plot(Bx_, 0, 'o', color=RED, ms=6)
ax.text(Bx_-0.1, 0.62, '$B(ut, 0)$', ha='center', va='bottom', color=RED, fontsize=10,
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot([Ax_, Bx_], [Ay_, 0], ls='--', color=GRAY, lw=1.2)
ax.text((Ax_+Bx_)/2 - 0.35, Ay_/2 + 0.35, '$AB(t)$', ha='right', va='bottom', color=GRAY, fontsize=10)
dx, dy = Bx_-Ax_, 0.0-Ay_
d = np.hypot(dx, dy)
ax.annotate('', xy=(Ax_+dx/d*1.2, Ay_+dy/d*1.2), xytext=(Ax_, Ay_),
            arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=2, shrinkA=2, shrinkB=0))
ax.text(Ax_+dx/d*0.6 - 0.3, Ay_+dy/d*0.6 - 0.15, r'$\vec{v}$', color=BLUE, ha='right', va='top')
ax.annotate('', xy=(Bx_+1.2, 0), xytext=(Bx_, 0),
            arrowprops=dict(arrowstyle='-|>', color=RED, lw=2, shrinkA=2, shrinkB=0))
ax.text(Bx_+0.65, 0.42, r'$\vec{u}$', color=RED, ha='left', va='bottom',
        bbox=dict(fc='white', ec='none', pad=1))
ax.plot([Ax_, Ax_+1.5], [Ay_, Ay_], ls=':', color=GRAY, lw=1.2)
alpha = np.arctan2(-Ay_, Bx_-Ax_)
ax.add_patch(MArc((Ax_, Ay_), 1.4, 1.4, angle=0, theta1=0, theta2=np.rad2deg(alpha), color='k', lw=1))
ax.text(Ax_+0.95, Ay_+0.3, r'$\alpha$', ha='left', va='bottom')
ax.add_patch(MArc((Bx_, 0), 1.2, 1.2, angle=180, theta1=180, theta2=180+np.rad2deg(alpha), color='k', lw=1))
ax.text(Bx_-0.75, -0.3, r'$\alpha$', ha='right', va='top')
ax.set_xlabel('$x$', fontsize=13); ax.set_ylabel('$y$', fontsize=13, rotation=0, labelpad=12)
ax.set_xlim(-0.6, 7.2); ax.set_ylim(-10.5, 1.6)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/pursuit90_mpl.png', dpi=150); plt.close(fig)

# ---- 7. piecewise v(t) polyline through literal nodes ----
fig, ax = plt.subplots(figsize=(7.0, 4.6))
nodes = [(0,0),(2,0),(4,2),(6,6),(8,0),(9,0)]
xs, ys = zip(*nodes)
ax.plot(xs, ys, color=RED, lw=2)
for x_, y_ in nodes:
    ax.plot(x_, y_, 'o', color=RED, ms=6)
ax.text(4, 2, '$(4,2)$', ha='right', va='bottom', color=RED)
ax.text(6, 6, '$(6,6)$', ha='center', va='bottom', color=RED)
ax.text(8.15, 0.35, '$(8,0)$', ha='left', va='bottom', color=RED)
for x_ in (2, 4, 6, 8):
    ax.plot([x_, x_], [-0.12, 0.12], color='k', lw=1, zorder=5)
for y_ in (2, 4, 6):
    ax.plot([-0.12, 0.12], [y_, y_], color='k', lw=1)
ax.plot([4, 4], [0, 2], ls=':', color=GRAY, lw=1.2, zorder=1)
ax.plot([0, 4], [2, 2], ls=':', color=GRAY, lw=1.2, zorder=1)
ax.plot([6, 6], [0, 6], ls=':', color=GRAY, lw=1.2, zorder=1)
ax.plot([0, 6], [6, 6], ls=':', color=GRAY, lw=1.2, zorder=1)
ax.set_xlabel('$t$ (s)', fontsize=13); ax.set_ylabel('$v$ (m/s)', fontsize=13)
ax.set_xlim(-0.4, 9.5); ax.set_ylim(-0.6, 7.0)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/vgraph_mpl.png', dpi=150); plt.close(fig)
print('phy2 saved')
