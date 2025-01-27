const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  
  // Базовый путь для GitHub Pages
  publicPath: process.env.NODE_ENV === 'production'
    ? '/MiniAppRazvivahka/'
    : '/',
    
  // Настройки сборки
  configureWebpack: {
    optimization: {
      splitChunks: {
        chunks: 'all',
        minSize: 20000,
        maxSize: 250000,
      }
    }
  },
  
  // Настройки PWA
  pwa: {
    name: 'Развивахка',
    themeColor: '#2196F3',
    msTileColor: '#2196F3',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',
    workboxPluginMode: 'GenerateSW'
  }
}) 