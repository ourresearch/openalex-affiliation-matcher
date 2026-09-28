"""Draw the README's charts as static SVGs.

    python3 docs/charts/make_charts.py

Every number is typed in below or read from institution_change_quantiles.json; the README's tables carry the
same numbers, so the charts can be checked against them.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent / "img"

# One version per chart that reads on GitHub's light (#ffffff) and dark (#0d1117) pages alike: a <picture> with a
# dark variant follows the operating system, not the GitHub theme, and can put light text on a light page.
# Text #707a84 is 4.4:1 on both; the bar colors are mid-tones that clear 3:1 on both.
THEME = dict(ink="#707a84", ink2="#707a84", grid="#8b949e", zero="#8b949e",
             old="#888780", new="#2a78d6", ror="#199e70", bad="#d95926", neutral="#8f8e88",
             on_new="#ffffff", on_bad="#0b0b0b", on_neutral="#0b0b0b")
FONT = ('-apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif')


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Svg:
    def __init__(self, w, h, title):
        self.w, self.h, self.parts = w, h, []
        self.title = title

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, fill, size=14, anchor="start", weight=400):
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" fill="{fill}" font-size="{size}" font-weight="{weight}" '
                 f'text-anchor="{anchor}" dominant-baseline="middle">{esc(s)}</text>')

    def line(self, x1, y1, x2, y2, stroke, width=1, opacity=0.35):
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
                 f'stroke-width="{width}" stroke-opacity="{opacity}"/>')

    def save(self, path):
        body = "\n".join(self.parts)
        path.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
            f'role="img" font-family=\'{FONT}\' style="font-variant-numeric: tabular-nums">\n'
            f'<title>{esc(self.title)}</title>\n{body}\n</svg>\n')


def hbar(x0, y, w, h, r=4):
    """Bar from the baseline x0, square at the baseline, rounded at the data end."""
    if w < 0.5:
        return ""
    r = min(r, w / 2, h / 2)
    return (f"M{x0:.1f},{y:.1f} H{x0 + w - r:.1f} Q{x0 + w:.1f},{y:.1f} {x0 + w:.1f},{y + r:.1f} "
            f"V{y + h - r:.1f} Q{x0 + w:.1f},{y + h:.1f} {x0 + w - r:.1f},{y + h:.1f} H{x0:.1f} Z")


def legend(s, x, y, items, t):
    for label, color in items:
        s.add(f'<rect x="{x}" y="{y - 6}" width="12" height="12" rx="2" fill="{color}"/>')
        s.text(x + 18, y, label, t["ink"], 14)
        x += 18 + len(label) * 7.6 + 26


def benchmarks(t):
    """Exact match on each benchmark: grouped horizontal bars, three systems."""
    rows = [
        ("Random OpenAlex strings", "3,000, our labels", [72.7, 89.4, 63.3]),
        ("Crossref 2024", "3,000, ROR's evaluation set", [80.6, 91.3, 68.7]),
        ("Springer Nature 2023", "2,999", [73.5, 91.4, 70.0]),
        ("CWTS", "952, most name 2+ institutions", [47.6, 72.1, 0.4]),
    ]
    series = [("2023 system", t["old"]), ("New matcher", t["new"]), ("ROR's matcher", t["ror"])]
    W, L, R, bh, gap, pad = 720, 230, 56, 14, 4, 26
    top = 62
    rowH = 3 * bh + 2 * gap + pad
    H = top + len(rows) * rowH + 4
    s = Svg(W, H, "Exact match on four benchmarks: 2023 system, new matcher, ROR's matcher")
    x = lambda v: L + v / 100 * (W - L - R)
    legend(s, L, 14, series, t)
    for tick in (0, 25, 50, 75, 100):
        s.line(x(tick), top - 12, x(tick), H - 4, t["grid"], opacity=0.8 if tick == 0 else 0.35)
        s.text(x(tick), top - 22, f"{tick}%", t["ink2"], 12, "middle")
    for i, (label, sub, vals) in enumerate(rows):
        y0 = top + i * rowH + pad / 2
        cy = y0 + (3 * bh + 2 * gap) / 2
        s.text(0, cy - 9, label, t["ink"], 15, weight=600)
        s.text(0, cy + 10, sub, t["ink2"], 12.5)
        for j, v in enumerate(vals):
            y = y0 + j * (bh + gap)
            s.add(f'<path d="{hbar(x(0), y, x(v) - x(0), bh)}" fill="{series[j][1]}"/>')
            s.text(x(v) + 6, y + bh / 2, f"{v:.1f}", t["ink"] if j == 1 else t["ink2"], 13, weight=600 if j == 1 else 400)
    return s


def verdicts(t):
    """Blind judge on 300 changed strings: one 100% stacked bar."""
    parts = [("New answer better", 80.5, t["new"], t["on_new"]),
             ("Old answer better", 11.2, t["bad"], t["on_bad"]),
             ("Both wrong", 8.3, t["neutral"], t["on_neutral"])]
    W, H, bar_y, bh = 720, 86, 12, 34
    s = Svg(W, H, "Blind judge on 300 changed strings: new answer better 81%, old better 11%, both wrong 8%")
    x = 0.0
    for k, (label, v, color, on) in enumerate(parts):
        w = v / 100 * W
        gw = w if k == len(parts) - 1 else w - 2
        if k == len(parts) - 1:
            s.add(f'<path d="{hbar(x, bar_y, gw, bh)}" fill="{color}"/>')
        else:
            s.add(f'<rect x="{x:.1f}" y="{bar_y}" width="{gw:.1f}" height="{bh}" fill="{color}"/>')
        s.text(x + 8, bar_y + bh / 2, f"{int(v + 0.5)}%", on, 15, weight=600)
        x += w
    legend(s, 0, H - 16, [(p[0], p[2]) for p in parts], t)
    return s


def institutions(t):
    """Change in works per institution, sorted: one line."""
    P = json.loads((HERE / "institution_change_quantiles.json").read_text())
    pts = P["points"]
    W, H, L, R, T, B = 720, 330, 54, 16, 16, 50
    s = Svg(W, H, "Change in works per institution, 27,820 institutions sorted from biggest loss to biggest gain")
    clip = lambda v: max(-100, min(100, v))
    x = lambda p: L + p / 100 * (W - L - R)
    y = lambda v: T + (100 - clip(v)) / 200 * (H - T - B)
    for tick in (-100, -50, 0, 50, 100):
        s.line(L, y(tick), W - R, y(tick), t["grid"], opacity=0.8 if tick == 0 else 0.35)
        lab = ("+" if tick > 0 else "−" if tick < 0 else "") + f"{abs(tick)}%"
        s.text(L - 8, y(tick), lab, t["ink2"], 12, "end")
    for tick in (0, 25, 50, 75, 100):
        s.text(x(tick), H - B + 16, f"{tick}%", t["ink2"], 12, "middle")
    s.text(L + (W - L - R) / 2, H - 12, "institutions, sorted from biggest loss to biggest gain", t["ink2"], 13, "middle")
    d = "M" + " L".join(f"{x(p):.1f},{y(v):.1f}" for p, v in pts)
    s.add(f'<path d="{d}" fill="none" stroke="{t["new"]}" stroke-width="2" stroke-linejoin="round"/>')
    lost = P["share_losing_pct"]
    s.add(f'<circle cx="{x(lost):.1f}" cy="{y(0):.1f}" r="5" fill="{t["new"]}" stroke="{t["ink"]}" stroke-opacity="0" />')
    s.text(x(lost) - 10, y(0) - 16, f"{lost}% of institutions lose works", t["ink"], 14, "end", 600)
    med = min(pts, key=lambda p: abs(p[0] - 50))
    s.add(f'<circle cx="{x(50):.1f}" cy="{y(med[1]):.1f}" r="4" fill="{t["new"]}"/>')
    s.text(x(50) + 10, y(med[1]) + 16, f"median {med[1]:+.0f}%".replace("-", "−"), t["ink2"], 13)
    s.text(L + 8, y(100) + 12, "gains above +100% drawn at +100%", t["ink2"], 12)
    return s


def hero(title, sub, values):
    """One benchmark, three systems: a column each on a 0-100% scale, value above, name below (the dashboard's form)."""
    def draw(t):
        items = [("2023 system", values[0], t["old"]), ("New matcher", values[1], t["new"]),
                 ("ROR's matcher", values[2], t["ror"])]
        W, H, L, R, T, B = 440, 330, 44, 8, 84, 34
        s = Svg(W, H, f"{title}, {sub}: exact match, 2023 system {values[0]}%, new matcher {values[1]}%, "
                      f"ROR's matcher {values[2]}%")
        s.text(0, 16, title, t["ink"], 18, weight=650)
        s.text(0, 40, sub, t["ink2"], 14)
        y = lambda v: T + (1 - v / 100) * (H - T - B)
        for tick in (0, 25, 50, 75, 100):
            s.line(L, y(tick), W - R, y(tick), t["grid"], opacity=0.8 if tick == 0 else 0.35)
            s.text(L - 8, y(tick), f"{tick}%", t["ink2"], 12, "end")
        gw = (W - L - R) / 3
        cw = 72
        for i, (label, v, color) in enumerate(items):
            cx = L + gw * i + gw / 2
            x0, top, r = cx - cw / 2, y(v), 4
            s.add(f'<path d="M{x0:.1f},{y(0):.1f} V{top + r:.1f} Q{x0:.1f},{top:.1f} {x0 + r:.1f},{top:.1f} '
                  f'H{x0 + cw - r:.1f} Q{x0 + cw:.1f},{top:.1f} {x0 + cw:.1f},{top + r:.1f} V{y(0):.1f} Z" fill="{color}"/>')
            s.text(cx, top - 14, f"{v:.1f}%", t["ink"], 20 if i == 1 else 17, "middle", 700 if i == 1 else 500)
            s.text(cx, H - B + 18, label, t["ink"], 14, "middle", 600 if i == 1 else 400)
        return s
    return draw


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    charts = (
        ("benchmark-ours", hero("Our benchmark", "3,000 random OpenAlex strings", [72.7, 89.4, 63.3])),
        ("benchmark-external", hero("External benchmarks", "6,951 strings, three sets pooled", [73.0, 88.7, 59.9])),
        ("benchmarks-by-set", benchmarks), ("verdicts", verdicts), ("institutions", institutions),
    )
    for name, fn in charts:
        fn(THEME).save(OUT / f"{name}.svg")
        print(OUT / f"{name}.svg")
