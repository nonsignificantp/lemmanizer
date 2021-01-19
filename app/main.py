
import stanza
from fastapi import FastAPI

stNLP = stanza.Pipeline(processors = 'tokenize,mwt,pos,lemma', lang = 'es', use_gpu = False) 
app = FastAPI()

@app.get("/lemmanizer")
def read_root(oracion: str):
    doc = stNLP(oracion) 
    oracion = [word.lemma for sent in doc.sentences for word in sent.words]
    doc = " ".join(oracion)
    return {
        "response": doc
    }