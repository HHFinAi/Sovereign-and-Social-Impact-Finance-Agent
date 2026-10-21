"""Optional Matplotlib chart; no plotting dependency in model or CI."""
from pathlib import Path
import argparse
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def render(preview=None):
    root = Path(__file__).resolve().parent / 'ageing-fiscal'
    rows = json.loads((root / 'results.json').read_text())['countries']
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'svg.fonttype': 'none',
                         'svg.hashsalt': 'hhfinai-ageing-20261021', 'axes.spines.top': False, 'axes.spines.right': False})
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for i, r in enumerate(rows):
        ax.plot([r['ratio_2024'], r['ratio_2054']], [i, i], color='#a9b9c4', lw=5)
        ax.scatter(r['ratio_2024'], i, color='#267d8d', s=100, label='2024 estimate' if i == 0 else None, zorder=3)
        ax.scatter(r['ratio_2054'], i, color='#17365d', s=100, label='2054 projection' if i == 0 else None, zorder=3)
        ax.text(r['ratio_2024'] - 1.5, i + .16, f"{r['ratio_2024']:.1f}", ha='right')
        ax.text(r['ratio_2054'] + 1.5, i + .16, f"{r['ratio_2054']:.1f}")
    ax.set_yticks(range(3), ['Japan', 'Germany', 'UK'])
    ax.set(title='Ageing increases the demographic financing pressure', xlabel='People aged 65+ per 100 people aged 20–64', xlim=(0, 90), ylim=(-.6, 2.8))
    ax.invert_yaxis()
    ax.legend(loc='lower right', frameon=False)
    fig.text(.08, .025, 'Source: OECD Pensions at a Glance 2025, Table 6.2; underlying UN WPP 2024.\nAge groups are not actual pensioners and workers. No fiscal spending or bond-return inference.', fontsize=9, color='#526170')
    fig.tight_layout(rect=(0, .11, 1, 1))
    fig.savefig(root / 'chart.svg', metadata={'Date': None})
    if preview:
        preview.mkdir(parents=True, exist_ok=True)
        fig.savefig(preview / 'ageing-fiscal.png', dpi=120)
    plt.close(fig)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--preview-dir', type=Path)
    render(p.parse_args().preview_dir)
