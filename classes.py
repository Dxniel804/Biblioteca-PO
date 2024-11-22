class Clientes:
    def __init__(self, nome, email, usuario, senha):
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha
        self.emprestado = ""

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email

    def getUser(self):
        return self.usuario
    
    def setUser(self, usuario):
        self.usuario = usuario

    def getSenha(self):
        return self.senha
    
    def setSenha(self, senha):
        self.senha = senha

    def getEmp(self):
        return self.emprestado
    
    def setEmp(self, emprestado):
        self.emprestado = emprestado