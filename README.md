# Note Book Theme for VS Code

A Solarized and Rosé Pine-inspired suite of calm, readable themes for VS Code. Softened surfaces, warm neutrals, muted accents, and stable focus states support long coding sessions.

## Themes

### Recommended for long hours
- **Note Book Parchment** — warm paper light theme; recommended light default
- **Note Book Solarized Dark HC** — deep teal dark theme with stronger text and focus contrast; recommended dark default

### Solarized family
- **Note Book Solarized Light** — classic cream and teal light theme (comfort contrast)
- **Note Book Solarized Dark** — canonical Solarized Dark palette and text balance
- **Note Book Solarized Dark HC** — Solarized Dark with raised body-text contrast for marathon sessions

### Rosé Pine family
- **Note Book Rosé Pine Dawn** — warm Rosé Pine-inspired light theme

### Other light surfaces
- **Note Book Farmhouse** — warm gray editorial light theme
- **Note Book Sage** — muted green light theme
- **Note Book Minimal** — neutral, high-clarity light theme
- **Note Book Dark** — deep teal dark companion theme

Comfort editions maintain at least 7:1 body-text contrast in the editor and terminal. Solarized Dark preserves the canonical Solarized foreground contrast (at least 4.5:1) to remain faithful to its original palette. Warm paper and teal surfaces reduce perceived glare without sacrificing readable focus states.

These themes improve readability and reduce visual noise. They are not a medical treatment and do not replace good lighting, display brightness, breaks, or vision care.

## Installation

```bash
npx vsce package
code --install-extension note-book-theme-0.5.1.vsix
```

Then open **Preferences: Color Theme** and choose a Note Book theme.

## Long-session settings

An optional User Settings preset (`vs-code-setting.jsonc`) ships with the repo. It provides:

- Automatic OS light/dark switching between Parchment and Solarized Dark HC
- 16 px editor type, generous line height, higher terminal contrast, and a calm static cursor
- Reduced motion, restrained chrome, and stronger Search/Replace borders
- Native VS Code fallback when Custom UI Style is not installed

Copy the file contents into your VS Code User `settings.json`.

For the greatest benefit, set your display brightness to match the room, use a warm night-light profile after sunset if it is comfortable for you, and take regular screen breaks.

If you use Custom UI Style, run **Custom UI Style: Reload** or **Developer: Reload Window** after changing stylesheet rules.

## Validation

```bash
python3 scripts/validate_themes.py
```

## License

MIT
