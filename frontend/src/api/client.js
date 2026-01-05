import axios from "axios";

const API = axios.create({
  baseURL: "https://resume-ai-app-2.onrender.com",
  timeout: 120000, // 2 minutes
});

export const analyzeResume = async (formData) => {
  const res = await API.post("/resume/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });
  return res.data;
};
