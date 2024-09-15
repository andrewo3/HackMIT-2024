import json
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

def get_secret(secret_file: Path=Path('SECRET_TuneStudio.txt')) -> str:
    """Load an API secret from a file.
    """
    with open(secret_file, 'r') as f:
        secret = f.read().strip()
    return secret

def query_llm(message) -> str:
    model = ChatOpenAI(openai_api_key=get_secret(), base_url="https://proxy.tune.app/", model= "rohan/tune-gpt-4o-mini", n = 1,max_tokens=50)
    QueryMessage = [SystemMessage(content="You are a helpful Assistant"), HumanMessage(content="In 10 words or less, "+message)]
    response = model.generate([QueryMessage])
    answer_dict = response.dict(exclude={'run'})
    answer = answer_dict["generations"][0][0]["text"]
    store_dict = {"Input" : "In 10 words or less, "+message, "Output": answer}
    print(store_dict)
    with open("llm_query.json", mode='a') as f:
        json.dump(store_dict, f)
    return answer

if __name__ == "__main__":
    print("Input message:")
    message = input()
    print(query_llm(message))