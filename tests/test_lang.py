from language_detect.detect import LanguageDetect
detector = LanguageDetect()
def check_language(text,expected):
    result=detector.lang(text)
    assert result==expected
def test_detect_hindi():
    check_language(
        "यह हिंदी भाषा का एक वाक्य है।",
        "hi"
    )


def test_detect_telugu():
    check_language(
        "ఇది తెలుగు భాషలో ఒక వాక్యం.",
        "te"
    )


def test_detect_french():
    check_language(
        "Bonjour tout le monde.",
        "fr"
    )


def test_detect_spanish():
    check_language(
        "Hola, ¿cómo estás?",
        "es"
    )


def test_detect_german():
    check_language(
        "Hallo, wie geht es dir?",
        "de"
    )


def test_detect_japanese():
    check_language(
        "こんにちは世界。",
        "ja"
    )


def test_detect_korean():
    check_language(
        "안녕하세요.",
        "ko"
    )


def test_detect_chinese():
    check_language(
        "你好，世界。",
        "zh-cn"
    )


def test_empty_text():
    check_language(
        "",
        "Unknown"
    )


def test_numbers_only():
    check_language(
        "123456789",
        "Unknown"
    )


def test_special_characters():
    check_language(
        "@#$%^&*()",
        "Unknown"
    )
    