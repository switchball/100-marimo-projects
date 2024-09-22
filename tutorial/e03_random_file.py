import marimo

__generated_with = "0.8.13"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    file_browser_ui = mo.ui.file_browser(selection_mode="directory", multiple=False)
    file_browser_ui
    return file_browser_ui,


@app.cell
def __(file_browser_ui):
    file_browser_ui.value[0].path
    return


@app.cell
def __():
    return


@app.cell
def __():
    def random_file_from_directory(directory_path):  # 定义一个函数来从目录中随机选择文件
        import os
        import random
        files_in_directory = os.listdir(directory_path)  # 获取目录下的所有文件和子目录
        while True:  # 开始循环直到找到一个文件
            selected_file = random.choice(files_in_directory)  # 随机选择一个条目
            selected_file_path = os.path.join(directory_path, selected_file)  # 构建完整的路径
            if os.path.isfile(selected_file_path):  # 如果是一个文件则返回
                return selected_file_path
            elif os.path.isdir(selected_file_path):  # 如果是目录则递归调用
                return random_file_from_directory(selected_file_path)
    return random_file_from_directory,


@app.cell
def __(file_browser_ui, random_file_from_directory):
    filename = random_file_from_directory(file_browser_ui.value[0].path)
    filename
    return filename,


@app.cell
def __(filename):
    with open(filename, 'r', encoding='utf-8') as file_:
        content = file_.read()
    return content, file_


@app.cell
def __(content, mo):
    mo.ui.code_editor(value=content, disabled=True)
    return


@app.cell
def __():
    1
    return


if __name__ == "__main__":
    app.run()
