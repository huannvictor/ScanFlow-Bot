import os
import pandas as pd
import logging
from datetime import datetime

def extrair_dados_dos_arquivos(diretorio_entrada):
    """
    Escaneia a pasta de entrada e agrupa dados por entidade.
    """
    if not os.path.exists(diretorio_entrada):
        logging.error(f"O diretório de entrada não foi encontrado: {diretorio_entrada}")
        return None

    logging.info(f"Escaneando arquivos de: {diretorio_entrada}")
    entidades = {}

    for filename in os.listdir(diretorio_entrada):
        try:
            # Padrão: 'PREFIXO_CODIGO_ANO_INDEX.EXT'
            partes = filename.split('_')
            if len(partes) < 2:
                continue
                
            codigo = partes[1]
            path_completo = os.path.join(diretorio_entrada, filename)
            data_timestamp = os.path.getmtime(path_completo)
            data_envio = datetime.fromtimestamp(data_timestamp)

            # Mantém apenas a primeira ocorrência
            if codigo not in entidades or data_envio < entidades[codigo]:
                entidades[codigo] = data_envio
        except Exception as e:
            logging.error(f"Erro ao processar {filename}: {e}")

    if not entidades:
        logging.warning("Nenhum dado encontrado.")
        return None

    # Construção do DataFrame
    df = pd.DataFrame(list(entidades.items()), columns=['código', 'data_envio'])
    df['código'] = pd.to_numeric(df['código'], errors='coerce')
    df['data_envio'] = pd.to_datetime(df['data_envio'])
    df = df.sort_values(by='data_envio', ascending=False)
    
    return df

def salvar_relatorio(df, diretorio_saida):
    """Gera o arquivo Excel com os dados processados."""
    if df is None or df.empty:
        logging.warning("Não há dados para salvar.")
        return

    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    hoje = datetime.now().strftime('%Y-%m-%d')
    output_path = os.path.join(diretorio_saida, f'relatorio_envio_{hoje}.xlsx')
    
    df.to_excel(output_path, index=False)
    logging.info(f"Relatório gerado em: {output_path}")
    return output_path
