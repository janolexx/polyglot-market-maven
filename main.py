#!/usr/bin/env python3
"""
Polyglot Market Maven - Main Application
"""

import sys
from utils.language_manager import LanguageManager
from modules.market_analyzer import MarketAnalyzer
from modules.display_manager import DisplayManager


class PolyglotMarketMaven:
    def __init__(self):
        self.language_manager = LanguageManager()
        self.market_analyzer = MarketAnalyzer()
        self.display_manager = DisplayManager(self.language_manager)

    def run(self):
        self._show_welcome()

        while True:
            self._show_main_menu()
            choice = input(f"{self.language_manager.translate('select_option')}: ").strip()

            if choice == "1":
                self._handle_exchange_rate_analysis()
            elif choice == "2":
                self._handle_exchange_rate()
            elif choice == "3":
                self._handle_language_selection()
            elif choice == "4":
                self._handle_exit()
            else:
                print(f"\n{self.language_manager.translate('invalid_input')}\n")

    # --------------------------------------------------
    # UI
    # --------------------------------------------------
    def _show_welcome(self):
        t = self.language_manager.translate
        print("\n" + "=" * 50)
        print(f"  {t('welcome')}")
        print("=" * 50 + "\n")

    def _show_main_menu(self):
        print(self.display_manager.show_menu())

    # --------------------------------------------------
    # INPUT
    # --------------------------------------------------
    def _ask_currency_pair(self):
        t = self.language_manager.translate
        base = input(f"{t('enter_symbol')} (Base): ").strip().upper()
        target = input("Target currency: ").strip().upper()
        return base, target

    # --------------------------------------------------
    # OPTION 1 — EXCHANGE RATE ANALYSIS
    # --------------------------------------------------
    def _handle_exchange_rate_analysis(self):
        t = self.language_manager.translate
        base, target = self._ask_currency_pair()

        if not base or not target:
            print(f"\n{t('invalid_input')}\n")
            return

        print(f"\n{t('loading')}...")
        data = self.market_analyzer.get_market_data(base, target)
        yesterday = self.market_analyzer.get_yesterday_data(base, target)

        if not data or not yesterday:
            print("\nMarket data not available\n")
            return

        change = data["current_price"] - yesterday["current_price"]
        percent = (change / yesterday["current_price"]) * 100

        direction = "📈 Increased" if change > 0 else "📉 Decreased" if change < 0 else "➡️ No change"
        assumption = (
            "likely to remain upward"
            if percent > 0
            else "likely to decline"
            if percent < 0
            else "expected to stay stable"
        )

        print("\n" + "=" * 50)
        print(f"Market Analysis: {base}/{target}")
        print("=" * 50)
        print(f"1 {base} equals {data['current_price']:.4f} {target}")
        print(f"{direction} compared to yesterday ({percent:.2f}%)")
        print(f"Based on daily movement, the rate is {assumption}.")
        print("=" * 50 + "\n")

    # --------------------------------------------------
    # OPTION 2 — EXCHANGE RATE (PRICE ONLY)
    # --------------------------------------------------
    def _handle_exchange_rate(self):
        t = self.language_manager.translate
        base, target = self._ask_currency_pair()

        if not base or not target:
            print(f"\n{t('invalid_input')}\n")
            return

        print(f"\n{t('loading')}...")
        data = self.market_analyzer.get_market_data(base, target)

        if not data:
            print("\nMarket data not available\n")
            return

        print(f"\n{t('current_price')}: {data['current_price']:.4f}\n")

    # --------------------------------------------------
    # OPTION 3 — LANGUAGE
    # --------------------------------------------------
    def _handle_language_selection(self):
        print(self.display_manager.show_language_menu())
        choice = input("Select option: ").strip()

        from locales.translations import get_available_languages
        languages = get_available_languages()

        if choice.isdigit() and 1 <= int(choice) <= len(languages):
            self.language_manager.set_language(languages[int(choice) - 1])
            print("\n✓ Language updated\n")
        else:
            print("\nInvalid input\n")

    # --------------------------------------------------
    # OPTION 4 — EXIT
    # --------------------------------------------------
    def _handle_exit(self):
        print(f"\n{self.language_manager.translate('exit')}...\n")
        sys.exit(0)


if __name__ == "__main__":
    PolyglotMarketMaven().run()

