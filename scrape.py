from bs4 import BeautifulSoup
import urllib2
url="https://www.practo.com/bangalore/doctors?page=2"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
doctor=soup.findAll('img',{'class':'doc_avatar'})
for eachdoctor in doctor:
    print eachdoctor['alt']
