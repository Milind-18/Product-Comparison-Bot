# 🛒 Product Comparison Bot

An AI-powered assistant that compares **two products** in real-time and provides a side-by-side analysis with a final recommendation.  
Built during my **IIT Jammu Internship** as a CrewAI mini-project under the mentorship of **Parmveer Nandal**.

## 📌 Overview
The **Product Comparison Bot** takes the names of two products as input, fetches real-time information from the web, analyzes key specifications, and generates a clear comparison along with a recommendation for the better option.

This project demonstrates the power of **multi-agent workflows** using CrewAI combined with the **OpenAI API** for intelligent analysis.

---

## ✨ Features
- Takes **two product names** as input
- Fetches real-time product details via web search
- Extracts and structures specifications, features, and reviews
- Compares products side-by-side
- Provides a **final AI-generated recommendation**
- Modular design for easy customization

---

## 🛠 Tech Stack
- **Python** – Core programming language
- **CrewAI** – Multi-agent workflow orchestration
- **OpenAI API** – Natural language processing & comparison generation
- **LangChain** – LLM integration & agent handling
- **dotenv** – Environment variable management

---

## 📂 Project Structure
```

.
├── crew\.py               # Main script to run the bot
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment file
└── README.md             # Project documentation

````

---

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/product-comparison-bot.git
cd product-comparison-bot
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
   Create a `.env` file in the root folder and add:

```
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4
```

5. **Run the bot**

```bash
python crew.py
```

---

## 🚀 Usage

* Run the bot and enter **two product names** when prompted.
* The bot will search the web, extract details, compare features, and give a recommendation.

Example:

```
Enter first product name: iPhone 14
Enter second product name: Samsung Galaxy S23
```

---

## 📚 Learning Outcomes

* Building multi-agent AI workflows
* Integrating LLMs into real-world applications
* Orchestrating data retrieval, processing, and recommendation pipelines

---

## 🙏 Acknowledgments

Special thanks to **Parmveer Nandal** for his mentorship and guidance during this internship.

---

## 📜 License

This project is licensed under the MIT License – feel free to use and modify it.

---

## 🔗 Connect

If you found this project interesting, feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/milind18/) or check out more of my work!



