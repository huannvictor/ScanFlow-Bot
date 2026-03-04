# ScanFlow-Bot

Este projeto automatiza o controle de envio de documentos digitalizados, gerando relatórios consolidados em Excel a partir de metadados de arquivos. Desenvolvido originalmente para otimizar fluxos de trabalho manuais em um ambiente de produção real.

## 🚀 Funcionalidades
- **Varredura Automática:** Escaneia diretórios em busca de arquivos de imagem e texto.
- **Extração de Metadados:** Identifica códigos de entidades (ex: escolas) diretamente do nome do arquivo.
- **Análise Temporal:** Detecta a data da primeira ocorrência de cada entidade com base nos timestamps do sistema de arquivos.
- **Relatório Profissional:** Gera uma planilha Excel formatada e ordenada para tomada de decisão.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Pandas:** Para manipulação e estruturação de dados.
- **OS/Datetime:** Para operações nativas de sistema de arquivos e datas.
- **Openpyxl:** Para suporte à exportação de planilhas Excel.

## 📁 Estrutura do Projeto (Padrão @TEMPLATE.md)
```text
/ScanFlow-Bot
├── data/                   # Gestão de arquivos
│   ├── input/              # Arquivos crus (.JPG, .TXT)
│   └── output/             # Resultados gerados (.XLSX)
├── src/                    # O Coração (Código-fonte)
│   ├── __init__.py
│   ├── main.py             # Ponto de entrada (Orquestrador)
│   ├── core.py             # Lógica principal (Regex, cálculos, extração)
│   └── utils.py            # Ferramentas de apoio (Logs, caminhos, datas)
├── logs/                   # Histórico de execução para auditoria
├── scripts/                # Facilitadores (.BAT, scripts de apoio)
│   ├── gerador_testes.py   # Ferramenta para povoar ambiente de testes
│   └── executar.bat        # Script de execução rápida
├── tests/                  # Testes para garantir que o código não quebre
├── .gitignore              # Proteção (Não sobe lixo ou dados sensíveis para o Git)
├── README.md               # O seu "cartão de visitas" (Documentação)
└── requirements.txt        # Lista de dependências (Bibliotecas)
```

## 💻 Como Rodar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Caso queira testar em um ambiente vazio, rode o gerador de testes:
   ```bash
   python scripts/gerador_testes.py
   ```
3. Execute o processador principal:
   ```bash
   python -m src.main
   ```
   ou use o `executar.bat` (Windows).

---
*Este projeto foi adaptado para portfólio para proteger dados sensíveis, utilizando ferramentas de geração de dados fictícios (Mock Data).*
