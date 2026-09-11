from template import run_assistant

if __name__ == "__main__":
    print("\n=== Trợ lý CLI (gõ 'quit' để thoát) ===")
    stats = run_assistant(
        persona="Bạn là senior BE python, "
                "trả lời ngắn gọn, đúng trọng tâm.",
    )
    print("\n--- Thống kê phiên chat ---")
    for key, value in stats.items():
        if key != "history":
            print(f"{key}: {value}")