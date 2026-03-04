import os
import logging
from src.utils import setup_logging, get_path
from src.core import extrair_dados_dos_arquivos, salvar_relatorio

def main():
    """Ponto de entrada do ScanFlow-Bot."""
    # 1. Configuração inicial
    setup_logging()
    logging.info("Iniciando processamento do ScanFlow-Bot.")

    # 2. Caminhos
    diretorio_input = os.path.join(get_path('data'), 'input') 
    diretorio_output = os.path.join(get_path('data'), 'output')

    # 3. Lógica principal
    try:
        df_processado = extrair_dados_dos_arquivos(diretorio_input)
        
        if df_processado is not None:
            salvar_relatorio(df_processado, diretorio_output)
        else:
            logging.warning("Nenhum arquivo foi processado.")
            
    except Exception as e:
        logging.error(f"Ocorreu um erro inesperado durante a execução: {e}", exc_info=True)
        
    logging.info("Execução finalizada.")

if __name__ == "__main__":
    main()
