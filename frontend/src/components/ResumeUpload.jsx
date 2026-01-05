import { useState } from "react";
import { analyzeResume } from "../api/client";

export default function ResumeUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyze = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setError("");
      const data = await analyzeResume(formData);
      onResult(data);
    } catch (err) {
      setError("Analysis failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl p-6 bg-white rounded-xl shadow-md space-y-4">
      <div>
        <label className="block font-medium mb-2">Upload Resume</label>
        <input
          type="file"
          accept=".pdf,.docx"
          onChange={(e) => setFile(e.target.files[0])}
          className="block w-full text-sm"
        />
        <p className="text-xs text-gray-500 mt-1">
          PDF or DOCX • Max 5MB
        </p>
      </div>

      <button
        onClick={handleAnalyze}
        disabled={!file || loading}
        className={`px-6 py-2 rounded-lg text-white font-semibold transition
          ${loading || !file
            ? "bg-gray-400 cursor-not-allowed"
            : "bg-black hover:bg-gray-800"
          }`}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {error && (
        <p className="text-red-600 text-sm font-medium">{error}</p>
      )}
    </div>
  );
}
