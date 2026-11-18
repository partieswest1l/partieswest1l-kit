"""Sort files in a directory into subfolders by extension."""
from __future__ import annotations

import shutil
from pathlib import Path

VERSION = "0.9.2"

CATEGORIES = {
    "images": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"},
    "docs": {".pdf", ".txt", ".md", ".docx", ".odt"},
    "audio": {".mp3", ".wav", ".flac", ".ogg"},
    "video": {".mp4", ".mkv", ".mov", ".webm"},
    "archives": {".zip", ".tar", ".gz", ".7z", ".rar"},
}


class Partieswest1lTool:
    """Move files into per-category folders."""

    def __init__(self, root):
        self.root = Path(root)

    def category_of(self, path):
        ext = Path(path).suffix.lower()
        for name, exts in CATEGORIES.items():
            if ext in exts:
                return name
        return "other"

    def plan(self):
        if not self.root.is_dir():
            raise NotADirectoryError(str(self.root))
        return [(p.name, self.category_of(p))
                for p in sorted(self.root.iterdir()) if p.is_file()]

    def apply(self):
        moved = []
        for name, folder in self.plan():
            target = self.root / folder
            target.mkdir(exist_ok=True)
            shutil.move(str(self.root / name), str(target / name))
            moved.append((name, folder))
        return moved
