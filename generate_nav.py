import os
from natsort import natsorted

def generate_nav(path):
    entries = {}
    # Define the directories to exclude
    exclude_dirs = ['stylesheets', 'assets', '公开课', '番外篇']
    for root, dirs, files in os.walk(path):
        # Exclude the directories in the blacklist
        if any(exclude_dir in root for exclude_dir in exclude_dirs):
            continue
        for file in files:
            if file.endswith(".md"):
                # Remove the file extension and replace spaces with hyphens
                title = os.path.splitext(file)[0]
                # Get the relative path of the file
                rel_path = os.path.relpath(os.path.join(root, file), path)
                # Get the directory name
                dir_name = os.path.basename(root)
                # Add the file to the entries list
                if dir_name not in entries:
                    entries[dir_name] = []
                entries[dir_name].append((title, rel_path))

    # Sort the entries by directory name using natural sorting
    entries = dict(natsorted(entries.items()))

    # Sort the files in each directory by title using natural sorting
    for key in entries:
        entries[key] = natsorted(entries[key], key=lambda x: x[0])

    # Generate the nav content
    nav = "nav:\n"
    for dir_name, files in entries.items():
        nav += f"  - {dir_name}:\n"
        for title, file in files:
            nav += f"    - {title}: {file}\n"
    return nav

# Replace 'your_project_path' with the path to your project
nav_content = generate_nav('docs/')
print(nav_content)