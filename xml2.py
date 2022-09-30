import xml.etree.ElementTree as x
data='''<staff>
<student>
<person>
<name z='1310'>Hasibul</name>
<phn type="intl">+88017567666</phn>
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
</student>
</staff>'''
infoall= x.fromstring(data)
all=infoall.findall("student/person")
print(len(all))
print(all)
for allin in all:
 print(f"Name: {allin.find('name').text}")
 print(f"Phone: {allin.find('phn').text}")
 print(f"Attr: {allin.find('email').get('hide')}")#get the child attribute
 print(f"Attribute: {allin.get('z')}")