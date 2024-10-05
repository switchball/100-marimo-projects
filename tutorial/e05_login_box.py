import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def __(mo):
    login_box = mo.md("""
    - Username: {name}
    - Password: {pswd}
    """).batch(
        name=mo.ui.text(placeholder="用户名"),
        pswd=mo.ui.text(kind="password")
    ).form()
    login_box
    return (login_box,)


@app.cell
def __(login_box):
    login_box.value
    return


@app.cell
def __(check_login, login_box):
    check_login(**login_box.value)
    return


@app.cell
def __(ACCOUNT, mo):
    def check_login(name, pswd):
        if name in ACCOUNT and pswd == ACCOUNT[name]:
            mo.status.toast("登录成功！")
            return True
        mo.status.toast("用户名或密码错误！", kind="danger")
        return False
    return (check_login,)


@app.cell
def __():
    return


@app.cell
def __():
    ACCOUNT = {
        "guest": "guest",
        "root": "123456",
    }
    return (ACCOUNT,)


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    mo.accordion({
        "版权声明": f"""
    本项目代码及其实例均遵循开源协议，更多实例请访问：[项目主页](https://github.com/switchball/100-marimo-projects)。
    """,
    })
    return


if __name__ == "__main__":
    app.run()
