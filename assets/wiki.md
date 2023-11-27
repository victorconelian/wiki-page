### Descrição do que será realizado no Projeto:
Utilizaremos da linguagem *Python* para leitura dos dados de um arquivo *markdown* e um arquivo *JSON*, gerando uma página *index.html* estático, onde subiremos ao Git Pages. 
O arquivo *markdown* terá o conteúdo da nossa página e o *JSON* as informações de título, descrição e autores. 
Para realizarmos tudo isso, faremos a instalação do Git Flow para configuração de um fluxo de trabalho onde criaremos uma branch de desenvolvimento (*develop*) e também criaremos um ambiente virtual (*venv*) para isolarmos o nosso projeto. 
No Github usaremos o Actions para automatizar a cada *push* a atualização da nossa página hospedada no Git Pages.

### Instalação e Execução do Git Flow:
```
sudo apt-get install git-flow
git flow init
```

### Foi criado uma nova branch para desenvolvimento do projeto:
```bash
git branch -l
* develop
main

git checkout develop
```

### Arquivos utilizados:
- **Markdown:** wiki.md (conteúdo escrito em md);
- **JSON:** config.json (título, descrição e autores);
- **HTML:** layout.html (template) e index.html (escrito a partir do script.py);
- **Python:** script.py (responsável em escrever nosso index.html a partir dos outros arquivos).

### Criação de um Ambiente Virtual:
**Para isolarmos as dependências do projeto de modo que cada projeto tenha suas bibliotecas separadas do sistema principal, criamos um ambiente virtual:**

```python
python3 -m venv venv
```

**Ativamos nosso ambiente virtual (linux):**
```bash
source venv/bin/activate
```

**Instalamos as bibliotecas que utilizaremos no Script:**
```python
pip install jinja2 markdown2
```

### Script em Python:
```python
from markdown2 import markdown 
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath='./'))
template = template_env.get_template('layout.html')

with open('wiki.md') as markdown_file:
    wiki = markdown(
        markdown_file.read(),
        extras=['fenced-code-blocks', 'code-friendly'])

with open('config.json') as config_file:
    config = load(config_file)

with open('index.html', 'w') as output_file:
    output_file.write(
        template.render(
            title=config['title'],
            description=config['description'],
            authors=config['authors'],
            wiki=wiki
        )
    )
```

### Criando um arquivo .gitignore:
Foi criado o .gitignore para ignorar a pasta venv (ambiente virtual Python), pois na hora de realizar a *build* e o *deploy* do Git Pages, havia conflito com um arquivo presente dentro da pasta venv.


