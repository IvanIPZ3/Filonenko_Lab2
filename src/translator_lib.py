from typing import Tuple
from googletrans import Translator, LANGUAGES

_translator = Translator()

def CodeLang(lang: str) -> str:
    if not isinstance(lang, str) or not lang.strip():
        return "Помилка: порожній параметр мови."
    s = lang.strip()
    low = s.lower()

    if low in LANGUAGES:
        name = LANGUAGES[low]
        return name[:1].upper() + name[1:]
    for code, name in LANGUAGES.items():
        if name.lower() == low:
            return code
    return "Помилка: мову не знайдено."

def TransLate(text: str, lang: str) -> str:
    if not isinstance(text, str) or not text.strip():
        return "Помилка: порожній текст для перекладу."
    code_or_name = CodeLang(lang)
    if "Помилка" in code_or_name:
        low = str(lang).strip().lower()
        if low in LANGUAGES:
            dest_code = low
        else:
            return code_or_name  
    else:
        low = str(lang).strip().lower()
        if low in LANGUAGES:
            dest_code = low 
        else:
            dest_code = code_or_name 

    try:
        result = _translator.translate(text, dest=dest_code)
        return result.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt: str) -> str:
    if not isinstance(txt, str) or not txt.strip():
        return "Помилка: порожній текст для визначення мови."
    try:
        det = _translator.detect(txt)
        conf = getattr(det, "confidence", None)
        if conf is None:
            conf_str = "N/A"
        else:
            try:
                conf_f = float(conf)
                conf_str = str(int(conf_f)) if conf_f.is_integer() else f"{conf_f:.2f}"
            except Exception:
                conf_str = str(conf)
        return f"Detected(lang={det.lang}, confidence={conf_str})"
    except Exception as e:
        return f"Помилка визначення мови: {e}"
