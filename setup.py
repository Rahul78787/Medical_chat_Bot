from setuptools import find_packages, setup

setup(
    name="Medical_chat_Bot",
    version="0.1.0",
    author="Rahul shah",
    author_email="contactrahul9090@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain==0.3.26",
        "flask==3.1.1",
        "sentence-transformers==4.1.0",
        "pypdf==5.6.1",
        "python-dotenv==1.1.0",
        "langchain-pinecone==0.2.8",
        "langchain-openai==0.3.24",
        "langchain-community==0.3.26"
    ]
)