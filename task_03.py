import re


def run():
    text = ("Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m ""\n"
            "good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask ""\n"
            "ChatGPT.")

    text_list = re.split("[!?.]", text)

    text_space_list = [i for i in text if i == " "]

    text_without_spaces_01 = text.replace(' ', '')

    text_without_spaces_02 = "".join(text.split(" "))

    text_a_list = [i for i in text.lower() if i == "a"]

    enter = "\n\n"

    print(f"\nlen proposals list : {len(text_list[:-1])}{enter}"
          f"len spase list : {len(text_space_list)}{enter}"
          f"len a list : {len(text_a_list)}{enter}"
          f"lower case list : {text.lower()}{enter}"
          f"text without spaces 01 : {text_without_spaces_01}{enter}"
          f"text without spaces 02 : {text_without_spaces_02}{enter}"
          f"replacing words in text : {text.replace("Python", "Java")
          .replace("ChatGPT", "Python")}{enter}"
          f"every fifth character in text : {text[::5]}{enter}")
    if len(text) % 2 == 0:
        print(f"Is the text length even or odd :len text is even{enter}")
    else:
        print(f"Is the text length even or odd : len text is odd{enter}")

    print(f"text in reverse order : {text[::-1]}{enter}")