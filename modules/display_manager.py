"""
Display Manager for formatting and displaying market data
"""

class DisplayManager:
    """Manages display formatting for different languages"""

    def __init__(self, language_manager):
        self.lang = language_manager

    # --------------------------------------------------
    # MARKET / EXCHANGE RATE ANALYSIS DISPLAY
    # --------------------------------------------------
    def format_market_data(self, data: dict) -> str:
        t = self.lang.translate

        lines = [
            f"\n{'='*50}",
            f"{self._menu_label('analysis')}: {data['symbol']}",
            f"{'='*50}",
            f"{t('current_price')}: {self.format_price(data['current_price'])}",
            f"{'='*50}\n"
        ]
        return "\n".join(lines)

    # --------------------------------------------------
    # MENU DISPLAY
    # --------------------------------------------------
    def show_menu(self) -> str:
        t = self.lang.translate

        menu = [
            f"\n{'='*50}",
            f"  {t('app_name')}",
            f"{'='*50}",
            f"1. {self._menu_label('analysis')}",
            f"2. {self._menu_label('price')}",
            f"3. {t('select_language')}",
            f"4. {t('exit')}",
            f"{'='*50}\n"
        ]
        return "\n".join(menu)

    # --------------------------------------------------
    # LANGUAGE SELECTION MENU
    # --------------------------------------------------
    def show_language_menu(self) -> str:
        from locales.translations import get_language_name, get_available_languages

        t = self.lang.translate
        menu = [f"\n{t('select_language')}:\n"]

        languages = get_available_languages()
        for idx, lang_code in enumerate(languages, 1):
            name = get_language_name(lang_code)
            current = " ✓" if lang_code == self.lang.get_language() else ""
            menu.append(f"{idx}. {name}{current}")

        menu.append("")
        return "\n".join(menu)

    # --------------------------------------------------
    # PRICE FORMATTER
    # --------------------------------------------------
    def format_price(self, price: float) -> str:
        return f"{price:,.4f}"

    # --------------------------------------------------
    # MENU LABELS (POLYGLOT + ACADEMIC)
    # --------------------------------------------------
    def _menu_label(self, key: str) -> str:
        lang = self.lang.get_language()

        labels = {
            "analysis": {
                "en": "Exchange Rate Analysis",
                "tr": "Döviz Kuru Analizi",
                "es": "Análisis del Tipo de Cambio",
                "ar": "تحليل سعر الصرف",
                "fa": "تحلیل نرخ ارز",
                "zh": "汇率分析",
            },
            "price": {
                "en": "Exchange Rate",
                "tr": "Döviz Kuru",
                "es": "Tipo de Cambio",
                "ar": "سعر الصرف",
                "fa": "نرخ ارز",
                "zh": "汇率",
            }
        }

        return labels.get(key, {}).get(lang, labels[key]["en"])
