import json
import re  # 파이썬 정규표현식 라이브러리
from bs4 import BeautifulSoup
import requests


def extract_cocktail_collection(url):
    page_detail = requests.get(url)
    soup = BeautifulSoup(page_detail.text, "html.parser")

    # 크롤링으로 수집 가능 정보↓
    # <script>태그 안 JSON에 저장된 정보
    cocktail_page = soup.find("script", {"type": "application/ld+json"})
    string_cocktail_page = cocktail_page.text  # HTML 요소 내 JSON으로 작성된 부분 문자열화
    dict_result = json.loads(string_cocktail_page)  # 문자열화한 결과를 다시 JSON으로 변환

    # 칵테일 이름
    name = dict_result['name']
    # 이미지url
    img = dict_result['image']
    # 부재료(=가니쉬)
    cells = soup.find_all("div", {"class": "cell"})
    paragraphs = []
    for cell in cells:
        p = cell.find("p", {"class": ""})
        if p is not None:
            paragraphs.append(p)
    garnish = paragraphs[0].text
    # 맛
    try:
        flavor_chart = soup.find("div", {"class": "grid-x align-justify"}).find("img")
        flavor = int(flavor_chart["alt"])
    except:
        flavor = 0  # flavor 척도 없는 경우의 예외 처리
    # 상세도수
    alcohol_content = soup.find("ul", {"class": "no-margin-bottom"}).find_all("li")
    abv = alcohol_content[1].get_text()
    # floats_in_ab_v = re.findall("\d+.\d+", abv)  # 정규표현식으로 AbV라는 문자열 안에 있는 숫자 추출
    # alc_by_vol = float(floats_in_ab_v[0])  # 추출한 숫자의 자료형: 문자열>실수 로 변환
    # 도수(범주형)
    try:
        alc_by_vol = float(re.findall("\d+.\d+", abv)[0])

        if alc_by_vol <= 10.0:
            abv_lv = 1
        elif 10.0 <= alc_by_vol <= 20.0:
            abv_lv = 2
        elif 20.0 <= alc_by_vol <= 30.0:
            abv_lv = 3
        elif 30.0 <= alc_by_vol <= 40.0:
            abv_lv = 4
        elif 40.0 <= alc_by_vol <= 50.0:
            abv_lv = 5
        else:
            abv_lv = 6
    except Exception as e:
        alc_by_vol = 0.0
        abv_lv = 1

    # 레시피 재료
    ingredients_origin = dict_result['recipeIngredient']
    # 레시피
    recipe = dict_result['recipeInstructions'][0]['text']

    ingredients = list()
    print(name)
    try:
        cnt = 0

        for ingredient in ingredients_origin:

            if ingredient.find("ml") != -1:
                ingredient_amount = ingredient.split('ml ')[0]
                ingredient_name = ingredient.split('ml ')[1].lower()
                ingredients.append(ingredient_amount + 'ml ')
                cnt += 1
                if cnt == 1:
                    if ingredient_name.find("whiskey") != -1:
                        main_base = "Whisky"
                    elif ingredient_name.find("brandy") != -1:
                        main_base = "Brandy"
                    elif ingredient_name.find("gin") != -1:
                        main_base = "Gin"
                    elif ingredient_name.find("rum") != -1:
                        main_base = "Rum"
                    elif ingredient_name.find("tequila") != -1:
                        main_base = "Tequila"
                    elif ingredient_name.find("vodka") != -1:
                        main_base = "Vodka"
                    else:
                        main_base = "Etc."
                ingredients.append(ingredient_name)

            elif ingredient.find("leaves") != -1:
                items = re.split('(\d+) ', ingredient)
                ingredient_amount = items[1]
                ingredient_name = items[2]
                ingredients.append(ingredient_amount + ' fresh')
                ingredients.append(ingredient_name)
            elif ingredient.find("bitters") != -1 or ingredient.find("solution") != -1:
                # match = re.match(r"([0-9]+)([a-z]+)", ingredient, re.I)
                items = re.split('(\d+) ', ingredient)
                ingredient_amount = items[1]
                ingredient_name = items[2]
                ingredients.append(ingredient_amount + ' drop')
                ingredients.append(ingredient_name)
            elif ingredient.find("jam") != -1:
                items = re.split('/(\d+) ', ingredient)
                ingredient_amount = items[0] + '/' + items[1] + ' spoon'
                ingredient_name = items[2]
                ingredients.append(ingredient_amount)
                ingredients.append(ingredient_name)
            #     items = re.split('(\d+)', ingredient)
            #     ingredient_amount = items[1]
            #     ingredient_name = items[2]
            #     ingredients.append(ingredient_amount + ' drop')
            #     ingredients.append(ingredient_name)
            # elif ingredient.find("spoon") != -1:
            #     ingredient_amount = ingredient.split(sep='spoon')[0]
            #     ingredient_name = ingredient.split(sep='spoon')[1]
            #     ingredients.append(ingredient_amount + 'spoon')
            # elif ingredient.find("fresh") != -1:
            #     ingredient_amount = ingredient.split(sep='fresh')[0]
            #     ingredient_name = ingredient.split(sep='fresh')[1]
            #     ingredients.append(ingredient_amount + 'fresh')


            else:
                ingredients.append(ingredient)



    except Exception as e:
        print("** Exception 발생!!!!!!!!!!!!!!", e)

    cocktail_data = {
        "name": name,
        "img": img,
        "base": main_base,
        "garnish": garnish,
        "flavor": flavor,
        "abv": alc_by_vol,
        "abv_lv": abv_lv,
        "ingredients": ingredients,
        "recipe": recipe
    }
    print(cocktail_data)
    with open("cocktail_data_file", 'a', encoding='utf-8') as json_file:
        json.dump(cocktail_data, json_file, indent=4)
