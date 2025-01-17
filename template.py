import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
project_name='wasteDetection'

list_of_files=[
    '.github/workflows/.gitkeep',
    'data/.gitkeep',
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_validation.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/constant/__init__.py',
    f'{project_name}/constant/training_pipeline/__init__.py',
    f'{project_name}/constant/application.py',
    f'{project_name}/entitiy/config_entity.py',
    f'{project_name}/entitiy/artifact_entity.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/pipeline/training_pipeline.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/main_utils.py',
    'requirements.txt',
    'setup.py',
    'tests.py',
    'Dockerfile',
    'app.py',
    'templetes/index.html',
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file: {filename}')
    if(not os.path.exists(filepath)) or os.path.getsize(filepath)==0:
        with open(filepath,'w') as f:
            pass
            logging.info(f'Creating file: {filename}')
    else:
        logging.info(f'File: {filename} already exists')