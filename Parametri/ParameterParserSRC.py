import yaml


class Parameter:
    def __init__(self):
        self.parameter_dictionary = {}

    def parse_file(self, filename="../parametri.txt"):
        with open(filename, "r") as stream:
            try:
                self.parameter_dictionary = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_emails(self):
        return self.parameter_dictionary["email"].split()

    def get_ricerca(self):
        return list(self.parameter_dictionary["ricerca"].values())


if __name__ == '__main__':
    p = Parameter()
    p.parse_file()
    print(p.get_emails())
    print(p.get_ricerca())
