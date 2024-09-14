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

model = ChatOpenAI(openai_api_key=get_secret(), base_url="https://proxy.tune.app/", model= "rohan/tune-gpt-4o-mini", n = 1)
QueryMessage = [SystemMessage(content="You are a helpful Assistant"), HumanMessage(content="What is 1 + 1?")]
response = model.generate([QueryMessage])

with open("test.json", mode='a') as f:
        f.write(json.dumps(response.dict(exclude={'run'})) + '\n')