from trans import TranslateToEn, TranslateToVi
# from search_paragraph import SearchAnwser
# from bert_qa import answer_question
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
  return 'Server Works!'


# @app.route('/ai/QA',  methods=['GET'])
# def QA_Question():
#   question = request.args.get('question')
#   print("Get question_vi to en" )
#   q_en = TranslateToEn(question)
#   print("Translate question_en: ", q_en)
#   print("Tìm kiếm đoạn văn phù hợp")
#   paragraph = SearchAnwser(q_en)
#   print("Search paragraph_en")
#   question_en, answer_en = answer_question(q_en, paragraph)
#   print("Predict question_en and answer_en")
#   answer_vi = TranslateToVi(answer_en)
#   print("Translate question_en to vi")

#   return {
#       "question_vi": question,
#       "question_en": question_en,
#       "answer_en": answer_en,
#       "answer_vi": answer_vi
#   }

  # export FLASK_ENV=development
