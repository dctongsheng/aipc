from openai import OpenAI
from typing import List,Iterator

client = OpenAI(api_key="sk-U0jC98VPl4GngyWbE8C7Ef11F2904d9eBbE5Ca545668728b",base_url="http://one.95271111.xyz/v1")
completion=client.embeddings.create(
    model="text-embedding-v3",
    input=["Tiktoken library For Tokenization In OpenAI API","你是谁？","今天天气好啊"]
    )

print(completion.data[0])
print(len(completion.data[0].embedding))