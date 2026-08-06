#!/usr/bin/env python3
"""Generate the profile banner in light and dark variants.

The motif on the right is a causal attention mask — the lower-triangular
pattern a decoder-only transformer actually produces, with attention decaying
away from the diagonal. Hand-tuned, not generated at view time: no third-party
service, no tracking pixel, no runtime dependency.
"""
import math
from pathlib import Path

W, H = 1200, 300
COLS, ROWS = 14, 8
CELL, GAP = 15, 5
GRID_W = COLS * CELL + (COLS - 1) * GAP
GRID_X = W - GRID_W - 64
GRID_Y = (H - (ROWS * CELL + (ROWS - 1) * GAP)) / 2

THEMES = {
    "light": dict(panel="#FBFAF9", edge="#E7E5E4", ink="#1C1917",
                  muted="#78716C", accent="#B45309", cell="#B45309"),
    "dark": dict(panel="#0D1117", edge="#21262D", ink="#F0EDE9",
                 muted="#8B8681", accent="#F59E0B", cell="#F59E0B"),
}


def attention(row: int, col: int) -> float:
    """Causal mask: a query at `row` may only attend to keys at col <= row.

    Weight decays with distance from the diagonal, with a small always-on
    floor at col 0 — the attention sink that real GPT-2 heads exhibit.
    """
    span = (COLS - 1) / (ROWS - 1)
    limit = row * span + 1.0
    if col > limit:
        return 0.0
    recency = math.exp(-((limit - col) ** 2) / 11.0)
    sink = 0.34 * math.exp(-(col ** 2) / 1.6)
    return min(1.0, 0.10 + 0.80 * recency + sink)


def build(theme: str) -> str:
    t = THEMES[theme]
    cells = []
    for r in range(ROWS):
        for c in range(COLS):
            a = attention(r, c)
            x = GRID_X + c * (CELL + GAP)
            y = GRID_Y + r * (CELL + GAP)
            if a <= 0.0:
                cells.append(
                    f'<rect x="{x:.0f}" y="{y:.0f}" width="{CELL}" height="{CELL}" '
                    f'rx="2.5" fill="none" stroke="{t["edge"]}" stroke-width="1"/>'
                )
            else:
                cells.append(
                    f'<rect x="{x:.0f}" y="{y:.0f}" width="{CELL}" height="{CELL}" '
                    f'rx="2.5" fill="{t["cell"]}" fill-opacity="{a:.3f}"/>'
                )
    grid = "\n    ".join(cells)

    mono = "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, monospace"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     viewBox="0 0 {W} {H}" role="img"
     aria-label="Ethan Sam — AI Engineer. LLM agents and automation systems that reach production.">
  <rect width="{W}" height="{H}" rx="14" fill="{t["panel"]}"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="13.5"
        fill="none" stroke="{t["edge"]}" stroke-width="1"/>
  <rect x="0" y="0" width="4" height="{H}" rx="2" fill="{t["accent"]}"/>

  <text x="64" y="118" font-family="{mono}" font-size="46" font-weight="600"
        letter-spacing="1.5" fill="{t["ink"]}">Ethan Sam</text>
  <text x="64" y="158" font-family="{mono}" font-size="17" font-weight="500"
        letter-spacing="3.4" fill="{t["accent"]}">AI ENGINEER</text>
  <line x1="64" y1="182" x2="404" y2="182" stroke="{t["edge"]}" stroke-width="1"/>
  <text x="64" y="212" font-family="{mono}" font-size="16" fill="{t["muted"]}">LLM agents and automation systems</text>
  <text x="64" y="236" font-family="{mono}" font-size="16" fill="{t["muted"]}">that reach production — and stay there.</text>

  <g>
    {grid}
  </g>
  <text x="{GRID_X}" y="{H - 34}" font-family="{mono}" font-size="11"
        letter-spacing="1.6" fill="{t["muted"]}">CAUSAL ATTENTION MASK</text>
</svg>
'''


out = Path(__file__).parent
for name in THEMES:
    p = out / f"banner-{name}.svg"
    p.write_text(build(name))
    print(f"wrote {p.name}  ({p.stat().st_size} bytes)")
