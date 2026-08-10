# Note Book Theme & VS Code Settings Redesign

A Solarized and Rosé Pine-inspired suite for VS Code, redesigned as one Glass Paper system for long coding sessions, stable focus states, and predictable workspace ergonomics.

## What changed in the redesign

- **Unified interaction contract across all 8 themes:** normalized foreground/background pairs for focused lists, menus, tabs, controls, settings, tree guides, terminals, command palette, notebooks, diffs, SCM, chat, and testing.
- **Distinct list states:** clear visual separation between focused items, active selection, and hover rows.
- **Glass Paper chrome:** restrained translucent surfaces, hairline separators, and opt-in blur only for hierarchy-bearing widgets—not decorative glow.
- **Ergonomic settings preset:** 16 px editor typography with a 28 px line height, structural minimap (mouseover slider, no characters), compact scrollbars, and a 120 / 180 / 260 ms motion ramp.
- **Accessibility-first defaults:** baseline 3:1 control contrast validation, immediate focus rings, strict reduced-motion support, reduced-transparency fallback, and full readability when Custom UI Style is absent.

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

The validator checks color format, required UI state keys, baseline foreground/background contrast, and package registration.
## Installation

```bash
npx vsce package
code --install-extension note-book-theme-0.8.0.vsix
```
