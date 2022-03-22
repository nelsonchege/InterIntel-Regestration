import xml.etree.ElementTree as ETree

tree = ETree.parse("SOAP.xml")

root = tree.getroot()

# adding an element to xml file
# method 1
body1 = ETree.fromstring("<body>added this body element from code</body>")
root.append(body1)

# method 2

body2 = ETree.Element("body")
body2.text = "added another body element from code"
root.append(body2)

# adding id attribute to xml elements
id = 1
for body in tree.findall("body"):
    body.set("id", str(id))
    id += 1

# save xml file
tree.write("SOAP.xml")
