"""
Market Analyzer Module
Uses Frankfurter API for exchange rate data
"""

import requests
from datetime import datetime, timedelta


class MarketAnalyzer:
    BASE_URL = "https://api.frankfurter.app"

    def get_market_data(self, base_currency, target_currency):
        """
        Get latest exchange rate
        """
        try:
            url = f"{self.BASE_URL}/latest"
            params = {
                "from": base_currency,
                "to": target_currency
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            rate = data["rates"].get(target_currency)

            if rate is None:
                return None

            return {
                "base": base_currency,
                "target": target_currency,
                "current_price": rate,
                "date": data.get("date")
            }

        except Exception:
            return None

    def get_yesterday_data(self, base_currency, target_currency):
        """
        Get yesterday's exchange rate
        """
        try:
            yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
            url = f"{self.BASE_URL}/{yesterday}"
            params = {
                "from": base_currency,
                "to": target_currency
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            rate = data["rates"].get(target_currency)

            if rate is None:
                return None

            return {
                "base": base_currency,
                "target": target_currency,
                "current_price": rate,
                "date": yesterday
            }

        except Exception:
            return None

    def analyze_trend(self, base_currency, target_currency):
        """
        Simple trend analysis (today vs yesterday)
        """
        today = self.get_market_data(base_currency, target_currency)
        yesterday = self.get_yesterday_data(base_currency, target_currency)

        if not today or not yesterday:
            return "stable"

        if today["current_price"] > yesterday["current_price"]:
            return "up"
        elif today["current_price"] < yesterday["current_price"]:
            return "down"
        else:
            return "stable"

