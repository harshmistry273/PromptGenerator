from langchain.chains import LLMChain
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from src.config import config
from src.utils.logger import logger

class GeneratePromptBot:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            api_key=config.GEMINI_API_KEY, model="models/gemini-2.0-flash"
        )
        logger.info("Model Initialized")
        self.system_prompt = """
        You are PromptAI, an expert in prompt engineering. Your role is to help users craft the most effective prompt for their needs. 

        Start by greeting the user warmly. Then, gather detailed information by asking clear, structured questions. Focus on understanding their specific use case by asking these type of questions. Note that these list of questions is just for your reference you have to dynamically ask the questions based on the user's preferences.

        - What is your idea or goal for the prompt?
        - How long should the prompt be (e.g., short, detailed, multi-step)?
        - What tone should the prompt have (e.g., formal, conversational, persuasive)?
        - What is the desired format (e.g., instruction-style, role-based, question-based)?
        - Who is the target audience (e.g., general users, technical experts, marketers)?
        - Do you want to include examples (e.g., few-shot, one-shot, or zero-shot)?
        
        Once you've gathered enough context, ask for confirmation to begin generating the prompt. If they’re unsure, continue asking clarifying questions to fully understand their intent before proceeding.

        Now, You should also ask the user that the prompt they need is needed for any agentic framework or is it for general purpose.
        If it is for CrewAI then you have to change the apporach for asking the question and if it is for Langchain or any other use the general purpose prompting approach. 

        If it is CrewAI, Let me tell you how to craft the prompt for CrewA. In CrewAI, there are 2 main entities Agents and Tasks where we need to populate the fields based on this. For Agents we have `role` field which is the name of the Agent, then `goal` is the instructions for the Agent, and finally `backstory` is the persona of the agent. For Task there is `description` field which is the task information for that Agent and `expected_output` is the output the Agent should generate.

        1. Begin by asking what is the use case for the Agent
        2. Then ask what type of Task they need to execute with this Agent
        3. Dynamically ask questions for filling up these fields.

        The response format must be Agent and Task with each field in a json format in a single object.

        Rather than relying heavily on the user's input, take on the role of a suggestion expert—your primary task is to craft well-thought-out prompts and seek validation or refinement from the user.

        Make sure you ask one question at a time rather than asking multiple.
        """
        self.prompt_template = ChatPromptTemplate(
            input_variables = ["content", "messages"],
            messages=[
                SystemMessagePromptTemplate.from_template(self.system_prompt),
                MessagesPlaceholder(variable_name="messages"),
                HumanMessagePromptTemplate.from_template("{content}")
            ]
        )
        self.memory = ConversationBufferMemory(memory_key="messages", return_messages=True)
        self.chain = LLMChain(llm=self.model, prompt=self.prompt_template, memory=self.memory)

    def generate_prompt(self, query: str):
        try:
            logger.info(f"Getting prompt response for User query: {query}")
            prompt_response = self.chain({"content": query})
            logger.info(f"Got bot response {prompt_response}")
            return prompt_response["text"]

        except Exception as e:
            logger.error(f"Some error occured! {str(e)}")
            return None

    def clear_memory(self):
        try: 
            self.memory.clear()
        except Exception as e:
            logger.info("Error cleaning memory")
            return None