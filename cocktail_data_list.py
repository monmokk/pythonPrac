from bs4 import BeautifulSoup
import requests
from cocktail_data_detail import extract_cocktail_collection

page_1 = "https://www.diffordsguide.com/cocktails/search?include%5Bdg%5D=1&limit=20&sort=rating&offset=0"
page_3 = "https://www.diffordsguide.com/cocktails/search?include%5Bdg%5D=1&limit=20&sort=rating&offset=40"
soup = BeautifulSoup(requests.get(page_1).text, "html.parser")
grid = soup.find("div", {"class": "grid-x grid-margin-x grid-margin-y landing-page-grid"})
anchors = grid.find_all("a")
links = []
for anchor in anchors[1:]: #칵테일별 상세페이지로 연결되지 않는 0번째 요소 제거
    hrefs = f"https://www.diffordsguide.com{anchor['href']}"
    links.append(hrefs)

for link in links:
    extract_cocktail_collection(link)




