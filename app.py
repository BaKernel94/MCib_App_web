import requests

busqueda = input("Que quiere buscar?: ")
url = f"https://api.wallapop.com/api/v3/general/search?keywords={busqueda}%20&category_ids=12900&filters_source=seo_landing&longitude=-3.69196&latitude=40.41956&order_by=closest"

r = requests.get(url)


for elemento in r.json().get("search_objects"):
    print(elemento.get("title"))
    print(elemento.get("price"))
