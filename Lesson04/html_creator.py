from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '     <p {}>Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '     <p {}>Preassure: {} c</p>\n'\
        .format(style, preassure_view(device))
    html += '     <p {}>Wind Speed: {} c</p>\n'\
        .format(style, wind_speed_view(device))
    html += '   </body>\n </html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html