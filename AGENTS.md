# Note Book Theme - AGENTS.md

This file provides context and instructions for AI coding agents working on the Note Book Theme VS Code extension.

## Project Overview
Note Book Theme is a VS Code extension that contributes two warm, comfortable themes:
- **Note Book** (Light theme): A hybrid design blended between Rosé Pine Dawn and Claude Light UI. Path: [note-book-theme.json](file:///Users/thaihai-swe/Desktop/notebook-vs-theme/themes/note-book-theme.json).
- **Note Book Dark** (Dark theme): A warm, low-contrast sepia experience inspired by Solarized Dark+. Path: [note-book-dark-theme.json](file:///Users/thaihai-swe/Desktop/notebook-vs-theme/themes/note-book-dark-theme.json).

## Setup & Development Commands
This is a configuration-only extension with no node dependencies or compilation steps.
- **Package the Extension:** Generates a `.vsix` package in the root directory.
  ```bash
  npx vsce package
  ```
- **Install Extension Locally:** Installs the built `.vsix` package.
  ```bash
  code --install-extension note-book-theme-*.vsix
  ```

## Development Workflow & Debugging
To test and preview changes interactively:
1. Open the project folder in VS Code.
2. Open the **Run and Debug** view (`Ctrl+Shift+D` or `Cmd+Shift+D`).
3. Press **F5** or select **Launch Extension** to run an Extension Development Host window.
4. In the new window, select "Note Book" or "Note Book Dark" under Color Themes to inspect the UI and syntax styling.

## Design Guidelines & Aesthetics
- **Note Book (Light)**: Must maintain a warm, soft paper-like background. Colors should not be too bright or clinical. Avoid harsh whites and high-contrast blacks.
- **Note Book Dark (Dark/Sepia)**: Focus on low-contrast sepia tones. Avoid pure blacks and neon colors. Text should be legible but soft.
- **Theme JSON Structure**:
  - `colors`: Used for VS Code UI elements (sidebar, editor, tabs, status bar).
  - `tokenColors`: Used for syntax highlighting. Ensure standard scopes (`keyword`, `string`, `comment`, `constant`, etc.) are styled appropriately.
