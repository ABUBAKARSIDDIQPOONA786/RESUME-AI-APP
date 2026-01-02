import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css'; // This imports your Tailwind and global styles

// 2026 Standard: Using createRoot for concurrent rendering features
const rootElement = document.getElementById('root');

if (!rootElement) {
  throw new Error("Failed to find the root element. Ensure index.html has <div id='root'></div>");
}

ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    {/* 
      StrictMode helps identify potential problems in an application during development.
      It does not render any visible UI. It activates additional checks and warnings.
    */}
    <App />
  </React.StrictMode>
);