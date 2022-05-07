import json
import re
import traceback

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url = 'https://www.diffordsguide.com'
search_url = '/cocktails/search?include%5Bdg%5D=1&gentle_to_boozy%5B%5D=0&gentle_to_boozy%5B%5D=10&sweet_to_sour%5B%5D=0&sweet_to_sour%5B%5D=10&calories%5B%5D=0&calories%5B%5D=9'

data = requests.get(url+search_url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
lists = soup.select('#search-form > div.grid-x > a ')

count = 0

for li in lists:
    cnt = 0

    garnish = ""
    abv = 0
    abv_lv = 0
    recipe = list()
    img = li.select_one('div > div > img')['src']
    title = li.select_one('h3.box__title').text

    # if count == 2:
    #     break
    #
    href = li.get('href')
    data = requests.get(url+href, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # ingredients_table = soup.findAll("table", {"class":"ingredients-table"})
    ingredients_table = soup.find("table", "ingredients-table")
    ingredients = ingredients_table.findAll("td", "td-align-top")
    main_base = ""
    garnish = soup.find_all("h3")[1].find_next_sibling().get_text()
    abv_li = list(soup.find("ul", "no-margin-bottom").children)
    abv_t = abv_li[3].get_text()
    try:
        abv = re.findall("\d+.\d+", abv_t)[0]

        if abv <= 10:
            abv_lv = 1
        elif 10 <= abv <= 20:
            abv_lv = 2
        elif 20 <= abv <= 30:
            abv_lv = 3
        elif 30 <= abv <= 40:
            abv_lv = 4
        elif 40 <= abv <= 50:
            abv_lv = 5
        else: abv_lv = 6

    except Exception as e:
        abv = 0.0
        abv_lv = 1

    for ingredient in ingredients:
        ingredient_name = ingredient.get_text().strip().lower()

        cnt += 1

        if cnt % 2 != 1:
            in_cnt = '재료'
            if cnt == 2:

                try:
                    if ingredient_name.find("whiskey") != -1 :
                        main_base = "Whisky"
                    elif ingredient_name.find("brandy") != -1 :
                        main_base = "Brandy"
                    elif ingredient_name.find("gin") != -1 :
                        main_base = "Gin"
                    elif ingredient_name.find("rum") != -1:
                        main_base = "Rum"
                    elif ingredient_name.find("tequila") != -1 :
                        main_base = "Tequila"
                    elif ingredient_name.find("vodka") != -1 :
                        main_base = "Vodka"
                    else:
                        main_base = "Etc."
                except Exception as e:
                    main_base = "Etc."
        else :
            in_cnt = '양'
        recipe.append(ingredient_name)

    count += 1

    try:
        svg_ranges = soup.find_all("img", "svg-range__image")
        svg_range = svg_ranges[1]["alt"]
    except Exception as e:
        svg_range = 0

    cocktail_data = {
        "count" : count,
        "title" : title,
        "img_url" : img,
        "base" : main_base,
        "garnish" : garnish,
        "flavour" : svg_range,
        "abv_lv" : abv_lv,
        "abv" : abv,
        "recipe" : recipe
    }

    print(cocktail_data)
    with open("cocktail_data_file", 'a', encoding='utf-8') as json_file:
        json.dump(cocktail_data, json_file, indent=4)







# for link in landing_page_grid:
#     href = link.get('href')
#     print(href)




# cocktailList = list()
# for cocktail in cocktails:
#     cocktail = cocktail.text
#     cocktailList.append(cocktail)

# wrap_addresses = soup.select('#search-form > div.grid-x')
# addresses = wrap_addresses.find("a")['href']
# print(addresses)

# hrefs = [address.find("a")['href'] for address in landing_page_grid]
# print(hrefs)
