// for development return to see .env.development file
const PrerenderSPAPlugin = require('prerender-spa-plugin')
const PuppeteerRenderer = PrerenderSPAPlugin.PuppeteerRenderer
const path = require('path')


const Puppeteer = new PrerenderSPAPlugin({
  staticDir: path.resolve(__dirname, '..', 'dist'), // The path to the folder where index.html is.
  routes: ['/', '/contact', '/prestations'], // List of routes to prerender.
  captureAfterElementExists: '#main-skeleton',
  renderer: new PuppeteerRenderer({
    renderAfterElementExists: '#main-skeleton',
    executablePath: '/usr/bin/chromium-browser',
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
  }),
})
module.exports = {
  publicPath: process.env.VUE_APP_BASE_URL,
  outputDir: '../dist/',
  lintOnSave: JSON.parse(process.env.VUE_APP_USE_LINT),
  pwa: {
    iconPaths: {
      favicon32: '/favicon.ico',
    }
  },
  configureWebpack: {
    plugins: []
  },
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
if (process.env.NODE_ENV === "production") {
  // there are a issue with chromium motor in contaiber !!! 
  module.exports.configureWebpack.plugins.push(Puppeteer)
}
// prerender withn spa-plugin and chromium motor.
// if (process.env.NODE_ENV === 'production') {
// module.exports.
// }
