import { useState } from "react";
import { analyzeResume } from "../api";

export default function ResumeUpload({ setResult }) {
  const [file, setFile] = useState(null);
  const [role, setRole] = useState("Data Analyst");

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("target_role", role);

    const res = await analyzeResume(formData);
    setResult(res.data);
  };

  return (
    <div>
      <h2>Upload Resume</h2>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <select onChange={e => setRole(e.target.value)}>
        <option>Data Analyst</option>
        <option>Software Engineer</option>
        <option>Product Manager</option>
      </select>
      <button onClick={handleSubmit}>Analyze</button>
    </div>
  );
}