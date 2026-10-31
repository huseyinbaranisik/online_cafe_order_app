"""Renders the README figures in assets/: cover.png, demo.gif, screens.png.

usage:
  python tools/capture_app.py shots        # drives the real app hidden (PyQt5), saves shots/ and shots/frames/
  python tools/render_figures.py shots
Needs Pillow. Fonts (OFL) in tools/fonts/: Baloo 2 and Quicksand. Colours are sampled from the app's own screens.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "tools", "fonts")
OUT = os.path.join(ROOT, "assets")

# Sampled from the app: tan background, coffee-brown cards and buttons.
TAN, COFFEE = "#DBA67A", "#7B524C"
CREAM, PAPER, INK, SUB, LINE = "#F6E7D6", "#FBF4EC", "#4A2F2B", "#8A6A62", "#EBD9C6"

def font(name, size, weight):
    f = ImageFont.truetype(os.path.join(FONTS, name), size)
    f.set_variation_by_axes([weight])
    return f

DISPLAY = lambda s: font("Baloo2.ttf", s, 800)
ROUND = lambda s: font("Baloo2.ttf", s, 600)
BODY = lambda s: font("Quicksand.ttf", s, 500)
BODY_B = lambda s: font("Quicksand.ttf", s, 700)

def wrap(d, text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    return lines + [cur]

def glow(im, xy, r, rgb, alpha):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse([xy[0] - r, xy[1] - r, xy[0] + r, xy[1] + r], fill=rgb + (alpha,))
    im.alpha_composite(layer.filter(ImageFilter.GaussianBlur(r // 2)))

def shadow(im, box, r, offset=16, blur=24, alpha=80):
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    x0, y0, x1, y1 = box
    ImageDraw.Draw(layer).rounded_rectangle([x0, y0 + offset, x1, y1 + offset], r, fill=(74, 47, 43, alpha))
    im.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))

def window(im, xy, shot, width, title="Hoşgeldiniz"):
    """Windows 11 style window (light title bar) around a real screenshot of the Qt app."""
    x0, y0 = xy
    s = shot.convert("RGB").resize((width, int(width * shot.height / shot.width)), Image.LANCZOS)
    bar = 40
    box = (x0, y0, x0 + width + 4, y0 + bar + s.height + 2)
    shadow(im, box, 10)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, 10, fill="#F3F3F3", outline="#D6CCC2", width=2)
    d.text((x0 + 16, y0 + 9), title, font=BODY_B(17), fill="#333333")
    bx, by = x0 + width - 96, y0 + bar // 2
    d.line([(bx, by), (bx + 12, by)], fill="#555555", width=2)
    d.rectangle([bx + 34, by - 6, bx + 46, by + 6], outline="#555555", width=2)
    d.line([(bx + 70, by - 6), (bx + 82, by + 6)], fill="#555555", width=2)
    d.line([(bx + 70, by + 6), (bx + 82, by - 6)], fill="#555555", width=2)
    im.paste(s, (x0 + 2, y0 + bar))
    return box

def pill(d, xy, text, f, fill, color, pad=(18, 8)):
    x, y = xy
    w = d.textlength(text, font=f)
    h = f.size + 2 * pad[1]
    d.rounded_rectangle([x, y, x + w + 2 * pad[0], y + h], h // 2, fill=fill)
    d.text((x + pad[0], y + pad[1] - 3), text, font=f, fill=color)
    return x + w + 2 * pad[0]

def cover(shots):
    W, H = 1800, 960
    im = Image.new("RGBA", (W, H), PAPER)
    glow(im, (1420, 300), 520, (219, 166, 122), 120)
    glow(im, (300, 980), 360, (219, 166, 122), 70)
    d = ImageDraw.Draw(im)
    x, nx = 100, 100
    for t in ["Python", "PyQt5", "SQLite"]:
        nx = pill(d, (nx, 130), t, ROUND(22), COFFEE, CREAM) + 10
    d.text((x - 4, 186), "Gloo-ffee", font=DISPLAY(124), fill=COFFEE)
    d.text((x, 346), "Bakery sales & staff automation", font=ROUND(38), fill=INK)
    d.text((x, 400), "Pastane Satış ve Yönetim Otomasyonu", font=BODY_B(26), fill=SUB)
    y = 470
    for line in wrap(d, "A desktop app for a small bakery: customers log in and fill a cart, the till "
                        "shows a payment QR code, and every sale adds a 5 % bonus to the staff member "
                        "who made it.", BODY(26), 620):
        d.text((x, y), line, font=BODY(26), fill=INK); y += 40
    d.text((x, y + 28), "Programlamaya Giriş 2  ·  Hüseyin Baran Işık", font=BODY_B(20), fill=SUB)

    window(im, (1080, 70), shots["shop_filled"], 400)
    window(im, (1340, 240), shots["staff"], 360, title="Yönetici")
    return im.convert("RGB")

def demo(shots_dir):
    frames_dir = os.path.join(shots_dir, "frames")
    files = sorted(f for f in os.listdir(frames_dir) if f.endswith(".png"))
    w = 472
    probe = Image.open(os.path.join(frames_dir, files[0]))
    h = int(w * probe.height / probe.width)
    W, H = w + 4 + 120, h + 40 + 2 + 140
    base = Image.new("RGBA", (W, H), PAPER)  # flat: soft gradients band in a GIF palette
    d = ImageDraw.Draw(base)
    nx = pill(d, (60, 34), "Fig. 2", ROUND(20), COFFEE, CREAM)
    d.text((nx + 14, 30), "Real run", font=ROUND(30), fill=INK)
    frame_box = window(base, (60, 100), probe, w)
    base = base.convert("RGB")
    out = []
    for f in files:
        p = base.copy()
        p.paste(Image.open(os.path.join(frames_dir, f)).convert("RGB").resize((w, h), Image.LANCZOS), (frame_box[0] + 2, frame_box[1] + 40))
        out.append(p.quantize(colors=192, method=Image.Quantize.FASTOCTREE))
    out[0].save(os.path.join(OUT, "demo.gif"), save_all=True, append_images=out[1:] + [out[-1]] * 12,
                duration=110, loop=0, optimize=True)

def screens(shots):
    """Fig. 3: the six main screens, as the app draws them."""
    items = [("welcome", "Welcome"), ("shop", "Shop"), ("shop_filled", "Products added"),
             ("cart", "Cart"), ("qr", "Payment QR"), ("staff", "Staff bonuses")]
    tw = 250
    th = int(tw * shots["welcome"].height / shots["welcome"].width)
    W = 70 * 2 + len(items) * tw + (len(items) - 1) * 22
    H = 120 + th + 80
    im = Image.new("RGBA", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    nx = pill(d, (70, 36), "Fig. 3", ROUND(20), COFFEE, CREAM)
    d.text((nx + 14, 32), "The six main screens", font=ROUND(30), fill=INK)
    for i, (key, label) in enumerate(items):
        x0, y0 = 70 + i * (tw + 22), 110
        shadow(im, (x0, y0, x0 + tw, y0 + th), 12, offset=8, blur=12, alpha=60)
        d = ImageDraw.Draw(im)
        s = shots[key].convert("RGB").resize((tw, th), Image.LANCZOS)
        mask = Image.new("L", s.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, tw - 1, th - 1], 12, fill=255)
        im.paste(s, (x0, y0), mask)
        d.text((x0 + 4, y0 + th + 14), label, font=BODY_B(22), fill=INK)
    return im.convert("RGB")

if __name__ == "__main__":
    shots_dir = sys.argv[1]
    shots = {n: Image.open(os.path.join(shots_dir, f"{n}.png")) for n in ["welcome", "shop", "shop_filled", "cart", "qr", "staff"]}
    cover(shots).save(os.path.join(OUT, "cover.png"), optimize=True)
    demo(shots_dir)
    screens(shots).save(os.path.join(OUT, "screens.png"), optimize=True)
    print("figures ->", OUT)
