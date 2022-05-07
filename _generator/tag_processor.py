import re

class TAGProcessor:

    def extract_content_to_dict(self, content):
        filtered_content = {}
        tags = re.findall(r'{{(.+?)}}', content)

        for i in range(0, (len(tags)-1), 2):
            filtered_content[tags[i]] = re.search(f"{{{{{tags[i]}}}}}(.+?){{{{{tags[i+1]}}}}}", content).group(1)

        return filtered_content


    def insert_content(self, page, content_dict):
        tags = re.findall(r'{{(.+?)}}', page)
        for tag in tags:
            replace_tag = "{{%s}}" % tag

            if tag in content_dict:
                page = page.replace(replace_tag, content_dict[tag])

        return page

    
    def execute_include(self, page):
        pass
