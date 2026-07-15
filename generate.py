import yaml
import os
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright

def generate_image():
    print("[1/3] Loading config.yaml...")
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    print("[2/3] Rendering layout via template.html...")
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    html_content = template.render(config=config)
    
    # Write temporary HTML file
    html_path = os.path.abspath('temp_render.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("[3/3] Launching browser engine to capture high-res image...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(set_viewport_size={"width": 1400, "height": 1050}, device_scale_factor=2)
        
        file_url = f"file://{html_path}"
        page.goto(file_url)
        page.wait_for_timeout(1000) # Wait for Tailwind CSS to load and render
        
        output_name = 'platform_architecture.png'
        page.screenshot(path=output_name, full_page=True)
        browser.close()
    
    # Clean up temporary file
    if os.path.exists(html_path):
        os.remove(html_path)
    print(f"✅ Success! Architecture diagram generated and saved as: {output_name}")

if __name__ == "__main__":
    generate_image()
