import os
import random
import time
from datetime import datetime, timedelta

def gerar_arquivos_teste(num_escolas=10, arquivos_por_escola=3):
    """
    Gera arquivos JPG e TXT fictícios para simular um ambiente de produção.
    Isso permite que o projeto de portfólio seja testado sem expor dados reais.
    """
    # Define o caminho relativo à pasta do script
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'processadas')
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir, exist_ok=True)
        
    print(f"Gerando arquivos de teste em: {os.path.abspath(base_dir)}")
    
    # Lista de códigos de escolas fictícios
    codigos = [f"{random.randint(10000, 99999):05d}" for _ in range(num_escolas)]
    
    for codigo in codigos:
        # Define uma data base aleatória para o envio (até 60 dias atrás)
        dias_base = random.randint(5, 60)
        data_base = datetime.now() - timedelta(days=dias_base)
        
        for j in range(1, arquivos_por_escola + 1):
            # Gera nomes no padrão 01_CODIGO_2026_INDEX.JPG
            filename_base = f"01_{codigo}_2026_{j}"
            
            # Cada arquivo subsequente tem uma data um pouco posterior
            data_arquivo = data_base + timedelta(hours=random.randint(1, 48))
            timestamp = data_arquivo.timestamp()

            for ext in ['.JPG', '.TXT']:
                filepath = os.path.join(base_dir, filename_base + ext)
                
                # Cria arquivo vazio
                with open(filepath, 'w') as f:
                    f.write(f"Dados de teste para escola {codigo}")
                
                # Altera a data de criação/modificação (no Windows é difícil alterar criação pura via Python, 
                # mas 'os.utime' altera modificação, que usaremos no script principal)
                os.utime(filepath, (timestamp, timestamp))
                
    print(f"Sucesso! {len(os.listdir(base_dir))} arquivos criados na pasta 'data/processadas'.")

if __name__ == "__main__":
    gerar_arquivos_teste()
