import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/generate': {
        target: 'https://ai-content-creator-w4py.onrender.com',
        changeOrigin: true,
        secure: false,
      }
    },
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Content-Security-Policy": "default-src * 'self' 'unsafe-inline' 'unsafe-eval' data:; connect-src * 'self' https://ai-content-creator-w4py.onrender.com;"
    }
  }
});
