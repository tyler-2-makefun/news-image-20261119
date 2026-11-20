#!/usr/bin/env python3
"""19 November 2026 — The World in One Image.

Generates a deterministic 1024x1024 PNG infographic summarising six major
world-news stories from Thursday 19 November 2026.

Determinism: every input is a literal in this file (fixed text, fixed
colours, fixed layout). There is no randomness, no current time, no network
access and no external data at runtime, so repeated runs produce a
byte-identical PNG.

Usage:
    python3 main.py            # writes output.png in the current directory
    python3 main.py out.png    # writes to a custom path

Requires: Pillow (pip install pillow). Runs on Python 3.12+ / 3.13.
"""

import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Layout constants (fixed)
# ---------------------------------------------------------------------------
W, H = 1024, 1024
BG = (13, 27, 46)          # deep navy
PANEL = (24, 44, 71)       # card background
PANEL_EDGE = (52, 92, 140)  # card border
WHITE = (245, 247, 250)
MUTED = (168, 184, 205)
GOLD = (232, 184, 84)

FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:  # pragma: no cover - fallback if DejaVu is absent
        return ImageFont.load_default()


# ---------------------------------------------------------------------------
# The news — six stories from 19 November 2026 (see NOTES.md for sources).
# Headlines are kept short on purpose so they fit the cards; the detail
# line adds the one fact that matters. Wording stays within what the
# cited reporting actually said (e.g. "claims" where damage is claimed).
# ---------------------------------------------------------------------------
STORIES = [
    {
        "tag": "JUSTICE",
        "color": (84, 160, 232),
        "headline": "ICJ: Myanmar committed genocide",
        "detail": "The UN court finds Myanmar's military acted with genocidal intent against the Rohingya in 2017.",
    },
    {
        "tag": "DIPLOMACY",
        "color": (232, 110, 84),
        "headline": "Trump, Xi, Putin meet in Shenzhen",
        "detail": "First-ever trilateral summit issues a four-point 'Declaration toward Peace' and pledges more talks on nuclear risks.",
    },
    {
        "tag": "MIDDLE EAST",
        "color": (245, 196, 66),
        "headline": "Hormuz tanker attack injures 11",
        "detail": "An ADNOC Logistics vessel is hit in the Strait of Hormuz, 11 crew injured and one missing, as US-Iran strikes escalate.",
    },
    {
        "tag": "CLIMATE",
        "color": (120, 200, 140),
        "headline": "COP31 ministers race to unblock talks",
        "detail": "Ministers meet in informal session in Antalya, Turkey, to bridge differences and adopt a final climate text.",
    },
    {
        "tag": "EUROPE",
        "color": (160, 140, 232),
        "headline": "EU proposes EUR 45bn loan for Ukraine",
        "detail": "The European Commission proposes a new 45-billion-euro loan; Kyiv is hit again and Crimea bridge traffic is suspended.",
    },
    {
        "tag": "AFRICA",
        "color": (232, 150, 200),
        "headline": "Migrant boat sinks off Senegal",
        "detail": "A wooden boat carrying about 100 migrants strikes a rocky outcrop and capsizes overnight; dozens are missing.",
    },
]

SOURCES_LINE = "Sources: ICJ  •  AP  •  AFP  •  Al Jazeera  •  Le Monde  •  Reuters"


def wrap(draw, text, font_obj, max_width):
    """Word-wrap `text` to fit `max_width` pixels; returns list of lines."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        cur = ""
        for word in words:
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=font_obj) <= max_width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


def draw_card(draw, x, y, w, h, story, index):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14,
                           fill=PANEL, outline=PANEL_EDGE, width=2)
    # Number badge
    badge_r = 17
    cx, cy = x + 30, y + 30
    draw.ellipse([cx - badge_r, cy - badge_r, cx + badge_r, cy + badge_r],
                 fill=story["color"])
    num_font = font(FONT_BOLD, 20)
    num = str(index + 1)
    tw = draw.textlength(num, font=num_font)
    draw.text((cx - tw / 2, cy - 13), num, font=num_font, fill=BG)

    # Tag chip (text only, in the story colour)
    tag_font = font(FONT_BOLD, 19)
    draw.text((x + 58, y + 19), story["tag"], font=tag_font,
              fill=story["color"])

    # Headline (bold, up to 2 lines)
    head_font = font(FONT_BOLD, 27)
    lines = wrap(draw, story["headline"], head_font, w - 40)
    ly = y + 62
    for line in lines[:2]:
        draw.text((x + 20, ly), line, font=head_font, fill=WHITE)
        ly += 34

    # Detail (regular, up to 3 lines)
    det_font = font(FONT_REG, 20)
    dlines = wrap(draw, story["detail"], det_font, w - 40)
    dy = ly + 8
    for line in dlines[:3]:
        draw.text((x + 20, dy), line, font=det_font, fill=MUTED)
        dy += 27


def build() -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Header
    draw.text((48, 36), "THE WORLD IN ONE IMAGE",
              font=font(FONT_BOLD, 26), fill=GOLD)
    draw.text((48, 68), "19 November 2026",
              font=font(FONT_BOLD, 64), fill=WHITE)
    draw.text((48, 142), "Six stories that shaped the day",
              font=font(FONT_REG, 26), fill=MUTED)
    draw.line([(48, 186), (976, 186)], fill=PANEL_EDGE, width=2)

    # 2 x 3 grid of cards
    margin, gap = 48, 20
    card_w = (W - 2 * margin - gap) // 2
    card_h = 216
    top = 208
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = margin + col * (card_w + gap)
        y = top + row * (card_h + gap)
        draw_card(draw, x, y, card_w, card_h, story, i)

    # Footer
    fy = top + 3 * card_h + 2 * gap + 18
    draw.line([(48, fy), (976, fy)], fill=PANEL_EDGE, width=2)
    foot_font = font(FONT_REG, 19)
    draw.text((48, fy + 16), SOURCES_LINE, font=foot_font, fill=MUTED)
    draw.text((48, fy + 44), "Infographic generated deterministically by main.py — no live data at runtime.",
              font=foot_font, fill=MUTED)
    return img


def main(argv):
    out = Path(argv[1]) if len(argv) > 1 else Path("output.png")
    img = build()
    img.save(out, format="PNG", compress_level=9)
    print(f"Wrote {out} ({img.width}x{img.height}, {out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
