import os
import re
import yaml


class SiteGenerator:

    def __init__(self, site_configs = "_config"):
        with open(f"{site_configs}.yml") as config_file:
            self.__configs = yaml.load(config_file)

        self.__layouts_dict = {}


    def __discover_html_file_names(self, path):
        file_name = []
        for root, directory_names, file_names in os.walk(path):
            for file in file_names:
                if file.endswith('.html'):
                    file_name.append(os.path.join(root, file))
        return file_name


    def __remove_older_pages(self):
        pass


    def __read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read()


    def __write_file(self, file_path, file_name, content):
        path = ""
        if file_path:
            for directory in file_path:
                path += directory + "/"
                try:
                    os.mkdir(os.path.dirname(path))
                except:
                    pass

        with open(f"{path}{file_name}", "w") as file:
            file.write(content)


    def __load_content_to_dict(self, content):
        filtered_content = {}
        tags = re.findall(r'{{(.+?)}}', content)

        for i in range(0, (len(tags)-1), 2):
            filtered_content[tags[i]] = re.search(f"{{{{{tags[i]}}}}}(.+?){{{{{tags[i+1]}}}}}", content).group(1)
        
        return filtered_content
    

    def __insert_content(self, page, content_dict):
        tags = re.findall(r'{{(.+?)}}', page)
        for tag in tags:
            replace_tag = "{{%s}}" % tag

            if tag in content_dict:
                page = page.replace(replace_tag, content_dict[tag])
        return page


    def __pre_process_site(self):
        layouts_file_names = self.__discover_html_file_names(self.__configs["layouts_directory"])
        
        for layout_file in layouts_file_names:
            layout = self.__read_file(layout_file)
            layout_file = layout_file.replace(f"{self.__configs['layouts_directory']}/", "")
            self.__layouts_dict[layout_file] = layout

        for layout_name in self.__layouts_dict:
            included_layout_names = []
            while True:
                include_layout_names = re.findall(r'{{include (.+?)}}', self.__layouts_dict[layout_name])

                for included_layout_name in include_layout_names:
                    if included_layout_name in included_layout_names:
                        include_layout_names.remove(included_layout_name)

                if not include_layout_names:
                    break

                for include_layout_name in include_layout_names:
                    if (include_layout_name in self.__layouts_dict) and (include_layout_name != layout_name):
                        include_content = self.__layouts_dict[include_layout_name]
                        included_layout_names.append(include_layout_name)
                    else:
                        include_content = ""

                    replace_tag = f"{{{{include {include_layout_name}}}}}"
                    self.__layouts_dict[layout_name] = self.__layouts_dict[layout_name].replace(replace_tag, include_content)

            any_include_tag_left = r'{{include (.+?)}}'
            self.__layouts_dict[layout_name] = re.sub(any_include_tag_left, '', self.__layouts_dict[layout_name])


    def __process_site(self):
        content_file_names = self.__discover_html_file_names(self.__configs["content_directory"])

        for content_file in content_file_names:
            content = self.__read_file(content_file)
            content_dict = self.__load_content_to_dict(content)



            # Process layout (insert content/include)(loop until no tags are left)



            page = self.__insert_content(self.__layouts_dict[content_dict["layout"]], content_dict)
            
            content_file = content_file.replace(f"{self.__configs['content_directory']}/", "").split("/")
            file_name = [string for string in content_file if ".html" in string][0]
            content_file.remove(file_name)
            file_path = content_file

            self.__write_file(file_path, file_name, page)


    def render_site(self):
        self.__remove_older_pages()
        self.__pre_process_site()
        self.__process_site()


if __name__ == "__main__":
    site_generator = SiteGenerator()
    site_generator.render_site()
