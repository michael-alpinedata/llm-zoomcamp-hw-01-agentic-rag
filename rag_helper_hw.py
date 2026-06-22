INSTRUCTIONS = '''
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
'''

PROMPT_TEMPLATE = '''
QUESTION: {question}

CONTEXT:
{context}
'''.strip()


class RAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions=INSTRUCTIONS,
        prompt_template=PROMPT_TEMPLATE,
        filename='',
        model="meta-llama/llama-4-scout-17b-16e-instruct"
        # model="llama-3.1-8b-instant"
        # model='gpt-5.4-mini'
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.filename = filename
        self.prompt_template = prompt_template
        self.model = model

    def search(self, query, num_results=5):
        # boost_dict = {'question': 3.0, 'section': 0.5}
        # filter_dict = {'filename': self.filename}

        return self.index.search(
            query,
            num_results=num_results,
            # boost_dict=boost_dict,
            # filter_dict=filter_dict
        )

    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            # lines.append(doc['section'])
            lines.append('Lesson content: ' + doc['content'])
            # lines.append('A: ' + doc['answer'])
            lines.append('')

        return '\n'.join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )

    def llm(self, prompt):
        input_messages = [
            {'role': 'developer', 'content': self.instructions},
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        print("response.usage.input_tokens")
        print(response.usage.input_tokens)

        return response.output_text

    def rag(self, query):
        # print("Query:")
        # print(query)

        search_results = self.search(query)
        # print("Search result:")
        # print(search_results)

        prompt = self.build_prompt(query, search_results)
        # print("Prompt built:")
        # print(prompt)

        answer = self.llm(prompt)
        return answer
