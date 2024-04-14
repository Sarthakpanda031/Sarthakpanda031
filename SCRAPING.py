from bs4 import BeautifulSoup 
import html5lib as  ht
import requests as req 
#-----------------------------------------------------#
# url="https://www.gmuniversity.ac.in/"
url="https://www.gmuniversity.ac.in/programme-offered.php"

response=req.get(url)                                        # request is sent to website for fetching data
# print(response)                                            # complete page structure will be printed
soup=BeautifulSoup(response.content, "html.parser")          # MAKING THE SOUP FOR ALL THE TASKs
#-----------------------------------------------------#
# print(soup)
# print(soup.prettify)                                       # to see the content in a better way or pretty way
 
# title=soup.title
# print("Title of the webpage: ", title.string,"\n")
# print(title.parent.name)
# print(soup.p,"\n")
# print(soup.p['class'])

# paras=soup.find_all('p')
# print(paras)                                               # printing the <p> tagas in the page 

# print(soup.find('p'))                       # it will return the first paragraph tag  
# print(soup.find('p')['class'])              # it will show error as there is no class in paragraph extracted

# To find elements with class lead
# print(soup.find_all('p',class_= "lead"))    # it will return all the <p> tags which has class lead

# print(soup.find('p').get_text())            # get text inside the <p> and remove any leading/trailing spaces 


#-------------------------------------------#
'''
print(soup.get_text())                      # Get the text out of HTML tags - strip=True removes any leading/trailing space
anchors=soup.find_all('a')
print(anchors)                              # returns all the anchor tags of the link specified
Net_links=set()
for link in anchors:
    lnk=link.get('href')                       # getting href
    Net_links.add(lnk)                         # adding each link into set
i=1
for l in Net_links:                          # SET taken for non duplicating values
    print(i,". ",l,"\n")                     # printing all the unique links present on the web page
    i+=1
'''
#--------------------------------------------#
# nav_bar=soup.find(id='divcontent')
# print(nav_bar.children)

programs=soup.find_all("div", class_="point")           # finding names of programs offered by university
# for program in programs:
#     print(program.text)
# print(programs)

# for program in programs:                              # GETTING links of each department
#     anchors = program.find_all("a")
#     for anchor in anchors:
#         print(anchor.get("href"))

#-------------------------------------------------------------#
# structured  formnated link with department name
i=0
for program in programs:
    
    links = program.find_all("a")
    for link in links:
        i=i+1
        link_name = link.text
        link_url = link.get("href")
        print(i,link_name) 

#--------------------------------------------------------------#

