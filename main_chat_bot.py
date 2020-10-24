print("Starting ChatBot...")
from model_transformer import predict

while True:
    question = input("Tell me something: ")
    answer = predict(question)
    print(answer)
