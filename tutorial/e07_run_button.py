import marimo

__generated_with = "0.9.8"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    # define a switch
    switch_ui = mo.ui.switch(label="开关(Switch)")
    switch_ui
    return (switch_ui,)


@app.cell
def __(mo, switch_ui):
    mo.md(f"**Swicth 的状态是 `{switch_ui.value}`**")
    return


@app.cell
def __(mo, show_tips):
    # define a button
    button_ui = mo.ui.button(label="按钮(Button)", value=123, on_click=show_tips)
    button_ui
    return (button_ui,)


@app.cell
def __(mo):
    # 只是弹出一个提示
    def show_tips(x):
        mo.status.toast(f"你点击了按钮 {x}", kind="danger")
        return x+1
    return (show_tips,)


@app.cell
def __(button_ui, datetime):
    # 只是打印当前时间
    button_ui
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return


@app.cell
def __(button_ui, mo):
    mo.md(f"**Button 的状态是 `{button_ui.value}`**")
    return


@app.cell
def __():
    from datetime import datetime
    return (datetime,)


@app.cell
def __(mo):
    # define a run button
    run_button_ui = mo.ui.run_button(label="执行按钮(Run Button)")
    run_button_ui
    return (run_button_ui,)


@app.cell
def __(mo, run_button_ui):
    mo.md(f"**Run Button 的状态是 `{run_button_ui.value}`**")
    return


@app.cell
def __(mo, run_button_ui):
    # 展示每日 XKCD 漫画
    mo.stop(not run_button_ui.value)

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


@app.cell(hide_code=True)
def __(mo):
    mo.accordion({
        "案例对比 button 和 run_button 和差异（点击展开）": "- `run_button` 可以实现当前置输入改变时，必须要用户点击确认才会执行后续与输入相关的计算\n- `button` 由于其只是存储了一个计数器，则无法做到需要用户确认才能执行\n- 必要时，使用 `mo.stop(not run_button.value)` 截断计算流"
    }
    )

    return


@app.cell
def __(mo):
    aui = mo.ui.slider(1,10)
    aui
    return (aui,)


@app.cell
def __(mo):
    pass  # btn
    button = mo.ui.run_button()
    button
    return (button,)


@app.cell
def __(aui, button, mo):
    mo.stop(not button.value)
    mo.md(f"slider button = {aui.value}")
    return


@app.cell(hide_code=True)
def __(mo):
    mo.accordion({
        "版权声明": f"""
    本项目代码及其实例均遵循开源协议，更多实例请访问：[项目主页](https://github.com/switchball/100-marimo-projects)。
    """,
    })
    return


if __name__ == "__main__":
    app.run()
