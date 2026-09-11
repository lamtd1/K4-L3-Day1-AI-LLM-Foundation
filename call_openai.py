from template import call_openai
import os

OPENAI_MODEL= os.getenv("LAB_MODEL", "gemini-3-flash-preview")


if __name__ == "__main__":
    text1, _ = call_openai(
                    prompt="Hãy kể cho tôi một sự thật thú vị về Việt Nam.",
                    model=OPENAI_MODEL,
                    temperature= 0.0,
                    top_p= 0.9,
                    max_tokens= 1024)

    text2, _ = call_openai(
                        prompt="Hãy kể cho tôi một sự thật thú vị về Việt Nam.",
                        model=OPENAI_MODEL,
                        temperature= 0.5,
                        top_p= 0.9,
                        max_tokens= 1024)
    text3, _ = call_openai(
                        prompt="Hãy kể cho tôi một sự thật thú vị về Việt Nam.",
                        model=OPENAI_MODEL,
                        temperature= 1.0,
                        top_p= 0.9,
                        max_tokens= 256)

    print(f"temp 0.0: text - {text1}")
    print(f"temp 0.5: text - {text2}")
    print(f"temp 1.0: text - {text3}")