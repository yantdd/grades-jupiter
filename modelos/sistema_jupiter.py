from modelos.unidade import Unidade
from modelos.curso import Curso
from modelos.disciplina import Disciplina
from bs4 import BeautifulSoup
import os
import glob
from tqdm import tqdm

class SistemaJupiter:
    def __init__(self):
        self.unidades = {}  # nome -> objeto Unidade
        self.cursos = {}    # nome -> objeto Curso 
        self.disciplinas = {} # codigo -> objeto Disciplina
    
    def processar_todas_grades(self):
        arquivos_html = glob.glob("grades/*.html")
        for i in tqdm(range(len(arquivos_html)),bar_format="{l_bar}{bar:20}", desc="Processando grades curriculares", ncols=60):
            arquivo = arquivos_html[i]
            try:
                self.processar_grade(arquivo)
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")
    
    def processar_grade(self, arquivo_html):
        """Processa um arquivo HTML específico"""

        with open(arquivo_html, encoding='utf-8') as fp:
            grade = BeautifulSoup(fp, features="lxml")
        
        # Extrair informações básicas do curso
        try:
            nome_unidade = grade.find('span', class_='unidade').text.strip()
            nome_curso = grade.find('span', class_='curso').text.strip()
            duracao = grade.find('span', class_='duridlhab').text.strip()
            duracao_minima = grade.find('span', class_='durminhab').text.strip()
            duracao_maxima = grade.find('span', class_='durmaxhab').text.strip()
        except:
            return  # Grade inválida
        
        # Criar/obter unidade
        if nome_unidade not in self.unidades:
            self.unidades[nome_unidade] = Unidade(nome_unidade)
        unidade = self.unidades[nome_unidade]
        
        # Criar curso
        curso = Curso(nome_curso, nome_unidade, duracao, duracao_minima, duracao_maxima)
        self.cursos[nome_curso] = curso
        unidade.adicionar_curso(curso)
        
        # Processar disciplinas
        tables = grade.select("#gradeCurricular table")
        
        for table in tables:
            tipo_atual = None
            
            for row in table.select("tr"):
                cols = row.find_all("td")
                
                # Detectar tipo de disciplina
                if len(cols) == 1 and "colspan" in cols[0].attrs:
                    tipo_atual = cols[0].get_text(strip=True)
                    if tipo_atual == "Disciplinas Obrigatórias":
                        tipo_atual = "obrigatoria"
                    elif tipo_atual == "Disciplinas Optativas Livres":
                        tipo_atual = "opt_livre"
                    elif tipo_atual == "Disciplinas Optativas Eletivas":
                        tipo_atual = "opt_eletiva"
                    continue
                
                # Ignorar linhas de materias requisito
                if len(cols) == 8 and "Requisito" in cols[-1].get_text():
                    continue
                
                # Processar disciplina
                if row.select_one("a.disciplina"):
                    cod = row.select_one("a.disciplina")["data-coddis"]
                    nome = cols[1].get_text(strip=True)
                    cred_aula = cols[2].get_text(strip=True)
                    cred_trab = cols[3].get_text(strip=True)
                    ch = cols[4].get_text(strip=True) or "0"
                    ce = cols[5].get_text(strip=True) or "0"
                    cp = cols[6].get_text(strip=True) or "0"
                    atpa = cols[7].get_text(strip=True) or "0"
                    
                    # Criar/obter disciplina
                    if cod not in self.disciplinas:
                        disciplina = Disciplina(cod, nome, cred_aula, cred_trab, ch, ce, cp, atpa)
                        self.disciplinas[cod] = disciplina
                    else:
                        disciplina = self.disciplinas[cod]
                    
                    # Adicionar ao curso com o tipo específico
                    curso.adicionar_disciplina(disciplina, tipo_atual)
    
    # Métodos de consulta
    def listar_cursos_por_unidade(self):
        print("\nEscolha uma unidade:\n")
        i = 1
        for unidade in self.unidades:
            print(f"{i}) {unidade}")
            i += 1
        nome_unidade = input("\nDigite o número da unidade: ")
        nome_unidade = list(self.unidades.keys())[int(nome_unidade) - 1]

        if nome_unidade:
            if nome_unidade in self.unidades:
                print("\nCursos ministrados em " + nome_unidade + ":\n")
                for curso in self.unidades[nome_unidade].cursos:
                    print(f" {curso.nome}\n")
    
    def dados_curso(self):
        """2. Dados de um determinado curso"""
        print("\nEscolha um curso:\n")
        i = 1
        for curso in self.cursos:
            print(f"{i}) {curso}")
            i += 1
        nome_curso = input("\nDigite o número do curso: ")
        nome_curso = list(self.cursos.keys())[int(nome_curso) - 1]
        self.cursos[nome_curso].__str__()
        return self.cursos[nome_curso]
    
    def dados_todos_cursos(self):
        """3. Dados de todos os cursos"""
        print("Dados de todos os cursos:\n")
        for curso in self.cursos.values():
            print(curso.__str__())
            print("\n")
               
    def dados_disciplina(self):
        """4. Dados de uma disciplina, inclusive quais cursos ela faz parte"""
        codigo_disciplina = input("\nDigite o código da disciplina ou ENTER para ver todas as disciplinas: ")
        if codigo_disciplina:
            print("\n")
            print(self.disciplinas[codigo_disciplina.strip().upper()].__str__())
        else:
            print("Escolha uma disciplina:\n")
            i = 1
            for disciplina in self.disciplinas.values():
                print(f"{i}) {disciplina.codigo} - {disciplina.nome}")
                i += 1
            num_disciplina = input("\nDigite o número da disciplina: ")
            codigo_disciplina = list(self.disciplinas.keys())[int(num_disciplina) - 1]
            print("\n")
            print(self.disciplinas[codigo_disciplina].__str__())
    
    def disciplinas_multiplos_cursos(self):
        """5. Disciplinas que são lecionadas em mais de um curso"""
        return [disc for disc in self.disciplinas.values() if len(disc.cursos) > 1]
    
    def estatisticas_gerais(self):
        """Consulta adicional: estatísticas gerais"""
        return {
            'total_unidades': len(self.unidades),
            'total_cursos': len(self.cursos),
            'total_disciplinas': len(self.disciplinas),
            'disciplinas_compartilhadas': len(self.disciplinas_multiplos_cursos())
        }
    
    def buscar_disciplina_por_nome(self, nome_parcial):
        """Consulta adicional: buscar disciplina por nome parcial"""
        resultados = []
        nome_parcial = nome_parcial.lower()
        for disc in self.disciplinas.values():
            if nome_parcial in disc.nome.lower():
                resultados.append(disc)
        return resultados 