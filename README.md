# Note Book Theme for VS Code

A Rosé Pine-inspired suite of calm, readable themes for VS Code. The palette uses softened surfaces, warm neutrals, muted accents, and stable focus states for comfortable long coding sessions.

## Themes

- **Note Book Rosé Pine Dawn** — warm, pastel light theme; recommended light default.
- **Note Book Solarized Dark HC** — deep teal dark theme with stronger text and focus contrast; recommended dark default.
- **Note Book Farmhouse** — warm gray editorial light theme.
- **Note Book Parchment** — cream paper light theme.
- **Note Book Sage** — muted green light theme.
- **Note Book Minimal** — neutral, high-clarity light theme.
- **Note Book Solarized Light** — classic cream and teal light theme.
- **Note Book Dark** — deep teal dark theme.

The theme colors are designed around readable text, clear selection states, and non-neon diagnostics. They are not a medical treatment or a substitute for appropriate lighting, display brightness, breaks, and vision care.

## Long-session settings

`vs-code-setting.jsonc` is an optional User Settings preset. It provides:

- Automatic OS-based switching between Rosé Pine Dawn and Solarized Dark HC.
- Comfortable type scale, line height, editor padding, and terminal spacing.
- A quieter cursor, reduced motion, less prominent minimap, and restrained Liquid Glass chrome.
- A native VS Code fallback for users who do not install Custom UI Style.

Copy the settings you want into VS Code’s User `settings.json`; do not replace project-specific settings without reviewing them first.

## Installation

### Building and Installing from Source

If you've cloned the repository and want to build and install the theme locally:

1. **Clone the repository and enter the directory:**
   ```bash
   git clone <your-repo-url>
   cd notebook-vs-theme
   ```

2. **Package the extension:**
   ```bash
   npx vsce package
   ```

3. **Install the generated VSIX file:**
   ```bash
   code --install-extension note-book-theme-x.x.x.vsix
   ```

## Activation

1. Open the Command Palette (`Cmd+Shift+P` on macOS / `Ctrl+Shift+P` on Windows/Linux).
2. Select **Preferences: Color Theme**.
3. Choose one of the contributed themes.

For automatic day/night switching, enable `window.autoDetectColorScheme` and use the preferred light/dark themes shown in `vs-code-setting.jsonc`.

## Validation

Run the local theme integrity and contrast check:

```bash
python3 scripts/validate_themes.py
```

## License

MIT
