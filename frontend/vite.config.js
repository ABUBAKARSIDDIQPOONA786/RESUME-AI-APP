import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// vitejs.dev
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      // 2026 Best Practice: Proxying API calls during development 
      // This allows you to use fetch('/resume/upload') without CORS errors locally
      '/api': {
        target: 'http://127.0.0.1:8000', // Your local FastAPI address
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true, // Helpful for debugging production issues
    minify: 'terser', // High-efficiency minification for 2026 performance standards
  },
});