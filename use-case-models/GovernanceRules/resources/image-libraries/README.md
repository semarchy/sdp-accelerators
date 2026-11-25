(c) Semarchy 2026

# GovernanceRules image library

The GovernanceRules application uses the image library `GovernanceRules` for its logo, avatar, cover, favicon and navigation tiles. The images are flat SVG files without text, drawn for a fictitious brand ("Quiet Harbor": slate blue, steel surfaces, sea-green accent). Replace them with your own brand assets if you wish: keep the file names, or change the `images://GovernanceRules/...` URLs in `src/GovernanceRules/applications/GovernanceRules.Application.seml`.

## Import the library

Import it **before** opening the application, otherwise the images show as broken.

1. Create a ZIP archive whose root contains a folder named `GovernanceRules` holding the SVG files of `GovernanceRules/`.
2. Import it as the image library `GovernanceRules`: Platform administration › Image libraries, or with the Platform CLI:
   ```
   sem dm admin image-libraries import GovernanceRules -i GovernanceRules.zip
   ```
   With the Semarchy SDP plugin for Claude Code, `node <plugin>/tools/sdp-bridge.mjs brand pack resources/image-libraries/GovernanceRules` builds the archive for you.
3. No redeployment of the data product is needed.

## Assets

| File | Used for | Size (viewBox) |
|---|---|---|
| `avatar.svg` | Application avatar (title bar) | 96 × 96 |
| `logo.svg` | Application logo (welcome page, search) | 128 × 128 |
| `cover.svg` | Navigation drawer cover | 320 × 128 |
| `favicon.svg` | Browser tab icon | 48 × 48 |
| `tile-rules.svg` | Rules folder | 160 × 160 |
| `tile-policies.svg` | Policies | 160 × 160 |
| `tile-applicability.svg` | Applicability folder (domains, classifications, attribute types) | 160 × 160 |
| `tile-regulations.svg` | Regulations and standards | 160 × 160 |
| `tile-bodies.svg` | Governance bodies | 160 × 160 |
| `tile-coverage.svg` | Governance coverage dashboard tile | 160 × 160 |

## Theme

The application theme matches the images: title bar `#243B53` with white text, primary colour Material blue-grey (`#2F6690` in the images), secondary colour Material teal (`#2A9D8F`). Other palette values used in the images and the dashboard: background `#F2F5F8`, text `#1B2733`, muted text `#4B5D6E`, border `#D3DCE4`, valid `#1E7B4F`, warning `#8A5700`, error `#B0301F`.


## Category avatars

Round 96 x 96 avatars for the rule categories (filled circle in the category colour, white line pictogram, optional teal `#2A9D8F` accent). Every colour has a contrast of at least 4.5:1 with white.

| File | Category code | Colour | Pictogram |
|---|---|---|---|
| `cat-data-quality.svg` | DATA_QUALITY | `#2F6690` | Check mark in a seal (white) |
| `cat-privacy.svg` | PRIVACY | `#6B4FA0` | Shield with a person |
| `cat-security-access.svg` | SECURITY_ACCESS | `#243B53` | Padlock |
| `cat-retention.svg` | RETENTION | `#8A5700` | Hourglass |
| `cat-reference-data.svg` | REFERENCE_DATA | `#1E7B4F` | Open book with code lines |
| `cat-identity-matching.svg` | IDENTITY_MATCHING | `#1F6F8B` | Two linked circles (merge) |
| `cat-metadata-documentation.svg` | METADATA_DOCUMENTATION | `#4B5D6E` | Document with lines |
| `cat-ai-usage.svg` | AI_USAGE | `#A23B72` | Robot head |
| `cat-stewardship.svg` | STEWARDSHIP | `#B0301F` | Person with a check (white) |
| `cat-modeling-conventions.svg` | MODELING_CONVENTIONS | `#2A6F5E` | Connected boxes (entity diagram) |
