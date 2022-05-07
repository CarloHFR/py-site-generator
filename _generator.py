from _generator.file_manager import FileManager
from _generator.tag_processor import TAGProcessor


file_manager = FileManager()
layout = file_manager.read_file("_layouts/default.html")
content = file_manager.read_file("_content/index.html")

tag_processor = TAGProcessor()
content_dict = tag_processor.extract_content_to_dict(content)
page = tag_processor.insert_content(layout, content_dict)

print(layout)
print(page)
