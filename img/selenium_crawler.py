from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib.request

def crawler(sendkey):
    driver=webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get('https://naver.com')
    driver.find_element_by_xpath('//*[@id="query"]').send_keys(sendkey)
    driver.find_element_by_xpath('//*[@id="search_btn"]/span[2]').click()
    driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a/span').click()
    link=[]

    try:
        for i in range(1,100):
            time.sleep(2)
            for j in range(1, 10000):
                time.sleep(0.5)
                try:
                    img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div['+str(i+1)+']/div[' + str(j) + ']/a[1]/img')
                    link.append(img.get_attribute('src'))
                except:
                    break

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            if i%6==0:
                driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div['+str(i+2)+']/a').click()
    except:
        print("1번끝")

    print(link)
    count=1
    for i in link:
        print("link["+str(count-1)+"] : "+link[count-1])
        count+=1
        urllib.request.urlretrieve(i,'test/'+sendkey+str(count)+".jpg")










##############naver.com 실패#####################
# try:
#     for i in range(1,100):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(3)
#         if i%6==0:
#             driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div['+str(i+2)+']/a').click()
# except:
#     html=driver.page_source
#
# print(html)
# bs_html=BeautifulSoup(html,"html.parser")
# photowall = bs_html.find('div',{"class":"photowall"})
# img_list = photowall.find_all("img",{"class":"_img"})
#
# try:
#     for i in range(10000):
#         img_link=img_list[i]['src']
#         img_con=requests.get(img_link).content
#         file=open("test/"+i+".jpg",'wb')
#         file.write(img_con)
#         file.close()
# except:
#     print("종료!")
#########google.com#########
#driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('팰리세이드')
#driver.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]').click()
#driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()
#for i in range(100):
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#    time.sleep(3)

