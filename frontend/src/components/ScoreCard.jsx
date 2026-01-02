export default function ScoreCard({ score }) {
  return (
    <div className="card">
      <h3>ATS Score</h3>
      <h1>{score}%</h1>
    </div>
  );
}