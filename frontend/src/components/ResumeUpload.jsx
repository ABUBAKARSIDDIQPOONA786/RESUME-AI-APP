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

  return (
    <div className="upload-box">
      <input type="file" onChange={handleFile} id="fileInput" hidden />
      <button onClick={() => document.getElementById('fileInput').click()}>
        {uploading ? "Analyzing Resume..." : "Upload Resume (PDF/DOCX)"}
      </button>
    </div>
  );
}
