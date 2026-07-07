# Note Book Theme for VS Code

A premium suite of warm, comfortable themes for VS Code offering soft paper-like backgrounds, sepia tones, and a highly polished UI. 

This extension contributes five distinct visual experiences:
- **Note Book Farmhouse** (Light theme): A hybrid light design blended between Rosé Pine Dawn and Claude Light UI to create a calm, editorial aesthetic.
- **Note Book Dark** (Dark theme): A warm, low-contrast dark sepia experience inspired by Solarized Dark+.
- **Note Book Farmhouse Dark** (Dark theme): A cozy, deep sepia dark mode for comfortable long-duration coding sessions.
- **Note Book Minimal** (Light theme): A clean, high-clarity minimalist light theme focusing on semantic simplicity.
- **Note Book Rosé Pine Dawn** (Light theme): A cozy, warm pastel-toned light theme directly implementing the beautiful Rosé Pine Dawn palette.

## Installation

### Building and Installing from Source

If you've cloned the repository and want to build and install the theme locally:

1. **Clone the repository and enter the directory:**
   ```bash
   git clone <your-repo-url>
   cd notebook-vs-theme
   ```

2. **Package the extension:**
   You can build the Visual Studio Code extension file (`.vsix`) using `npx` and `vsce`:
   ```bash
   npx vsce package
   ```
   *This will generate a file named `note-book-theme-x.x.x.vsix` in your current directory.*

3. **Install the generated VSIX file:**
   You can install the generated extension directly via your terminal (replace `x.x.x` with the actual version built):
   ```bash
   code --install-extension note-book-theme-x.x.x.vsix
   ```
   
   *Alternatively, inside VS Code:*
   - Go to the Extensions view (`Cmd+Shift+X` / `Ctrl+Shift+X`)
   - Click the `...` menu at the top right of the extensions pane
   - Select **Install from VSIX...**
   - Choose the downloaded `.vsix` file

## Activation

1. Open the Command Palette (`Cmd+Shift+P` on macOS / `Ctrl+Shift+P` on Windows/Linux)
2. Type and select **Preferences: Color Theme**
3. Select one of the contributed themes (e.g. **Note Book Farmhouse**, **Note Book Dark**, **Note Book Farmhouse Dark**, or **Note Book Minimal**).

## License

MIT


