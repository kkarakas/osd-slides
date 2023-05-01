from bs4 import BeautifulSoup
import requests
from collections import defaultdict
import re
import webbrowser
class Search:
    #hash algorithms to library
    #Boyer Moore algorithm or KMP could be used
    #https://stackoverflow.com/questions/56418773/when-is-rabin-karp-more-effective-than-kmp-or-boyer-moore
    #or a custom page hash

    def __init__(self, url, slides=[]):
        self.text = [defaultdict(dict)] * len(slides)
        self.answers = []
        self.slides = slides
        self.url = url # TODO this should be read from properties file

        for z,slide in enumerate(slides):
            response = requests.get(url+slide)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find("div", class_="slides")
            sections = table.find_all("section", attrs={'data-markdown': True})

            for idx, section in enumerate(sections):

                if "data-separator" in section.attrs:
                    seperator = section["data-separator"]
                    non_seperated_text = section.contents[1].text #current all the stuff

                    seperated_text = non_seperated_text.split(seperator)
                    for yindx, individual_text in enumerate(seperated_text):
                        temp = re.sub("(<!--.*?-->)", "",individual_text, flags=re.DOTALL) # removes html comments
                        self.text[z][idx][yindx] = re.sub(r"\s+", " ", temp).strip() # removes empty spaces
                else: # only has one page in that
                    # section.contents[1].text.remove('\n')
                    # self.text[idx][0] = section.contents[1].extract()
                    temp = re.sub("(<!--.*?-->)", "",  section.contents[1].text, flags=re.DOTALL) # removes html comments
                    self.text[z][idx][0] = re.sub(r"\s+", " ", temp).strip() # removes empty spaces
            print(self.text)
            #clean_text = re.sub(r"\s+", " ", text).strip()
            #https://stackoverflow.com/questions/761824/python-how-to-convert-markdown-formatted-text-to-text
            #TODO remove markdown stuff
    def lookup(self,keyword):
        #it will look up the word in the dict and come up with possible answers
        for i in range(len(self.text)):
            for idx,outer in self.text[i].items():
                for yidx, inner in outer.items():
                    if keyword in inner:
                        self.answers.append(tuple([idx, yidx, self.slides[i]]))

        print("Slides that can be found are")
        print(self.answers)
        # TODO perhpas make all lowercase
    def open(self,idx = 0): #open up that website
        if not self.answers:
            raise FileNotFoundError("Lookup not performed in order to open")

        webbrowser.open("{}{}#/{}/{}".format(self.url, self.answers[idx][2], self.answers[idx][0], self.answers[idx][1]))

