// for development return to see .env.development file
console.log(process.env)
module.exports = {
  publicPath: process.env.PUBLIC_PATH, // if use docker without VM in fact if you use a unix core
  outputDir: '../dist/',
  lintOnSave: JSON.parse(process.env.VUE_APP_USE_LINT),
  chainWebpack: config => {
    config.optimization
      .splitChunks(false)

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
