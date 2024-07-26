def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    
    key = "ffdb3d192c4143329758e5d3a56d7d0c"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)




