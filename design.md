# Glass Paper — Glass Paper System

A locked visual system for the Glass Paper VS Code theme suite and its companion
settings preset. The suite keeps each paper palette distinct while sharing one
calm interaction language.

## Genre

Modern-minimal with an editorial paper influence.

## Theme families

- Light themes: paper-first surfaces, graphite ink, one restrained chromatic accent.
- Dark themes: deep ink-teal editor, lifted teal panels, one warm or cool syntax accent.
- Rosé Pine Dawn remains the softer lavender exception; it shares the same state and motion contract.

## Surface and state rules

- Editor is the quietest, most stable surface.
- Sidebars and panels are one step lighter (dark) or darker (light) than the editor.
- Active selection is stronger than hover, but never brighter than the focus ring.
- Focus is always a 2px visible ring or a 1px inset outline; never color-only.
- Accent color is reserved for focus, active tabs, links, progress, and semantic emphasis.
- No persistent glow, bounce, or hover translation in dense lists.

## Motion

- `--nb-motion-fast`: 120ms for color, opacity, and focus state changes.
- `--nb-motion-base`: 180ms for buttons, tabs, and compact surfaces.
- `--nb-motion-slow`: 260ms for widgets and toast entry.
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` for enter/state changes; `cubic-bezier(0.7, 0, 0.84, 0)` for exit/press.
- Animate only `transform` and `opacity` for spatial motion. Width animation is reserved for the functional progress indicator.
- Reduced motion disables spatial motion and all decorative animation.
- Reduced transparency removes blur and uses opaque theme surfaces.

## Interaction contract

- Hover: clarify surface only; no lift in navigation lists.
- Focus: immediate 2px ring with 2px offset; never animated.
- Active: a short 0.98 scale press on buttons/actions only.
- Disabled: reduce opacity and remove pointer affordance.
- Loading: only functional progress may loop.
- Error/success: use the theme's existing semantic red/green colors and keep feedback quiet.

## CSS authoring syntax tier

- **Custom Properties (`--*`)**: bolded distinct token tier for immediate visual scan.
- **Selectors & Specificity**: classes and IDs distinct from quieted HTML/tag selectors.
- **Pseudo-classes & Elements**: italicized interactive state markers (`:hover`, `:focus-visible`, `::before`).
- **Values & Units**: numerical units dimmed relative to value literals to maintain reading rhythm.
- **At-Rules**: italicized structural boundaries (`@media`, `@container`, `@layer`, `@keyframes`).

## Ergonomics

- Editor typography defaults to 16px with a 28px line-height.
- Minimap is a structural overview, not a second editor: no rendered characters and a mouseover slider.
- Tabs remain compact and readable; settings rows gain a calm border/focus treatment.
- User-specific zoom is intentionally not part of the shared preset.

## Files

- `themes/*.json` — palette and syntax contracts.
- `vs-code-setting.jsonc` — ergonomics, optional Custom UI Style chrome, and motion.
- `scripts/validate_themes.py` — repeatable integrity and contrast checks.
