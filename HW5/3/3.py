from pathlib import Path


# tip : dir.stat().st_size returns the size of the directory itself not the size of the content
# so for getting the size of inside files use another mechansim

def total_file_size(dir_path: str):
    sum_file_size = 0
    current_dir = Path(dir_path)
    assert current_dir.is_dir(), "Enter a dir name"
    for path in current_dir.iterdir():
        if path.is_file():
            if process_file_name(path.name):
                sum_file_size += path.stat().st_size

    return sum_file_size


def process_file_name(name: str):
    if name.startswith("."):
        return False
    split_name = name[::-1].split(".")
    return True if len(split_name[0]) > 5 else False


print(total_file_size("/home/humanbeing/"))
