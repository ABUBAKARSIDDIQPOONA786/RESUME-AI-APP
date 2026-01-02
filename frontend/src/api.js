import axios from "axios";

const API = axios.create({
  baseURL: "https://resume-ai-app-2.onrender.com" 
});

export const analyzeResume = (formData) =>
  API.post("/resume/upload", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });

export const recommendRoles = (formData) =>
  API.post("/resume/recommend-roles", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });
