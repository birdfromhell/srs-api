from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: str = "3306"
    DATABASE_USER: str = "root"
    DATABASE_PASSWORD: str = ""
    DATABASE_NAME: str = "restaurant"
    
    @property
    def DATABASE_URL(self) -> str:
        # Add charset and SSL parameters
        return f"mysql+pymysql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}?charset=utf8mb4"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()