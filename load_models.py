from transformers import AutoModelForCausalLM, AutoTokenizer, T5ForConditionalGeneration, T5Tokenizer
import torch

# ---- Chat Model: MPT-7B ----
chat_tokenizer = AutoTokenizer.from_pretrained("mosaicml/mpt-7b-instruct")
chat_model = AutoModelForCausalLM.from_pretrained("mosaicml/mpt-7b-instruct")

# ---- Code Generation Model: Code LLaMA 7B ----
code_tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-hf")
code_model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-7b-hf")

# ---- Summarization Model: T5-small ----
sum_tokenizer = T5Tokenizer.from_pretrained("t5-small")
sum_model = T5ForConditionalGeneration.from_pretrained("t5-small")

print("All models loaded successfully!")
