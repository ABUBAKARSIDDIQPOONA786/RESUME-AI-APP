export default function ScoreCard({ score }) {
  const isHigh = score >= 80;
  const colorClass = isHigh ? "text-emerald-400 border-emerald-500" : "text-yellow-400 border-yellow-500";

  return (
    <div className="bg-slate-900 border border-slate-800 p-8 rounded-2xl shadow-xl flex flex-col items-center justify-center transition-all hover:scale-105">
      <span className="text-slate-500 uppercase text-xs tracking-[0.2em] font-bold mb-4">ATS Compatibility</span>
      <div className={`w-36 h-36 rounded-full border-[6px] flex items-center justify-center bg-slate-950 shadow-[0_0_30px_rgba(52,211,153,0.1)] ${colorClass}`}>
        <span className="text-5xl font-black">{score}%</span>
      </div>
      <p className="text-slate-400 text-sm mt-6 font-medium">
        {isHigh ? "Ready for submission! ✅" : "Needs Optimization ⚠️"}
      </p>
    </div>
  );
}
