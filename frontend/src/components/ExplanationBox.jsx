export default function ExplanationBox({ text }) {
  return (
    <div className="explanation">
      <h4>AI Insights</h4>
      <p>{text}</p>
    </div>
  );
}