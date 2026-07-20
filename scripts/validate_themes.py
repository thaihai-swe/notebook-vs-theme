#!/usr/bin/env python3
"""Validate Note Book theme integrity, coverage, and contrast."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_COLORS = (
    "editor.background",
    "editor.foreground",
    "editor.selectionBackground",
    "editor.lineHighlightBackground",
    "editor.findMatchBackground",
    "editorError.foreground",
    "editorWarning.foreground",
    "editorInfo.foreground",
    "editorGhostText.foreground",
    "editorInlayHint.foreground",
    "editorStickyScroll.background",
    "editorHoverWidget.background",
    "peekViewEditor.background",
    "diffEditor.insertedTextBackground",
    "diffEditor.removedTextBackground",
    "charts.foreground",
    "editorBracketHighlight.foreground1",
    "terminalCursor.foreground",
    "terminal.selectionBackground",
    "focusBorder",
    "button.background",
    "button.hoverBackground",
    "tab.activeBorderTop",
    "tab.hoverBackground",
    "list.hoverBackground",
    "list.activeSelectionBackground",
    "menu.selectionBackground",
    "menubar.selectionBackground",
    "toolbar.hoverBackground",
    "inputOption.activeBackground",
    "editorCursor.foreground",
    "editorCursor.background",
)

REQUIRED_SEMANTIC = (
    "function",
    "method",
    "class",
    "type",
    "parameter",
    "variable",
    "property",
    "string",
    "number",
    "keyword",
    "decorator",
    "comment",
)

THEME_LABELS = {
    "Note Book Dark",
    "Note Book Solarized Light",
    "Note Book Solarized Dark",
    "Note Book Solarized Dark HC",
    "Note Book Rosé Pine Dawn",
    "Note Book Farmhouse",
    "Note Book Parchment",
    "Note Book Sage",
    "Note Book Minimal",
}


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
    blended = (
        fr * alpha + br * (1 - alpha),
        fg * alpha + bg * (1 - alpha),
        fb * alpha + bb * (1 - alpha),
    )
    first, second = luminance(blended), luminance((br, bg, bb))
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def check_settings_presets(root: Path, failures: list[str]) -> None:
    path = root / "vs-code-setting.jsonc"
    if not path.exists():
        failures.append("missing settings preset vs-code-setting.jsonc")
        return
    text = path.read_text()
    for key in (
        "window.autoDetectColorScheme",
        "workbench.preferredLightColorTheme",
        "workbench.preferredDarkColorTheme",
        "workbench.reduceMotion",
        '"workbench.reduceMotion": "user"',
        "custom-ui-style.stylesheet",
        "--nb-border-visible",
        "--nb-border-focus",
        "--nb-surface-input",
        "--nb-ease-soft",
        "--nb-lift-1",
        "--nb-lift-2",
        "@media (prefers-reduced-motion: reduce)",
    ):
        if key not in text:
            failures.append(f"vs-code-setting.jsonc: missing {key}")
    if "nb-ease-bounce" in text:
        failures.append("vs-code-setting.jsonc: bounce easing should be removed")
    if "nb-shimmer 1.5s infinite" in text:
        failures.append("vs-code-setting.jsonc: continuous shimmer animation should be disabled")
    for label in THEME_LABELS:
        if f"[{label}]" not in text:
            failures.append(f"vs-code-setting.jsonc: missing colorCustomizations for {label}")
    if "Note Book Rosé Pine Dawn" not in text or "Note Book Solarized Dark HC" not in text:
        failures.append("vs-code-setting.jsonc: missing preferred theme pair")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    themes_dir = root / "themes"
    package = json.loads((root / "package.json").read_text())
    registered = {Path(entry["path"]).name: entry["label"] for entry in package["contributes"]["themes"]}
    failures: list[str] = []

    if package.get("license") != "MIT":
        failures.append("package.json license must remain MIT")
    if not (root / "LICENSE").exists():
        failures.append("LICENSE file is missing")

    for path in sorted(themes_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            failures.append(f"{path.name}: invalid JSON ({exc})")
            continue
        if path.name not in registered:
            failures.append(f"{path.name}: not registered in package.json")
        colors = data.get("colors", {})
        semantic = data.get("semanticTokenColors", {})
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
        minimum_ratio = 4.5 if path.name == "note-book-solarized-dark.json" else 7.0
        if editor_ratio < minimum_ratio:
            failures.append(f"{path.name}: editor text contrast below {minimum_ratio}:1")
        if terminal_ratio < minimum_ratio:
            failures.append(f"{path.name}: terminal text contrast below {minimum_ratio}:1")
        line = colors.get("editorLineNumber.foreground")
        if line and contrast(line, background) < 3.0:
            failures.append(f"{path.name}: line number contrast below 3:1")
        focus = colors.get("focusBorder")
        if focus and contrast(focus, background) < 3.0:
            failures.append(f"{path.name}: focus border contrast below 3:1")
        for required in REQUIRED_COLORS:
            if required not in colors:
                failures.append(f"{path.name}: missing color key {required}")
        for required in REQUIRED_SEMANTIC:
            if required not in semantic:
                failures.append(f"{path.name}: missing semantic token {required}")

    for name, label in registered.items():
        if not (themes_dir / name).exists():
            failures.append(f"package.json references missing theme file {name} ({label})")

    check_settings_presets(root, failures)

    if failures:
        print("\nVALIDATION FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("\nVALIDATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
