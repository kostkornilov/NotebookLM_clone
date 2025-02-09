import { useState } from "react";
import axios from "axios";
import { TextField, Button } from "@mui/material";
import ReactMarkdown from "react-markdown";

const ChatBox = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!query) return;
    setLoading(true);
    
    try {
      const res = await axios.post("http://localhost:8000/chat/ask/", { query });
      setResponse(res.data.answer);
    } catch (error) {
      setResponse("Error fetching answer.");
    }

    setLoading(false);
  };

  return (
    <div>
      <TextField fullWidth label="Ask a question" value={query} onChange={(e) => setQuery(e.target.value)} />
      <Button variant="contained" onClick={handleAsk} disabled={loading}>
        {loading ? "Thinking..." : "Ask"}
      </Button>
      <ReactMarkdown>{response}</ReactMarkdown>
    </div>
  );
};

export default ChatBox;
