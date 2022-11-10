import PySimpleGUI as sg
import methods
sg.theme("BrightColors")
layout = [[sg.Text("eBay Web-Scraper 1.0", font=("Courier 28"), key='title')], 
          [sg.InputText(do_not_clear=False), sg.Submit("Search")]
          ]

window = sg.Window("eBay Web-Scraper 1.0", layout, margins=(100, 50), resizable=True)

while True:
    event, values = window.read()
    # if event == "Search" or event == sg.WIN_CLOSED:
    #     break

    if event == sg.WIN_CLOSED:
        break

    if event == "Search":
        # layout[1][0].update()
        keyword = values[0]
        output = methods.performSearch(keyword)
        window.extend_layout(window, [[sg.Text(f"{methods.summarizeTest(keyword, output)}", font="Arial 14")]])
        methods.plotHistogram(keyword, output)
        # methods.plotHistogram(keyword, output)

        

#this is only a test

window.close()