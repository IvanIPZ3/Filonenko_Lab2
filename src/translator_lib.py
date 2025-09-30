# -*- coding: utf-8 -*-
"""Бібліотека функцій для ЛР2: TransLate, LangDetect, CodeLang.
Працює з googletrans. За замовчуванням синхронні виклики.
"""
from typing import Tuple
from googletrans import Translator, LANGUAGES

_translator = Translator()

def CodeLang(lang: str) -> str:
    """
    Якщо lang = назва мови -> повертає код (ISO-639-1).
    Якщо lang = код -> повертає назву мови (English‑style, з великої літери).
    Якщо не знайдено -> рядок з помилкою.
    Приклади:
    - CodeLang("English") -> "en"
    - CodeLang("En") -> "English"
    """
    if not isinstance(lang, str) or not lang.strip():
        return "Помилка: порожній параметр мови."
    s = lang.strip()
    low = s.lower()

    # Якщо це код
    if low in LANGUAGES:
        # Назва з великої літери (English -> English, ukrainian -> Ukrainian)
        name = LANGUAGES[low]
        return name[:1].upper() + name[1:]
    # Якщо це назва
    for code, name in LANGUAGES.items():
        if name.lower() == low:
            return code
    return "Помилка: мову не знайдено."

def TransLate(text: str, lang: str) -> str:
    """
    Перекладає text на мову lang (код або назва).
    Повертає переклад або повідомлення про помилку.
    """
    if not isinstance(text, str) or not text.strip():
        return "Помилка: порожній текст для перекладу."
    code_or_name = CodeLang(lang)
    # Якщо користувач подав назву — отримаємо код; якщо подав код — отримаємо назву.
    # Нам потрібен код для dest.
    if "Помилка" in code_or_name:
        # Можливо, користувач ввів код — тоді CodeLang повернув назву (не помилка).
        # Перевіримо знову: якщо lang — код, треба отримати код назад.
        low = str(lang).strip().lower()
        if low in LANGUAGES:
            dest_code = low
        else:
            return code_or_name  # це помилка з CodeLang
    else:
        # Якщо користувач подав назву, CodeLang повернув код; якщо код — назву.
        # Визначимо код призначення:
        low = str(lang).strip().lower()
        if low in LANGUAGES:
            dest_code = low  # вже був код
        else:
            dest_code = code_or_name  # це код, отриманий з назви

    try:
        result = _translator.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt: str) -> str:
    """
    Повертає рядок формату: 'Detected(lang=uk, confidence=1)'
    """
    if not isinstance(txt, str) or not txt.strip():
        return "Помилка: порожній текст для визначення мови."
    try:
        det = _translator.detect(txt)
        conf = getattr(det, "confidence", None)
        if conf is None:
            conf_str = "N/A"
        else:
            try:
                # Вигляд як у прикладі: без крапок, якщо ціле
                conf_f = float(conf)
                conf_str = str(int(conf_f)) if conf_f.is_integer() else f"{conf_f:.2f}"
            except Exception:
                conf_str = str(conf)
        return f"Detected(lang={det.lang}, confidence={conf_str})"
    except Exception as e:
        return f"Помилка визначення мови: {e}"
