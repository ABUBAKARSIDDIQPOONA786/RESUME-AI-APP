import { MessageSquare, Info } from 'lucide-react';

export default function ExplanationBox({ text }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl animate-fade-in">
      {/* Header */}
      <div className="bg-slate-800/50 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <MessageSquare className="w-5 h-5 text-blue-400" />
          <span className="text-sm font-bold uppercase tracking-wider text-slate-300">AI Feedback</span>
        </div>
        <Info className="w-4 h-4 text-slate-500 cursor-help" />
      </div>

      {/* Content */}
      <div className="p-6">
        <div className="prose prose-invert max-w-none text-slate-300 leading-relaxed">
          {text ? (
            <p className="whitespace-pre-line">{text}</p>
          ) : (
            <div className="flex flex-col items-center py-4 opacity-40">
              <p className="text-sm italic">Analysis will appear here after upload.</p>
            </div>
          )}
        </div>
        
        {/* Footer Hint */}
        {text && (
          <div className="mt-6 pt-6 border-t border-slate-800/50 flex items-center gap-2 text-xs text-slate-500">
            <span className="w-2 h-2 bg-emerald-500 rounded-full"></span>
            Agentic AI processing completed for 2026 standards.
          </div>
        )}
      </div>
    </div>
  );
}
