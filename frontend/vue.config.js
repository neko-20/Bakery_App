module.exports = {
  assetsDir: "static",
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    proxy: 'http://localhost:5000'
  },
  pages: {
    index: {
      entry: 'src/main.js',
      title: 'Takamatsu Bakary',
    }
  }
}
