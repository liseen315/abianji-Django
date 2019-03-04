const webpack = require('webpack')
const webpackConfig = require('../../webpack.config')

module.exports = function (gulp, plugin, pathConfig) {
  let wpConfig = webpackConfig(process.env.NODE_ENV, pathConfig)
  if (!wpConfig) {
    return
  }
  let compiler = webpack(wpConfig)
  gulp.task('compileJS', function (callback) {
    compiler.run(function (err, stats) {
      if (err) {
        throw new Error('webpack:build-js' + err)
      }
      console.log(stats.toString({ colors: true, chunks: false }))
      callback()
    })
  })
}
