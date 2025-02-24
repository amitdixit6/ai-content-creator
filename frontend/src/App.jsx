const generateContent = async () => {
    setLoading(true);
    setContent(""); // Clear old content
    try {
      const response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, content_type: type }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      setContent(data.content);
    } catch (error) {
      console.error("Error fetching content:", error);
      setContent("❌ Error fetching content. Please try again!");
    }
    setLoading(false);
};
