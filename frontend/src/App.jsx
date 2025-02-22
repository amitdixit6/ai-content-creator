import { useState } from "react";

function App() {
  const [topic, setTopic] = useState("");
  const [content, setContent] = useState("");
  const [type, setType] = useState("blog");
  const [loading, setLoading] = useState(false);

  const generateContent = async () => {
    setLoading(true);
    setContent(""); // Clear old content
    try {
      const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, content_type: type }),
      });
      const data = await response.json();
      setContent(data.content);
    } catch (error) {
      setContent("Error fetching content. Please try again!");
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">🚀 AI Content Generator</h1>
      
      <input
        className="border p-2 w-80 mb-2"
        type="text"
        placeholder="Enter Topic..."
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />
      
      <select 
        className="border p-2 w-80 mb-2" 
        value={type} 
        onChange={(e) => setType(e.target.value)}
      >
        <option value="blog">📝 Blog</option>
        <option value="youtube_script">🎬 YouTube Script</option>
      </select>
      
      <button 
        onClick={generateContent} 
        className="bg-blue-500 text-white px-4 py-2 rounded"
        disabled={loading}
      >
        {loading ? "Generating..." : "Generate Content"}
      </button>

      <div className="mt-4 p-4 bg-white border w-80 text-sm">
        {loading ? "⏳ Generating AI Content..." : content}
      </div>
    </div>
  );
}

export default App;
