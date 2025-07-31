import sys
import os

from lib.repository import download_github_repo
from lib.loader import load_files
from lib.utils import (
    load_LLM,
    select_model,
    read_prompt,
    get_available_models
)
from lib.chain import create_retriever, create_qa_chain

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <GitHub Repository URL>")
        sys.exit(1)

    repo_url = sys.argv[1]
    repo_dir = "./repo"

    # Step 1: Download or update GitHub repository
    download_github_repo(repo_url, repo_dir)

    # Step 2: Load documents from the repo
    docs = load_files(repo_dir)

    # Step 3: Select model
    llm_name = select_model()
    llm = load_LLM(llm_name)

    # Step 4: Create retriever
    db_path = "./vectorstore"
    retriever = create_retriever(llm_name, db_path, docs)

    # Step 5: Load prompts
    initial_prompt = read_prompt("initial_prompt.txt")
    eval_prompt = read_prompt("evaluation_prompt.txt")
    prompts = {
        "initial_prompt": initial_prompt,
        "evaluation_prompt": eval_prompt
    }

    # Step 6: Create QA chain
    chain = create_qa_chain(llm, retriever, prompts)

    # Step 7: Run interactive Q&A
    print("\n[System] QA chain is ready. Ask your questions about the codebase!\n")
    while True:
        user_input = input(">> Your question (or 'exit'): ")
        if user_input.lower() == "exit":
            print("[System] Exiting...")
            break
        result = chain.invoke({"question": user_input})
        print(f"\nAnswer: {result['output']}")
        print(f"Accuracy: {result['evaluation'].accuracy}")
        print(f"Feedback: {result['evaluation'].feedback}\n")

if __name__ == "__main__":
    main()
