with open("sample.txt", "r", encoding="UTF-8") as file:
    text_ = file.read()

new_text = ". ".join(
    map(lambda str_: str_.capitalize(), text_.split(". ")))

with open("sample_new.txt", "w", encoding="UTF-8") as file:
    print(new_text, file=file, end="")
