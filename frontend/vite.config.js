import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    headers: {
      "Content-Security-Policy": "font-src 'self' https: data:;",
    },
  },
  esbuild: {
    loader: "jsx", // 👈 Yeh JSX error fix karega
  }
});
