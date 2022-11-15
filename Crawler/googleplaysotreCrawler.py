import os

import pandas as pd
from google_play_scraper import Sort, reviews

tmp = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(tmp, "data")
if "data" not in os.listdir(tmp):
    os.mkdir(data_dir)


def main(id, lang, country, title, count=100000):
    result, continuation_token = reviews(
        id,
        lang=lang,  # default: 'en'
        country=country,  # default: 'us'
        sort=Sort.MOST_RELEVANT,  # default: Sort.MOST_RELEVANT
        count=count,  # default: 100
        filter_score_with=5,  # default: None (모든 평점을 다 가져옴)
    )

    playstore_list = []
    for r in result:
        temp_list = [
            r["userName"],
            r["content"],
            r["score"],
            r["thumbsUpCount"],
            r["at"].date().isoformat(),
            r["reviewCreatedVersion"],
            r["reviewId"],
        ]
        playstore_list.append(temp_list)

    df = pd.DataFrame(
        playstore_list,
        columns=[
            "userName",
            "content",
            "score",
            "thumbsUpCount",
            "at",
            "reviewCreatedVersion",
            "reviewId",
        ],
    )

    df.to_csv(
        os.path.join(data_dir, "{}_googlePlayStoreReview.csv".format(title)),
        index=False,
        encoding="utf-8-sig",
    )
    print("저장되었습니다.")


id = input("아이디를 입력하세요. : ")
print("1. 한국,한글\n2. 일본,일본어\n(디폴트: 미국, 영어)")
num = int(input("설정할 번호를 입력하세요"))
if num == 1:
    country, lang = "kr", "ko"
elif num == 2:
    country, lang = "jp", "ja"
else:
    country, lang = "us", "en"

count = int(input("최대 리뷰 개수를 입력하시오(기본:10000개) : "))
title = input("저장할 파일 제목을 입력하시오.")

if __name__ == "__main__":
    main(id, lang, country, title, count)
