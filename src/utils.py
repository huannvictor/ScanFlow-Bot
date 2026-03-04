import os
import logging
from datetime import datetime

def setup_logging():
    """Configura o sistema de logs para o projeto."""
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_file = os.path.join(log_dir, f"execucao_{datetime.now().strftime('%Y-%m-%d')}.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    logging.info("Sistema de logs iniciado.")

def get_path(folder_name):
    """Retorna o caminho absoluto para uma pasta na raiz do projeto."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', folder_name))
