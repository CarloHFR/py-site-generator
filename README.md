# Static site generator in python

### About *_content* directory:
- All content has to be inside this directory. 
- The internal structure with all files and subdirectories is replicated in project folder.

### About *_generator* directory:
- Python files for the generator goes here.

### About *_layouts* directory:
- Pages templates goes here.

### About *assets* directory:
- CSS, JS, images goes here.

### About *_config.yml* file:
- Site configs file.

### About *_generator.py* file:
- Generator main file.


### Develop notes:
Render flow: 
    - Look for layouts directory
    - Store layouts in dict
    - Pre processes layout (loop)(make includes, ignore other tags)(self include is not allowed)
    - Look for content files
    - Extract all content tags to dict
    - process layout (insert content/include)(loop until no tags are left)
    - generate html files.