
class FileManager:
    
    def read_file(self, file_path):
        with open(file_path, "r") as file:
            return file.read()


    def write_file(self, file_path, file_name, content):
        pass