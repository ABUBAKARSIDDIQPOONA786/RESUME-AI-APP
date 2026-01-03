export default function RecommendedRoles({ roles = [] }) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6">
      <h3 className="font-semibold mb-3">Best-Fit Roles</h3>
      <ul className="space-y-2 text-slate-300">
        {roles.map((r, i) => (
          <li key={i} className="flex justify-between">
            <span>{r}</span>
            <span className="text-green-400 text-sm">High Match</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
