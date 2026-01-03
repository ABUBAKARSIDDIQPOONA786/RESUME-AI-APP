import { useState } from "react";
import ResumeUpload from "../components/ResumeUpload";
import ScoreCard from "../components/ScoreCard";
import SkillsList from "../components/SkillsList";
import RecommendedRoles from "../components/RecommendedRoles";
import ExplanationBox from "../components/ExplanationBox";

export default function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <div className="space-y-12">
      {/* HERO */}
      <section className="text-center space-y-4">
        <h1 className="text-4xl font-bold leading-tight">
          AI Resume Intelligence Platform
        </h1>
        <p className="text-slate-400 max-w-2xl mx-auto">
          Upload your resume to receive a 2026-ready ATS score, skill intelligence,
          and AI-powered role recommendations — in seconds.
        </p>
      </section>

      {/* UPLOAD */}
      {!result && (
        <section className="max-w-xl mx-auto">
          <ResumeUpload onResult={setResult} />
        </section>
      )}

      {/* RESULTS */}
      {result && (
        <section className="space-y-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <ScoreCard score={result.ats_score} />
            <SkillsList skills={result.skills} />
            <RecommendedRoles roles={result.recommended_roles} />
          </div>

          <ExplanationBox explanation={result.explanation} />
        </section>
      )}
    </div>
  );
}
