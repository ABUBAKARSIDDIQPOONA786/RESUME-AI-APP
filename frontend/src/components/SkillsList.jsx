import { CheckCircle, AlertTriangle } from 'lucide-react';

export default function SkillsList({ title, skills = [], type = "match" }) {
  const isMatch = type === "match";

  return (
    <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl shadow-xl h-full">
      <h3 className="text-lg font-bold mb-5 flex items-center gap-2 text-slate-100">
        {isMatch ? <CheckCircle className="text-emerald-400 w-5 h-5"/> : <AlertTriangle className="text-yellow-400 w-5 h-5"/>}
        {title}
      </h3>
      <div className="flex flex-wrap gap-2">
        {skills.length > 0 ? skills.map((skill, index) => (
          <span key={index} className={`px-4 py-1.5 rounded-full text-sm font-semibold border transition-colors ${
            isMatch 
              ? "bg-emerald-500/10 text-emerald-300 border-emerald-500/30 hover:bg-emerald-500/20" 
              : "bg-blue-500/10 text-blue-300 border-blue-500/30 hover:bg-blue-500/20"
          }`}>
            {skill}
          </span>
        )) : (
          <p className="text-slate-500 text-sm italic">Scanning content...</p>
        )}
      </div>
    </div>
  );
}
