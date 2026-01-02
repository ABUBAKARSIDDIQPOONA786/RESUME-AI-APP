import { Briefcase, Target, ChevronRight } from 'lucide-react';

export default function RecommendedRoles({ roles = [] }) {
  return (
    <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl shadow-xl h-full animate-fade-in">
      <h3 className="text-xl font-bold mb-6 flex items-center gap-3 text-slate-100">
        <Target className="text-blue-400 w-6 h-6" />
        Best-Fit Job Roles
      </h3>
      
      <div className="space-y-3">
        {roles.length > 0 ? roles.map((role, index) => (
          <div 
            key={index} 
            className="group flex items-center justify-between p-4 bg-slate-950/50 border border-slate-800 rounded-xl hover:border-blue-500/50 transition-all cursor-default"
          >
            <div className="flex items-center gap-4">
              <div className="bg-slate-800 p-2 rounded-lg group-hover:bg-blue-600/10 transition-colors">
                <Briefcase className="w-5 h-5 text-blue-400" />
              </div>
              <div>
                <p className="font-bold text-slate-200">{role.title}</p>
                <p className="text-xs text-slate-500">Confidence Match: {role.match_score}%</p>
              </div>
            </div>
            <ChevronRight className="w-5 h-5 text-slate-600 group-hover:text-blue-400 group-hover:translate-x-1 transition-all" />
          </div>
        )) : (
          <p className="text-slate-500 text-sm italic">Analyze your resume to see recommended career paths.</p>
        )}
      </div>
    </div>
  );
}
