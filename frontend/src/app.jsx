import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';

function App() {
<<<<<<< HEAD
  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 selection:bg-blue-500/30">
      {/* Global Navigation */}
      <Navbar />
      
      {/* Main Page Content */}
      <main>
        <Dashboard />
      </main>

      {/* Simple Footer */}
      <footer className="py-12 border-t border-slate-900 text-center text-slate-600 text-sm">
        &copy; 2026 Resume.AI Platform • Built with Agentic AI logic
      </footer>
=======
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
>>>>>>> 27955f9902d99cd5954861ba4381a6a4b038d34c
    </div>
  }
}

export default App;
