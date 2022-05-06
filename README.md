# Static site generator in python

### About *_content* directory:
- All content has to be inside this directory. 
- The internal structure with all files and subdirectories is replicated in project folder.

### About *_generator* directory:
- Python files for the generator goes here.

### About *_includes* directory:
- Reusable html code goes here.

### About *_layouts* directory:
- Pages templates goes here.

### About *assets* directory:
- CSS, JS, images goes here.

### About *_config.yml* file:
- Site configs file.

### About *_generator.py* file:
- Generator main file.


### Develop notes:
- Render flow: look for content files > extract all content tags > put content in layout > make all operations upon {{}} tags until no one is left > generate html files.