# Note Book Theme for VS Code

A warm, comfortable light theme for VS Code that's easy on the eyes. It is perfectly blended between the Rosé Pine Dawn palette and the Claude Light UI to create a calm, middle-range aesthetic.

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
3. Select **Note Book (Blended)** from the list

## License

MIT
