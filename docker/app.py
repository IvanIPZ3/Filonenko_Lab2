from googletrans import Translator, LANGUAGES

translator = Translator()

def _sanitize(s: str) -> str:
    try:
        return s.encode('utf-8', 'ignore').decode('utf-8', 'ignore')
    except Exception:
        return s

def CodeLang(lang: str) -> str:
    lang = _sanitize(lang)
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
    text = _sanitize(text)
    lang = _sanitize(lang)
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
        dest_code = low if low in LANGUAGES else code_or_name
    try:
        res = translator.translate(text, dest=dest_code)
        return res.text
    except Exception as e:
        return f"Помилка перекладу: {e}"

def LangDetect(txt: str) -> str:
    txt = _sanitize(txt)
    if not isinstance(txt, str) or not txt.strip():
        return "Помилка: порожній текст для визначення мови."
    try:
        det = translator.detect(txt)
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

if __name__ == "__main__":
    try:
        txt = _sanitize(input("Введіть текст для перекладу: ")).strip()
    except Exception:
        txt = ""
    try:
        lang = _sanitize(input("На яку мову перекласти (код або назва): ")).strip()
    except Exception:
        lang = ""

    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang("En"))
    print(CodeLang("English"))
