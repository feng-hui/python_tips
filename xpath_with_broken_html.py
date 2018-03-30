# -*- coding: utf-8 -*-
# @author = 'Feng_hui'
# @time = '2018/3/16 11:56'
# @email = 'fengh@asto-inc.com'
from lxml.html import soupparser, fromstring, tostring


def deal_broken_html():
    """
    output all content including the tags of the first p tag
    Maybe the content is not you wanted.
    If you want to get the content of the first p tag, you can use the second function.
    :return <p></p>
    """
    html = """
    <html><body><article >
        <p><div  ><img src="xyz"><noscript><img src="xyz" /></noscript>
        <p class="caption">ABC</p></div>EFG. </p>
        <p>HIJ.</p>
        <p>KLM</p>
        <p>NOP</p>
    </article></body></html>
    """
    html_element = fromstring(html)
    # print(tostring(html_element))
    output = html_element.xpath('//article/p')
    content = tostring(output[0]).decode('utf-8')
    return content


def deal_broken_html2():
    """
    output all content including the tags of the first p tag
    :return <p><div><img src="xyz"><noscript><img src="xyz"></noscript><p class="caption">ABC</p></div>EFG. </p>
    """
    with open('broken_html', 'rb') as f:
        tree = soupparser.parse(f)
    # print(tostring(tree))
    output = tree.findall('//article/p')
    content = tostring(output[0]).decode('utf-8')
    return content


if __name__ == "__main__":
    print('The result of the first function: {0}'.format(deal_broken_html()))
    print('The result of the first function: {0}'.format(deal_broken_html2()))
