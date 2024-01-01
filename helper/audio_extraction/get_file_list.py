import os
def get_file_list(dir, item_list = []):
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if os.path.isdir(path):
            items = get_file_list(path, item_list)
            for item in items:
                item_list.append(item)
        else:
            item_list.append(path)
    return list(set(item_list))