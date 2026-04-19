import os
import csv
import time
import requests
from bs4 import BeautifulSoup

INVENTORS = [

"Thomas_Edison",
"Nikola_Tesla",
"Alexander_Graham_Bell",
"James_Watt",
"Alan_Turing",
"Tim_Berners-Lee",
"Johannes_Gutenberg",
"Leonardo_da_Vinci",
"Wright_brothers",
"Benjamin_Franklin"

]

OUTPUT_DIR="inventor_files"
MASTER_FILE="inventions_inventors_dataset.csv"


def scrape_page(name):

    url="https://en.wikipedia.org/wiki/"+name

    try:

        response=requests.get(url)

        soup=BeautifulSoup(
            response.text,
            "html.parser"
        )

        content=soup.find(
            "div",
            {"id":"mw-content-text"}
        )

        if content is None:
            return ""

        paragraphs=content.find_all("p")

        text=" ".join(
            p.get_text(
                strip=True
            )
            for p in paragraphs[:10]
        )

        return text

    except:

        return ""



def save_individual_files():

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    for inventor in INVENTORS:

        print(
            "Scraping:",
            inventor
        )

        text=scrape_page(
            inventor
        )

        filename=(
            inventor.lower()
            +".txt"
        )

        path=os.path.join(
            OUTPUT_DIR,
            filename
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)

        time.sleep(1)



def merge_files():

    with open(
        MASTER_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer=csv.writer(
            csvfile
        )

        writer.writerow(
            [
                "Inventor",
                "Text"
            ]
        )

        for file in os.listdir(
            OUTPUT_DIR
        ):

            if file.endswith(".txt"):

                with open(

                    os.path.join(
                        OUTPUT_DIR,
                        file
                    ),

                    "r",

                    encoding="utf-8"

                ) as f:

                    text=f.read()

                    writer.writerow(

                        [
                          file.replace(
                           ".txt",
                           ""
                          ),

                          text

                        ]

                    )



if __name__=="__main__":

    save_individual_files()

    merge_files()

    print(
      "Assignment Completed"
    )