const API_BASE = import.meta.env.VITE_API_BASE_URL;

const analyzeResume = async (file) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE}/analyze-resume`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Resume analysis failed");
  }

  return await response.json();
};
