# Note Book Theme for VS Code

A Solarized and Rosé Pine-inspired suite of calm, readable themes for VS Code, rebuilt with premium Liquid Glass surfaces and refined motion. Softened frosted chrome, warm neutrals, muted accents, and adaptive transition behavior support long coding sessions.

## Themes

### Recommended for long hours
- **Note Book Minimal** — neutral, high-clarity light theme; preferred light default
- **Note Book Solarized Dark** — canonical Solarized Dark palette and text balance; recommended dark default
- **Note Book Rosé Pine Dawn** — warm Rosé Pine-inspired light alternative for lower-stimulation days

### Solarized family
- **Note Book Solarized Light** — classic cream and teal light theme (comfort contrast)
- **Note Book Solarized Dark** — canonical Solarized Dark palette and text balance

### Rosé Pine family
- **Note Book Rosé Pine Dawn** — warm Rosé Pine-inspired light theme

### Other light surfaces
- **Note Book Farmhouse** — warm gray editorial light theme
- **Note Book Sage** — muted green light theme
- **Note Book Minimal** — neutral, high-clarity light theme
- **Note Book Dark** — deep teal dark companion theme

Comfort editions maintain at least 7:1 body-text contrast in the editor and terminal. Solarized Dark preserves the canonical Solarized foreground contrast (at least 4.5:1) to remain faithful to its original palette. Interactive chrome tokens (tabs, buttons, menus, toolbars, and focus states) are complete so hover and selection feedback stay consistent across themes.

These themes improve readability and reduce visual noise. They are not a medical treatment and do not replace good lighting, display brightness, breaks, or vision care.

## Installation

```bash
npx vsce package
code --install-extension note-book-theme-0.6.0.vsix
```

Then open **Preferences: Color Theme** and choose a Note Book theme.

## Optional premium Liquid Glass preset

The published VSIX remains theme-only. For premium frosted chrome, Settings Editor polish, and OS-adaptive motion, copy the repo file `vs-code-setting.jsonc` into your VS Code User `settings.json`.

### Requirements

- [Custom UI Style](https://marketplace.visualstudio.com/items?itemName=subframe7536.custom-ui-style) is required only for the `custom-ui-style.stylesheet` section
- After changing stylesheet rules, run **Custom UI Style: Reload** or **Developer: Reload Window**

### What the preset provides

- Automatic OS light/dark switching between **Note Book Minimal** (light) and **Note Book Solarized Dark** (dark)
- Premium Liquid Glass materials: thin / regular / thick / overlay / card surfaces
- Continuous radii, specular edges, layered elevation, and focus glows
- Settings Editor redesign: frosted cards, pill search field, clearer TOC selection, modified-state indicators
- OS-adaptive motion (`workbench.reduceMotion: user`) with a strict reduced-motion CSS fallback
- 10 keyframe animations: slide-in-left, fade-scale, emerge, notify, spotlight, slide-out, focus-pulse, cursor-glow, bracket-pop, shimmer
- 38 transition rules across sidebar, tabs, buttons, inputs, scrollbars, and panels for spring-based UI
- Smooth theme-switch cross-fade via `--nb-theme-motion` variable
- Skeleton loading pulse for list items and progress shimmer
- 16 px editor type, 1.9 line height, higher terminal contrast, and a calm cursor with subtle glow pulse
- Stronger Search/Replace borders and native VS Code fallback when Custom UI Style is not installed

### Performance notes

Backdrop blur is intentional for the glass look. If scrolling or typing feels heavy:

1. Temporarily remove or comment out the `custom-ui-style.stylesheet` block
2. Keep the theme and non-CSS settings for a lighter native chrome
3. Prefer reduced-motion OS settings if animations feel restless

### Troubleshooting

| Issue | Fix |
| --- | --- |
| Styles not applying | Run **Custom UI Style: Reload**, then **Developer: Reload Window** |
| Settings cards look default | Confirm Custom UI Style is installed and enabled |
| UI feels laggy | Disable the stylesheet section; keep theme tokens only |
| Fonts look wrong | Install preferred fonts or rely on the fallback stack |
| Glass too strong | Lower window zoom or switch to a denser theme like Minimal / Solarized Dark |

`.vscodeignore` intentionally excludes `vs-code-setting.jsonc`, scripts, and local design notes so the marketplace package stays lightweight.

For the greatest benefit, set your display brightness to match the room, use a warm night-light profile after sunset if comfortable, and take regular screen breaks.

## Validation

```bash
python3 scripts/validate_themes.py
```

The validator checks theme contrast, required color/semantic coverage, package registration, and Liquid Glass settings-preset integrity.

## License

MIT
