from takecmd import Speak
import requests


def news():
    main_url="https://newsapi.org/v2/everything?q=india&sortBy=publishedAt&apiKey=44b6e1cb8d66442a83832e12d84cd8d3"
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=['first','second','third','fourth','fifth','sixth','seventh','eighth','nineth','tenth']
    for ar in articles:
        head.append(ar['title'])
    for i in range(len(day)):
        Speak(f"today's {day[i]} news is {head[i]}")


