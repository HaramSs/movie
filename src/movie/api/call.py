import requests
import os
import pandas as pd

def save2df(load_dt='20120101'):
    """airflow 호출 지점"""
    df = list2df(load_dt)
    # df 에 load_dt 컬럼 추가 (조회 일자 YYYYMMDD 형식으로)
    # 아래 파일 저장시 load_dt 기본으로 파티셔닝
    df['load_dt']= '20120101'
    print(df.head(5))
    df.to_parquet('~/tmp/test_parquet', partition_cols=['load_dt'])
    return df

def list2df(load_dt='20120101'):
    l = req2list()
    df = pd.DataFrame(l)
    return df

def req2list(load_dt='20120101') -> list:
    _, data = req()
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(load_dt='20120101'):
    
    url = gen_url(load_dt)

    r = requests.get(url)
    
    code = r.status_code
    
    data = r.json()
    
    return [code, data]

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url
