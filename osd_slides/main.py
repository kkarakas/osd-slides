import requests
from bs4 import BeautifulSoup
import sys
import subprocess

# TODO perhaps better to use properties file
#  using jproperties here instead of using a string.
url = "https://www.cs.columbia.edu/~paine/4995/lectures/"


class Downloader:
    def fefmalsmc(self):
        if len(sys.argv) >= 3:
            print("Too many arguments")
            # perhaps should throw an error or something

        elif len(sys.argv) < 2:
            print("Too few arguments")
        # length 2 acceptable
        else:
            if sys.argv[1] == "download":
                self.searchAndDownloadPdf()

            elif sys.argv[1] == "show":
                self.showDownloadablePdf()

    # TODO be able to download individual files
    def searchAndDownloadPdf(self):
        '''Downloads all the class presentations.

        Returns:
            Null
        '''
        docs = self.readAvailableHtmlDocs()

        for doc in docs:
            try:
                file = doc.find("a")["href"]
                # file = doc
                self.downloadPdf(file)
            except TypeError:
                pass

        print("done")

    def showDownloadablePdf(self):
        '''Shows all the downloaddable pdf's.

        Returns:
            Null
        '''
        docs = self.readAvailableHtmlDocs()

        for doc in docs:
            print(doc.find("a")["href"])
            # print(doc)

    def readAvailableHtmlDocs(self):
        # TODO handle when response is not 200
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        table_rows = table.find_all("tr")
        blacklist = {
            "example.html",
        }
        docs = []
        for row in table_rows:
            if row.find("a") and row.find("a")["href"].endswith(".html"):
                link = row.find("a")["href"]
                if link in blacklist:  # blacklisted
                    continue
                docs.append(row)
                # TODO we can change this to link to make it simpler

        return docs

    def downloadPdf(self, file):
        print("Downloading file: ", file)
        try:
            a = subprocess.run(
                ["npx", "decktape", "reveal", url + file + "#/", file[:-4] + "pdf"],  # noqa: E501
                capture_output=True,
                check=True,
            )
            print(a.stderr)
        except subprocess.CalledProcessError as exc:
            print("Standard error was {}".format(exc.stderr))

        # print(a.stdout)
        print("File ", file, " downloaded")
