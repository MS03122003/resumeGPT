import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Application configuration"""
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Gemini AI configuration
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    
    # Google Drive configuration
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
    GOOGLE_REDIRECT_URI = os.environ.get('GOOGLE_REDIRECT_URI')
    
    # File upload configuration
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB max file size
    UPLOAD_FOLDER = 'uploads'
    PROCESSED_FOLDER = 'processed'
    ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
    
    # Google Drive scopes
    GOOGLE_SCOPES = [
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/documents.readonly'
    ]
    
    # Gemini model configuration
    GEMINI_MODEL = 'gemini-2.0-flash'
    MAX_TOKENS = 32000
    
    @staticmethod
    def validate_config():
        """Validate required configuration"""
        required_vars = ['GEMINI_API_KEY']
        missing = [var for var in required_vars if not getattr(Config, var)]
        
        if missing:
            raise ValueError(f"Missing required configuration: {', '.join(missing)}")
        
        return True