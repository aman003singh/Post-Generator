from few_shot import FewShotPosts
from llm_model import llm

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "2-5 Lines"
    if length == "Medium":
        return "5 - 10 Lines"
    if length == "Long":
        return "10 - 25 Lines"
    
def generate_post(length , language , tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)
    return response.content

def get_prompt(length, language, tag):
    length_str = get_length_str(length)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble and only topic related content

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English and try using relevant emogis wherever necessary.
    '''

    examples = few_shot.get_filtered_posts(length, language, tag)

    if len(examples) > 0:
        prompt += "4) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: # Use max two samples
            break

    return prompt


# if __name__ == "__main__":
#     print(generate_post("Short", "Hinglish", "Mental Health"))