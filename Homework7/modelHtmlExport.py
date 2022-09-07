def createHTML(data):
    style = 'style="font-size:30px;"'
    html = '  <body>\n'
    html += '    <p {}>Name: {} </p>\n' \
        .format(style, data[0])
    html += '    <p {}>Surname: {} </p>\n' \
        .format(style, data[1])
    html += '    <p {}>Company: {} </p>\n' \
        .format(style, data[2])
    html += '    <p {}>Phone: {} </p>\n' \
        .format(style, data[3])
    html += '    <p {}>Home phone: {} </p>\n' \
        .format(style, data[4])
    html += '  </body>'
    html += '---------------------------------------------\n'

    with open('catalog.html', 'a', encoding="utf-8") as page:
        page.write(html)

    return html

head = '<html>\n  <head></head>\n'
