import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_pipeline/__init__.py",
    "src/components/data_pipeline/data_ingetion.py",
    "src/components/data_pipeline/data_transformation.py",
    "src/components/model_pipeline/model_trainer.py",
    "src/components/model_pipeline/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/data_ingetion_pipeline.py",
    "src/pipeline/data_transformation_pipeline.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/exception.py",
    "src/logger.py",
    "setup.cfg",
    "pyproject.toml",
    "init_setup.sh",
    'tox.ini',
    "research/experiments.ipynb",
    "setup.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file