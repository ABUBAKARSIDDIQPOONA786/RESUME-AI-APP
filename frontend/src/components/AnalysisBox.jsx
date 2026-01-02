import { Sparkles, Activity } from 'lucide-react';

export default function AnalysisBox({ text }) {
  return (
    <div className="bg-gradient-to-br from-blue-600/10 to-purple-600/10 border border-blue-500/20 p-8 rounded-3xl shadow-2xl relative overflow-hidden">
      <div className="absolute top-0 right-0 p-4 opacity-10">
        <Activity size={80} />
      </div>
      
      <div className="flex items-center gap-3 mb-4">
        <Sparkles className="text-blue-400 w-6 h-6" />
        <h3 className="text-xl font-bold text-white tracking-tight">Executive Summary</h3>
      </div>
      
      <p className="text-slate-300 text-lg leading-relaxed italic">
        "{text}"
      </p>
      
      <div className="mt-6 flex gap-4">
        <div className="text-xs font-bold text-blue-400 uppercase tracking-widest bg-blue-500/10 px-3 py-1 rounded-md">
          AI Verified
        </div>
        <div className="text-xs font-bold text-slate-500 uppercase tracking-widest px-3 py-1 border border-slate-800 rounded-md">
          2026 Logic
        </div>
      </div>
    </div>
  );
}
