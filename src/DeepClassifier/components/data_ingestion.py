import os
import urllib.request as request   ## for downloading the data its the kibrary
from zipfile import ZipFile         ## for zipping  and unzipping the file data
from DeepClassifier.entity import DataIngestionConfig
from DeepClassifier import logger
from DeepClassifier.utils import get_size
from tqdm import tqdm  
from pathlib import Path




class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):  ## To check if file is present or not
            logger.info("Download started...")

            filename, headers = request.urlretrieve(        
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size:{get_size(Path(self.config.local_data_file))}")

    def _get_updated_list_of_files(self, list_of_files):  ## To get the list of files that ends with extension .jpg and inages of cat and dog
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)  
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:  ## To check if the file is having the size 0
            logger.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    def unzip_and_clean(self):    ## To unzip the file that we want to open
        logger.info(f"unzipping file and removing unawanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:   ##zf is zip file alias
            list_of_files = zf.namelist()    ## To get name list of files
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)  ## 
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)    ## f is the pointer to updated_list_of_files
                                                                ##
                                                                                