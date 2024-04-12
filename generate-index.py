import os

def generate_index_html(docs_dir):
    index_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My GitHub Pages Site</title>
    </head>
    <body>
        <h1>Welcome to My GitHub Pages Site</h1>
        <ul>
    """

    for filename in os.listdir(docs_dir):
        if filename.endswith('.html'):
            index_content += f'<li><a href="{filename}">{filename}</a></li>\n'

    index_content += """
        </ul>
    </body>
    </html>
    """

    with open(os.path.join(docs_dir, 'index.html'), 'w') as f:
        f.write(index_content)

if __name__ == '__main__':
    docs_dir = 'docs'  # Path to your docs folder
    generate_index_html(docs_dir)
