import re

def check_prompt(prompt: str):
    try:
        match = re.search(r"```json\s+(.*?)```", prompt, re.DOTALL)

        if match:
            print(match)
            prompt_content = match.group(1)
            return True, prompt_content
        else:
            return False, ""
    
    except Exception as e:
        return False, ""
