import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 selection:bg-blue-500/30">
      {/* Global Navigation */}
      <Navbar />
      
      {/* Main Page Content */}
      <main>
        <Dashboard />
      </main>

      {/* Simple Footer */}
      <footer className="py-12 border-t border-slate-900 text-center text-slate-600 text-sm">
        &copy; 2026 Resume.AI Platform • Built with Agentic AI logic
      </footer>
    </div>
  );
}

export default App;
