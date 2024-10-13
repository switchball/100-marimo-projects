import marimo

__generated_with = "0.9.6"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    # define a switch
    pass
    return


@app.cell
def __():
    # mo.md(f"**Swicth 的状态是 `{switch_ui.value}`**")
    return


@app.cell
def __():
    # define a button
    pass
    return


@app.cell
def __():
    # mo.md(f"**Button 的状态是 `{button_ui.value}`**")
    return


@app.cell
def __():
    from datetime import datetime
    return (datetime,)


@app.cell
def __(datetime):
    # 只是打印当前时间
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return


@app.cell
def __(mo):
    # 只是弹出一个提示
    mo.status.toast(f"你点击了按钮", kind="danger")
    return


@app.cell
def __():
    # define a run button
    pass
    return


@app.cell
def __():
    # mo.md(f"**Run Button 的状态是 `{run_button_ui.value}`**")
    return


@app.cell
def __():
    # 展示每日 XKCD 漫画
    import requests
    import pandas as pd
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url, headers=headers)
    data = response.json()
    return data, headers, pd, requests, response, url


@app.cell
def __(data, image, mo):
    mo.hstack([image, data])
    return


@app.cell
def __(data, headers, requests):
    from PIL import Image
    import io

    response1 = requests.get(data["img"], headers=headers)
    image = Image.open(io.BytesIO(response1.content))
    return Image, image, io, response1


@app.cell
def __():
    # 一个例子对比 button 和 run_button
    return


@app.cell
def __(mo):
    aui = mo.ui.slider(1,10)
    aui
    return (aui,)


@app.cell
def __():
    pass  # btn
    return


@app.cell
def __(aui, mo):
    mo.md(f"slider button = {aui.value}")
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
