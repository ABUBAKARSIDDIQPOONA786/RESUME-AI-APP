import { useState } from "react";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";

/**
 * AI Resume Intelligence Platform - Main Entry
 * Date: January 2, 2026
 */
function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-50 selection:bg-blue-500/30">
      {/* Navigation Bar */}
      <Navbar />

      {/* Main Content Area */}
      <main className="transition-all duration-500 ease-in-out">
        <Dashboard />
      </main>

      {/* Footer */}
      <footer className="py-12 border-t border-slate-900 bg-slate-950 text-center">
        <div className="max-w-7xl mx-auto px-4">
          <p className="text-slate-500 text-sm font-medium tracking-wide">
            &copy; 2026 Resume.AI Platform • Powered by Agentic AI Analysis
          </p>
          <div className="mt-4 flex justify-center gap-6 text-slate-600 text-xs">
            <a href="#" className="hover:text-blue-400 transition-colors">Privacy Policy</a>
            <a href="#" className="hover:text-blue-400 transition-colors">Terms of Service</a>
            <a href="github.com" className="hover:text-blue-400 transition-colors">Documentation</a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
