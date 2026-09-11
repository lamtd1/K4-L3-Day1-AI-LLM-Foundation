# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)

> 0.0: trả lời gần như cố định, lặp lại nội dung tương tự mỗi lần gọi (deterministic).
0.5 → 1.0: sự đa dạng tăng dần — cùng prompt nhưng câu trả lời khác nhau về cách diễn đạt, góc kể.
1.5: có thể chệch hướng, lặp, hoặc sinh nội dung kém logic — "sáng tạo" quá mức.
→ Quy luật: temperature càng cao → entropy sampling càng lớn → độ ngẫu nhiên tăng, độ nhất quán giảm.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Đặt temperature ≈ 0.2–0.5 (thường 0.3).

Lý do: khách hàng cần đúng, nhất quán, an toàn — không cần sáng tạo. Temperature thấp giúp tránh hallucination và trả lời đồng nhất giữa các phiên.

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> GPT-4o đắt hơn khoảng 17 lần. Phân tích pháp lý, y khoa, hoặc cần suy luận phức tạp chính xác thì dùng GPT-4o, Chatbot FAQ, phân loại ticket, tóm tắt ngắn — volume cao, độ khó thấp dùng GPT-4o-mini.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> System prompt ảnh hưởng rõ đến cách model trả lời. Persona giáo viên dùng từ ngữ đơn giản, ví dụ gần gũi; persona chuyên gia dùng thuật ngữ kỹ thuật và giải thích sâu hơn. Vì vậy, system prompt định hướng từ vựng, độ dài, mức độ chi tiết và cách trình bày của model.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> tiktoken cho số token chính xác hơn so với cách ước lượng số từ / 0.75. Hai con số chênh lệch vì một từ có thể được tách thành nhiều token. Tiếng Việt thường tốn nhiều token hơn tiếng Anh do đặc điểm dấu và cách tokenizer chia nhỏ từ.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming phù hợp khi response dài và cần phản hồi ngay, giúp người dùng không phải chờ toàn bộ kết quả. Non-streaming phù hợp với response ngắn hoặc khi cần xử lý toàn bộ kết quả trước khi hiển thị.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff giúp giảm tải cho API bằng cách tăng dần thời gian chờ giữa các lần retry. Nếu hàng nghìn client cùng retry sau đúng 1 giây, chúng sẽ gửi request đồng thời, gây thundering herd và làm API càng quá tải.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Persona: Senior Backend Python.
System prompt: “Bạn là senior Backend Python, trả lời bằng tiếng Việt, ngắn gọn và đúng trọng tâm.”
“Senior Backend Python” giúp câu trả lời tập trung vào kiến thức thực tế và chuyên môn. “Ngắn gọn, đúng trọng tâm” giúp tránh giải thích dài dòng, phù hợp khi xử lý vấn đề kỹ thuật.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất là history chỉ lưu được vài lượt hội thoại, nên trợ lý dễ quên ngữ cảnh. Có thể cải thiện bằng cách lưu lịch sử vào database hoặc Redis, sau đó lấy lại các cuộc trò chuyện liên quan khi người dùng hỏi.

---

## Danh Sách Kiểm Tra Nộp Bài

- [X] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [X] Cả 4 checkpoint pytest đều pass
- [X] Tất cả 9 câu trong file này đã được trả lời
- [x] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
