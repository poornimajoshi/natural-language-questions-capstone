# natural-language-questions-capstone

This project is to provide an interface where users can fit their data to BERT of DistBert in order to find answers to their questions. In the application, once can observe the results of the prediction and compare them with the expected answer. Thus, the website uses the model to predict and show the answer.

### How to run
- Checkout out the repository
- Download the `models` using

`# Downloading pre-trained BERT fine-tuned on SQuAD 1.1
download_model('bert-squad_1.1', dir=directory)

# Downloading pre-trained DistilBERT fine-tuned on SQuAD 1.1
download_model('distilbert-squad_1.1', dir=directory)`
- Run the `app.py` file in order to start-up the server
- Replace the dataset file with your our file
 

