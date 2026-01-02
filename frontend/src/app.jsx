import { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import ScoreCard from "./components/ScoreCard";
import SkillsList from "./components/SkillsList";
import ExplanationBox from "./components/ExplanationBox";

function App() {
  const [result, setResult] = useState(null);

  // Based on your live backend response structure:
  // result.ats_analysis.total_score
  // result.ats_analysis.details.skills_detected

  return (
    <div className="container">
      <h1>AI Resume Intelligence Platform</h1>
      
      {/* Ensure ResumeUpload receives the correct setter */}
      <ResumeUpload setResult={setResult} />

      {result && result.ats_analysis && (
        <div className="result-grid">
          {/* Main Score Card */}
          <ScoreCard score={result.ats_analysis.total_score} />

          {/* Explanation from the AI layer */}
          <ExplanationBox 
             text={result.ats_analysis.explanation || "No automated explanation generated."} 
          />

          {/* Matched Skills */}
          <SkillsList 
            title="Skills Found" 
            skills={result.ats_analysis.details.skills_detected} 
          />

          {/* Suggestions Logic */}
          <SkillsList 
            title="Missing Sections" 
            skills={result.ats_analysis.details.sections_missing || []} 
            type="warning"
          />
        </div>
      )}
    </div>
  }
}

export default App;
