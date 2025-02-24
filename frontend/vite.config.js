import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/generate': {
        target: import.meta.env.VITE_BACKEND_URL,
        changeOrigin: true,
        secure: false,
      }
    }
  },
  headers: {
    "Content-Security-Policy": "connect-src 'self' " + import.meta.env.VITE_BACKEND_URL + ";"
  }
});
