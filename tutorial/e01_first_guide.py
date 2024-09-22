import marimo

__generated_with = "0.8.13"
app = marimo.App(width="medium")


@app.cell
def __(mo):
    mo.md(
        r"""
        # Introduction 导引 WYSIWYG

        `marimo` 是一款适用于 Python 的开源**响应式**笔记本，具有如下特点：

        - 交互式设计
        - 所见即所得、可重现
        - 可作为脚本执行，并可作为应用程序共享。

        来自官网地址：[https://marimo.io/](https://marimo.io/)
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## LaTeX 数学公式

        在文本中嵌入公式，比如 $E = mc^2$ ，或嵌入多行公式 
        $$e^{i\pi} = -1$$
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        ## 嵌入网络图片

         ![img](https://marimo.io/logotype-wide.svg)
        """
    )
    return


@app.cell
def __(mo):
    diagram = '''
    graph LR
        A[方块] -- Link text --> B((圆圆的东西))
        A --> C(圆角方块)
        B --> D{菱形}
        C --> D
    '''
    mo.vstack([
        mo.md("## 使用 Mermaid 绘制流程图"),
        mo.hstack([
            mo.mermaid(diagram),
            mo.ui.code_editor(value=diagram, disabled=True),
        ], widths=[2,1])
    ])
    return diagram,


@app.cell
def __(mo):
    mo.callout("Marimo = 编程 + markdown ?（i.e. 伪装成 md 的编程工具）", kind='success')
    return


@app.cell
def __():
    return


@app.cell(hide_code=True)
def __(amplitude, chart, mo, period):
    mo.vstack([chart, mo.md(f"$$ y(x) = {amplitude.value} * \sin(2\pi * {period.value})$$")])
    return


@app.cell
def __(mo):
    period = mo.ui.slider(start=1, stop=5, step=0.5, value=2, label="周期")
    amplitude = mo.ui.slider(start=0.2, stop=2.0, step=0.2, value=1, label="振幅")
    mo.vstack([period, amplitude])
    return amplitude, period


@app.cell
def __(get_gold_price, mo):
    result0 = get_gold_price()
    price, price_dr, price_ud = result0["middleprice"], result0["openprice_dr"], result0["updown_d"]
    mo.vstack([
        mo.md("### 使用 Stat 展示数据"),
        mo.stat(value=f"{price}", label="实时金价", caption=f"{price_dr}", direction=f"{price_ud}", bordered=True),
    ])
    return price, price_dr, price_ud, result0


@app.cell(hide_code=True)
def __(amplitude, mo, pd, period):
    import numpy as np
    import altair as alt

    # 定义周期和振幅
    _period = period.value * np.pi  # 周期为2π
    _amplitude = amplitude.value  # 振幅为1

    # 生成x轴数据
    x = np.linspace(0, 2 * _period, 1000)

    # 计算y轴数据
    y = _amplitude * np.sin(x)

    # 创建数据框
    data = pd.DataFrame({
        'x': x,
        'y': y
    })

    # 绘制图形
    chart = alt.Chart(data).mark_line().encode(
        x='x',
        y='y'
    ).encode(
        y=alt.Y('y', scale=alt.Scale(domain=(-1, 1)))
    )
    chart = mo.ui.altair_chart(chart)
    return alt, chart, data, np, x, y


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        ## 交互式查看数据

        对 MNIST 手写数据集进行可视化降维聚类。
        """
    )
    return


@app.cell(hide_code=True)
def __(embedding, mo, scatter):
    chart1 = mo.ui.altair_chart(scatter(embedding))
    chart1
    return chart1,


@app.cell
def __(chart1, mnist, mo, table1):
    # show 10 images: either the first 10 from the selection, or the first ten
    # selected in the table
    mo.stop(not len(chart1.value))

    def show_images(indices, max_images=10):
        import matplotlib.pyplot as plt

        indices = indices[:max_images]
        # images = raw_digits.reshape((-1, 8, 8))[indices]
        images = mnist.data.reshape((-1, 28, 28))[indices]
        fig, axes = plt.subplots(1, len(indices))
        fig.set_size_inches(12.5, 1.5)
        if len(indices) > 1:
            for im, ax in zip(images, axes.flat):
                ax.imshow(im, cmap="gray")
                ax.set_yticks([])
                ax.set_xticks([])
        else:
            axes.imshow(images[0], cmap="gray")
            axes.set_yticks([])
            axes.set_xticks([])
        plt.tight_layout()
        return fig

    selected_images = (
        show_images(list(chart1.value["index"]))
        if not len(table1.value)
        else show_images(list(table1.value["index"]))
    )
    mo.md(
        f"""
        **所选图片的预览**:

        {mo.as_html(selected_images)}

        查看详细数据：

        {table1}
        """
    )
    return selected_images, show_images


@app.cell
def __(chart1, mo):
    table1 = mo.ui.table(chart1.value)
    return table1,


@app.cell
def __(mo):
    mo.md(r"""## 特性1：响应式""")
    return


@app.cell
def __(b):
    c = b + 2
    c
    return c,


@app.cell
def __(a_ui):
    b = a_ui.value + 1
    b
    return b,


@app.cell
def __(mo):
    a_ui = mo.ui.slider(start=1, stop=100, label="Set a:")
    a_ui
    return a_ui,


@app.cell(hide_code=True)
def __(requests, ssl):
    import json

    def get_gold_price(prodcode="130060000043"):
        context = ssl.create_default_context()
        context.options |= ssl.OP_NO_SSLv2
        context.options |= ssl.OP_NO_SSLv3
        # 目标 URL
        url = "https://mybank.icbc.com.cn/servlet/AsynGetDataServlet"

        # POST 请求的数据
        data = {
            # 根据实际情况填写 POST 请求的数据
            "Area_code": "0200",
            "trademode": 1,
            "tranCode": "A00500"
        }

        # 发送 POST 请求
        response = requests.post(url, data=data, verify=False)

        # 检查请求是否成功
        if response.status_code == 200:
            # 解析 JSON 数据
            data = response.json()

            # 查找 prodcode 对应的项
            for item in data.get('market', []):
                if item.get('prodcode') == prodcode:
                    # 返回中间价和涨跌值
                    k = item.get("updown_d", None)
                    if k is None:
                        d = None
                    elif k == "1":
                        d = "increase"
                    elif k == "2":
                        d = "decrease"
                    return {
                        "middleprice": item.get("middleprice"),
                        "openprice_dr": item.get("openprice_dr"),
                        "updown_d": d
                    }
            else:
                print(f"未找到 prodcode 为 {prodcode} 的项")
        else:
            print(f"请求失败，状态码：{response.status_code}")

    # 示例调用
    # prodcode = "130060000043"
    # result = get_gold_price(prodcode)
    # if result:
    #     print(f"中间价: {result['middleprice']}, 当日涨跌值: {result['updown_d']}")
    return get_gold_price, json


@app.cell(hide_code=True)
def __():
    # import requests
    import ssl
    from curl_cffi import requests # 使用该requests代替原本的requests使用即可
    return requests, ssl


@app.cell
def __():
    return


@app.cell
def __():
    from sklearn.datasets import fetch_openml

    # 加载MNIST数据集
    _mnist = fetch_openml('mnist_784', version=1)

    # 分割数据集为训练集和测试集
    _X, _y = _mnist["data"], _mnist["target"]
    X_train, X_test = _X[:6000], _X[60000:]
    y_train, y_test = _y[:6000], _y[60000:]
    raw_digits_f, raw_labels_f = X_train, y_train
    return (
        X_test,
        X_train,
        fetch_openml,
        raw_digits_f,
        raw_labels_f,
        y_test,
        y_train,
    )


@app.cell
def __():
    sliced_size = 5000
    return sliced_size,


@app.cell
def __():
    import pymde
    mnist = pymde.datasets.MNIST()
    mde = pymde.preserve_neighbors(mnist.data, device="cuda", constraint=pymde.Standardized(), verbose=True)
    return mde, mnist, pymde


@app.cell
def __(mde):
    embedding_ed = mde.embed(verbose=True)
    # pymde.plot(embedding_ed, color_by=mnist.attributes['digits'])
    v = embedding_ed.cpu()
    return embedding_ed, v


@app.cell
def __(mnist, pd, sliced_size, v):
    embedding = pd.DataFrame(
        {
            "x": v[:sliced_size, 0], 
            "y": v[:sliced_size, 1], 
            "digit": mnist.attributes['digits'][:sliced_size]
        }
    ).reset_index()
    return embedding,


@app.cell
def __():
    # X_embedded = sklearn.decomposition.PCA(
    #     n_components=2, whiten=True
    # ).fit_transform(raw_digits)

    # embedding = pd.DataFrame(
    #     {"x": X_embedded[:, 0], "y": X_embedded[:, 1], "digit": raw_labels}
    # ).reset_index()
    return


@app.cell
def __(alt):
    def scatter(df):
        return (alt.Chart(df)
        .mark_circle()
        .encode(
            x=alt.X("x:Q").scale(domain=(-2.5, 2.5)),
            y=alt.Y("y:Q").scale(domain=(-2.5, 2.5)),
            color=alt.Color("digit:N"),
        ).properties(width=500, height=500))
    return scatter,


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import pandas as pd
    return pd,


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
