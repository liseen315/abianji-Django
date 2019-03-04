module.exports = function (gulp, plugin, pathConfig) {
  gulp.task('hash:css', function (done) {
    gulp
      .src(pathConfig.distRoot + 'static/styles/**/*.css')
      .pipe(plugin.hashAssets(10, pathConfig.viewPath))
      .pipe(gulp.dest(pathConfig.distRoot + 'static/styles/'))
      .on('end', done)
  })
}
