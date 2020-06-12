
import bs4
import requests as rq

########################PARSING HTML FROM A LOCAL SOURCE########################

# First we get our files encoding
enc = open('D:\\Test GB Python\\Corey Schafer_Tutorials\Web_scraping\\CoreyMS - Development, Design, DIY, and more.html', 'r',).encoding

# We open the file and create a BeautifulSoup object
with open('D:\\Test GB Python\\Corey Schafer_Tutorials\Web_scraping\\CoreyMS - Development, Design, DIY, and more.html', 'r', encoding=f'{enc}', errors='ignore') as html_file:

    soup = bs4.BeautifulSoup(html_file, 'lxml')  # BeautifulSoup object with 'lxml' parser

# print(soup.prettify())  # Prettify method, allows us to get a readable object

match = soup.title.text  # Accessing the title tag(shows ONLY the first tag),
                         # and presenting the text, with the '.text' attribute.
# print(match)

# Searching for a tag, with a specific tag -ie social-links-li, we use the
# method find

st_match = soup.find('li', class_='social-links-li')

# print(st_match)

path_m = st_match.a.path # From our FIRST li with class = 'social-links-li',
                         # we access the FIRST tag a and
                         # within that tag we access the tag path
# print(path_m)
################################################################################
# Now if we want to have all our tags with a specific class, we use the
# find_all method, witch returns a list. So we can loop over.

st_matches = soup.find_all('li', class_='social-links-li')

for s_match in st_matches:
    path_m = s_match.a.path
    # print(path_m)
    # print() # Having a blank line between our results

#########################PARSING HTML FROM A LIVE SITE##########################

# html_file = rq.get('http://coreyms.com').text # We add the '.text' attribute
                                    # because otherwise it will return only the
                                    # servers response and not the html source
                                    # code that we want
# Creating a BeautifulSoup object

# soup = bs4.BeautifulSoup(html_file, 'lxml')

# Now, since we have the excact same html file in source, in order not to
# overwelm the sites server, we comment out the above connection
################################################################################

article = soup.find('article')  # Finding the first tag article in our object
# print(article.prettify())

# By looking at the printed html, we see that we have an h2 tag and
# within that tag, there is an <a> anchor witch helds our title
# in order to get that title we perform the following:

headline = article.h2.a.text
# print(headline)

# By again inspecting our article object, we see that the summary is inside
# a div tag with class="entry-content", and a <p> anchor
# So, for us to get that text we perform the following:

summary = article.find('div', class_='entry-content').p.text
# print(summary)

# Finally we want the videos link. For that, again we inspect our article object
# Since the videos are embeded we do not need to have the whole url, but only
# the video's id. To get that we must find inside our object the iframe tag.
# We will access this tag as a dictionary and retieve the 'src' attribute.
# After that we will perfom some string manipulation so to get
# the "src" element and again another manipulation to get the id.
# Since it is not quarnteed that the link will be there, the whole proccess
# will be encapsulated in a try-except block

try:
    vid_scr = article.find('iframe', class_='youtube-player')['src']  # Dictionary access
    # print(vid_scr)  # Since the url is redirecting in the local source file is
                    # under a new file and it's not presenting as we want it
                    # so for this purpose we will assing manualy the url to the
                    # vid_scr variable

    vid_scr = 'https://www.youtube.com/embed/       z0gguhEmWiY?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_lo   ad_policy=1&wmode=transparent'

# The video's id is after the 'embed/' and before the '?'

    vid_id = vid_scr.split('/')[-1]  # This gives us a list with the last element
                                    # the video's id and some metadata
                                    # so we retrieve that value with the index [-1]

# Now for us to have the value that we want, we perform another split
    vid_id = vid_id.split('?')[0]

# The standard yt url for a video has the format:
# https://youtube.com/watch?v="video id"

    yt_link = f'https://youtube.com/watch?v={vid_id.strip()}'

except Exception as e:
    yt_link = None

print(yt_link)
################################SAVING TO A CSV#################################
# In order to have the above's proccess saved in a csv file
# we would have to use the find_all() in the article search. So as we saw earlier
# a list would be returned and we could looped over it, passing all the searched
# values in our csv file.
