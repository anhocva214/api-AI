from googletrans import Translator


translator = Translator()

def TranslateToEn (question):
    question_trans = translator.translate(question, src='vi')
    return question_trans.text

def TranslateToVi (question):
    question_trans = translator.translate(question, src='en', dest="vi")
    return question_trans.text
