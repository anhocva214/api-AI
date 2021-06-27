from sentence_transformers import SentenceTransformer
import scipy

model = SentenceTransformer('bert-large-nli-mean-tokens')

# A corpus is a list with documents split by sentences.

file = open('./data_en.txt', "r")

paragraph = file.read()

while 1==1:
    if paragraph.find("\n") > -1:
        paragraph = paragraph.replace("\n", "")
    elif paragraph.find("\xa0") > -1:
        paragraph = paragraph.replace("\xa0", " ")
    else:
        break
# print(paragraph)

def SearchAnwser(question):
    p = paragraph

    sentences = p.split("[break]")

    sentence_embeddings = model.encode(sentences)

    query = question #@param {type: 'string'}

    queries = [query]
    query_embeddings = model.encode(queries)

    # Find the closest 3 sentences of the corpus for each query sentence based on cosine similarity
    number_top_matches = 2 #@param {type: "number"}

    print("Semantic Search Results")

    for query, query_embedding in zip(queries, query_embeddings):
        distances = scipy.spatial.distance.cdist([query_embedding], sentence_embeddings, "cosine")[0]

        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        # print("\n\n======================\n\n")
        # print("Query:", query)
        # print("\nTop most similar sentences in corpus:")

        r = ""
        for idx, distance in results[0:number_top_matches]:
            print(sentences[idx].strip(), "(Cosine Score: %.4f)" % (1-distance))
            r+=sentences[idx].strip()
            # return sentences[idx].strip()
        return r

# SearchAnwser("From July 1, 2020, do I have to register for temporary residence to another place for less than 30 days?")


file.close()