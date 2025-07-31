import os
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language

def load_files(repository_path):
    """
    Loads Python files from the specified repository path using a generic loader.

    Args:
        repository_path (str): Local path to the cloned GitHub repository.

    Returns:
        List of Document objects parsed and ready for chunking/embedding.
    """
    print(f"[INFO] Loading Python files from: {repository_path}")

    loader = GenericLoader.from_filesystem(
        repository_path,
        glob="**/*.py",
        suffixes=[".py"],
        parser=LanguageParser(language=Language.PYTHON)
    )

    docs = loader.load()
    print(f"[INFO] Loaded {len(docs)} documents from the repository.")

    return docs
