module.exports = function (gulp, plugin, pathConfig) {
  gulp.task('hash:js', ['compileJS'], function (done) {
    gulp
      .src(pathConfig.distRoot + 'static/scripts/**/*.js')
      .pipe(plugin.hashAssets(10, pathConfig.viewPath))
      .pipe(gulp.dest(pathConfig.distRoot + 'static/scripts/'))
      .on('end', done)
  })
}
