import pyproj
import xml.etree.ElementTree as ET

pyproj.network.set_network_enabled(True)
tr = pyproj.Transformer.from_crs(6697, 6667)


def get_geoid(lat, lon):
    lat, lon, geoid = tr.transform(lat, lon, 0.0)
    return geoid


def view_gml(path):
    tree = ET.parse(path)

    namespaces = {
        node[0]: node[1] for _, node in ET.iterparse(path, events=["start-ns"])
    }
    # for key, value in namespaces.items():
    #     ET.register_namespace(key, value)

    root = tree.getroot()

    tags = root.findall(".//gml:posList", namespaces)
    
    for tag in tags:
        print(tag.text)


view_gml("/home/ubuntu/citygml/gml/533925_dem_6697_op2.gml")
