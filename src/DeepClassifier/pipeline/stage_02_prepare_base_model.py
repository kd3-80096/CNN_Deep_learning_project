from DeepClassifier.config import ConfigurationManager
from DeepClassifier.components import PrepareBaseModel
from DeepClassifier import logger

STAGE_NAME = "Prepare base model"


def main():

    config = ConfigurationManager() 
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()


if __name__=='main':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<< \n\nx=======x")

    except Exception as e:
        logger.exception(e)  ## for logging the exceptions
        raise e









