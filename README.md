
# Groq Q/A Chatbot

This project is a user-friendly and interactive chatbot built using Streamlit, LangChain, Groq, and OpenAI APIs. The chatbot is designed to provide intelligent and accurate answers to user queries, leveraging cutting-edge Large Language Models (LLMs). Users can customize the chatbot’s behavior using parameters like temperature and token limit, and they can choose from multiple advanced LLMs available.

# Features

#### User Authentication:
Enter your API key securely using the sidebar.

#### Model Selection:
Choose between multiple pre-trained LLMs for varied responses.

#### Adjustable Parameters:

+ **Temperature**: Control the creativity of responses.
+ **Max Tokens**: Set the maximum token limit for the response length.

#### Intelligent Prompts:
Uses a custom-designed system prompt for enhanced, human-like responses.

#### Interactive User Interface: 
Simple  and intuitive input/output fields using Streamlit.


# Run Locally

### Clone the project

```bash
git clone https://github.com/pruthi-saksham/Groq-Q-A-Chatbot.git

```

### Go to the project directory

```bash
  cd Groq-Q-A-Chatbot
```

### Install dependencies

```bash
  pip install -r requirements.txt

```
### Set up the environment variables
#### Create a `.env` file in the root directory.
#### Add the following keys:
```bash
LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key
```

### Run the Application

```bash
 streamlit run app.py
```


## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file

`LANGCHAIN_API_KEY` : Your LangChain API key

`GROQ_API_KEY` :  Your Groq API key

`LANGCHAIN_TRACING_V2` : Set to "True" for LangChain tracing

`LANGCHAIN_PROJECT` : Name of your LangChain project

# Appendix

Here are the useful links related to the technologies and frameworks used in your project:

### LangChain Documentation

LangChain offers a robust framework for building applications powered by large language models (LLMs). It simplifies the lifecycle of LLM-based applications, from chaining components to deployment.

LangChain Documentation: https://python.langchain.com/docs/introduction/

GitHub Repository: https://github.com/langchain-ai/langchain

### Groq Documentation

Groq provides advanced computational capabilities for AI and machine learning applications.

Groq Playground: https://console.groq.com/playground

Groq Documentation: https://console.groq.com/docs/overview

### Streamlit Documentation

Streamlit is an open-source app framework for creating custom web apps for machine learning and data science.

Streamlit Playground : https://streamlit.io/generative-ai

Streamlit Documentation : https://docs.streamlit.io/

### OpenAI API Reference

The OpenAI platform documentation includes guidelines for using their APIs to integrate GPT models into your projects.

Link: https://platform.openai.com/docs/


These resources will help you understand and effectively utilize the frameworks and APIs in your project. Let me know if you need specific guidance!

# FAQ

#### 1. What if I encounter an API key error?
Ensure your `.env` file contains valid keys for both `LANGCHAIN_API_KEY` and `GROQ_API_KEY`. Restart the application after updating the file.

#### 2. Can I add more models?
Yes, you can extend the dropdown options in the app.py file by integrating additional supported LLMs via LangChain or Groq APIs, Or you can use OpenAi, Ollama or HuggingFace.

#### 3. How do I modify the system prompt?
Update the `ChatPromptTemplate` section in `app.py` to customize the chatbot's behavior.

#### 4. How do I test the chatbot locally?
Follow the 'Run Locally' steps in the README. Use the command `streamlit run app.py` to launch the application, then enter queries into the user input field.

#### 5. What is the purpose of the temperature setting?
The `temperature` slider adjusts the randomness of the responses:

*Lower values* (e.g., 0.0): Responses will be deterministic and focused.
*Higher values* (e.g., 1.0): Responses will be more creative and diverse.

#### 6. What does Max Tokens control?
This slider sets the maximum length of the chatbot's response. Longer responses consume more tokens and may be slower.

#### 7. How do I ensure my API keys are secure?
+ Store keys in a .env file and avoid hardcoding them in the script.
+ Do not share your .env file publicly (e.g., on GitHub).
+ Use .gitignore to exclude .env from version control.

#### 8. Why am I getting a Rate Limit error?
Rate limits are imposed by the API provider. To resolve this:

+ Check your usage quota on the API provider’s dashboard.
+ Upgrade your API plan if necessary.

#### 9. Can I integrate other APIs or frameworks?
Yes! You can extend the chatbot by integrating:

+ Other LLM providers (e.g., Hugging Face, OpenAI).
+ Vector databases for memory-based conversation.

#### 10. Is this chatbot multilingual?
The chatbot can respond in multiple languages depending on the capabilities of the selected model. Modify the system prompt to specify a target language if needed.

#### 11. How do I handle errors during runtime?
+ Invalid API Key: Double-check keys in the .env file.
+ Model Not Found: Ensure the selected model is supported by the API.
+ Timeout Errors: Increase the request timeout in the API settings.


***And if nothing works, you can go to ChatGPT and rant!***

# 🚀 About Me
*Hi, I’m Saksham Pruthi, an AI Engineer passionate about creating innovative AI-powered solutions. I specialize in Generative AI, designing systems that bridge cutting-edge research and practical applications. With expertise in various AI frameworks and an eye for scalable technology, I enjoy tackling challenging projects that drive real-world impact.*




## 🛠 Skills
+ **Programming Languages**: Python, C++
+ **Generative AI Technologies**:  Proficient in deploying and fine-tuning a variety of LLMs including Llama2, GPT (OpenAI), Mistral, Gemini Pro  using frameworks like Hugging Face, OpenAI,Groq and Groq. Expertise in NLP tasks like tokenization, sentiment analysis, summarization, and machine translation. Skilled in computer vision (CV) with models for image classification, object detection, and segmentation (YOLO). Expertise in MLOps, building and maintaining pipelines for model training and monitoring. Proficient in conversational AI with platforms LangChain. Skilled in synthetic data generation and code generation
+ **Vector Databases and Embedding Libraries**: Proficient in ChromaDB and FAISS for efficient vector storage, retrieval, and similarity search.
+ **Frameworks, Tools & Libraries**: LangChain, HuggingFace , OpenAI API, Groq, TensorFlow, PyTorch, Streamlit.
+ **Databases**: MongoDB, ChromaDB
+ **Version Control**: Proficient in using Git for version control and GitHub for collaborative development, repository management, and continuous integration workflows.

