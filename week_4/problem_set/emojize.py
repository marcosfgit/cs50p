import emoji

str = input("Input: ")
str_emojized = emoji.emojize(str, language="alias")

print("Output:", str_emojized)
