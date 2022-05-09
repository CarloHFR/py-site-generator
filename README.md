# Static site generator in python

### About *_content* directory:
- All content has to be inside this directory. 
- The internal structure with all files and subdirectories is replicated in project folder.

### About *_layouts* directory:
- Pages templates goes here.

### About *assets* directory:
- CSS, JS, images goes here.

### About *_config.yml* file:
- Site configs file.

### About *_site_generator.py* file:
- Generator main file.


### Develop notes:
Render flow: 
    - Look for layouts directory - [OK]
    - Store layouts in dict - [OK]
    - Pre processes layout (loop)(make includes, ignore other tags)(self include is not allowed)
    - Look for content files - [OK]
    - Extract all content tags to dict - [OK]
    - process layout (insert content/include)(loop until no tags are left)
    - generate html files - [OK]