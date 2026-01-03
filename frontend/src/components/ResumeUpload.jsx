import { useState } from "react";
import api from "../api/client";

export default function ResumeUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const submit = async () => {
    if (!file) return setError("Please upload a resume.");

    setLoading(true);
    setError("");

    const form = new FormData();
    form.append("file", file);

    try {
      const res = await api.post("/resume/upload", form);
      onResult(res.data);
    } catch {
      setError("Analysis failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8 space-y-6 shadow-xl">
      <label className="flex flex-col items-center justify-center border-2 border-dashed border-slate-700 rounded-xl p-8 cursor-pointer hover:border-indigo-500 transition">
        <p className="text-slate-300 font-medium">Upload Resume</p>
        <p className="text-xs text-slate-500 mt-1">
          PDF or DOCX • Max 5MB
        </p>
        <input
          type="file"
          accept=".pdf,.doc,.docx"
          className="hidden"
          onChange={(e) => setFile(e.target.files[0])}
        />
      </label>

      <button
        onClick={submit}
        disabled={loading}
        className="w-full bg-indigo-600 hover:bg-indigo-700 py-3 rounded-xl font-semibold disabled:opacity-50"
      >
        {loading ? "Analyzing with Agentic AI..." : "Analyze Resume"}
      </button>

      {error && <p className="text-red-400 text-sm">{error}</p>}
    </div>
  );
}
