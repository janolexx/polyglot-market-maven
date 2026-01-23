# Polyglot Market Maven

**Polyglot Market Maven** is a multilingual, command-line currency exchange application written in Python.
It provides real-time exchange rates and simple exchange rate analysis using live market data, with support for six languages.

This project was developed as a practical demonstration of Python programming, modular software design, API integration, and internationalization (i18n).

---

## Features

**Multilingual Interface**
  Supports English, Turkish, Persian, Arabic, Spanish, and Chinese.

**Real-Time Exchange Rates**
  Fetches live currency exchange data from the **Frankfurter Exchange Rates API**.

**Exchange Rate Analysis**
  Presents exchange rates in a clear, human-readable format
  (e.g. *“1 USD equals 43.35 TRY”*), including a simple daily comparison.

**Clean Command-Line Interface**
  Menu-driven interaction with clear prompts and formatted output.

**Modular Architecture**
  Separation of concerns between data fetching, display logic, and language handling.

---

## Supported Languages

* **English**
* **Türkçe (Turkish)**
* **فارسی (Persian)**
* **العربية (Arabic)**
* **Español (Spanish)**
* **中文 (Chinese)**

Languages can be switched at runtime without restarting the application.

---

## How It Works 

1. The user selects an option from the main menu.
2. The application asks for a base currency and a target currency.
3. Live exchange rate data is fetched from the Frankfurter API.
4. Results are formatted and displayed according to the selected language.
5. The user can switch languages or perform additional queries at any time.

The application focuses on clarity, correctness, and reliability rather than complex financial predictions.

---

## Installation & Usage

### Requirements

* Python **3.8+**
* Internet connection (for live exchange rates)

### Setup

```bash
pip install -r requirements.txt
python main.py
```

---

## Project Structure

```
polyglot_market_maven/
├── main.py                   # Application entry point
├── modules/
│   ├── market_analyzer.py    # API interaction and data processing
│   └── display_manager.py    # Output formatting and menus
├── utils/
│   └── language_manager.py   # Language selection and state handling
├── locales/
│   └── translations.py       # All language translations
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## Technologies Used

* **Python 3**
* **Requests** (HTTP API communication)
* **Frankfurter Exchange Rates API**
* Modular CLI application design

---

## Academic Note

This project was created as part of a personal learning journey in preparation for undergraduate studies in Computer Science.

It demonstrates:

* practical Python programming skills
* clean code organization
* API integration
* multilingual software design
* iterative debugging and feature refinement

The project intentionally prioritizes correctness, usability, and maintainability over unnecessary complexity.


---

## License

This project is intended for educational and demonstration purposes.
