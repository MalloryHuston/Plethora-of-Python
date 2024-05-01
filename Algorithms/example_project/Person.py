class Person:
    def __init__(self, first_name="John", last_name="Doe"):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def set_first(self, first_name):
        self.first_name = first_name

    def set_last(self, last_name):
        self.last_name = last_name