class Person:
    def __init__(self, name, partners):
        self.name=name
        self.partners=partners

    def get_name(self): 
        return self.name
    def get_partners(self): 
        return self.partners
    def add_partner(self, new):
        self.partners.append(new)
    def clear_partners(self):
        self.partners = []