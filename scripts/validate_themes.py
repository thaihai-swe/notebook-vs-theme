#!/usr/bin/env python3
"""Validate theme JSON files and basic WCAG contrast targets."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def parse_hex(value: str) -> tuple[float, float, float, float]:
    raw = value.strip().lstrip("#")
    if len(raw) == 3:
        raw = "".join(ch * 2 for ch in raw)
        alpha = 1.0
    elif len(raw) == 4:
        alpha = int(raw[3] * 2, 16) / 255
        raw = "".join(ch * 2 for ch in raw[:3])
    elif len(raw) == 6:
        alpha = 1.0
    elif len(raw) == 8:
        alpha = int(raw[6:8], 16) / 255
        raw = raw[:6]
    else:
        raise ValueError(f"unsupported color: {value}")
    return tuple(int(raw[i:i + 2], 16) / 255 for i in (0, 2, 4)) + (alpha,)


def luminance(rgb: tuple[float, float, float]) -> float:
    def channel(value: float) -> float:
        return value / 12.92 if value <= 0.03928 else ((value + 0.055) / 1.055) ** 2.4

    r, g, b = map(channel, rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(foreground: str, background: str) -> float:
    fr, fg, fb, alpha = parse_hex(foreground)
    br, bg, bb, _ = parse_hex(background)
    blended = (fr * alpha + br * (1 - alpha), fg * alpha + bg * (1 - alpha), fb * alpha + bb * (1 - alpha))
    first, second = luminance(blended), luminance((br, bg, bb))
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    themes_dir = root / "themes"
    package = json.loads((root / "package.json").read_text())
    registered = {Path(entry["path"]).name for entry in package["contributes"]["themes"]}
    failures: list[str] = []

    for path in sorted(themes_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            failures.append(f"{path.name}: invalid JSON ({exc})")
            continue
        if path.name not in registered:
            failures.append(f"{path.name}: not registered in package.json")
        colors = data.get("colors", {})
        background = colors.get("editor.background")
        foreground = colors.get("editor.foreground")
        terminal_background = colors.get("terminal.background", background)
        terminal_foreground = colors.get("terminal.foreground", foreground)
        if not background or not foreground:
            failures.append(f"{path.name}: missing editor background/foreground")
            continue
        editor_ratio = contrast(foreground, background)
        terminal_ratio = contrast(terminal_foreground, terminal_background)
        print(f"{path.name}: editor {editor_ratio:.2f}:1, terminal {terminal_ratio:.2f}:1")
        if editor_ratio < 4.5:
            failures.append(f"{path.name}: editor text contrast below 4.5:1")
        if terminal_ratio < 4.5:
            failures.append(f"{path.name}: terminal text contrast below 4.5:1")
        for required in ("editor.selectionBackground", "editor.lineHighlightBackground", "editor.findMatchBackground", "editorError.foreground", "editorWarning.foreground", "editorInfo.foreground"):
            if required not in colors:
                failures.append(f"{path.name}: missing color key {required}")

    for name in registered:
        if not (themes_dir / name).exists():
            failures.append(f"package.json references missing theme file {name}")

    if failures:
        print("\nVALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("\nVALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
