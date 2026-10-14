
print("=" * 50)
print("Welcome to emoji & slang translator")
print("=" * 50)
user_sentence = input("Enter message or sentence : ")
text_lower = user_sentence.lower()
#string replace
#we use .replace method here
translated = text_lower.replace("love","❤️")
translated = translated.replace("python","🐍✨")
translated = translated.replace("coding","💻🔥")
translated = translated.replace("happy","😄🎉")
translated = translated.replace("sad", "😢📉")
translated = translated.replace("fire", "🔥🚀")
translated = translated.replace("cool","😎✨")

# 4. Results display garne

print("\n" + "-" * 50)
print(" ORIGINAL TEXT :", user_sentence)
print("TRANSLATED   :", translated)
print("-" * 50)


reversed_text = user_sentence[::-1]
print("MIRROR TEXT  :", reversed_text)

# # 6. Basic Statistics (Length check)
total_chars = len(user_sentence)
print(f"Total Characters processed: {total_chars}")
print("=" * 50)
print("Thank you for using Emoji Translator!")