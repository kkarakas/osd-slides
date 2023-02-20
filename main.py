import requests
from bs4 import BeautifulSoup
import sys

def downloadPdf():
    # TODO perhaps better to use properties file using jproperties here instead of using a string.
    url = "https://www.cs.columbia.edu/~paine/4995/lectures/"
    # TODO keeping track of when it was downloaded (it will be written on pdf
    # TODO handle when response is not 200
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    table_rows = table.find_all('tr')

    for i in range(3, len(table_rows)-4): #fixme this will lead to errors as the number of files might change
        #instead of above one must check wheather each row contains viable rows
        try:
            file = table_rows[i].find('a')['href']
            download(url,file)
        except:
            pass

    print("done")

def download(url,file):
    #TODO like said above, url must be a global variable read through properties

    # info such as when downloaded can be extracted here
    print("Downloading file: ", file)

    response = requests.get(url + file + "?print-pdf=true")

    # Write content in pdf file
    pdf = open(file + ".pdf", 'wb')
    pdf.write(response.content)
    pdf.close()
    print("File ", file, " downloaded")




def main():
    if len(sys.argv) > 2:
        print("Too many arguments")

    if sys.argv[1] == "download":
        downloadPdf()


if __name__ == "__main__":
    #TODO dont know how package this python code into a service run from terminal this will do for now
    main()