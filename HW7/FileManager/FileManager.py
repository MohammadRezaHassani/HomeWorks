import os


# تمرین کلاسی برای محاسبه مجموع سایز یک فولدر شامل تمام فایل ها و زیر فولدر ها

def total_dir_size(file_path):
    total_size = 0
    counter = 0
    for root, dirs, files in os.walk(file_path):
        if counter:
            break
        for file in files:
            total_size += os.path.getsize(os.path.join(file_path, file))
        if dirs:
            for dir in dirs:
                total_size += total_dir_size(os.path.join(file_path, dir))
        counter += 1

    return total_size


# مسیر فایل رو این پایین بگذار
# print(total_dir_size("/home/humanbeing/Documents"))

def extract_file_extension(file_name):
    file_name = file_name[::-1]
    return file_name.split(".")[0][::-1]


def filter_by_extension(file_name: str, ext, **kwargs):
    if ext == "":
        return True
    file_ext = extract_file_extension(file_name)
    if file_ext == ext:
        return True

    return False


def list_content(file_path):
    for root, dirs, files in os.walk(file_path):
        for file_name in files:
            if filter_by_extension(file_name, ext="py"):
                print(file_name)


list_content("/home/humanbeing/2021/Work/Maktab-Sharif/Homeworks/HW7")


