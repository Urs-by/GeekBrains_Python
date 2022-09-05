
def createXml(data):

    xml = '<xml>\n'
    xml += '    <name >{}</name>\n' \
        .format(data[0])
    xml += '    <surname >{}</surname>\n' \
        .format(data[1])
    xml += '    <company >{}</company>\n' \
        .format(data[2])
    xml += '    <phone >{}</phone>\n' \
        .format(data[3])
    xml += '    <home_phone>{}</home_phone>\n' \
        .format(data[4])
    xml += '</xml>'
    xml += '\n'


    with open('catalog.xml', 'a',encoding="utf-8") as page:
        page.write(xml)

    return xml





