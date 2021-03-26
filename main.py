# import codecademylib3_seaborn
from bs4 import BeautifulSoup       # імпортуэмо потрібні бібліотеки
import requests                     # імпортуэмо потрібні бібліотеки
# підготовчы роботи
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
webpage = webpage_response.content
# загружаємо у вигляді HTML коду всю сторінку сайту
soup = BeautifulSoup(webpage, "html.parser")
# закінчили підготовчы роботи
table_str = ["Company", "Origin", "REF", "ReviewDate", "CocoaPercent", "CompanyLocation", "Rating", "BeanType",
             "BroadBeanOrigin"]
table = [[], [], [], [], [], [], [], [], []]
for i, clas in enumerate(table_str):
    # через select вибираємо рядки які містять як class значення задане в даному випадку змінною clas
    # та крапка перед фігурними дужками необхідна вона означає, що шукаємо свме в class
    for line in soup.select(".{}".format(clas)):
        # доюавляємо до таблиці значення тексту закріпленого за class знайденого в попередньому рядку
            table[i].append(line.text)

print("tabl", table)
