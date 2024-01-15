import logging
from typing import List, Optional

import mteb.abstasks.AbsTask
from mteb import MTEB

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("main")


def _get_preferred_split(available_splits):
    order = ["test", "valid", "validation", "dev"]
    for possibility in order:
        if possibility in available_splits:
            return possibility
    return available_splits[0]


def evaluate(
    model,
    model_name: str,
    task_list: Optional[List[str]] = None,
    task_langs: Optional[List[str]] = None,
):
    task_list = task_list or TASK_LIST
    task_langs = task_langs or ["en"]
    for task in task_list:
        logger.info(f"Running task: {task}")
        cat_classes = [cls for cls in mteb.abstasks.AbsTask.__subclasses__()]
        task_instances = [
            task_cls()
            for cat_cls in cat_classes
            for task_cls in cat_cls.__subclasses__()
            if cat_cls.__name__.startswith("AbsTask")
        ]
        task_instances = [
            tsk for tsk in task_instances if tsk.description['name'] == task
        ]
        assert len(task_instances) == 1, task_instances
        eval_splits = [
            _get_preferred_split(task_instances[0].description['eval_splits'])
        ]
        evaluation = MTEB(
            tasks=[task], task_langs=task_langs
        )
        evaluation.run(
            model, output_folder=f"results/{model_name}", eval_splits=eval_splits
        )

if __name__ == '__main__':
    from sentence_transformers import SentenceTransformer

    TASK_LIST = ["MIRACL", "GermanDPR", "PawsX", "GermanSTSBenchmark", "XMarket", "WikiCLIR", "GerDaLIR"]

    model_name = 'multilingual-e5-base'
    model = SentenceTransformer(f'intfloat/{model_name}', device='cuda')
    evaluate(model, model_name, TASK_LIST, ['en', 'de', 'en-de', 'de-en'])