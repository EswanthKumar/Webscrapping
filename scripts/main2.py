import requests
from bs4 import BeautifulSoup


main_link = 'https://www.imdb.com/chart/top/'
heads = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(main_link, headers=heads)
if response.status_code == 200:
    name = []
    year = []
    length = []
    certificate = []
    rating = []
    rated = []

    soup = BeautifulSoup(response.text, 'html.parser')
    main_div = soup.find('ul', class_ = 'ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 dHaCOW compact-list-view ipc-metadata-list--base')
    articles = main_div.find_all('li', class_ = 'ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent')
    # print(articles)
    print(len(articles))

    for article in articles:
        # print(article)
        cur_name = article.find('h3')
        cur_name = cur_name.text
        name.append(cur_name)

        year_len_div = article.find('div', class_ = 'sc-b189961a-7 btCcOY cli-title-metadata')
        spans = year_len_div.find_all('span')
        cur_year = spans[0].text
        cur_len = spans[1].text
        cur_certi = spans[2].text
        year.append(cur_year)
        length.append(cur_len)
        certificate.append(cur_certi)

        rating_div = article.find('div', class_ = 'sc-e2dbc1a3-0 jeHPdh sc-b189961a-2 bglYHz cli-ratings-container')
        cur_rating = rating_div.find('span', class_= 'ipc-rating-star--rating')
        cur_rating = (cur_rating.text)
        rating.append(cur_rating)

        cur_rated = rating_div.find('span', class_ = 'ipc-rating-star--voteCount')
        cur_rated = cur_rated.text
        rated.append(cur_rated)
        # break
    
    print(name, "\n\n", year, "\n\n", length, "\n\n", certificate, "\n\n", rating, "\n\n", rated)
    print(len(name), len(year), len(length), len(certificate), len(rating), len(rated))

else:
    print("Failed", response.status_code)