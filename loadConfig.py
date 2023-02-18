import os
from configparser import ConfigParser


def get_config():
    """ 获取配置文件  """
    print("#获得当前工作目录".format(os.getcwd()))
    print("#获得当前工作目录--{}".format(os.path.abspath('.')))
    print("#获得当前工作目录的父目录--{}".format(os.path.abspath('..')))
    print("#获得当前工作目录--{}".format(os.path.abspath(os.curdir)))
    cfg = ConfigParser()
    cfg.read('config.ini', 'UTF-8')
    count_column_config = cfg.get('installation', 'count_column')
    group_column_config = cfg.get('installation', 'group_column')
    sheet_name_config = cfg.get('installation', 'sheet_name')
    output_path = cfg.get('installation', 'output_path')
    wip_xlsx = cfg.get('installation', 'wip_xlsx')
    path = cfg.get('installation', 'path')
    if count_column_config is not None and group_column_config is not None:
        count_columns = count_column_config.split(",")
        group_columns = group_column_config.split(",")
        sheet_names = sheet_name_config.split(",")
        return ConfigObj(count_columns, group_columns, sheet_names, output_path, wip_xlsx, path)
    return None

class ConfigObj:
    """ 配置类OBJ """

    def __init__(self, count_columns, group_columns, sheet_names, output_path, wip_xlsx, path) -> None:
        super().__init__()
        self.count_columns = count_columns
        self.group_columns = group_columns
        self.sheet_names = sheet_names
        self.all_columns = group_columns + count_columns
        self.output_path = output_path
        self.wip_xlsx = wip_xlsx
        self.path = path

    def __str__(self):
        return str(self.group_columns) + str(self.count_columns) + str(sheet_names)

if __name__ == '__main__':
    print(get_config())
    pass
