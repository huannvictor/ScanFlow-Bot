# TEMPLATE PROJECT

## Estrutura de Pastas Padrão (The Blueprint)

  Sempre comece criando esta estrutura. Ela separa o "cérebro" (código) dos "músculos" (dados) e da "memória" (logs).

```text
nome-do-projeto/
├── data/                   # Gestão de arquivos
│   ├── input/              # Arquivos crus recebidos (PDFs, CSVs, etc.)
│   └── output/             # Resultados gerados (Excel, Relatórios, etc.)
├── src/                    # O Coração (Código-fonte)
│   ├── __init__.py         # Torna a pasta um pacote Python
│   ├── main.py             # Ponto de entrada (Orquestrador)
│   ├── core.py             # Lógica principal (Regex, cálculos, extração)
│   └── utils.py            # Ferramentas de apoio (Logs, caminhos, datas)
├── logs/                   # Histórico de execução para auditoria
├── scripts/                # Facilitadores (Arquivos .bat ou scripts de apoio)
├── tests/                  # Testes para garantir que o código não quebre
├── .gitignore              # Proteção (Não sobe lixo ou dados sensíveis para o Git)
├── README.md               # O seu "cartão de visitas" (Documentação)
└── requirements.txt        # Lista de dependências (Bibliotecas)
```

---

## Divisão de Responsabilidades (O Padrão de Código)

Para manter o código limpo, siga esta regra de ouro:

* `utils.py`: Aqui ficam as funções que não "sabem" o que o projeto faz, mas ajudam. Ex: configurar log, criar pastas automaticamente, formatar CNPJ.
* `core.py`: Aqui fica a inteligência. Se o projeto é extrair de PDF, a função que abre o PDF e roda o Regex mora aqui.
* `main.py`: Este arquivo deve ser curto. Ele apenas chama o utils para iniciar o log e o core para processar os arquivos.

---

## O "Kit de Sobrevivência" de Arquivos Base

O `.gitignore` Universal:
Sempre inclua isso para não expor dados de clientes no GitHub:

```text
__pycache__/
venv/
.env
logs/*.log
data/input/
data/output/
*.pdf
```

O Script de Execução (`.bat`):
Facilite a vida do usuário final (ou a sua própria):

```bat
  @echo off
  python -m src.main
  pause
```

---

## Repositório

verifique se o diretório local é um repositório, se não crie

sempre crie com a branch sendo main em vez de master. se já houver uma master, renomeie para main.

se certifique que os repositórios, local e remoto, estão interligados

---

## Checklist de Inicialização (Workflow)

### Toda vez que começar, siga estes 5 passos

1. Ambiente: Crie a estrutura de pastas acima.
2. Dependências: Crie o requirements.txt com o que vai usar (pandas, pdfplumber, openpyxl).
3. Logs: Implemente o setup_logging no utils.py logo no primeiro dia. Se o código der erro, você saberá porquê.
4. Prototipagem: Crie o core.py focando em resolver o problema para um único arquivo.
5. Escalabilidade: Use o main.py para fazer um loop que processe todos os arquivos da pasta data/input.
