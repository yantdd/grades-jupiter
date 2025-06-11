# Sistema de Consulta Grades Jupiter

Sistema para coleta e consulta de dados dos cursos de graduação da USP através do Jupiter Web.

(Projeto final da disciplina SSC0103 - Programação Orientada a Objetos)

## Instalação

### Dependências Necessárias
**ATENÇÃO:** esse projeto usa **python 3**!

Execute o comando:

```bash
pip install -r requirements.txt
```

Dependências incluídas:
- `selenium>=4.15.0` - Automação do navegador
- `beautifulsoup4>=4.12.0` - Parsing HTML
- `lxml>=4.9.0` - Parser XML/HTML
- `tqdm>=4.67.1` - Barras de progresso

### ChromeDriver

Para que seja possível acoleta de dados das grades usando o Chrome, configure o ChromeDriver:

1. Baixe o ChromeDriver compatível com sua versão do Chrome:
   - Verifique sua versão do Chrome em: `chrome://version/`
   - Baixe em: https://googlechromelabs.github.io/chrome-for-testing/#stable
   - Descomprima o zip baixado e coloque o ChromeDriver onde desejar

2. Configure o caminho no arquivo `scraper.py` (linha 10):
   ```python
   service = Service(executable_path='/seu/caminho/para/chromedriver')
   ```

## Como Usar

### Executar o Sistema

```bash
python3 interface.py <numero_de_unidades>
```

**Exemplos:**
```bash
python3 interface.py 5    # Analisa as primeiras 5 unidades
python3 interface.py 10   # Analisa as primeiras 10 unidades
```

**Como funciona:**
1. O sistema automaticamente faz scraping das grades curriculares da USP
2. Processa os dados diretamente na memória
3. Apresenta o menu interativo para consultas

**Banner e Menu:**
O sistema exibe um banner ASCII e menu formatado:

```
+---------------------------------------------+
|              MENU DE CONSULTAS              |
+---------------------------------------------+
| 1. Listar cursos por unidade                |
| 2. Dados de um curso específico             |
| 3. Dados de todos os cursos                 |
| 4. Dados de uma disciplina                  |
| 5. Disciplinas em múltiplos cursos          |
| 6. Estatísticas gerais                      |
| 7. Buscar disciplina por nome               |
| 8. Buscar curso por nome                    |
|                                             |
| 0. Sair                                     |
+---------------------------------------------+
```

## Funcionalidades

### Consultas Disponíveis:

1. **Listar cursos por unidade** - Lista todos os cursos de uma unidade específica.
2. **Dados de curso específico** - Informações detalhadas incluindo disciplinas obrigatórias, optativas livres e eletivas.
3. **Dados de todos os cursos** - Resumo de todos os cursos coletados
4. **Dados de disciplina** - Informações completas de uma disciplina e cursos que a incluem.
5. **Disciplinas em múltiplos cursos** - Lista disciplinas compartilhadas entre diferentes cursos.
6. **Estatísticas gerais** - Totais de unidades, cursos, disciplinas e disciplinas compartilhadas.
7. **Buscar disciplina por nome** - Busca disciplinas por nome parcial.
8. **Buscar curso por nome** - Busca cursos por nome parcial.

### Interface do Sistema:

- **Banner ASCII artístico** na inicialização.
- **Menu formatado em caixa ASCII** para melhor visualização.
- **Navegação intuitiva** com opções numeradas.
- **Exibição organizada** de resultados com separadores visuais.
- **Contagem de progresso** durante carregamento das grades.

### Dados Coletados:

**Unidade:**
- Nome da unidade
- Lista de cursos oferecidos

**Curso:**
- Nome do curso
- Unidade responsável
- Duração ideal, mínima e máxima
- Disciplinas separadas por tipo:
  - Obrigatórias
  - Optativas Livres  
  - Optativas Eletivas

**Disciplina:**
- Código único
- Nome completo
- Créditos aula e trabalho
- Carga horária (CH)
- Carga horária de estágio (CE)
- Carga horária de Práticas como Componentes Curriculares (CP)
- Atividades Teórico-Práticas de Aprofundamento (ATPA)
- Lista de cursos que incluem a disciplina

## Estrutura do Projeto

```
├── modelos/
│   ├── sistema_jupiter.py  # Sistema principal com todas as consultas
│   ├── unidade.py          # Classe Unidade
│   ├── curso.py            # Classe Curso  
│   └── disciplina.py       # Classe Disciplina
├── scraper.py              # Script de coleta de dados via Selenium
├── interface.py            # Interface de usuário com menu ASCII
├── requirements.txt        # Dependências do projeto
└── README.md               # Este manual
```

## Características Técnicas

- **Orientação a objetos**: Classes bem definidas com responsabilidades claras
- **Reutilização de disciplinas**: Uma disciplina pode estar em múltiplos cursos
- **Tipo dinâmico**: Disciplinas podem ter tipos diferentes em cursos diferentes
- **Busca eficiente**: Uso de dicionários para consultas O(1)


## Correção de problemas

**Erro de ChromeDriver:**
- Verifique se o Chrome está instalado
- Confirme o caminho do ChromeDriver em `scraper.py`
- Baixe a versão compatível do ChromeDriver

