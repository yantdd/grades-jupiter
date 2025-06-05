class Disciplina:
    def __init__(self, codigo, nome, creditos_aula, creditos_trabalho, carga_horaria, carga_estagio, carga_cp, carga_atpa):
        self.codigo = codigo
        self.nome = nome
        self.creditos_aula = creditos_aula
        self.creditos_trabalho = creditos_trabalho
        self.carga_horaria = carga_horaria
        self.carga_estagio = carga_estagio
        self.carga_cp = carga_cp
        self.carga_atpa = carga_atpa
        self.cursos = []  # Lista de cursos que incluem esta disciplina

    def adicionar_curso(self, curso):
        if curso not in self.cursos:
            self.cursos.append(curso)

    def __eq__(self, value: object) -> bool:
        if value.get_codigo() == self.codigo:
            return True
        return False
    
    def __str__(self):
        cursos = ""
        for curso in self.cursos:
            cursos += " " + curso.nome + "\n"
        return f"Disciplina: {self.codigo} - {self.nome}\nCreditos aula: {self.creditos_aula}\nCreditos trabalho: {self.creditos_trabalho}\nCarga horaria: {self.carga_horaria}\nCarga estagio: {self.carga_estagio}\nCarga CP: {self.carga_cp}\nCarga ATPA: {self.carga_atpa}\nCursos em que é ministrada:\n{cursos}"

    def get_codigo(self):
        return self.codigo

    def get_nome(self):
        return self.nome