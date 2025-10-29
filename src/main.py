from textnode import TextNode, TextType
from htmlnode import *
from markdown_to_html_node import markdown_to_html_node
import shutil
import os

def copy_to_directory(static, public, wipe=True):
    if wipe and os.path.exists(public):
        shutil.rmtree(public)
    if not os.path.exists(public):
        os.mkdir(public)
   
    for d_o_f in os.listdir(static):
        source_path = os.path.join(static, d_o_f)
        dest_path = os.path.join(public, d_o_f)
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        elif os.path.isdir(source_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_to_directory(source_path, dest_path, wipe=False)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:       
        line = line.lstrip()
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("No h1 title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()  
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    
    md_to_html_string = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", md_to_html_string)
    
    parent = os.path.dirname(dest_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)

def build_all_content(content_dir, template_path, public_dir):
    for root, dirs, files in os.walk("content"):
        if "index.md" in files:
            src = os.path.join(root, "index.md")
            rel = os.path.relpath(src, content_dir)
            dest = os.path.join(public_dir, rel).removesuffix(".md") + ".html"

            generate_page(src, template_path, dest)

def main():
    copy_to_directory('static', 'public')
    build_all_content('content', 'template.html', 'public')
   
   #generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
