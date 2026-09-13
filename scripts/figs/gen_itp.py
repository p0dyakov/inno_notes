import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, Rectangle
import matplotlib.patheffects as pe
import os
OUT = '/Users/p0dyakov/Desktop/Projects/inno_notes/semester-1/Introduction to Programming/fig-mpl'
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.family': 'serif', 'font.size': 10})

def arrow(ax, p, q, col='black', w=1.4):
    ax.annotate('', xy=q, xytext=p, arrowprops=dict(arrowstyle='-|>', color=col,
                lw=w, shrinkA=2, shrinkB=3))

# ---- fig 1: compilation pipeline ----
fig, ax = plt.subplots(figsize=(9.5, 4.6))
BLUE, ORG, GRN, GRY = '#dbeafe', '#ffedd5', '#dcfce7', '#f3f4f6'
cols = [1.0, 3.6, 6.2, 9.3, 12.3]
rows = [3.1, 1.7, 0.3]
names = ['main.c', 'foo.c', 'bar.c']
for y, n in zip(rows, names):
    ax.add_patch(FancyBboxPatch((cols[0]-0.7, y-0.35), 1.4, 0.7,
                 boxstyle='round,pad=0.02,rounding_size=0.12', fc=BLUE, ec='black'))
    ax.text(cols[0], y, n, ha='center', va='center')
    ax.text(cols[1], y, 'Compiler', ha='center', va='center')
    # cylinder: body + top ellipse
    ax.add_patch(Rectangle((cols[2]-0.6, y-0.35), 1.2, 0.6, fc=ORG, ec='black'))
    ax.add_patch(Ellipse((cols[2], y+0.25), 1.2, 0.3, fc='#fdba74', ec='black'))
    ax.text(cols[2], y-0.05, n.replace('.c', '.o'), ha='center', va='center', fontsize=9)
    arrow(ax, (cols[0]+0.7, y), (cols[1]-0.75, y))
    arrow(ax, (cols[1]+0.75, y), (cols[2]-0.6, y))
    arrow(ax, (cols[2]+0.6, y), (cols[3]-0.85, 1.7))
ax.text(cols[3], 1.7, 'Linker', ha='center', va='center')
ax.add_patch(FancyBboxPatch((cols[4]-1.0, 1.7-0.7), 2.0, 1.4,
             boxstyle='round,pad=0.02,rounding_size=0.15', fc=GRN, ec='black'))
ax.text(cols[4], 1.7, 'Executable\nProgram (fubar)', ha='center', va='center')
ax.add_patch(Ellipse((cols[3], 0.0), 1.7, 0.55, fc=GRY, ec='black'))
ax.text(cols[3], 0.0, 'Libraries', ha='center', va='center')
arrow(ax, (cols[3], 0.28), (cols[3], 1.15))
arrow(ax, (cols[3]+0.85, 1.7), (cols[4]-1.0, 1.7))
ax.set_xlim(-0.2, 13.8); ax.set_ylim(-0.6, 3.9); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/compilation_mpl.png', dpi=150); plt.close(fig)

# ---- fig 2: memory model ----
fig, ax = plt.subplots(figsize=(9.5, 6.2))
segs = [('Program (Code) Segment', '#bfdbfe'), ('Static/Global Data Segment', '#bbf7d0'),
        ('Heap', '#fed7aa'), ('Stack', '#fecaca')]
ys = [0.0, 1.7, 3.4, 5.4]; hs = [1.3, 1.3, 1.6, 1.6]
ann = [['Machine instructions', 'Read-only', 'Fixed size'],
       ['Global variables', 'Static variables', 'Lifetime: entire program'],
       ['Dynamic allocation', 'malloc() / free()', 'Variable size at runtime'],
       ['Local variables', 'Function parameters', 'Return addresses', 'LIFO structure']]
for (name, col), y, h, a in zip(segs, ys, hs, ann):
    ax.add_patch(Rectangle((1.2, y), 5.6, h, fc=col, ec='black', lw=1.4))
    ax.text(3.0, y + h/2, name, ha='center', va='center', fontweight='bold')
    for i, t in enumerate(a):
        ax.text(7.3, y + h - 0.35 - i*0.32, '\u2022 ' + t, ha='left', va='center', fontsize=9)
    ax.plot([6.8, 7.1], [y + h/2]*2, color='gray', ls='--', lw=1)
ax.text(0.2, 0.65, 'Low Address', ha='left', va='center', fontsize=9, family='monospace', color='dimgray')
ax.text(0.2, 6.7, 'High Address', ha='left', va='center', fontsize=9, family='monospace', color='dimgray')
ax.plot([0.7]*2, [0, 7.0], color='black', lw=2.5)
ax.annotate('', xy=(5.9, 3.4+1.5), xytext=(5.9, 3.4+0.1),
            arrowprops=dict(arrowstyle='-|>', color='#2563eb', lw=2))
ax.text(5.9, 4.2, 'grows upward', fontsize=9, ha='center',
        bbox=dict(fc='white', ec='none', pad=1))
ax.annotate('', xy=(5.9, 5.4+0.1), xytext=(5.9, 5.4+1.5),
            arrowprops=dict(arrowstyle='-|>', color='#2563eb', lw=2))
ax.text(5.9, 6.15, 'grows downward', fontsize=9, ha='center',
        bbox=dict(fc='white', ec='none', pad=1))
ax.text(4.0, 7.6, 'Program Memory Layout', ha='center', fontsize=14, fontweight='bold')
ax.set_xlim(0, 12.5); ax.set_ylim(-0.3, 8.0); ax.axis('off')
fig.tight_layout(); fig.savefig(f'{OUT}/memory_mpl.png', dpi=150); plt.close(fig)
print('itp saved')
