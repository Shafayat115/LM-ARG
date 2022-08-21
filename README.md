# LM-ARG
#Requirements
For protein feature extraction or fine-tuninng our pre-trained models, Pytorch and Transformers library from huggingface is needed. For model visualization, you need to install BertViz library.
The model is highly computational. So, using GPU is advised. But, you can run it on CPU as well.

#Instructions
Generate Embeddings.py will generate the embeddings for given input fasta files from ProtAlbert model. Mention the path of the fasta file and save the model path.
Train.py will train the supervised network using the embeddings. Give the path of the embedding model and training fasta file. Add the class labels accordingly - change dimension accordingly. 
Test.py will generate the results. Change the test file and test embedding model paths accordingly. 
