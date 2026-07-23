import json

from explorer import read_workspace_file
from llm import ask
from prompts import SYSTEM_PROMPT


current_file = "README.md"

visited = set()


while True:

    print("=" * 60)
    print(f"Reading: {current_file}")

    content = read_workspace_file(current_file)

    prompt = f"""
Task:

Find an ACTIVE AWS credential.

Current File:

{current_file}

Content:

{content}
"""

    response = ask(SYSTEM_PROMPT, prompt)

    print(response)

    result = json.loads(response)

    visited.add(current_file)

    if result["finished"]:
        print("\nMission Finished.")
        break

    next_file = result["next_file"]

    if next_file in visited:
        print("Loop detected.")
        break

    current_file = next_file