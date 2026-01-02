import { Cpu, Github, ExternalLink } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-50 w-full border-b border-slate-800 bg-slate-950/80 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo Section */}
          <div className="flex items-center gap-2">
            <div className="bg-blue-600 p-1.5 rounded-lg">
              <Cpu className="w-6 h-6 text-white" />
            </div>
            <span className="text-xl font-bold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
              Resume.AI
            </span>
          </div>

          {/* Links Section */}
          <div className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-400">
            <a href="#" className="hover:text-blue-400 transition-colors">Analyzer</a>
            <a href="#" className="hover:text-blue-400 transition-colors">Role Mapping</a>
            <a href="#" className="hover:text-blue-400 transition-colors">Pricing</a>
          </div>

          {/* Action Section */}
          <div className="flex items-center gap-4">
            <a 
              href="github.com" 
              target="_blank" 
              className="p-2 text-slate-400 hover:text-white transition-colors"
            >
              <Github className="w-5 h-5" />
            </a>
            <button className="hidden sm:flex items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white text-sm font-bold rounded-lg transition-all">
              Sign Up <ExternalLink className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}
