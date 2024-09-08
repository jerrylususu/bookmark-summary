import json
import re
from pathlib import Path
import shutil
from datetime import datetime

# Old slugify implementation
def old_slugify(text: str) -> str:
    invalid_fs_chars: str = '/\\:*?"<>|'
    return text.lower().replace(invalid_fs_chars, '-').replace(' ', '-')

# New slugify implementation
def new_slugify(text: str) -> str:
    invalid_fs_chars: str = '/\\:*?"<>|'
    return re.sub(r'[' + re.escape(invalid_fs_chars) + r'\s]+', '-', text.lower()).strip('-')

def get_file_path(month: str, title: str, timestamp: int, slugify_func) -> Path:
    date_str = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    return Path(f"{month}/{date_str}-{slugify_func(title)}.md")

def migrate_slugs():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    changes = []
    for item in data:
        old_slug = old_slugify(item['title'])
        new_slug = new_slugify(item['title'])
        
        if old_slug != new_slug:
            old_path = get_file_path(item['month'], item['title'], item['timestamp'], old_slugify)
            new_path = get_file_path(item['month'], item['title'], item['timestamp'], new_slugify)
            
            if old_path.exists():
                changes.append((old_path, new_path, item))
    
    # Perform migrations
    for old_path, new_path, item in changes:
        print(f"Moving: {old_path} -> {new_path}")
        # new_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(old_path, new_path)
        
        # Update raw content file if it exists
        old_raw_path = old_path.with_name(old_path.stem + "_raw.md")
        if old_raw_path.exists():
            new_raw_path = new_path.with_name(new_path.stem + "_raw.md")
            print(f"Moving raw content: {old_raw_path} -> {new_raw_path}")
            shutil.move(old_raw_path, new_raw_path)

    print(f"Migration complete. {len(changes)} files were moved.")

if __name__ == "__main__":
    migrate_slugs()