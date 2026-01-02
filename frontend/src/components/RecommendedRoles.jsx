export default function RecommendedRoles({ roles }) {
  return (
    <div>
      <h3>Recommended Job Roles</h3>
      {roles.map(role => (
        <div key={role.role} className="card">
          <h4>{role.role}</h4>
          <p>Match Score: {role.match_score}%</p>
          <p><b>Matched:</b> {role.matched_skills.join(", ")}</p>
          <p><b>Missing:</b> {role.missing_skills.join(", ")}</p>
        </div>
      ))}
    </div>
  );
}