---
name: Orbital Telemetry HUD
colors:
  surface: '#0c1321'
  surface-dim: '#0c1321'
  surface-bright: '#323949'
  surface-container-lowest: '#070e1c'
  surface-container-low: '#151b2a'
  surface-container: '#19202e'
  surface-container-high: '#232a39'
  surface-container-highest: '#2e3544'
  on-surface: '#dce2f6'
  on-surface-variant: '#d8c3ad'
  inverse-surface: '#dce2f6'
  inverse-on-surface: '#2a3040'
  outline: '#a08e7a'
  outline-variant: '#534434'
  surface-tint: '#ffb95f'
  primary: '#ffc174'
  on-primary: '#472a00'
  primary-container: '#f59e0b'
  on-primary-container: '#613b00'
  inverse-primary: '#855300'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d3'
  on-secondary-container: '#00424e'
  tertiary: '#56e5a9'
  on-tertiary: '#003824'
  tertiary-container: '#30c88f'
  on-tertiary-container: '#004e34'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddb8'
  primary-fixed-dim: '#ffb95f'
  on-primary-fixed: '#2a1700'
  on-primary-fixed-variant: '#653e00'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0c1321'
  on-background: '#dce2f6'
  surface-variant: '#2e3544'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
  headline-xl-mobile:
    fontFamily: Inter
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 32px
  headline-lg:
    fontFamily: Inter
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 28px
  headline-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 22px
  body-md:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  data-mono-xl:
    fontFamily: JetBrains Mono
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: -0.02em
  data-mono-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  data-mono-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 18px
  label-mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.08em
  label-mono-xs:
    fontFamily: JetBrains Mono
    fontSize: 9px
    fontWeight: '700'
    lineHeight: 12px
    letterSpacing: 0.12em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 0.75rem
  margin: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1rem
  space-xl: 1.5rem
---

## Brand & Style

This design system establishes an authentic industrial aerospace telemetry console tailored for high-stakes operational simulation. The interface is precision-driven, tactical, and functional, evoking the tension, vigilance, and focus of an orbital life-support engineer on a critical shift (*Telemetri Nöbeti*).

### Aesthetic Direction: Tactical Sci-Fi Instrumentation
The aesthetic merges high-density aerospace instrumentation with contemporary flat ergonomics. It eschews gratuitous decorative sci-fi tropes in favor of purposeful, legible data displays:
- **Low-glare surfaces:** Deep void navy and ballistic slate containers reduce fatigue during prolonged monitoring cycles.
- **Instrument-grade luminosity:** High-visibility amber, spectral cyan, and tactical green indicators guide situational awareness.
- **Structured density:** Precision borders, chamfered sub-panels, segmented readouts, and monospace scalar arrays deliver immediate tactical feedback.
- **Localized vernacular:** Industrial Turkish aerospace terminology (e.g., *Sistem Nominal*, *Telemetri Kaydı*, *Kritik Uyarı*, *Nöbet Devri*) with crisp alphanumeric notation.

## Colors

The palette simulates backlit instrumentation panels in an unlit cockpit environment. Contrast is calibrated to prioritize signal recognition under stress.

### Color Tiers & Token Application
- **Deep Void Base (`#0b1220`):** The primary canvas background; an ultra-absorbent dark navy that eliminates eye strain and heightens luminescent elements.
- **Console Panels:**
  - `surface-panel`: `#111c33` (Primary structural containers, card backings).
  - `surface-panel-elevated`: `#16223e` (Interactive inputs, raised telemetry pods, module bays).
  - `surface-subdued`: `#0e1628` (Recessed instrument troughs, inactive track strips).
- **Instrumentation Outlines & Wireframes:**
  - `border-dim`: `#1e3a5f` (Structural separation grids and standard card borders).
  - `border-tactical`: `#334155` (Interactive controls, modular dividing pins).
  - `border-glow-cyan`: `rgba(6, 182, 212, 0.35)` (Active data links, telemetry line connectors).
  - `border-glow-amber`: `rgba(245, 158, 11, 0.4)` (Active focus frames, manual override triggers).
- **Telemetry Signals & Alarms:**
  - `signal-primary-amber`: `#f59e0b` (Primary brand accent, interactive elements, manual actuators).
  - `signal-telemetry-cyan`: `#06b6d4` (Sensor streams, vector trackers, atmospheric pressure readouts).
  - `signal-nominal-green`: `#10b981` (Nominal states, stabilized pod biometrics, sealed airlocks).
  - `signal-warning-amber`: `#fbbf24` (Drifting vectors, approaching thresholds, non-critical faults).
  - `signal-alert-red`: `#ef4444` (Breaches, critical decompression, lethal system failures).
- **Text & Readout Hierarchy:**
  - `text-primary`: `#f8fafc` (Primary data readings, high-importance labels).
  - `text-secondary`: `#94a3b8` (Standard units, secondary parameters, telemetry timestamps).
  - `text-dim`: `#475569` (Static axis legends, inactive toggle indicators, panel IDs).

## Typography

The typographic hierarchy strictly separates structural narrative content from scalar telemetry data.

### Dual-Font Operational Paradigm
- **Inter (Human Interface / Narrative):** Applied to panel headers, situational directives, operator prompts, and incident descriptions. Inter provides fast visual parsing without distracting ornamental artifacts.
- **JetBrains Mono (Telemetry Streams & Scalar Gauges):** Applied to telemetry values, decimal status coordinates, log timestamps, and sub-system identifiers. Tabular lining figures ensure vertical data columns align without visual drift when live numbers update.

### Letter-Spacing & Case Rules
- All `label-mono-*` roles must be rendered in uppercase (`text-transform: uppercase`) with positive tracking to simulate engraved cockpit switch plates.
- Turkish character sets (e.g., `İ`, `ı`, `Ş`, `Ğ`, `Ç`, `Ö`, `Ü`) must maintain explicit baseline alignment; monospace scalar units use non-breaking spaces before units (e.g., `101.3 kPa`, `0.04 bar`).

## Layout & Spacing

The layout philosophy mirrors a mission-control HUD: high informational efficiency optimized for one-thumb mobile gameplay and tactical situational sweeps.

### Mobile Grid Architecture
- **Canvas System:** A strict 4-column fluid mobile grid spanning a default `1rem` outer canvas margin, collapsing to compact `0.75rem` internal module gutters to maximize data density.
- **Rhythm & Grid Alignment:** Spacing strictly adheres to an 8px base rhythm (with 4px micro-steps for compact data rows). UI panels dock seamlessly against module dividers.
- **Telemetry Partitioning:** Heavy vertical stacking with multi-cell horizontal instrumentation rows. Critical telemetry metrics occupy twin-cell split units (50/50 width) or quad telemetry banks (25% each) for glanceable status validation.

## Elevation & Depth

Visual hierarchy uses physical panel layering reinforced by narrow luminescent photonic fringes rather than traditional drop shadows.

### Surface Tiers & Depth Strategy
1. **Tier 0 (The Deep Void - `#0b1220`):** Base structural canvas representing the mainframe hull. No illumination.
2. **Tier 1 (Tactical Enclosures - `#111c33`):** Recessed structural console panels. Finished with a 1px hairline border in `#1e3a5f`. No diffuse shadow.
3. **Tier 2 (Active Gauges & Cells - `#16223e`):** Interactive cards, telemetry monitors, and switch blocks. Layered directly over Tier 1.
4. **Tier 3 (Superimposed HUD Alerts & Overlays):** Modal system checks, emergency bypass confirmations, and critical alerts. Uses `#111c33` backed by a 12px blur backdrop (`backdrop-filter: blur(12px)`) with a perimeter warning border (`#ef4444` or `#f59e0b`).

### Photonic Edge Glows
- Inactive elements rely strictly on low-contrast structural outlines (`#1e3a5f`).
- Live nodes and interactive hotkeys cast a concentrated 0px blur, 1px spread edge highlight accompanied by an ambient rim halo: `box-shadow: inset 0 0 0 1px rgba(6, 182, 212, 0.4), 0 0 12px rgba(6, 182, 212, 0.2)`.

## Shapes

The interface employs an industrial, lightly beveled shape system. Structural forms convey reinforced aerospace hardware rather than soft consumer software.

### Corner Architecture
- Base components use `0.25rem` (4px) radii to maintain rigid mechanical alignment.
- Containers and tactical card surfaces scale to `0.5rem` (8px).
- Status indicator pills and sensor pulse nodes utilize clipped rectangular geometry or strict capsule profiles (`rounded-full`) solely to distinguish living data channels from structural chassis containers.

## Components

### 1. Actuator Buttons (Primary & Tactical Overrides)
- **Primary Action (Sistem Onayı / Manuel Müdahale):** Solid `#f59e0b` fill, text in `#0b1220` (`JetBrains Mono`, bold, uppercase). 1px outer ring in `rgba(245, 158, 11, 0.5)`. On press: scales to 0.98 with a luminescent inner burst.
- **Tactical Secondary (İkincil Kontrol):** Transparent background with `#16223e` fill, bordered with 1px `#1e3a5f`. Text in `#f8fafc`. Hover/Active induces a cyan border shift (`#06b6d4`) and `rgba(6, 182, 212, 0.15)` background glow.
- **Emergency Override (Acil Tahliye / Basınç Boşaltma):** Diagonal hazard stripes (subtle 45-degree dark slate/crimson pattern) framed by 1px solid `#ef4444`. Requires swipe-to-activate or sustained 1.5s press.

### 2. Telemetry Status Pills & Indicators
- Compact, high-density tags communicating subsystem state.
- **Nominal (NOMİNAL):** Dark green backing (`rgba(16, 185, 129, 0.12)`), text `#10b981`, 1px border `#10b981`. Preceded by a pulsing 6px luminescent dot.
- **Warning (UYARI):** Amber backing (`rgba(251, 191, 36, 0.12)`), text `#fbbf24`, 1px border `#fbbf24`.
- **Critical (KRİTİK):** Red backing (`rgba(239, 68, 68, 0.2)`), text `#ef4444`, 1px border `#ef4444`. Synchronized 1Hz blink cycle.

### 3. Telemetry Data Cards & Gauges
- Structured container with a top header strip displaying the subsystem tracking ID (e.g., `MODÜL-04 // O2 BASINCI`) in `label-mono-xs` text (`#475569`).
- Primary scalar metric rendered in `data-mono-xl` (`#f8fafc`), with the engineering unit (`kPa`, `PPM`, `°C`) set in `label-mono-sm` (`#94a3b8`) baseline-aligned.
- Bottom card edge integrates a glowing vector track: a 2px horizontal sparkline or segmented LED bar graph displaying real-time drift.

### 4. Input Fields & Calibration Sliders
- **Numeric Calibration Input:** Boxed in `#0e1628` with `#1e3a5f` border. Typing font is `JetBrains Mono` with leading zero notation (`004.82`). Focused states trigger glowing amber border illumination.
- **Throttle / Step Sliders:** Recessed horizontal track (`#0e1628`) with ticks spaced at measured intervals. Draggable thumb is a faceted hexagonal slider badge tinted with primary amber.

### 5. Tactical Data Lists & Incident Logs
- Alternating subtle rows (`transparent` to `rgba(22, 34, 62, 0.4)`).
- Left-flanked by a precision timestamp (`14:28:09.412` in `label-mono-xs`, `#94a3b8`).
- Log event text rendered in `body-md` with critical errors highlighted in inline `#ef4444` telemetry tokens.
- Right flank displays a quick-action acknowledge toggle button (`MUTLAK`).

### 6. Airlock & Pod Matrix HUD (Product-Specific)
- A tactical grid matrix representing life-support pods.
- Inactive/Locked pods display ghosted outlines (`#1e3a5f`) with `#475569` index tags.
- Occupied/Monitored pods project internal ambient glow in cyan or green depending on telemetry stability.
- Decompression hazard triggers pulsing peripheral amber/red wireframe overlays.
