# Azure Icons

[![GitHub Pages](https://github.com/jajera/azure-icons/actions/workflows/deploy.yml/badge.svg)](https://jajera.github.io/azure-icons/)

A searchable web library for browsing and copying official Azure architecture
icons (product / service icons from the Azure Architecture Center pack).

## Features

- Search by service name, tags, or common abbreviations
- Filter by Azure category tags
- Copy SVG or PNG data to the clipboard
- Download icons as SVG or PNG
- Light and dark themes
- Responsive layout for desktop and mobile
- Shareable search and tag filters in the URL

## Statistics

- **638** unique Azure service icons (deduplicated from the official SVG pack)
- Organized by Azure Architecture Center categories (compute, networking,
  databases, security, identity, and more)

## Usage

Serve the repository from a local web server:

```shell
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

Use the search box or tags to find an icon. Hover over a card to copy or
download its SVG or PNG representation.

## Repository structure

```text
icons/
  <category>/   Azure service icons grouped by category
icons.json      Searchable icon metadata used by the web app
favicon.svg     Site favicon
og-image.png    Open Graph / social preview image
scripts/        Metadata generation tooling
```

Regenerate `icons.json` after adding or renaming an icon:

```shell
python3 scripts/generate_icons_json.py
```

## Attribution

Icons are provided by
[Azure architecture icons](https://learn.microsoft.com/en-us/azure/architecture/icons/).
Microsoft permits use in architectural diagrams, training materials, or
documentation per the icon terms on that page. Azure and related marks are
trademarks of Microsoft. Do not modify icons beyond Microsoft brand guidance.

## License

The website code is available under the [MIT License](LICENSE). Azure icon
assets remain subject to Microsoft's applicable terms and are not relicensed
under MIT.
