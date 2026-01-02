import axios from "axios";

const API = axios.create({
  baseURL: "https://resume-intelligence-api.onrender.com"
});

export const analyzeResume = (formData) =>
  API.post("/resume/explain", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });

export const recommendRoles = (formData) =>
  API.post("/resume/recommend-roles", formData, {
    headers: { "Content-Type": "multipart/form-data" }
  });
