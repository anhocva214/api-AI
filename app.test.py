# from trans import TranslateToEn, TranslateToVi
# from search_paragraph import SearchAnwser
# from bert_qa import answer_question


# def QA(question):
#     print("question_vi : ", question )
#     q_en = TranslateToEn(question)
#     print("Translate question_en: ", q_en)
#     paragraph = SearchAnwser(q_en)
#     print("Search paragraph_en")
#     question_en, answer_en = answer_question(q_en, paragraph)
#     print("Predict question_en and answer_en")
#     answer_vi = TranslateToVi(answer_en)
#     print("Translate question_en to vi")
#     print({
#         "question_vi": question,
#         "answer_vi": answer_vi,
#         "question_en": question_en,
#         "answer_en": answer_en
#     })

# QA("What is margin trading in USD? ?")