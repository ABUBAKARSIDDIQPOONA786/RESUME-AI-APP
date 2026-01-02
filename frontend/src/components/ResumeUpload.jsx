
import { Upload, FileText, Loader2 } from 'lucide-react';

import axios from "axios";

export default function ResumeUpload({ setResult }) {
  const [uploading, setUploading] = useState(false);

  const handleFile = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setUploading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      // 2026 Live Backend URL
      const response = await axios.post(
        "resume-ai-app-2.onrender.com", 
        formData
      );
      setResult(response.data);
    } catch (err) {
      alert("Error: Check if the backend is awake or file is too large.");
    } finally {
      setUploading(false);
    }
  };
>>>>>>> 27955f9902d99cd5954861ba4381a6a4b038d34c

export default function ResumeUpload({ onUpload, loading }) {
  return (
<<<<<<< HEAD
    <div className="w-full max-w-xl mx-auto">
      <label className="group relative flex flex-col items-center justify-center w-full h-56 border-2 border-slate-800 border-dashed rounded-[2rem] cursor-pointer bg-slate-900/40 hover:bg-slate-900 hover:border-blue-500/50 transition-all duration-500">
        <div className="flex flex-col items-center justify-center space-y-4">
          <div className="p-4 bg-slate-800 rounded-2xl group-hover:scale-110 transition-transform duration-500">
            {loading ? <Loader2 className="w-10 h-10 text-blue-400 animate-spin" /> : <Upload className="w-10 h-10 text-blue-400" />}
          </div>
          <div className="text-center">
            <p className="text-xl font-bold text-slate-200">
              {loading ? "AI is processing..." : "Upload Resume"}
            </p>
            <p className="text-sm text-slate-500 mt-1">PDF or DOCX accepted (Max 5MB)</p>
          </div>
        </div>
        <input 
          type="file" 
          className="hidden" 
          onChange={(e) => onUpload(e.target.files[0])} 
          accept=".pdf,.docx" 
          disabled={loading}
        />
      </label>

    <div className="upload-box">
      <input type="file" onChange={handleFile} id="fileInput" hidden />
      <button onClick={() => document.getElementById('fileInput').click()}>
        {uploading ? "Analyzing Resume..." : "Upload Resume (PDF/DOCX)"}
      </button>

    </div>
  );
}
