import os
from pprint import pprint

# 1. 구글번역 라이브러리를 가져옵니다.
import googletrans
import pandas as pd
import requests
import xmltodict
from tqdm import tqdm, tqdm_pandas

# 2. 번역기 객체를 생성합니다.
translator = googletrans.Translator()

# 진행률 체크를 위한 조치
tqdm.pandas()


def get_googleTranslate(inStr):
    answer = str(inStr)
    try:
        # 4. 라이브러리를 사용하여 번역합니다.
        outStr = translator.translate(inStr, dest="ko", src="auto")
        answer = str(outStr.text)
    except Exception as e:
        print(e)
    return answer


def get_url_index(url):
    #  requests에 response에 대해서 한글 깨짐을 방지하기 위해서 UTF8로 decoding
    response = requests.get(url).content.decode("utf8")
    # xml 을 dict로 변환
    xml = xmltodict.parse(response)

    # 사용자 리뷰 Page의  last Index 가져오기
    last_url = [l["@href"] for l in xml["feed"]["link"] if (l["@rel"] == "last")][0]
    last_index = [
        int(s.replace("page=", "")) for s in last_url.split("/") if ("page=" in s)
    ][0]

    return last_index


# https://stackoverflow.com/questions/1090282/api-to-monitor-iphone-app-store-reviews
# AppStore에서 Review 전체를 가져오는 함수
def appstore_crawler(appid, region="kr", outfile="./appstore_reviews.csv"):
    url = "https://itunes.apple.com/{0}/rss/customerreviews/page=1/id={1}/sortby=mostrecent/xml".format(
        region, str(appid)
    )

    # 예외 처리 1:  Review가 전혀 없는 경우
    try:
        last_index = get_url_index(url)
    except Exception as e:
        print(url)
        print("\tNo Reviews: appid %i" % appid)
        print("\tException:", e)
        return

    # Apple RSS Feed URL을 Page 1 ~ last index page까지 Iteration
    result = list()
    for idx in range(1, last_index + 1):
        url = "https://itunes.apple.com/{0}/rss/customerreviews/page={1}/id={2}/sortby=mostrecent/xml?urlDesc=/customerreviews/id={3}/sortBy=mostRecent/xml".format(
            region, str(idx), str(appid), str(appid)
        )
        print(url)

        # 사용자 리뷰 xlm을 다운로드  (한글 깨짐 방지를 위해서 utf8로 인코딩)
        response = requests.get(url).content.decode("utf8")

        # xml을  dict로 변환, Apple Site에서 xml이 깨져 있는 경우가 있어  예외처리 추가
        try:
            xml = xmltodict.parse(response)
        except Exception as e:
            print("\tXml Parse Error %s\n\tSkip %s :" % (e, url))
            continue
        # 사용자 Review가 존재하는지 확인, 리뷰가 없으면 이후 처리를 하지 않음
        try:
            num_reivews = len(xml["feed"]["entry"])
        except Exception as e:
            print("\tNo Entry", e)
            continue

        # 사용자 리뷰가 단 1개인 경우 XML 처리 시 에러 발생 방지
        try:
            xml["feed"]["entry"][0]["author"]["name"]
            single_reviews = False
        except:
            # print ('\tOnly 1 review!!!')
            single_reviews = True
            pass

        # 사용자 리뷰를 list에 저장
        if single_reviews:
            result.append(
                {
                    "USER": xml["feed"]["entry"]["author"]["name"],
                    "DATE": xml["feed"]["entry"]["updated"],
                    "STAR": int(xml["feed"]["entry"]["im:rating"]),
                    "LIKE": int(xml["feed"]["entry"]["im:voteSum"]),
                    "TITLE": xml["feed"]["entry"]["title"],
                    "REVIEW": xml["feed"]["entry"]["content"][0]["#text"],
                }
            )
        else:
            for i in range(len(xml["feed"]["entry"])):
                result.append(
                    {
                        "USER": xml["feed"]["entry"][i]["author"]["name"],
                        "DATE": xml["feed"]["entry"][i]["updated"],
                        "STAR": int(xml["feed"]["entry"][i]["im:rating"]),
                        "LIKE": int(xml["feed"]["entry"][i]["im:voteSum"]),
                        "TITLE": xml["feed"]["entry"][i]["title"],
                        "REVIEW": xml["feed"]["entry"][i]["content"][0]["#text"],
                    }
                )

    # 사용자 리뷰 결과 list를 DataFrame을 생성
    res_df = pd.DataFrame(result)

    # DATE Column은 String에서 Dataframe의 Date로 변환
    res_df["DATE"] = pd.to_datetime(res_df["DATE"], format="%Y-%m-%dT%H:%M:%S")
    if region != "kr":
        res_df["TITLE_KO"] = res_df["TITLE"].progress_apply(get_googleTranslate)
        res_df["REVIEW_KO"] = res_df["REVIEW"].progress_apply(get_googleTranslate)
    # CSV  파일로 저장, 한글 깨짐을 방지하고 위해서 'utf-8-sig'로 저장, Index column은 저장하지 않음
    res_df.to_csv(outfile, encoding="utf-8-sig", index=False)
    print("Save reviews to file: %s \n" % (outfile))


if __name__ == "__main__":
    appName = input("크롤링해올 앱의 이름을 입력하시오. : ")
    app_id = int(input("앱의 ID를 입력하시오. : "))
    countryList = "Korea : kr\nJapan: jp \nUSA: us"
    print(countryList)
    country = input("국가 코드를 입력하시오. : ")

    tmp = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(tmp, "data")
    if "data" not in os.listdir(tmp):
        os.mkdir(data_dir)

    title = input("저장할 파일 제목을 입력하시오.")

    outfile = os.path.join(
        data_dir, "{}_AppStoreReview.csv".format(title)
    )  # 자신의 컴퓨터에 맞게 변경

    appstore_crawler(app_id, country, outfile=outfile)
