import requests as rq
import lxml.etree as et

# RETRIEVE WEB CONTENT
data = rq.get("https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Datasets/yield.xml")

# LOAD XML AND XSL FILES
doc = et.fromstring(data.text)
xsl = et.parse("TreasuryYields.xsl")

# TRANSFORM XML
transformer = et.XSLT(xsl)
result = transformer(doc)

# OUTPUT TO CONSOLE AND FILE
print(str(result))

with open("TreasuryYields.csv", 'w') as f:
    f.write(str(result))
