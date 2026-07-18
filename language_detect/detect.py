from langdetect import detect
class LanguageDetect:
    def lang(self,text):
        try:
            return detect(text)
        except:
            return "Unknown"

