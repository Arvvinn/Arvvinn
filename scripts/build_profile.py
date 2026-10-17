"""Render self-hosted profile SVGs using public GitHub repository metadata only."""

import json
import os
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OWNER = "Arvvinn"
BG, PANEL, LINE = "#0b1020", "#111a2d", "#253149"
WHITE, MUTED, CYAN, PURPLE = "#edf3ff", "#91a1bc", "#67e8f9", "#b69cff"
FONT = "Segoe UI, Arial, sans-serif"
MONO = "Consolas, monospace"


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Arvvinn-profile"}
    if os.environ.get("GH_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
    with urlopen(Request("https://api.github.com/" + path, headers=headers), timeout=30) as response:
        return json.load(response)


def text(x, y, value, size=16, color=WHITE, weight="400", font=FONT, extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{font}" font-size="{size}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'


def rect(x, y, w, h, fill=PANEL, radius=16, stroke=LINE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def svg(name, w, h, body, title):
    ASSETS.mkdir(exist_ok=True)
    output = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title">
<title id="title">{escape(title)}</title>
<defs><linearGradient id="accent"><stop stop-color="{CYAN}"/><stop offset="1" stop-color="{PURPLE}"/></linearGradient><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#27324b" stroke-opacity=".32"/></pattern></defs>
{body}</svg>'''
    (ASSETS / name).write_text(output, encoding="utf-8")


def hero():
    b = rect(1, 1, 1198, 408, BG, 24)
    b += '<rect x="1" y="1" width="1198" height="408" rx="24" fill="url(#grid)"/>'
    b += '<path d="M32 1H1168" stroke="url(#accent)" stroke-width="3"/>'
    b += text(46, 48, "ARVVINN / PERSONAL ENGINEERING SPACE", 13, MUTED, font=MONO, extra='letter-spacing="2"')
    b += '<circle cx="1114" cy="43" r="4" fill="#6ee7b7"/>' + text(1126, 48, "BUILD", 11, "#6ee7b7", font=MONO)
    b += text(44, 152, "Asuka", 92, WHITE, "700", extra='letter-spacing="-4"')
    b += text(48, 196, "Exploring agents.", 30, CYAN, "600")
    b += text(48, 239, "Building across the stack.", 30, WHITE, "600")
    b += text(48, 285, "AI AGENTS  /  FULL STACK  /  SMART HARDWARE", 13, MUTED, font=MONO)
    b += '<path d="M48 320H642" stroke="#253149"/>'
    b += text(48, 359, "HENAN UNIVERSITY", 12, MUTED, font=MONO, extra='letter-spacing="2"')
    b += text(365, 359, "CHINA  ·  @ARVVINN", 12, MUTED, font=MONO)
    b += '<g transform="translate(768 106)"><circle cx="142" cy="110" r="108" fill="none" stroke="#263853"/><circle cx="142" cy="110" r="74" fill="none" stroke="#263853" stroke-dasharray="4 8"/><path d="M34 110H250M142 2V218" stroke="#263853"/><circle cx="142" cy="2" r="5" fill="#b69cff"/><circle cx="250" cy="110" r="5" fill="#67e8f9"/><circle cx="142" cy="218" r="5" fill="#b69cff"/>'
    b += rect(73, 67, 138, 86, "#131e33", 18, CYAN)
    b += text(91, 119, "{ build }", 22, CYAN, "600", MONO) + '</g>'
    b += text(836, 363, "IDEA → CODE → SYSTEM", 12, MUTED, font=MONO)
    svg("hero.svg", 1200, 410, b, "Asuka / Arvvinn — Exploring agents. Building across the stack.")


def projects():
    rows = [
        ("foodglass", "01 / WEARABLE AI", "ZeroSense", "FoodGlass", "From firmware to frontend.", CYAN, "sensor → vision → insight"),
        ("harness", "02 / AGENT INTERNALS", "Harness", "Lab", "Trace the loop. Replay the decisions.", PURPLE, "context → model → tool → trace"),
        ("monitor", "03 / AUTOMATION", "Course", "Monitor", "A small tool for a real problem.", "#6ee7b7", "observe → detect → notify"),
        ("voicelog", "04 / INTERACTIVE UI", "VoiceLog", "声迹", "Explore the moments behind the audio.", "#f9b97c", "timeline → people → connections"),
    ]
    for slug, label, first, second, description, color, flow in rows:
        b = rect(1, 1, 558, 238, BG, 18)
        b += f'<path d="M26 1H534" stroke="{color}" stroke-width="2"/>'
        b += text(26, 35, label, 11, color, font=MONO, extra='letter-spacing="1.4"')
        b += text(25, 92, first, 37, WHITE, "700", extra='letter-spacing="-1"')
        b += text(25, 135, second, 37, WHITE, "700", extra='letter-spacing="-1"')
        b += text(27, 173, description, 14, MUTED)
        b += text(27, 213, flow, 12, color, font=MONO)
        if slug == "foodglass":
            b += '<g fill="none" stroke="#67e8f9" stroke-width="3"><rect x="405" y="81" width="48" height="35" rx="13"/><rect x="469" y="81" width="48" height="35" rx="13"/><path d="M453 93Q461 85 469 93M405 91L394 80M517 91L528 80"/></g>'
        elif slug == "harness":
            b += '<path d="M410 105H441L453 82L472 127L486 105H525" fill="none" stroke="#b69cff" stroke-width="3"/>'
        elif slug == "monitor":
            b += '<path d="M406 122H521M414 114V99M434 114V78M454 114V88M474 114V63M494 114V53M514 114V38" fill="none" stroke="#6ee7b7" stroke-width="5"/>'
        else:
            b += '<g stroke="#f9b97c" stroke-width="3" stroke-linecap="round"><path d="M413 90V111M427 74V126M441 58V141M455 80V120M469 69V132M483 86V114M497 61V139M511 82V118"/></g>'
        svg(f"project-{slug}.svg", 560, 240, b, first + " " + second + " — " + description)


def signals():
    repos = []
    for page in range(1, 101):
        batch = api(f"users/{OWNER}/repos?type=owner&per_page=100&page={page}")
        repos.extend(r for r in batch if not r.get("private") and not r["fork"])
        if len(batch) < 100:
            break
    user = api(f"users/{OWNER}")
    languages = Counter(r["language"] for r in repos if r.get("language"))
    stats = [(len(repos), "PUBLIC REPOS"), (sum(r["stargazers_count"] for r in repos), "STARS EARNED"), (len(languages), "PRIMARY LANGUAGES"), (user["followers"], "FOLLOWERS")]
    b = rect(1, 1, 1198, 312, BG, 20)
    b += text(30, 37, "PUBLIC FOOTPRINT", 12, CYAN, font=MONO, extra='letter-spacing="2"')
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    b += text(1168, 37, stamp, 11, MUTED, font=MONO, extra='text-anchor="end"')
    for i, (value, label) in enumerate(stats):
        x = 30 + i * 290
        b += rect(x, 62, 270, 110)
        b += text(x + 20, 117, value, 38, WHITE, "600")
        b += text(x + 20, 147, label, 10, MUTED, font=MONO, extra='letter-spacing="1"')
    b += text(30, 210, "PRIMARY LANGUAGE / REPOSITORY COUNT", 11, MUTED, font=MONO)
    colors = {"TypeScript": PURPLE, "Vue": "#6ee7b7", "JavaScript": "#f9d477", "Python": CYAN}
    x, total = 30, sum(languages.values())
    for i, (name, count) in enumerate(sorted(languages.items(), key=lambda item: (-item[1], item[0]))):
        color = colors.get(name, "#f9b97c")
        width = 1140 * count / max(total, 1)
        b += rect(round(x, 2), 229, round(max(width - 4, 1), 2), 11, color, 3, color)
        x += width
        lx = 30 + i * 210
        b += f'<circle cx="{lx+4}" cy="270" r="4" fill="{color}"/>'
        b += text(lx + 17, 275, f"{name} · {count}", 12, MUTED)
    svg("signals.svg", 1200, 314, b, "Public GitHub statistics — " + ", ".join(f"{value} {label.lower()}" for value, label in stats))


if __name__ == "__main__":
    hero()
    projects()
    signals()
    print("Rendered hero, four project cards and public GitHub signals.")
