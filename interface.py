import sys

from modelos.sistema_jupiter import SistemaJupiter
from scraper import scraper


def exibir_menu():
    """Exibe o menu principal formatado como uma caixa ASCII"""
    print("\n" + "+" + "-" * 45 + "+")
    print("|" + "MENU DE CONSULTAS".center(45) + "|")
    print("+" + "-" * 45 + "+")
    print("| 1. Listar cursos por unidade".ljust(46) + "|")
    print("| 2. Dados de um curso específico".ljust(46) + "|")
    print("| 3. Dados de todos os cursos".ljust(46) + "|")
    print("| 4. Dados de uma disciplina".ljust(46) + "|")
    print("| 5. Disciplinas em múltiplos cursos".ljust(46) + "|")
    print("| 6. Estatísticas gerais".ljust(46) + "|")
    print("| 7. Buscar disciplina por nome".ljust(46) + "|")
    print("| 8. Buscar curso por nome".ljust(46) + "|")
    print("|".ljust(46) + "|")
    print("| 0. Sair".ljust(46) + "|")
    print("+" + "-" * 45 + "+")


def exibe_banner():
    banner = f"""
        ____               _             
       / ___|_ __ __ _  __| | ___  ___   
      | |  _| '__/ _` |/ _` |/ _ \/ __|  
      | |_| | | | (_| | (_| |  __/\__ \  
       \____|_|  \__,_|\__,_|\___||___/  
          | |_   _ _ __ (_) |_ ___ _ __  
       _  | | | | | '_ \| | __/ _ \ '__| 
      | |_| | |_| | |_) | | ||  __/ |    
       \___/ \__,_| .__/|_|\__\___|_|    
                  |_|                    \n"""
    print(banner)

def main():
    
    sistema = SistemaJupiter()

    if len(sys.argv) > 1:
        exibe_banner()
        if scraper(int(sys.argv[1]), sistema) == 1:
            return

    else:
        print("Uso: python3 interface.py <numero_de_unidades>")
        return
        

    while True:
        exibir_menu()
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            sistema.listar_cursos_por_unidade()
        
        elif opcao == "2":
            curso = sistema.dados_curso()
            
            print(f"\n{curso}")
            ver_disciplinas = input("\nVer disciplinas? (s/n): ").lower()
            if ver_disciplinas == 's':
                if curso.obrigatorias:
                    print("\n----- DISCIPLINAS OBRIGATÓRIAS -----\n")
                    for disc in curso.obrigatorias:
                        print(f"  {disc.codigo} - {disc.nome}")
                if curso.optativas_livres:
                    print("\n----- DISCIPLINAS OPTATIVAS LIVRES -----\n")
                    for disc in curso.optativas_livres:
                        print(f"  {disc.codigo} - {disc.nome}")
                if curso.optativas_eletivas:
                    print("\n----- DISCIPLINAS OPTATIVAS ELETIVAS -----\n")
                    for disc in curso.optativas_eletivas:
                        print(f"  {disc.codigo} - {disc.nome}")
        
        elif opcao == "3":
            sistema.dados_todos_cursos()
        
        elif opcao == "4":
            sistema.dados_disciplina()
        
        elif opcao == "5":
            disciplinas = sistema.disciplinas_multiplos_cursos()
            print(f"\n----- DISCIPLINAS EM MÚLTIPLOS CURSOS ({len(disciplinas)}) -----\n")
            for i, disc in enumerate(disciplinas):
                print(f"{i+1:2d}. {disc.codigo} - {disc.nome} ({len(disc.cursos)} cursos)")
        
        elif opcao == "6":
            stats = sistema.estatisticas_gerais()
            print("\n----- ESTATÍSTICAS GERAIS -----\n")
            print(f"Total de Unidades: {stats['total_unidades']}")
            print(f"Total de Cursos: {stats['total_cursos']}")
            print(f"Total de Disciplinas: {stats['total_disciplinas']}")
            print(f"Disciplinas Compartilhadas: {stats['disciplinas_compartilhadas']}")
        
        elif opcao == "7":
            nome_parcial = input("Digite parte do nome da disciplina: ")
            disciplinas = sistema.buscar_disciplina_por_nome(nome_parcial)
            if disciplinas:
                print(f"\n----- RESULTADOS DA BUSCA ({len(disciplinas)}) -----\n")
                for i, disc in enumerate(disciplinas):
                    print(f"{i+1:2d}. {disc.codigo} - {disc.nome}")
            else:
                print("Nenhuma disciplina encontrada!")
        
        elif opcao == "8":
            nome_parcial = input("Digite parte do nome do curso: ")
            cursos = sistema.buscar_curso_por_nome(nome_parcial)
            if cursos:
                print(f"\n----- RESULTADOS DA BUSCA ({len(cursos)}) -----\n")
                for i, curso in enumerate(cursos):
                    print(f"{curso.__str__()}\n")
            else:
                print("Nenhum curso encontrado!")
        
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 