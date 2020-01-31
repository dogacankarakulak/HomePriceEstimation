from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("https://www.sahibinden.com/satilik-daire/istanbul-kadikoy?pagingOffset=")
url = "https://www.sahibinden.com/satilik-daire/istanbul-kadikoy?pagingOffset="

time.sleep(1)
elements5=[]
entries = []
a=0
BG=[]
while a <= 980:
    elements7 = []
    K = []
    elements2 = []
    ca = []
    R = 0
    beşli = 0
    newUrl= url + str(a)
    browser.get(newUrl)

    elements1 = browser.find_elements_by_css_selector("td.searchResultsPriceValue")
    abc = browser.find_elements_by_css_selector("td.searchResultsAttributeValue")
    elements3 = browser.find_elements_by_css_selector("td.searchResultsDateValue")
    elements4 = browser.find_elements_by_css_selector("td.searchResultsLocationValue")

    for i in abc:
        i = i.text
        ca.append(i)

    while R <= (len(ca)-1):
        list = ca[R] + " ," + ca[R + 1]
        elements2.append(list)
        R = R + 2

    for element1,element2,element3,element4 in zip(elements1,elements2,elements3,elements4):
        element1 = element1.text
        element3 = element3.text
        element4 = element4.text

        element3 = element3.strip()
        element3 = element3.replace("\n", "")

        element2 = element2.strip()
        element2 = element2.replace("\n", "")

        element1 = element1.strip()
        element1 = element1.replace("\n", "")

        element4 = element4.strip()
        element4 = element4.replace("\n", "")
        entry = ("{},{},{},{}".format(element1,element2,element3,element4))
        entries.append(entry)

    urlye_git = browser.find_elements_by_class_name("classifiedTitle")
    for i in urlye_git:
        K.append(i.get_attribute('href'))

    for j in K:
        browser.get(j)
        J = browser.find_elements_by_css_selector("ul.classifiedInfoList")
        for j in J:
            j = j.text
            j = j.split()

            try:
                g = j.index("Bulunduğu")
                elements5.append(j[g + 2])
            except (ValueError, IndexError):

                elements5.append("")

            try:
                g = j.index("Isıtma")
                elements5.append(j[g + 1])
            except (ValueError, IndexError):

                elements5.append("")

            try:
                g = j.index("İçerisinde")
                elements5.append(j[g + 1])
            except (ValueError, IndexError):

                elements5.append("")

            try:
                g = j.index("Yaşı")
                elements5.append(j[g + 1])
            except (ValueError, IndexError):

                elements5.append("")

    while beşli <= (len(elements5)-1):
        list = elements5[beşli] + " ," + elements5[beşli + 1]+ ", "+ elements5[beşli+2] + " ," + elements5[beşli + 3]
        elements7.append(list)
        beşli = beşli + 4

    a = a + 20
for i,j in zip(entries,elements7):
    H=i+","+j
    BG.append(H)
print(BG)

with open("kadikoy.txt","a",encoding = "UTF-8") as file:
    for i in BG:
        file.write(i)
        file.write("\n")

browser.close()