import { useState } from 'react';
import { Upload, Loader2, FileText } from 'lucide-react';

export default function ResumeUpload({ onUpload, loading }) {
  return (
    <div className="w-full max-w-xl mx-auto">
      <label className="group relative flex flex-col items-center justify-center w-full h-56 border-2 border-slate-800 border-dashed rounded-[2rem] cursor-pointer bg-slate-900/40 hover:bg-slate-900 hover:border-blue-500/50 transition-all duration-500">
        <div className="flex flex-col items-center justify-center space-y-4">
          <div className="p-4 bg-slate-800 rounded-2xl group-hover:scale-110 transition-transform duration-500">
            {loading ? (
              <Loader2 className="w-10 h-10 text-blue-400 animate-spin" />
            ) : (
              <Upload className="w-10 h-10 text-blue-400" />
            )}
          </div>
          <div className="text-center">
            <p className="text-xl font-bold text-slate-200">
              {loading ? "AI is processing..." : "Upload Resume"}
            </p>
            <p className="text-sm text-slate-500 mt-1">PDF or DOCX accepted (Max 5MB)</p>
          </div>
        </div>
        <input 
          type="file" 
          className="hidden" 
          onChange={(e) => onUpload(e.target.files)} 
          accept=".pdf,.docx" 
          disabled={loading}
        />
      </label>
    </div>
  );
}
