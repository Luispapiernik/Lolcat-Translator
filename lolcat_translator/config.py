from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    dictionary_filepath: str = Field(None, env="DICTIONARY_FILEPATH")

    class Config:
        env_file = "settings.env"
        env_file_encoding = "utf-8"
