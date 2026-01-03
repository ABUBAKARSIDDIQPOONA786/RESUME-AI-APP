export default function SkillsList({ skills = [] }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">
      <h3 className="font-semibold mb-3">Detected Skills</h3>
      <div className="flex flex-wrap gap-2">
        {skills.map((s, i) => (
          <span
            key={i}
            className="bg-indigo-500/10 text-indigo-300 px-3 py-1 rounded-full text-xs"
          >
            {s}
          </span>
        ))}
      </div>
    </div>
  );
}
