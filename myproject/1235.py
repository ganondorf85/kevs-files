import urllib2

req = urllib2.Request('http://my.pretend.org.uk')
response = urllib2.urlopen(req)
the_page = response.read()