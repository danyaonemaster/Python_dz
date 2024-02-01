import re


def run():
    print("\n","Tast_03","\n")
    text = """Hello Python! Hello User! How are you Python? I’m good, and you? Thank you, I’m
            good, too. Can you help me with task? Yes, sure. It’s my task (show the code). I want to ask
            ChatGPT."""

    text_list = re.split("[!?.]", text)
    text_space_list = [i for i in text if i == " "]
    text_without_spaces_01 = text.replace(' ', '')
    text_without_spaces_02 = "".join(text.split(" "))

    text_a_list = [i for i in text.lower() if i == "a"]

    print(f"\n\n\nlen proposals list : {len(text_list[:-1])}",
          f"len spase list : {len(text_space_list)}",
          f"len a list : {len(text_a_list)}",
          f"lower case list : {text.lower()}",
          f"text without spaces 01 : {text_without_spaces_01}",
          f"text without spaces 02 : {text_without_spaces_02}",
          f"replacing words in text : {text.replace("Python", "Java")
          .replace("ChatGPT", "Python")}",
          f"every fifth character in text : {text[::5]}", sep='\n\n')

    print(f"len text is {"even" if len(text) % 2 == 0 else "odd"}", end="\n\n")

    print(f"text in reverse order : {text[::-1]}",end="\n\n")
