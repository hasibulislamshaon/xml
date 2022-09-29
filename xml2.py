import xml.etree.ElementTree as x
data='''<student>
<person><name>Hasibul</name>
<phn type="intl">+8801756764966</phn>
<email hide="No"/>
</person>
<person><name>Polok</name>
<phn type="intl">+880173333</phn>
<email hide="No"/>
</person>
<person><name>Belai</name>
<phn type="intl">+880175#####</phn>
<email hide="No"/>
</person>
<person><name>jim</name>
<phn type="intl">+88017****</phn>
<email hide="No"/>
</person>
</student>'''
infoall= x.fromstring(data)
all=infoall.findall("student/person")
print(len(all))
"""for allin in all:
 print(f"Name: {allin.find('name').text}")
 print(f"Phone: {allin.find('phn').text}")
 print(f"Attr: {allin.find('email').get('hide')}")#get the child attribute
 """