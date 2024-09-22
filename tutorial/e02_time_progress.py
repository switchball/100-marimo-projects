import marimo

__generated_with = "0.8.13"
app = marimo.App(width="medium")


@app.cell
def __():
    from datetime import datetime, timedelta

    d = datetime.now()
    return d, datetime, timedelta


@app.cell
def __():
    return


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    datetime_picker_ui = mo.ui.datetime()
    datetime_picker_ui
    return datetime_picker_ui,


@app.cell
def __():
    def time_difference(input_time):
        from datetime import datetime
        current_time = datetime.now()
        difference = current_time - input_time
        return -difference
    return time_difference,


@app.cell
def __(datetime_picker_ui, time_difference):
    time_difference(datetime_picker_ui.value)
    return


@app.cell
def __(d):
    from termcolor import colored

    time_text = d.strftime('%Y-%m-%d %H:%M:%S')
    print(colored(time_text, color='green', attrs=['bold', 'underline']))
    return colored, time_text


@app.cell
def __(mo, time_text):
    mo.Html(f"<h1 style='font-size:24px;'>{time_text}</h1>")
    return


@app.cell
def __(mo, time_text):
    mo.Html(f"<h1 style='font-size:36px; color: green; font-family: science-fiction;'>{time_text}</h1>")
    return


@app.cell
def __(datetime_picker_ui, format_timedelta, mo, time_difference):
    mo.Html(f"<h1 style='font-size:96px; color: green; font-family: Courier New;'>{format_timedelta(time_difference(datetime_picker_ui.value))}</h1>")
    return


@app.cell
def __(datetime_picker_ui, time_difference):
    t = time_difference(datetime_picker_ui.value)
    return t,


@app.cell
def __(t):
    f"{t.days=} {t.seconds=} {t.microseconds=}"
    return


@app.cell
def __():
    def format_timedelta(td):
        years, days = divmod(td.days, 365)  # 计算年数和剩余天数
        weeks, days = divmod(days, 7)       # 计算周数和剩余天数
        hours, remainder = divmod(td.seconds, 3600)  # 计算小时数和剩余秒数
        minutes, seconds = divmod(remainder, 60)     # 计算分钟数和秒数
        return f"{years}:{weeks}:{days}:{hours}:{minutes}:{seconds}"  # 返回格式化后的字符串
    return format_timedelta,


@app.cell
def __(format_timedelta, t):
    format_timedelta(t)
    return


@app.cell
def __(mo):
    mo.md(r"""------------""")
    return


@app.cell
def __(mo, t):
    _max = max(1, t.days * 86400 + t.seconds)
    slider_ui = mo.ui.slider(start=0, stop=_max, value=1, show_value=True, full_width=True, label="*模拟斗时进度条*")
    slider_ui
    return slider_ui,


@app.cell
def __(format_timedelta, mo, slider_ui, timedelta):
    mo.Html(f"<h1 style='font-size:96px; color: green; font-family: Courier New;'>{format_timedelta(timedelta(seconds=slider_ui.value))}</h1>")
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        非线性变化版本
        ----------------
        """
    )
    return


@app.cell
def __():
    import math
    return math,


@app.cell
def __(math, mo, t):
    _max = math.log(max(1, t.days * 86400 + t.seconds))
    slider_ui2 = mo.ui.slider(start=0, stop=_max, value=1, show_value=True, full_width=True, step=0.1, label="*模拟斗时进度条*")
    slider_ui2
    return slider_ui2,


@app.cell
def __(format_timedelta, math, mo, slider_ui2, timedelta):
    _seconds = math.ceil(math.exp(slider_ui2.value) - 1)
    _dt = timedelta(seconds=_seconds)
    _color = "green" if _seconds > 0 else "red"
    mo.Html(f"<h1 style='font-size:96px; color: {_color}; font-family: Courier New;'>{format_timedelta(_dt)}</h1>")
    return


@app.cell
def __(mo):
    mo.vstack(
        [mo.Html("1<br><br>"),
        mo.ui.slider(start=0,stop=222)
        ])
    return


@app.cell
def __(mo):
    import random
    print([random.choice(dir(mo.ui)) for _ in range(5)])
    return random,


@app.cell
def __(mo):
    mo.ui.table(data=[123,44])
    return


@app.cell
def __(mo):
    mo.ui.checkbox(False, label="sss")
    return


@app.cell
def __(mo):
    fb_ui = mo.ui.file_browser(selection_mode="directory")
    fb_ui
    return fb_ui,


@app.cell
def __(fb_ui):
    fb_ui.value
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
