import json
import os
import re

baseurl = "/Kordiak_Park"
posts = []
posts_dir = "_posts"
if os.path.exists(posts_dir):
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            with open(os.path.join(posts_dir, filename), "r") as f:
                content = f.read()
                title_match = re.search(r"^title:\s*\"?(.+?)\"?\s*\n", content, re.MULTILINE)
                text_match = re.search(r"\n\n(.*)", content, re.DOTALL)
                
                if title_match and text_match:
                    # Get the date from the filename to make it a real Jekyll url
                    # e.g. 2026-05-15-blooms.md -> /2026-05-15-blooms.html
                    url = "/" + filename.replace(".md", ".html")
                    posts.append({
                        "title": title_match.group(1),
                        "url": baseurl + url,
                        "content": text_match.group(1)[:200].replace("\n", " ")
                    })

with open("search.json", "w") as f:
    json.dump(posts, f)
