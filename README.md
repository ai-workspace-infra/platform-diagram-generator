# Platform Diagram Generator

This tool provides an automated, stable way to generate the "Open Platform Toolkit" multi-cloud delivery architecture diagram.

Instead of manually editing shapes in a drawing tool, you modify the `config.yaml` file and run the Python script to render a pixel-perfect, high-resolution PNG using Web technologies (HTML/Tailwind CSS) and Playwright.

## Prerequisites

Ensure you have Python 3 installed. Then, install the required packages and the Playwright browser binaries:

```bash
pip3 install -r requirements.txt
python3 -m playwright install chromium
```

## Generating the Diagram

Run the generation script:

```bash
python3 generate.py
```

This will read `config.yaml`, inject it into `template.html`, and capture a high-resolution screenshot named `platform_architecture.png`.

## Customization

- **Change Text**: Edit `config.yaml`.
- **Change Colors**: Modify the `color` property under `hexagons.ring` in `config.yaml`. It uses Tailwind CSS gradient classes (e.g., `from-blue-500 to-cyan-400`).
- **Layout Tweaks**: If you want to change the size, spacing, or add real image icons, you can edit `template.html`.
