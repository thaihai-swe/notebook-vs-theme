# Glass Paper Theme & VS Code Settings Redesign

A Solarized and Rosé Pine-inspired suite for VS Code, redesigned as one Glass Paper system for long coding sessions, stable focus states, and predictable workspace ergonomics.

## What changed in the redesign

- **Unified interaction contract across all 8 themes:** normalized foreground/background pairs for focused lists, menus, tabs, controls, settings, tree guides, terminals, command palette, notebooks, diffs, SCM, chat, and testing.
- **Distinct list states:** clear visual separation between focused items, active selection, and hover rows.
- **Glass Paper chrome:** restrained translucent surfaces, hairline separators, and opt-in blur only for hierarchy-bearing widgets—not decorative glow.
- **Ergonomic settings preset:** 16 px editor typography with a 28 px line height, structural minimap (mouseover slider, no characters), compact scrollbars, and an 80 / 120 / 180 / 260 ms motion ramp.
- **Expanded design tokens:** `--nb-depth-1/2/3` shadows, `--nb-surface-2` / `--nb-surface-overlay`, `--nb-text-muted` / `--nb-text-faint`, `--nb-border-strong`, `--nb-glass-tint`, `--nb-ring`, `--nb-scrim`, `--nb-blur-strong`, and a 4 / 8 / 12 / 16 px spacing scale — all consumed by the Custom UI Style stylesheet.
- **Dark-mode chrome:** `.monaco-workbench.vs-dark` overrides deepen glass blur, raise shadow alpha, and switch surface blends to `oklch` so Midnight Teal and Solarized Dark stay readable.
- **Accessibility-first defaults:** 4.5:1 text and control-label contrast validation, offset focus rings (including inputs), strict reduced-motion, reduced-transparency fallback, `prefers-contrast: more` deepened borders and a 3 px focus ring, Windows High Contrast (`forced-colors`) CanvasText reset, `@supports` blur fallback, and full readability when Custom UI Style is absent.
- **First-class CSS & UI/UX authoring:** dedicated token tiers for CSS custom properties (`--var`), pseudo-states (`:hover`, `::backdrop`), selectors, units, and at-rules (`@container`, `@media`, `@layer`) alongside native color decorators and quiet linting defaults.
- **Modern CSS color system:** perceptual `color-mix(in oklch, …)` for surfaces, hairlines, focus rings, and accent glows so every palette stays natural in both light and dark modes.

## Included themes

### Light variants

- **Minimal** — neutral high-clarity default
- **Solarized Light** — warm cream and teal
- **Farmhouse** — warm gray editorial surface
- **Parchment** — warm paper surface
- **Rosé Pine Dawn** — soft low-stimulation palette
- **Sage** — calm green surface

### Dark variants

- **Solarized Dark** — canonical dark default
- **Midnight Teal** — deep teal companion

## Installation & setup

1. Install or update the extension in VS Code.
2. Open **Preferences: Color Theme** and choose a Glass Paper theme.
3. Optional: copy `vs-code-setting.jsonc` into your VS Code User `settings.json` for matching editor ergonomics and optional Custom UI Style chrome.

The optional `custom-ui-style.stylesheet` section requires [Custom UI Style](https://marketplace.visualstudio.com/items?itemName=subframe7536.custom-ui-style). After changing those rules, run **Custom UI Style: Reload** or **Developer: Reload Window**.

## Validation

```bash
python3 scripts/validate_themes.py
```

The validator checks color format, required UI state keys, baseline foreground/background contrast, and package registration.

You can also run it via:

```bash
npm test
```

## Installation

```bash
npx vsce package
code --install-extension glass-paper-theme-0.0.1.vsix
```
