import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md(
        r"""
        ## 奶茶点单系统 V1

        演示 dictionary 用法，只能点一杯，请点单：
        """
    )
    return


@app.cell
def __(mo):
    # 点单杯奶茶的情形
    tea_ui = mo.ui.dictionary({
        "品种": mo.ui.dropdown(options=["手打柠檬茶", "抹茶拿铁", "巴黎气泡水"]),
        "数量": mo.ui.number(start=0, stop=5, value=0),
        "甜度": mo.ui.radio(options=["正常甜", "少糖", "少少糖", "不加糖"], inline=True),
        "冰度": mo.ui.radio(options=["正常冰", "少冰", "去冰", "热"], inline=True),
    })
    tea_ui
    return (tea_ui,)


@app.cell
def __(get_single_tea_message, mo, tea_ui):
    mo.md(get_single_tea_message(tea_ui.value))
    return


@app.cell
def __(mo, tea_ui):
    mo.ui.table(tea_ui.value)
    return


@app.cell
def __(mo, total_number_ui):
    mo.md(
        rf"""
        -----
        ## 奶茶点单系统 V2

        演示 array 用法，可以点多杯

        你想点多少杯奶茶呢？ {total_number_ui}
        """
    )
    return


@app.cell
def __(mo):
    total_number_ui = mo.ui.slider(start=1, stop=10, value=1, show_value=True)
    return (total_number_ui,)


@app.cell
def __(mo, tea_ui, total_number_ui):
    N = total_number_ui.value
    many_tea_ui = mo.ui.array([tea_ui] * N)
    many_tea_ui
    return N, many_tea_ui


@app.cell
def __(get_single_tea_message, many_tea_ui, mo):
    _msg = ""
    for tea in many_tea_ui.value:
        _msg += get_single_tea_message(tea) + "\n\n"
    mo.md(_msg)
    return (tea,)


@app.cell
def __(many_tea_ui, mo):
    mo.ui.table(many_tea_ui.value)
    return


@app.cell
def __():
    def get_single_tea_message(_t):
        _kind, _amount, _sweet, _icey = _t['品种'], _t["数量"], _t["甜度"], _t["冰度"]
        if _amount > 0:
            message = f"您点了 {_amount} 杯 {_kind}, {_sweet}, {_icey}！"
        else:
            message = f"您还没有点奶茶呢！"
        return message
    return (get_single_tea_message,)


@app.cell
def __():
    import marimo as mo
    return (mo,)


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
