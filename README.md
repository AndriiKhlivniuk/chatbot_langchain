# chatbot_langchain

<h2>Installation</h2>

<ol>
  <li>Create venv: python3 -m venv env</li>
  <li>Activate venv: (Windows).\env\Scripts\activate (Linux/Mac) source env/bin/activate</li>
  <li>Install requirements: pip install -r requirements.txt</li>
  <li>In the chatbot.py file insert your OPEAI token</li>
  <li>Run server(Flask): uvicorn server:app --host 0.0.0.0 --port 8000 </li>
  <li>In new terminal run client: python client.py</li>
  <li>If you have the following error: "You are using a deprecated configuration of Chroma. Please pip install chroma-migrate and run chroma-migrate to upgrade your configuration. See https://docs.trychroma.com/migration for more information or join our discord at https://discord.gg/8g5FESbj for help!"<br>
  Remove the line chroma_db_impl="duckdb+parquet", from langchain.vectorstores/chroma.py</li>
</ol>  

<h2>Usage</h2>

<ol>
  <li>In the terminal where you run client you can chat with the chatbot</li>
  <li>Chatbot is using information from the "terms" pdf document, that is located in the root directory</li>
</ol>