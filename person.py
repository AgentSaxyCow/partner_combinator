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


    def get_names(self): return self.names
    def get_matrix(self): return self.matrix
    def add_person(self, person):
        self.names.append(person)
        self.matrix.append([])
        for row in self.matrix:
            while len(row) < len(self.names):
                row.append(0)

    def add_partners(self, name0, name1):
        index0, index1 = self.get_index(name0, name1)
        self.update_matrix(index0, index1, 1)
    
    def remove_partners(self, name0, name1):
        index0, index1 = self.get_index(name0, name1)
        self.update_matrix(index0, index1, 0)
    
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