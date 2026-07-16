# Note Book Theme for VS Code

A Rosé Pine-inspired suite of calm, readable themes for VS Code. Softened surfaces, warm neutrals, muted accents, and stable focus states support long coding sessions.

## Themes

- **Note Book Rosé Pine Dawn** — warm pastel light theme; recommended light default
- **Note Book Solarized Dark HC** — deep teal dark theme with stronger text and focus contrast; recommended dark default
- **Note Book Farmhouse** — warm gray editorial light theme
- **Note Book Parchment** — cream paper light theme
- **Note Book Sage** — muted green light theme
- **Note Book Minimal** — neutral, high-clarity light theme
- **Note Book Solarized Light** — classic cream and teal light theme
- **Note Book Dark** — deep teal dark theme

These themes improve readability and reduce visual noise. They are not a medical treatment and do not replace good lighting, display brightness, breaks, or vision care.

## Installation

```bash
npx vsce package
code --install-extension note-book-theme-0.3.0.vsix
```

Then open **Preferences: Color Theme** and choose a Note Book theme.

## Long-session settings

An optional User Settings preset (`vs-code-setting.jsonc`) ships with the repo. It provides:

- Automatic OS light/dark switching between Rosé Pine Dawn and Solarized Dark HC
- Readable type scale, calm cursor, reduced motion, restrained Liquid Glass chrome
- Stronger Search/Replace borders and equal-width Search/Replace fields
- Native VS Code fallback when Custom UI Style is not installed

Copy the file contents into your VS Code User `settings.json`.

If you use Custom UI Style, run **Custom UI Style: Reload** or **Developer: Reload Window** after changing stylesheet rules.

## Validation

```bash
python3 scripts/validate_themes.py
```

## License

MIT
