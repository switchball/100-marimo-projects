import marimo

__generated_with = "0.8.18"
app = marimo.App(
    width="medium",
    layout_file="layouts/e04_hot_search.grid.json",
)


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __():
    import requests
    from bs4 import BeautifulSoup

    url = "https://tophub.today/"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return BeautifulSoup, headers, requests, response, soup, url


@app.cell
def __(soup):
    elements = soup.select(' div > div.cc-cd-cb.nano > div.cc-cd-cb-l.nano-content')
    links = [element.find_all('a') for element in elements]
    links = [link for sublist in links for link in sublist]
    len(links)
    return elements, links


@app.cell
def __(mo):
    input_ui = mo.ui.text(label="search:") .form(label="#热点检索系统")
    input_ui
    return (input_ui,)


@app.cell
def __(input_ui):
    input_ui.value
    return


@app.cell
def __(input_ui, links, mo):
    # 使用 input_ui.value 检索 links 中所有符合条件的标题文本
    search_text = input_ui.value
    matching_links = [link for link in links if search_text in link.get_text()]
    output = ""
    for link in matching_links:
        # 输出符合条件的链接文本
        output += rf"""<p>{link}</p>"""
    mo.md(output)
    return link, matching_links, output, search_text


@app.cell
def __():
    import jieba
    from wordcloud import WordCloud
    return WordCloud, jieba


@app.cell
def __(jieba, links):
    _titles = [element.find(class_="t") for element in links]
    # 删除一些文本
    keywords = [t.get_text() for t in _titles if t is not None and "¥" not in t.get_text()]
    txt = "\n".join(keywords)
    words = jieba.lcut(txt)
    # 删除单个字
    words = [t for t in words if len(t) >= 2]
    print(words)
    return keywords, txt, words


@app.cell
def __(WordCloud, words):
    # 选择字体，初始化词云
    wordcloud = WordCloud(font_path="Assets\Smiley Sans.ttf", background_color="white").generate(" ".join(words))
    # 展示的同时，保存图片到文件中
    wordcloud.to_file("hot_cloud.png")
    img = wordcloud.to_image()
    img
    return img, wordcloud


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
