"""Draw the 24 Nov 2026 world-news front page (1024x1024 PNG).

One image, six stories, all verified against reporting published on
24 November 2026 (Reuters/AP/BBC/CNN/TOI/ANI via news search):
  - Jensen Huang reinstated as Nvidia CEO; shares +31% in a day
  - FIDE World Chess Championship Game 1 opens in Geneva
    (Gukesh defends vs Sindarov, youngest-ever title match)
  - Modi and Nepal's PM flag off the Saryu-Kamala Express
  - Russian drone strike hits Dymer, Kyiv region; cargo ship
    Sparta II burns off Finland after a drone attack
  - Rescue goes on after the Cikande factory fire (24 killed)
  - India v New Zealand first Test ends in a draw; Pant hits 128

Layout: navy masthead with the date, then a 2x3 grid of story cards.
Each card has a coloured top strip, a small-caps tag, a bold headline
and one detail line. Drawn with PIL + DejaVu; no AI imagery, so no
garbled text. Output is deterministic: same bytes every run.
"""
from PIL import Image, ImageDraw, ImageFont

CANVAS_W, CANVAS_H = 1024, 1024
PAPER = (250, 249, 246)
NAVY = (13, 38, 68)
GOLD = (198, 162, 60)
INK = (26, 26, 26)
GREY = (92, 98, 106)
RULE = (214, 210, 203)
CARD = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SANS = FONT_DIR + "DejaVuSans.ttf"
SANS_BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(draw, text, font, width):
    """Greedy word wrap returning a list of lines that fit `width`."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = word if not current else current + " " + word
        if draw.textlength(trial, font=font) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


STORIES = [
    ("TECH", (27, 77, 158),
     "Huang returns as Nvidia CEO",
     "Shares jump 31% in a day after reinstatement"),
    ("CHESS", (120, 53, 153),
     "Youngest title match opens",
     "Gukesh defends crown vs Sindarov in Geneva"),
    ("INDIA", (22, 122, 74),
     "New rail link to Nepal",
     "Modi, Nepal PM flag off Saryu-Kamala Express"),
    ("UKRAINE", (178, 34, 34),
     "Drones hit Kyiv region",
     "Strike on Dymer; cargo ship burns off Finland"),
    ("INDONESIA", (146, 90, 16),
     "Cikande fire rescue goes on",
     "24 killed at candy factory; search continues"),
    ("SPORT", (21, 94, 117),
     "Test ends in a draw",
     "Pant's 128 leads India fightback in Wellington"),
]


def draw_masthead(draw):
    draw.rectangle([0, 0, CANVAS_W, 164], fill=NAVY)
    draw.rectangle([0, 164, CANVAS_W, 170], fill=GOLD)
    date_font = load(SANS_BOLD, 66)
    sub_font = load(SANS, 25)
    draw.text((46, 24), "24 NOVEMBER 2026", font=date_font, fill=(255, 255, 255))
    draw.text((48, 106), "The world in one day  \u00b7  Tuesday",
              font=sub_font, fill=(203, 214, 228))


def draw_card(draw, story, x0, y0, w, h):
    tag, accent, headline, detail = story
    draw.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=14,
                           fill=CARD, outline=RULE, width=2)
    draw.rectangle([x0 + 14, y0, x0 + w - 14, y0 + 9], fill=accent)
    pad = 26
    inner = w - 2 * pad
    tag_font = load(SANS_BOLD, 19)
    head_font = load(SANS_BOLD, 32)
    det_font = load(SANS, 21)
    draw.text((x0 + pad, y0 + 26), tag, font=tag_font, fill=accent)
    head_lines = wrap_text(draw, headline, head_font, inner)
    y = y0 + 60
    for line in head_lines[:2]:
        draw.text((x0 + pad, y), line, font=head_font, fill=INK)
        y += 40
    det_lines = wrap_text(draw, detail, det_font, inner)
    y = y0 + h - 26 - 27 * len(det_lines)
    for line in det_lines:
        draw.text((x0 + pad, y), line, font=det_font, fill=GREY)
        y += 27


def main():
    img = Image.new("RGB", (CANVAS_W, CANVAS_H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw)

    grid_x, grid_y = 30, 194
    card_w, card_h = 466, 238
    gap_x, gap_y = 28, 22
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = grid_x + col * (card_w + gap_x)
        y = grid_y + row * (card_h + gap_y)
        draw_card(draw, story, x, y, card_w, card_h)

    foot_font = load(SANS, 18)
    draw.text((30, CANVAS_H - 32),
              "Sources: Reuters  \u00b7  AP  \u00b7  BBC  \u00b7  CNN  \u00b7  Times of India  \u00b7  ANI",
              font=foot_font, fill=GREY)

    out = "/home/hatch/workspace/makefun/news-image-24/entry.png"
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    main()
