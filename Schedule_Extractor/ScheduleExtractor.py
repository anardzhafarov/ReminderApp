import xml.etree.ElementTree as ET
from pprint import pprint
import helperFunctions

# Parse into Element Tree
tree= ET.parse("C:/Users/dzafa/Downloads/personal_20260323_013614.xml")
root=tree.getroot()

events=helperFunctions.parseData(root)

helperFunctions.removeDuplicates(events)
helperFunctions.orderedsetToList(events)

pprint(events, indent=2)

helperFunctions.updateJSON(events)