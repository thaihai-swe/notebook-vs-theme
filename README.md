# Note Book Theme & VS Code Settings Redesign

A Solarized and Rosé Pine-inspired suite for VS Code, redesigned for long coding sessions with restrained, readable interaction states and predictable workspace ergonomics.

## What changed in the redesign

- **Unified state coverage across all 8 themes:** normalized colors for lists, trees, tabs, inputs, command palette, notebooks, diffs, SCM, chat, and testing.
- **Distinct list states:** clear visual separation between focused items, active selection, and hover rows.
- **Restrained microinteractions:** static cursor and focus outlines; no constant pulsing, glowing, or hover translation in high-density areas.
- **Ergonomic settings preset:** 16 px editor typography with 28 px line height, non-intrusive minimap (mouseover slider, no characters), compact scrollbars, and fast 120–220 ms transition curves.
- **Accessibility-first defaults:** high terminal contrast target, strict reduced-motion support, and full fallback readability when custom CSS extensions are absent.

## Included themes

### Light variants

- **Note Book Minimal** — neutral high-clarity default
- **Note Book Solarized Light** — warm cream and teal
- **Note Book Farmhouse** — warm gray editorial surface
- **Note Book Parchment** — warm paper surface
- **Note Book Rosé Pine Dawn** — soft low-stimulation palette
- **Note Book Sage** — calm green surface

### Dark variants

- **Note Book Solarized Dark** — canonical dark default
- **Note Book Dark** — deep teal companion

## Installation & setup

1. Install or update the extension in VS Code.
2. Open **Preferences: Color Theme** and choose a Note Book theme.
3. Optional: copy `vs-code-setting.jsonc` into your VS Code User `settings.json` for matching editor ergonomics and optional Custom UI Style chrome.

The optional `custom-ui-style.stylesheet` section requires [Custom UI Style](https://marketplace.visualstudio.com/items?itemName=subframe7536.custom-ui-style). After changing those rules, run **Custom UI Style: Reload** or **Developer: Reload Window**.

## Validation

```bash
python3 scripts/validate_themes.py
```

The validator checks color format, required UI state keys, package registration, and settings integrity.
## Installation

```bash
npx vsce package
code --install-extension note-book-theme-0.6.0.vsix
```
