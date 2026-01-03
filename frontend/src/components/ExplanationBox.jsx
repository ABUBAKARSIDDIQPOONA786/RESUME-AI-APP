export default function ExplanationBox({ explanation }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">
      <h3 className="font-semibold mb-2">AI Reasoning & Explanation</h3>
      <p className="text-slate-400 text-sm leading-relaxed">
        {explanation}
      </p>
    </div>
  );
}
