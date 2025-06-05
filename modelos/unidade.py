class Unidade:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)

    def __str__(self):
        return f"Unidade: {self.nome}, Cursos: {[curso.nome for curso in self.cursos]}"