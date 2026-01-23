"""
Language Manager for handling multilingual support
"""

import json
import os
from pathlib import Path

class LanguageManager:
    """Manages language settings and translations"""
    
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.current_language = 'en'
        self.load_config()
    
    def load_config(self):
        """Load language configuration from file"""
        config_path = Path(__file__).parent.parent / self.config_file
        if config_path.exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    self.current_language = config.get('language', 'en')
            except Exception:
                self.current_language = 'en'
    
    def save_config(self):
        """Save language configuration to file"""
        config_path = Path(__file__).parent.parent / self.config_file
        config = {'language': self.current_language}
        try:
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception:
            pass
    
    def set_language(self, language_code):
        """Set the current language"""
        valid_languages = ['en', 'fa', 'ar', 'tr', 'es', 'zh']
        if language_code in valid_languages:
            self.current_language = language_code
            self.save_config()
            return True
        return False
    
    def get_language(self):
        """Get the current language code"""
        return self.current_language
    
    def translate(self, key):
        """Get translation for current language"""
        from locales.translations import get_translation
        return get_translation(self.current_language, key)
    
    def get_default_currency(self):
        """Return default currency based on selected language"""
        language_currency_map = {
            'en': 'USD',
            'fa': 'IRR',
            'ar': 'AED',
            'tr': 'TRY',
            'es': 'EUR',
            'zh': 'CNY'
        }
        return language_currency_map.get(self.current_language, 'USD')


