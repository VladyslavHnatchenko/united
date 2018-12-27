import time
import xml.etree.cElementTree as ET


def edit_xml(filename):
    """Edit xml file"""
    tree = ET.ElementTree(filename)
    root = tree.getroot()

    for begin_time in root.iter("begin"):
        begin_time.text = time.ctime(int(begin_time.text))

    tree = ET.ElementTree(root)

    with open(filename, "w") as f:
        f.write(ET.tostring(tree))
        print(f)


if __name__ == "__main__":
    edit_xml("new.xml")


# import xml.etree.ElementTree as xml
# # from xml.etree.ElementTree import ElementTree, tostring
#
#
# def create_xml(filename):
#     """Create xml file."""
#
#     root = xml.Element("zAppointments")
#     appt = xml.Element("appointment")
#     root.append(appt)
#
#     # create a child sub-element.
#     begin = xml.SubElement(appt, "begin")
#     begin.text = "1181251680"
#
#     uid = xml.SubElement(appt, "uid")
#     uid.text = "040000008200E000"
#
#     alarm_time = xml.SubElement(appt, "alarmTime")
#     alarm_time.text = "1181572063"
#
#     state = xml.SubElement(appt, "state")
#     state.text = "Cool"
#
#     location = xml.SubElement(appt, "location")
#     location.text = "Kyiv"
#
#     duration = xml.SubElement(appt, "duration")
#     duration.text = "1800"
#
#     subject = xml.SubElement(appt, "subject")
#     subject.text = "Bring pizza home"
#
#     tree = xml.ElementTree(root)
#
#     with open("example.xml", "w") as f:
#         tree.write(f)
#
#
# if __name__ == "__main__":
#     create_xml("test.xml")


# import xml.dom.minidom as minidom
#
#
# def get_titles(xml):
#     """We deduce all headings from xml."""
#
#     doc = minidom.parse(xml)
#     node = doc.documentElement
#     books = doc.getElementsByTagName("book")
#
#     titles = []
#     for book in books:
#         title_obj = book.getElementsByTagName("title")[0]
#         titles.append(title_obj)
#
#     for title in titles:
#         nodes = title.childNodes
#         for node in nodes:
#             if node.nodeType == node.TEXT_NODE:
#                 print(node.data)
#
#
# if __name__ == "__main__":
#     document = "example2.xml"
#     get_titles(document)

# import xml.dom.minidom
# import urllib.request
#
#
# class AppParser:
#
#     def __init__(self, url, flag='url'):
#         self.list = []
#         self.app_list = []
#         self.flag = flag
#         self.rem_value = 0
#         xml = self.get_xml(url)
#         self.handle_xml(xml)
#
#     def get_xml(self, url):
#         try:
#             print(url)
#             f = urllib.request.urlopen(url)
#         except:
#             f = url
#
#         doc = xml.dom.minidom.parse(f)
#         node = doc.documentElement
#         if node.nodeType == xml.dom.Node.ELEMENT_NODE:
#             print("Element: %s" % node.nodeName)
#             for (name, value) in node.attributes.items():
#                 print(" Attr -- name: %s valye: %s" % (name, value))
#
#         return node
#
#     def handle_xml(self, xml):
#         rem = xml.getElementsByTagName('zAppointments')
#         appointments = xml.getElementsByTagName('appointment')
#         self.handle_apps(appointments)
#
#     def get_element(self, element):
#         return self.get_text(element.childNodes)
#
#     def handle_apps(self, apps):
#         for app in apps:
#             self.handle_app(app)
#             self.list = []
#
#     def handle_app(self, app):
#         begin = self.get_element(app.getElementsByTagName("begin")[0])
#         duration = self.get_element(app.getElementsByTagName("duration")[0])
#         subject = self.get_element(app.getElementsByTagName("subject")[0])
#         location = self.get_element(app.getElementsByTagName("location")[0])
#         uid = self.get_element(app.getElementsByTagName("uid")[0])
#
#         self.list.append(begin)
#         self.list.append(duration)
#         self.list.append(subject)
#         self.list.append(location)
#         self.list.append(uid)
#
#         if self.flag == 'file':
#             try:
#                 state = self.get_element(app.getElementsByTagName("state")[0])
#                 self.list.append(state)
#                 alarm = self.get_element(app.getElementsByTagName("alarmTime")[0])
#                 self.list.append(alarm)
#             except Exception as e:
#                 print(e)
#
#         self.app_list.append(self.list)
#
#     def get_text(self, node_list):
#         rc = ""
#         for node in node_list:
#             if node.nodeType == node.TEXT_NODE:
#                 rc = rc + node.data
#         return rc
#
#
# if __name__ == "__main__":
#     app = AppParser("example.xml")
#     print(app.app_list)
