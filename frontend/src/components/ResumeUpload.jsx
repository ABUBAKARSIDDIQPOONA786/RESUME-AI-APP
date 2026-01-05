import { analyzeResume } from "../api/client";
import { useState } from "react";

export default function ResumeUpload({ onResult }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setError("");
      const data = await analyzeResume(formData);
      onResult(data);
    } catch {
      setError("Analysis failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <input type="file" accept=".pdf,.docx" onChange={handleUpload} />
      {loading && <p>Analyzing...</p>}
      {error && <p className="error">{error}</p>}
    </div>
  );
}
