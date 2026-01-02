import axios from 'axios';

// Use environment variable or fallback to your live Render URL
const API_URL = import.meta.env.VITE_API_URL || "https://resume-ai-app-2.onrender.com";

export const uploadResume = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await axios.post(`${API_URL}/resume/upload`, formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
};
