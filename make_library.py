#!/usr/bin/env python3
"""Scans the media folders and rewrites library.js. Run it after adding or removing files:
    python3 make_library.py        (Mac)
    py make_library.py             (Windows)
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
KINDS = {
    "photos": ("media/photos", (".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic")),
    "songs":  ("media/songs",  (".mp3", ".m4a", ".aac", ".wav", ".ogg")),
    "clips":  ("media/clips",  (".mp3", ".m4a", ".aac", ".wav", ".ogg")),
    "rain":   ("media/rain",   (".mp3", ".m4a", ".aac", ".wav", ".ogg")),
}

lib = {}
for key, (folder, exts) in KINDS.items():
    path = os.path.join(HERE, *folder.split("/"))
    names = sorted(n for n in os.listdir(path) if n.lower().endswith(exts) and not n.startswith(".")) if os.path.isdir(path) else []
    lib[key] = [folder + "/" + n for n in names]

lines = ["// Written by make_library.py. Run it again after adding or removing files.", "window.BR_LIBRARY = {"]
for i, (key, items) in enumerate(lib.items()):
    body = ",\n".join("    " + json.dumps(p, ensure_ascii=False) for p in items)
    lines.append("  %s: [\n%s\n  ]%s" % (key, body, "," if i < len(lib) - 1 else ""))
lines.append("};")
with open(os.path.join(HERE, "library.js"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print({k: len(v) for k, v in lib.items()})
