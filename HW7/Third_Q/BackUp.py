import os


class BackupOpen:

    def __init__(self, file_path, file_mode):
        self.file_path = file_path
        self.file_dir = os.path.dirname(file_path)
        self.file_base_name = os.path.basename(file_path)
        self.backup_file_name = "backup_" + self.file_base_name
        self.backup_file_path = os.path.join(self.file_dir, self.backup_file_name)
        self.file_mod = file_mode
        self.main_file = None
        self.backup_file = None

    def __enter__(self):
        self.backup_file = open(self.backup_file_path, "w")
        self.main_file = open(self.file_path, "r")
        content = self.main_file.read()
        self.backup_file.write(content)
        self.backup_file.close()
        self.main_file.close()
        self.main_file = open(self.file_path, self.file_mod)
        return self.main_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.main_file.close()
            self.main_file = open(self.file_path, "w")
            self.main_file.write("")
            self.backup_file = open(self.backup_file_path, "r")
            content = self.backup_file.read()
            self.main_file.write(content)
            self.main_file.close()
            self.backup_file.close()
            return True  # for suppressing exception

        self.main_file.close()




