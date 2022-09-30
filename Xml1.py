import xml.etree.ElementTree as x
data='''<person><name>Hasibul</name>
<phn type="intl">+8801756746</phn>
<email hide="No"/>
</person>'''
infoHasibul= x.fromstring(data)
print(f"Name: {infoHasibul.find('name').text}")
print(f"Phone: {infoHasibul.find('phn').text}")
print(f"Attr: {infoHasibul.find('email').get('hide')}")#get the child attribute
print(f"Email: {infoHasibul.find('email').text}")