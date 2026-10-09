# Design Tokens & Palette Specifications

## Light Mode Palette (Default Clinical Standard)
| Token | Hex | Role | Usage |
| :--- | :--- | :--- | :--- |
| `--bg-canvas` | `#F8FAFC` | Page Backdrop | Surrounds the presentation stage |
| `--surface-card` | `#FFFFFF` | Slide Canvas | Pure solid background of each slide |
| `--surface-elevated` | `#F1F5F9` | Secondary Cards | Callout containers, table header rows |
| `--surface-subtle` | `#F8FAFC` | Metric Cards | Low-contrast background boxes |
| `--text-main` | `#0F172A` | Primary Headings | Maximum contrast, crisp readability |
| `--text-muted` | `#334155` | Body / Paragraphs | Supporting copy, clear visual hierarchy |
| `--text-faint` | `#64748B` | Labels / Disclaimers | Footnotes, regulatory text, captions |
| `--border-subtle` | `#E2E8F0` | Dividers / Outlines | 1px clean hairlines, zero visual noise |
| `--accent-teal` | `#0D9488` | Primary Brand | Eye tags, positive highlights, tech stats |
| `--accent-amber` | `#D97706` | Caution / Numbers | Secondary metrics, financial figures |
| `--accent-red` | `#E11D48` | Urgent / Problem | Clinical risk, mortality stats, alerts |
| `--accent-green` | `#16A34A` | Success / Normal | WHO Green tier, ARR growth, milestones |

## Dark Mode Palette (Terminal / High Contrast)
| Token | Hex | Role | Usage |
| :--- | :--- | :--- | :--- |
| `--bg-canvas` | `#090D14` | Obsidian Backdrop | Deep background |
| `--surface-card` | `#111724` | Slide Canvas | Solid dark background of each slide |
| `--surface-elevated` | `#1A2234` | Secondary Cards | Elevated containers, table headers |
| `--surface-subtle` | `#151D2D` | Metric Cards | Metric callout boxes |
| `--text-main` | `#F8FAFC` | Primary Headings | Crisp white text |
| `--text-muted` | `#94A3B8` | Body / Paragraphs | Slate grey supporting copy |
| `--text-faint` | `#64748B` | Footers / Tags | Low-emphasis captions |
| `--border-subtle` | `#1E293B` | Hairlines | 1px border dividers |
| `--accent-teal` | `#14B8A6` | Primary Brand | Cyan-teal glowing accents |
| `--accent-amber` | `#F59E0B` | Highlights | Warm gold metrics |
| `--accent-red` | `#F43F5E` | Critical Alert | High-impact warning numbers |
| `--accent-green` | `#22C55E` | Success | Positive indicators |

## Typography Scale (16:9 1080p Target)
* **Slide Title (H1)**: `42pt – 48pt` (Space Grotesk, Bold, Tracking `-0.02em`)
* **Cover Hero Title**: `80pt – 96pt` (Space Grotesk, ExtraBold)
* **Eyebrow Kicker**: `12pt – 14pt` (JetBrains Mono, Bold, Uppercase, Tracking `+0.08em`)
* **Big Metric Callout**: `44pt – 56pt` (Space Grotesk, ExtraBold / JetBrains Mono)
* **Card Titles / Subheads**: `16pt – 18pt` (Space Grotesk, SemiBold)
* **Body Copy**: `14pt – 16pt` (Plus Jakarta Sans, Regular, Line-height `1.5`)
* **Footnotes & Disclaimers**: `10pt – 12pt` (JetBrains Mono / Plus Jakarta Sans)
