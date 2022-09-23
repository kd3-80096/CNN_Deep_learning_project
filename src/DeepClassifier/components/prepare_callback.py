import os
from DeepClassifier.entity import PrepareCallbacksConfig
from zipfile import ZipFile
import tensorflow as tf
import time

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S") ## timstamp will be created whenever we run the project
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,  ## tensorboard_root_log_dir we will append with the timestamp
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath, ## storing the checkpoint_model_filepath
            save_best_only=True  ## we need to save the best weights only
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]