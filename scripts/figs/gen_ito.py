import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os
OUT = '/Users/p0dyakov/Desktop/Projects/inno_notes/semester-4/Introduction to Optimization/fig-mpl'
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.family': 'serif', 'font.size': 10})
BLUE, RED, GRN, PUR = '#1f5fd0', '#d62728', '#2ca02c', '#9467bd'

# ---- fig 1: simplex path (literal coordinates from the tikz) ----
fig, ax = plt.subplots(figsize=(6.4, 5.2))
poly = np.array([[0,0],[2,0],[1,2],[0,2.5]])
ax.fill(poly[:,0], poly[:,1], color='#d4d4d4', alpha=0.7, zorder=1)
ax.set_xlim(-0.5, 5.5); ax.set_ylim(-2.0, 4.6)
ax.plot([0,2.2], [4-2*0, 4-2*2.2], ls='--', color='k', lw=1)
ax.plot([0,5.2], [2.5, 2.5-0.5*5.2], ls='--', color='k', lw=1)
ax.annotate('', xy=(0,2.4), xytext=(0,0),
            arrowprops=dict(arrowstyle='-|>', lw=2.2, shrinkA=0, shrinkB=0))
ax.annotate('', xy=(0.95,2.03), xytext=(0,2.5),
            arrowprops=dict(arrowstyle='-|>', lw=2.2, shrinkA=0, shrinkB=0))
ax.plot([0,0.95], [0,1.9], ls=':', color=RED, lw=2)
for p, t, o in [((0,0),'A(0,0)',(-0.35,-0.3)), ((0,2.5),'B(0,2.5)',(-0.75,0.05)),
                ((1,2),'C(1,2) [Optimum]',(0.12,0.08)), ((2,0),'D(2,0)',(0,-0.35))]:
    ax.plot(*p, 'ko', ms=6); ax.text(p[0]+o[0], p[1]+o[1], f'${t}$')
ax.text(0.05, 4.15, '$F(0,4)$'); ax.text(5.0, 0.35, '$E(5,0)$')
ax.text(2.5, -1.65, 'Dotted red path: interior traversal prohibited', color=RED, ha='center', fontsize=9)
ax.set_xlabel('$x_1$', fontsize=12); ax.set_ylabel('$x_2$', fontsize=12)
for s in ('top','right'): ax.spines[s].set_visible(False)
ax.set_xticks(range(0,6)); ax.set_yticks(range(0,5))
fig.tight_layout(); fig.savefig(f'{OUT}/simplex_mpl.png', dpi=150); plt.close(fig)

# ---- fig 2: ratio intercepts (literal endpoints) ----
fig, ax = plt.subplots(figsize=(7.2, 4.8))
poly = np.array([[0,0],[4,0],[1,2],[0,1]])
ax.fill(poly[:,0], poly[:,1], color='#d4d4d4', alpha=0.7, zorder=1)
ax.set_xlim(-2.6, 7.0); ax.set_ylim(-0.6, 4.1)
ax.plot([-0.5,5.5], [3.75,-0.75], color=BLUE, lw=2)
ax.plot([-1,7], [3.5,-0.5], color=RED, lw=2)
ax.plot([-1.5,2], [-0.5,3], color=GRN, lw=2)
ax.plot([-1.5,6.5], [2,2], color=PUR, lw=2)
for p, t, o in [((0,0),'A(0,0)',(-0.5,-0.4)), ((4,0),'B(4,0)',(-0.1,-0.4)),
                ((6,0),'(6,0)',(-0.1,-0.4)), ((-1,0),'(-1,0)',(-0.55,0.15))]:
    ax.plot(*p, 'ko', ms=6); ax.text(p[0]+o[0], p[1]+o[1], f'${t}$')
ax.annotate('', xy=(3.9,0), xytext=(0,0),
            arrowprops=dict(arrowstyle='-|>', color='#0d9488', lw=2.4, shrinkA=0, shrinkB=0))
ax.text(1.95, -0.32, r'$x_1 \to 4$', ha='center', fontsize=11)
ax.text(5.4, 3.1, '$6x_1 + 4x_2 = 24$\n$x_1 + 2x_2 = 6$\n$-x_1 + x_2 = 1$\n$x_2 = 2$',
        fontsize=9, va='top', ha='left',
        bbox=dict(fc='white', ec='#cccccc', pad=4))
ax.set_xlabel('$x_1$', fontsize=12); ax.set_ylabel('$x_2$', fontsize=12)
for s in ('top','right'): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(f'{OUT}/ratio_mpl.png', dpi=150); plt.close(fig)
print('ito saved')
