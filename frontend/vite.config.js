import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/generate': {
        target: 'https://ai-content-creator-w4py.onrender.com',
        changeOrigin: true,
        secure: false,
      }
    }
  },
  headers: {
    "Content-Security-Policy": "connect-src 'self' https://ai-content-creator-w4py.onrender.com;"
  }
});
