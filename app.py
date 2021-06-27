from trans import TranslateToEn, TranslateToVi
from search_paragraph import SearchAnwser
from bert_qa import answer_question
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/api/QA',  methods=['GET'])
def QA_Question():
  question =  request.args.get('question')
  q_en = TranslateToEn(question)
  paragraph = SearchAnwser(q_en)
  question_en, answer_en = answer_question(q_en, paragraph)
  answer_vi = TranslateToVi(answer_en)
  
  return {
    # "question_vi": question,
    # "question_en": question_en,
    # "answer_en": answer_en,
    "answer_vi": answer_vi
  }