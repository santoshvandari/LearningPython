import pyshorteners
s = pyshorteners.Shortener()
 
#Chilp.it
s.chilpit.short('http://www.google.com')    # gives output -> 'http://chilp.it/TEST'
s.chilpit.expand('http://chilp.it/TEST')
 
# Adf.ly
s = pyshorteners.Shortener(api_key='YOUR_KEY', user_id='USER_ID', domain='test.us', group_id=12, type='int')
s.adfly.short('http://www.google.com')    # gives output -> 'http://test.us/TEST'
 
#Git.io
s = pyshorteners.Shortener(code='12345')
s.gitio.short('https://github.com/TEST')     # gives output -> 'https://git.io/12345'
s.gitio.expand('https://git.io/12345')
 
#and many more services are supported