# 🧠 Smart Customer Support Router using Mixture of Experts (MoE)

## 📘 Unit 2 Assignment  
### Topic: Advanced Architecture using Groq API

---

## 🎯 Objective

The objective of this project is to build a **Smart Customer Support Router** using a **Mixture of Experts (MoE)** architecture.

Instead of using a single general-purpose AI model to handle all customer queries, this system intelligently routes user queries to specialized expert configurations such as:

- 👨‍💻 Technical Expert → Handles bug reports and coding issues  
- 💳 Billing Expert → Handles refunds and payment issues  
- 🤝 General Expert → Handles casual conversations  

The router determines the most appropriate expert using an LLM-based intent classification mechanism and forwards the request accordingly.

---

## 🏗️ System Architecture

The system consists of the following major components:

1. **Router (Gating Network)**  
   Uses an LLM to classify user intent into:
   - `technical`
   - `billing`
   - `general`

2. **Experts (Specialized LLM Configurations)**  
   Each expert is simulated using:
   - The same base model (`openai/gpt-oss-120b`)
   - Different System Prompts

3. **Orchestrator**  
   Responsible for:
   - Calling the router
   - Selecting the appropriate expert
   - Generating the final response

4. **Tool Expert (Bonus)**  
   Routes certain queries (e.g., Bitcoin price) to an external function instead of the LLM.

---

## ⚙️ Tech Stack

- Python
- Groq API
- Mixtral-8x7b-32768 Model
- python-dotenv

---

## 📦 Required Imports

```python
from groq import Groq
from dotenv import load_dotenv
import os
