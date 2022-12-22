from Parametri.ParameterParserSRC import Parameter
from WebInterface.CheckSite import SiteInterface


def get_search_parameters(parameter_instance):
    return parameter_instance.get_ricerca()


def update_search_parameters(si, urls):
    for u in urls:
        si.add_page(u)


if __name__ == '__main__':
    p = Parameter()
    p.parse_file("parametri.txt")

    si = SiteInterface()

    url_ricerca = get_search_parameters(p)
    update_search_parameters(si, url_ricerca)

    si.retrieve_elements()
    si.update_db()


