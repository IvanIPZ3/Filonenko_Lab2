from translator_lib import TransLate, LangDetect, CodeLang

def main():
    print("=== ЛР2: Перекладач на базі googletrans ===")
    txt = input("Введіть текст для перекладу: ").strip()
    lang = input("На яку мову перекласти (код або назва): ").strip()

    print("\n--- Результати ---")
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang("En"))
    print(CodeLang("English"))

if __name__ == "__main__":
    main()
