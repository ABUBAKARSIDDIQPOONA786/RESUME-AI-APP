export default function Navbar() {
  return (
    <header className="border-b border-slate-800">
      <div className="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <span className="text-2xl font-bold text-indigo-400">Resume.AI</span>
          <span className="text-xs bg-indigo-500/10 text-indigo-400 px-2 py-1 rounded-full">
            Agentic AI
          </span>
        </div>

        <nav className="hidden md:flex gap-6 text-sm text-slate-300">
          <a className="hover:text-white">Analyzer</a>
          <a className="hover:text-white">Role Mapping</a>
          <a className="hover:text-white">Pricing</a>
        </nav>

        <button className="bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded-lg text-sm font-medium">
          Sign In
        </button>
      </div>
    </header>
  );
}
