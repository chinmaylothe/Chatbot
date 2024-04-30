from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
question_answerer = pipeline("text-generation", model=model, tokenizer=tokenizer)

def answer_question(question, data):
    input_text = f"Context: {data}\nQuestion: {question}\nAnswer:"
    output = question_answerer(input_text, max_length=200)[0]['generated_text']
    return output.split("Answer:")[1].strip()

def preprocess_data(file_path):
   
    data = pd.read_csv(file_path)
    
   
    data = data.dropna()  
    data = data.drop_duplicates()
    
    text = data.to_string(index=False)
    
    return text