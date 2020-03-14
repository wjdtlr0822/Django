import re
#import requests
#from bs4 import BeautifulSoup

#url="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=자동차"
#html = requests.get(url)
#bs_html = BeautifulSoup(html.content,"html.parser")
#img_list = bs_html.find_all(bs_html,class_='_img')
#print(img_list)


# img_src=img_list['data-source']
# print(img_list1)
# for i in range(len(img_list)):
#for i in range(100):
#    img_link = re.findall('data-source="(.+?)"',str(img_list[i]))[0]
#    img_con = requests.get(img_link).content
#    file = open("search_img/"+'자동차'+str(i+1)+".jpg","wb")
#    file.write(img_con)
#    file.close()
#    print(img_link)


import re
import requests
from bs4 import BeautifulSoup

no=100
keyword='자동차'
url="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+keyword
html = requests.get(url)
bs_html = BeautifulSoup(html.content,"html.parser")
photowall = bs_html.find('div',{"class":"photowall"})
img_list = photowall.find_all("img",{"class":"_img"})
#for i in range(1,11):
#    print(img_list[i]['data-source'])
# for i in range(len(img_list)):
for i in range(no):
    img_link = img_list[i]['data-source']
    img_con = requests.get(img_link).content
    file = open("search_img/"+keyword+str(i+1)+".jpg","wb")
    file.write(img_con)
    file.close()
