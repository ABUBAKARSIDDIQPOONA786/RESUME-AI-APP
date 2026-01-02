import { useState } from 'react';
import axios from 'axios';

// Component Imports
import Navbar from '../components/Navbar';
import ResumeUpload from '../components/ResumeUpload';
import ScoreCard from '../components/ScoreCard';
import SkillsList from '../components/SkillsList';
import AnalysisBox from '../components/AnalysisBox'; // Added
import RecommendedRoles from '../components/RecommendedRoles';
import ExplanationBox from '../components/ExplanationBox';

export default function Dashboard() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleUpload = async (files) => {
    const file = files[0]; // Access the first file from the FileList
    if (!file) return;

    setLoading(true);
    setError(null);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const API_URL = import.meta.env.VITE_API_URL || "https://resume-ai-app-2.onrender.com";
      const response = await axios.post(`${API_URL}/resume/upload`, formData);
      setResult(response.data);
    } catch (err) {
      setError("Analysis failed. Please check your connection or file format.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-950">
      {/* 1. Navbar included at the top level of the Dashboard or App.jsx */}
      <Navbar /> 

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <header className="text-center mb-16">
          <h1 className="text-4xl md:text-6xl font-black text-white mb-6">
            AI Resume Intelligence
          </h1>
          <p className="text-slate-400 text-lg max-w-2xl mx-auto">
            Upload your resume for a 2026-standard ATS evaluation and career mapping.
          </p>
        </header>

        <ResumeUpload onUpload={handleUpload} loading={loading} />
        {error && <p className="text-red-400 text-center mt-4">{error}</p>}

        {result && (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mt-16 animate-in fade-in duration-1000">
            
            {/* Left/Main Column */}
            <div className="lg:col-span-2 space-y-8">
              {/* 2. AnalysisBox for High-Level Overview */}
              <AnalysisBox text={result.ats_analysis.summary || "Professional resume analysis complete."} />
              
              <ExplanationBox text={result.ats_analysis.explanation} />
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <SkillsList title="Matched Skills" skills={result.ats_analysis.details.skills_detected} type="match" />
                <SkillsList title="Missing Sections" skills={result.ats_analysis.details.sections_missing} type="missing" />
              </div>
            </div>

            {/* Right Sidebar */}
            <div className="space-y-8">
              <ScoreCard score={result.ats_analysis.total_score} />
              <RecommendedRoles roles={result.recommended_roles} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
