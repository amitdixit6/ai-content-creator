import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/generate': 'https://ai-content-creator-w4py.onrender.com'
    },
    headers: {
      "Content-Security-Policy": "default-src 'self'; connect-src 'self' https://ai-content-creator-w4py.onrender.com; font-src 'self' https: data:;"
    }
  }
});
