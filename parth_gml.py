from xml.etree import ElementTree
import get_address as ga

# XML ファイルから ElementTree オブジェクトを生成
tree = ElementTree.parse('53394610_bldg_6697_2_op.gml')

# 先頭要素を表す Element オブジェクトを取得
root = tree.getroot()
for building in root.findall('{http://www.opengis.net/citygml/2.0}cityObjectMember'):
  for gml_posList in building[0].findall('{http://www.opengis.net/citygml/building/2.0}lod0RoofEdge')[0][0][0][0][0][0]:
    posList = gml_posList.text.split()
    address = ElementTree.SubElement(building[0], 'address')
    address.text = ga.rev_geo(posList[0], posList[1])

tree = ElementTree.ElementTree(root)

tree.write('test.gml', encoding="UTF-8")