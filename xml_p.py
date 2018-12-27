import xml.dom.minidom
import urllib.request


class AppParser:

    def __init__(self, url, flag='url'):
        self.list = []
        self.app_list = []
        self.flag = flag
        self.rem_value = 0
        xml = self.get_xml(url)
        self.handle_xml(xml)

    def get_xml(self, url):
        try:
            print(url)
            f = urllib.request.urlopen(url)
        except:
            f = url

        doc = xml.dom.minidom.parse(f)
        node = doc.documentElement
        if node.nodeType == xml.dom.Node.ELEMENT_NODE:
            print("Element: %s" % node.nodeName)
            for (name, value) in node.attributes.items():
                print(" Attr -- name: %s valye: %s" % (name, value))

        return node

    def handle_xml(self, xml):
        rem = xml.getElementsByTagName('zAppointments')
        appointments = xml.getElementsByTagName('appointment')
        self.handle_apps(appointments)

    def get_element(self, element):
        return self.get_text(element.childNodes)

    def handle_apps(self, apps):
        for app in apps:
            self.handle_app(app)
            self.list = []

    def handle_app(self, app):
        begin = self.get_element(app.getElementsByTagName("begin")[0])
        duration = self.get_element(app.getElementsByTagName("duration")[0])
        subject = self.get_element(app.getElementsByTagName("subject")[0])
        location = self.get_element(app.getElementsByTagName("location")[0])
        uid = self.get_element(app.getElementsByTagName("uid")[0])

        self.list.append(begin)
        self.list.append(duration)
        self.list.append(subject)
        self.list.append(location)
        self.list.append(uid)

        if self.flag == 'file':
            try:
                state = self.get_element(app.getElementsByTagName("state")[0])
                self.list.append(state)
                alarm = self.get_element(app.getElementsByTagName("alarmTime")[0])
                self.list.append(alarm)
            except Exception as e:
                print(e)

        self.app_list.append(self.list)

    def get_text(self, node_list):
        rc = ""
        for node in node_list:
            if node.nodeType == node.TEXT_NODE:
                rc = rc + node.data
        return rc


if __name__ == "__main__":
    app = AppParser("example.xml")
    print(app.app_list)
