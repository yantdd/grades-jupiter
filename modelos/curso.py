class Curso:
    def __init__(self, nome, unidade, duracao, duracao_minima, duracao_maxima):
        self.nome = nome
        self.unidade = unidade
        self.duracao = duracao
        self.duracao_minima = duracao_minima
        self.duracao_maxima = duracao_maxima
        self.obrigatorias = []
        self.optativas_livres = []
        self.optativas_eletivas = []
    
    def adicionar_disciplina(self, disciplina, tipo):
        if tipo == "obrigatoria":
            self.obrigatorias.append(disciplina)
        elif tipo == "opt_livre":
            self.optativas_livres.append(disciplina)
        elif tipo == "opt_eletiva":
            self.optativas_eletivas.append(disciplina)
        disciplina.adicionar_curso(self)

    def __str__(self):
        return f"Curso: {self.nome}\nUnidade: {self.unidade}\nDuração ideal: {self.duracao}\nDuração mínima: {self.duracao_minima}\nDuração máxima: {self.duracao_maxima}\nDisciplinas obrigatórias: {len(self.obrigatorias)}\nDisciplinas optativas livres: {len(self.optativas_livres)}\nDisciplinas optativas eletivas: {len(self.optativas_eletivas)}"