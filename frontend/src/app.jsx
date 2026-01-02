import { useState } from "react";
import ResumeUpload from "./components/ResumeUpload";
import ScoreCard from "./components/ScoreCard";
import SkillsList from "./components/SkillsList";
import ExplanationBox from "./components/ExplanationBox";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <h1>AI Resume Intelligence Platform</h1>
      <ResumeUpload setResult={setResult} />

      {result && (
        <>
          <ScoreCard score={result.ats_score} />
          <SkillsList title="Matched Skills" skills={result.matched_skills} />
          <SkillsList title="Missing Skills" skills={result.improvement_suggestions} />
          <ExplanationBox text={result.explanation} />
        </>
      )}
    </div>
  );
}

export default App;