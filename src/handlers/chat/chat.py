from openai import OpenAI

# this prompt is used to define the personality and rules for AI
with open("src/handlers/chat/System-prompt.txt") as f:
    SYS_MESSAGE = f.read()
    f.close()
default_prompt = [{"role":"system", "content":SYS_MESSAGE}]

# all the dialogues with users will be stored here, with user id as a key
contexts = dict()
model = "databricks/dbrx-instruct"  # which model will api access.
client = OpenAI(
        api_key="ZWLcFFI9aMVFmki2078GdFNLfu4MkT38",
        base_url="https://api.deepinfra.com/v1/openai")

class chat():
    async def start_chat(id): # creates a new chat
        if id not in contexts.keys():
            contexts[id] = {"dialogue": []}


    async def clear_chat(id): # clears the context, almost the same as the previous one
        contexts[id] = {"dialogue": []}

    async def generate_response(id, msg):
        contexts[id]["dialogue"].append({"role":"user", "content":msg}) # adding users latest message
        messages = default_prompt + contexts[id]["dialogue"]

        chat_response = client.chat.completions.create( # generating the response
            model=model,
            messages=messages
        )
        
        return chat_response.choices[0].message.content # returning the text of the response

    async def update_context(id, msg): # adding assistant's response to context
        contexts[id]["dialogue"].append({"role":"assistant", "content":msg})

    async def resize_context(id): # slicing context if length is exceeded
        if len(contexts[id]["dialogue"]) > 50:
            contexts[id]["dialogue"] = contexts[id]["dialogue"][25:]