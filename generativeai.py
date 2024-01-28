import openai
key="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"
openai.api_key=key
myprompt=input('give a prompt')
out=openai.Completion.create(model="text-davinci-003",
                         prompt=myprompt)
print(out)