from template import chat_with_system_prompt

import os

OPENAI_MINI_MODEL = os.getenv("LAB_MINI_MODEL", "gemini-3.1-flash-lite")


if __name__ == "__main__":
    resp1, _ = chat_with_system_prompt(system_prompt="Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi.",
                                      user_prompt="Giải thích blockchain là gì?",
                                      model=OPENAI_MINI_MODEL)
    resp2, _ = chat_with_system_prompt(system_prompt="Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật.",
                                          user_prompt="Giải thích blockchain là gì?",
                                          model=OPENAI_MINI_MODEL)

    print(resp1, resp2)