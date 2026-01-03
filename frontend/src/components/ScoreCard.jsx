export default function ScoreCard({ score }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 text-center">
      <p className="text-sm text-slate-400">ATS Compatibility Score</p>
      <p className="text-5xl font-bold text-green-400 mt-3">{score}%</p>
      <p className="text-xs text-slate-500 mt-2">
        Based on keyword density, formatting, and role alignment
      </p>
    </div>
  );
}
