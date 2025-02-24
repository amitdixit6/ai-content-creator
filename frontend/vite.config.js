import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    headers: {
      "Content-Security-Policy": "connect-src 'self' https://ai-content-creator-w4py.onrender.com;"
    }
  },
  define: {
    "process.env": process.env
  }
});
