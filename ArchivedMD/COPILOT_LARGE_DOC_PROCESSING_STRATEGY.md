# GitHub Copilot Large Document Processing Strategy

When dealing with massive documentation files (such as 3000+ line markdown files), LLMs (including GitHub Copilot) deal with finite context windows and the "lost in the middle" phenomenon—where information exactly in the middle of a massive prompt gets ignored. 

Based on industry best practices and Copilot's architecture, here are the most current techniques for processing very large files without losing context:

## 1. Copilot-Specific Techniques
* **Targeted Context via Line Ranges:** Instead of asking Copilot to read an entire large file at once, use the `read_file` tool to read explicit line ranges. Copilot performs much better across several 500-line iterations than one 10,000-line load.
* **Avoid Relying on Implicit Context:** If a file exceeds the token limit, Copilot will truncate it implicitly. Always assume a very large file is being truncated unless scoped out logically.

## 2. Chunking Strategies & Overlap (General LLM Best Practices)
* **Chunk Size:** The industry standard for text processing has settled around chunk sizes of **512 to 2,000 tokens** (roughly 100-200 lines). 
* **Sliding Window / Overlap:** To prevent losing context between chunks, pipelines use an overlap of **10% to 20%** (e.g., 20 lines). This ensures that if a character description or plot point is cut in half, the next chunk has enough leading context to understand it.
* **Semantic Chunking:** Modern workflows split by semantic boundaries: Markdown headers or blank lines.

## 3. "Line-by-Line" Pipeline Techniques
If the goal is to truly review a massive file sequentially without missing a single line, we must use a **Stateful / Sliding Window Processing** approach:
1. **Map:** Pass each small chunk of the file (e.g., 100 lines + 20 lines overlap) independently with the same instructions.
2. **Digest:** Extract all relevant entities (characters, technology, logistics).
3. **Write:** Append these immediately to the structured files (`CHARACTERS.md`, etc.).
4. **Reduce (Optional):** Have a final sweep to aggregate and de-duplicate the results.

## Recommended Approach for this Project (The Read-Digest-Write Loop):
1. Create a checklist tracking parsing status (e.g., Lines 1-100: Done, 80-180: Next). Note the 20-line overlap.
2. The agent reads the exact chunk.
3. The agent maps data to the categorical markdown files.
4. Uncategorized or contradictory fluff goes to `RAW_BRAINSTORM.md` or `FLUFF.md`.
5. The agent stops and asks for confirmation to proceed to the next chunk.
