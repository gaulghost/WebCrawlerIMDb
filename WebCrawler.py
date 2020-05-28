import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Web crawler of IMDb.')
user = input('Input the Movie/Series you want to find the ratings of : ')

#IMDb starting url
imdbini = 'https://www.imdb.com/find?q='
#IMDb ending url
imdbend = '&ref_=nv_sr_sm'

userwords = user.split()
# fin is the final input to be searched in url
fin = ''
for i in userwords :
    fin = fin + i + '+'
usersearch = fin[:-1]

print('\nSearching...')

url = imdbini + usersearch + imdbend
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print('\nResult : ')

# Retriving all of the list
i = 1
tag1 = soup.find('table', class_ = 'findList')
for line in tag1.findAll('td', class_ = 'result_text'):
    for letter in line.find('a'):
        print(i,letter.string)
        i += 1

usernext = input('Select one of the movie/series from the given list : ')
j = 1
for line in tag1.findAll('td', class_ = 'result_text'):
    for letter in line.find('a'):
        if int(usernext) == j :
            print(letter)
            # nurl = letter.href.string
        j += 1
        # print(line.find_all(re.compile(".*\((.+)\).*")))

# print('\n this is nurl', nurl, '\n')
#
# html = urllib.request.urlopen(nurl, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
# print('The reviews for selected item are : ')
# tags = soup.find('div', class_ = 'title_bar_wrapper')
# for tag in tags:
#     for ta in tag.findAll('div', class_ = 'ratingValue'):
#         for t in ta.find('strong'):
#             print(tag.title.string)
