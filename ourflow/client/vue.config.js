// for development return to see .env.development file
module.exports = {
  publicPath: process.env.VUE_APP_BASE_URL, 
  outputDir: '../dist/',
  lintOnSave: JSON.parse(process.env.VUE_APP_USE_LINT),
  chainWebpack: config => {
    config.optimization
      .splitChunks(false)
      .minimize(false)

    config.resolve.alias
      .set('__STATIC__', 'static')

    config.devServer
      .overlay({
        warnings: true,
        errors: true
      })
      .host(process.env.HOST)
      .port(process.env.PORT)
      .hotOnly(true)
      .watchOptions({
        poll: 1000
      })
      .https(false)
      .headers({
        "Access-Control-Allow-Origin": ["\*"]
      })
  }

};
