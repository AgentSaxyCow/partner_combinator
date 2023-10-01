class PeopleMatrix:
    def __init__(self, names, matrix=0):
        self.names = names
        if matrix == 0:
            self.matrix = []
            for i in self.names:
                self.matrix.append([])
            for x in self.matrix:
                for y in range(len(self.names)):
                    x.append(0)
        else:
            self.matrix = matrix
        self.l = len(names)


    def get_names(self): return self.names
    def get_matrix(self): return self.matrix
    def get_partners_count(self, name):
        i = self.names.index(name)
        return self.matrix[i].count(0)

    def get_not_partners(self, name):
        i = self.names.index(name)
        not_partners = []
        for x in range(self.l):
            if self.matrix[i][x] == 0:
                not_partners.append(self.names[x])
        if len(not_partners) == 1:
            self.remove_all_person_partners(name)
            not_partners = self.names
        return not_partners

    def add_person(self, person):
        self.names.append(person)
        self.matrix.append([])
        self.l += 1
        for row in self.matrix:
            while len(row) < len(self.names):
                row.append(0)
    
    def remove_person(self, person):
        indexperson = self.names.index(person)
        self.names.pop(indexperson)
        self.matrix.pop(indexperson)
        self.l -= 1
        for row in self.matrix:
            row.pop(indexperson)

    def add_partners(self, name0, name1):
        index0, index1 = self.get_index(name0, name1)
        self.update_matrix(index0, index1, 1)
    
    def remove_partners(self, name0, name1):
        index0, index1 = self.get_index(name0, name1)
        self.update_matrix(index0, index1, 0)

    def not_partners(self, name0, name1):
        index0, index1 = self.get_index(name0, name1)
        self.update_matrix(index0, index1, -1)
    
    def remove_all_partners(self):
        for i in range(self.l):
            for j in range(self.l):
                self.matrix[i][j] = 0
    
    def remove_all_person_partners(self, name):
        person = self.names.index(name)
        for i in range(self.l):
            self.matrix[person][i] = 0

    
    def clean_matrix(self):
        l = len(self.matrix)
        for i in range(l):
            for j in range(l):
                if self.matrix[i][j] == -1:
                    self.matrix[i][j] = 0
    
    def print_matrix(self):
        for i in range(len(self.names)):
            tmp = self.names[i] + " partners: "
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1:
                    tmp += self.names[j] + " "
            print(tmp)
            

    def get_index(self, name0, name1):
        n0 = self.names.index(name0)
        n1 = self.names.index(name1)
        return n0, n1
    
    def update_matrix(self, i0, i1, num):
        self.matrix[i0][i1] = num
        self.matrix[i1][i0] = num