from spacy_transformers import TransformersLanguage, TransformersWordPiecer, TransformersTok2Vec
import os

name = "biobert"
results_dir= os.getcwd() + "/ner_outputs_BC5CDR-chem-IOB"
pytorch_path= results_dir + "/pytorch-biobert"

 
nlp = TransformersLanguage(trf_name=name, meta={"lang": "en"})
nlp.add_pipe(nlp.create_pipe("sentencizer"))
nlp.add_pipe(TransformersWordPiecer.from_pretrained(nlp.vocab, pytorch_path))
nlp.add_pipe(TransformersTok2Vec.from_pretrained(nlp.vocab, pytorch_path))
nlp.add_pipe(nlp.create_pipe("ner"), last=True)

print(nlp.pipe_names)

nlp.to_disk(results_dir + '/spacy')
