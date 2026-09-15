import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");

    try {
      const response = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error("Failed to get answer from backend.");
      }

      setAnswer(data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Something went wrong. Please make sure the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="chat-container">
        <h1>RAG Question Answering System</h1>

        <p className="subtitle">
          Ask questions from your documents
        </p>

        <div className="input-area">
          <input
            type="text"
            placeholder="Enter your question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleAsk();
              }
            }}
          />

          <button onClick={handleAsk} disabled={loading}>
            {loading ? "Asking..." : "Ask"}
          </button>
        </div>

        {answer && (
          <div className="answer-box">
            <h3>Answer</h3>
            <p>{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;